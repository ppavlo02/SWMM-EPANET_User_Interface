"""

Wrapper for SWMM Output API.

Written for SWMM-EPANET User Interface project
2016
Mark Gray, RESPEC
for US EPA

Inspired by ENOutputWrapper by Bryant E. McDonnell 12/7/2015

"""

from ctypes import *

import Externals.swmm.outputapi.outputapi as _lib

from outputapi import SMO_getLinkAttribute, SMO_getNodeAttribute, SMO_getSubcatchAttribute, SMO_getSystemAttribute

from outputapi import nodeCount, linkCount, subcatchCount, pollutantCount, SMO_elementCount

from outputapi import SMO_getLinkSeries, SMO_getNodeSeries, SMO_getSubcatchSeries, SMO_getSystemSeries

from outputapi import SMO_getNodeAttribute

cint = c_int()


class OutputObject(object):
    def __init__(self, output_file_name):
        """
        1) Initializes the opaque pointer to ptrapi struct.
        2) Opens the output file.
        """
        self.ptrapi = c_void_p()
        ret = _lib.SMR_open(str(output_file_name), byref(self.ptrapi))
        if ret != 0:
            self.RaiseError(ret)
        self._get_Units()
        self._get_Sizes()
        self._get_Times()
        self._cache_node_ids()
        self._cache_link_ids()

    def RaiseError(self, ErrNo):
        # if _RetErrMessage(ErrNo , errmsg, err_max_char)==0:
        #     raise Exception(errmsg.value)
        # else:
        raise Exception("Unknown error #{0}".format(ErrNo))

    def _get_Units(self):
        """
        Purpose: Returns pressure and flow units
        """
        _lib.SMO_getUnits(self.ptrapi, _lib.flow_rate, byref(cint))
        self.flowUnits = cint.value

        # _lib.SMO_getUnits(self.ptrapi, _lib.concentration, byref(cint))
        # self.concentrationUnits = cint.value

    def _get_Sizes(self):
        """
        Populates object attributes with the water object counts
        """
        ierr = _lib.SMO_getProjectSize(self.ptrapi, _lib.nodeCount, byref(cint))
        if ierr != 0:
            print "Error in SMO_getProjectSize(nodeCount)"
            self.RaiseError(ierr)
        self.nodeCount = cint.value

        ierr = _lib.SMO_getProjectSize(self.ptrapi, _lib.subcatchCount, byref(cint))
        if ierr != 0:
            print "Error in SMO_getProjectSize(subcatchCount)"
            self.RaiseError(ierr)
        self.subcatchCount = cint.value

        ierr = _lib.SMO_getProjectSize(self.ptrapi, _lib.linkCount, byref(cint))
        if ierr != 0:
            print "Error in SMO_getProjectSize(linkCount)"
            self.RaiseError(ierr)
        self.linkCount = cint.value

        ierr = _lib.SMO_getProjectSize(self.ptrapi, _lib.pollutantCount, byref(cint))
        if ierr != 0:
            print "Error in SMO_getProjectSize(pollutantCount)"
            self.RaiseError(ierr)
        self.pollutantCount = cint.value

    def _get_Times(self):
        """
        Purpose: Returns report and simulation time related parameters.
        """

        # _lib.SMO_getTimes(self.ptrapi, _lib.SMO_reportStart, byref(cint))
        # self.reportStart = cint.value

        _lib.SMO_getTimes(self.ptrapi, _lib.reportStep, byref(cint))
        self.reportStep = cint.value

        # _lib.SMO_getTimes(self.ptrapi, _lib.SMO_simDuration, byref(cint))
        # self.simDuration = cint.value

        _lib.SMO_getTimes(self.ptrapi, _lib.numPeriods, byref(cint))
        self.numPeriods = cint.value

    def _cache_node_ids(self):
        self.nodeIds = []
        c_return = _lib.SMO_getNodeIDs(self.ptrapi, byref(cint))
        if cint.value != 0:
            print "Error in SMO_getNodeIDs()"
            self.RaiseError(cint.value)
        while c_return:
            self.nodeIds.append(str(c_return.contents.IDname.data))
            print "Node " + self.nodeIds[-1]
            c_return = c_return.contents.nextID

    def _cache_link_ids(self):
        self.linkIds = []
        c_return = _lib.SMO_getLinkIDs(self.ptrapi, byref(cint))
        if cint.value != 0:
            print "Error in SMO_getLinkIDs()"
            self.RaiseError(cint.value)
        while c_return:
            self.linkIds.append(str(c_return.contents.IDname.data))
            print "Link " + self.linkIds[-1]
            c_return = c_return.contents.nextID

    def get_NodeID(self, index):
        """Retrieves the ID label of a node with a specified index.
        Arguments:
        index: node index"""
        return self.nodeIds[index]

    def get_NodeIndex(self, NodeID):
        """Retrieves the index of a node with a specified ID.

        Arguments:
        NodeID: node ID label"""
        try:
            return self.nodeIds.index(NodeID)
        except:
            return -1

    def get_LinkID(self, index):
        """Retrieves the ID label of a link with a specified index.

        Arguments:
        index: link index"""
        return self.linkIds[index]

    def get_LinkIndex(self, LinkID):
        """Retrieves the index of a link with a specified ID.

        Arguments:
        LinkID: link ID label"""
        try:
            return self.linkIds.index(LinkID)
        except:
            return -1

    def get_NodeValue(self, NodeInd, TimeInd, NodeAttr):
        """
        Purpose: Get results for particular node, time, attribute.
        """
        xval = c_float()
        ierr = _lib.SMO_getNodeValue(self.ptrapi, TimeInd, NodeInd, NodeAttr, byref(xval))
        if ierr == 0:
            return xval.value
        else:
            print "Error in get_NodeValue({}, {}, {})".format(str(NodeInd), str(TimeInd), str(NodeAttr))
            self.RaiseError(ierr)

    def get_LinkValue(self, NodeInd, TimeInd, NodeAttr):
        """
        Purpose: Get results for particular link, time, attribute.
        """
        xval = c_float()
        ierr = _lib.SMO_getLinkValue(self.ptrapi, TimeInd, NodeInd, NodeAttr, byref(xval))
        if ierr == 0:
            return xval.value
        else:
            self.RaiseError(ierr)

    def get_NodeSeries(self, NodeInd, NodeAttr, SeriesStartInd=0, SeriesLen=-1):
        """
        Purpose: Get time series results for particular attribute. Specify series
        start and length using seriesStart and seriesLength respectively.

        SeriesLen = -1 Default input: Gets data from Series Start Ind to end

        """
        if SeriesLen > self.numPeriods:
            raise Exception("Outside Number of TimeSteps")
        elif SeriesLen == -1:
            SeriesLen = self.numPeriods

        sLength = c_int()
        ErrNo1 = c_int()
        SeriesPtr = _lib.SMO_newOutValueSeries(self.ptrapi, SeriesStartInd,
                                               SeriesLen, byref(sLength), byref(ErrNo1))
        ErrNo2 = _lib.SMO_getNodeSeries(self.ptrapi,
                                        NodeInd,
                                        NodeAttr,
                                        SeriesStartInd,
                                        sLength.value,
                                        SeriesPtr)

        BldArray = [SeriesPtr[i] for i in range(sLength.value)]
        _lib.SMO_free(SeriesPtr)
        return BldArray

    def get_LinkSeries(self, LinkInd, LinkAttr, SeriesStartInd=0, SeriesLen=-1):
        """
        Purpose: Get time series results for particular attribute. Specify series
        start and length using seriesStart and seriesLength respectively.

        SeriesLen = -1 Default input: Gets data from Series Start Ind to end

        """
        if SeriesLen > self.numPeriods:
            raise Exception("Outside Number of TimeSteps")
        elif SeriesLen == -1:
            SeriesLen = self.numPeriods

        sLength = c_int()
        ErrNo1 = c_int()
        SeriesPtr = _lib.SMO_newOutValueSeries(self.ptrapi, SeriesStartInd,
                                               SeriesLen, byref(sLength), byref(ErrNo1))
        ErrNo2 = _lib.SMO_getLinkSeries(self.ptrapi, LinkInd, LinkAttr,
                                        SeriesStartInd, sLength.value, SeriesPtr)
        BldArray = [SeriesPtr[i] for i in range(sLength.value)]
        ret = _lib.SMO_free(SeriesPtr)

        return BldArray

    def get_NodeAttribute(self, NodeAttr, TimeInd):
        """
        Purpose: For all nodes at given time, get a particular attribute
        """
        alength = c_int()
        ErrNo1 = c_int()
        ValArrayPtr = _lib.SMO_newOutValueArray(self.ptrapi, _lib.SMO_getAttribute,
                                                _lib.SMO_node, byref(alength), byref(ErrNo1))
        ErrNo2 = _lib.SMO_getNodeAttribute(self.ptrapi, TimeInd, NodeAttr, ValArrayPtr)
        BldArray = [ValArrayPtr[i] for i in range(alength.value)]
        _lib.SMO_free(ValArrayPtr)
        return BldArray

    def get_LinkAttribute(self, LinkAttr, TimeInd):
        """
        Purpose: For all links at given time, get a particular attribute
        """
        alength = c_int()
        ErrNo1 = c_int()
        ValArrayPtr = _lib.SMO_newOutValueArray(self.ptrapi, _lib.SMO_getAttribute,
                                                _lib.SMO_link, byref(alength), byref(ErrNo1))
        ErrNo2 = _lib.SMO_getLinkAttribute(self.ptrapi, TimeInd, LinkAttr, ValArrayPtr)
        BldArray = [ValArrayPtr[i] for i in range(alength.value)]
        _lib.SMO_free(ValArrayPtr)
        return BldArray

    def get_NodeResult(self, NodeInd, TimeInd):
        """
        Purpose: For a node at given time, get all attributes
        """
        alength = c_int()
        ErrNo1 = c_int()
        ValArrayPtr = _lib.SMO_newOutValueArray(self.ptrapi,
                                                _lib.SMO_getResult,
                                                _lib.SMO_node,
                                                byref(alength),
                                                byref(ErrNo1))
        ErrNo2 = _lib.SMO_getNodeResult(self.ptrapi, TimeInd, NodeInd, ValArrayPtr)
        BldArray = [ValArrayPtr[i] for i in range(alength.value)]
        _lib.SMO_free(ValArrayPtr)
        return BldArray

    def get_LinkResult(self, LinkInd, TimeInd):
        """
        Purpose: For a link at given time, get all attributes
        """
        alength = c_int()
        ErrNo1 = c_int()
        ValArrayPtr = _lib.SMO_newOutValueArray(self.ptrapi,
                                                _lib.SMO_getResult,
                                                _lib.SMO_link,
                                                byref(alength),
                                                byref(ErrNo1))
        ErrNo2 = _lib.SMO_getLinkResult(self.ptrapi, TimeInd, LinkInd, ValArrayPtr)
        BldArray = [ValArrayPtr[i] for i in range(alength.value)]
        _lib.SMO_free(ValArrayPtr)
        return BldArray

    def CloseOutputFile(self):
        """
        Call to close binary file.
        """
        ret = _lib.SMO_close(byref(self.ptrapi))
        if ret != 0:
            raise Exception('Failed to Close *.out file')

