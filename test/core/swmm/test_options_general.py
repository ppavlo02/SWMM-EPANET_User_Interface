from core.swmm.options.general import General, FlowRouting, FlowUnits
import unittest


class OptionsGeneralTest(unittest.TestCase):
    """In core.swmm.options, test field values after setting from text.
     This primarily tests General, but also tests Dates, TimeSteps, and DynamicWave since those are set from General.
    """

    TEST_TEXT = (
        ("""[OPTIONS]
 FLOW_UNITS            \tCFS
 INFILTRATION          \tHORTON
 FLOW_ROUTING          \tKW
 START_DATE            \t01/01/1998
 START_TIME            \t00:00:00
 REPORT_START_DATE     \t01/01/1998
 REPORT_START_TIME     \t00:00:00
 END_DATE              \t01/02/1998
 END_TIME              \t12:00:00
 DRY_DAYS              \t5
 WET_STEP              \t00:15:00
 DRY_STEP              \t01:00:00
 ROUTING_STEP          \t00:01:00
 REPORT_STEP           \t01:00:00
 ALLOW_PONDING         \tNO
 INERTIAL_DAMPING      \tPARTIAL
 VARIABLE_STEP         \t0.75
 LENGTHENING_STEP      \t0
 MIN_SURFAREA          \t0
 COMPATIBILITY         \t5""",

         FlowUnits.CFS,
         "HORTON",
         FlowRouting.KINWAVE,
         "01/01/1998",
         "00:00:00",
         "01/01/1998",
         "00:00:00",
         "01/02/1998",
         "12:00:00",
         5,
         "00:15:00",
         "01:00:00",
         "00:01:00",
         "01:00:00",
         "NO",
         "PARTIAL",
         0.75,
         0,
         0,
         5),
        ("""[OPTIONS]
 FLOW_UNITS            \tMGD
 INFILTRATION          \tGREEN_AMPT
 FLOW_ROUTING          \tDYNWAVE
 START_DATE            \t02/02/2000
 START_TIME            \t00:01:00
 REPORT_START_DATE     \t02/03/2000
 REPORT_START_TIME     \t00:02:00
 END_DATE              \t02/04/2000
 END_TIME              \t12:30:00
 DRY_DAYS              \t4
 WET_STEP              \t00:30:00
 DRY_STEP              \t01:30:00
 ROUTING_STEP          \t00:02:00
 REPORT_STEP           \t02:00:00
 ALLOW_PONDING         \tYES
 INERTIAL_DAMPING      \tPARTIAL
 VARIABLE_STEP         \t0.6
 LENGTHENING_STEP      \t1
 MIN_SURFAREA          \t2
 COMPATIBILITY         \t4""",

         FlowUnits.MGD,
         "GREEN_AMPT",
         FlowRouting.DYNWAVE,
         "02/02/2000",
         "00:01:00",
         "02/03/2000",
         "00:02:00",
         "02/04/2000",
         "12:30:00",
         4,
         "00:30:00",
         "01:30:00",
         "00:02:00",
         "02:00:00",
         "YES",
         "PARTIAL",
         0.6,
         1,
         2,
         4)

    )

    def runTest(self):
        for current_text in self.TEST_TEXT:
            options = General()
            options.set_text(current_text[0])
            assert options.flow_units == current_text[1]
            assert options.infiltration == current_text[2]
            assert options.flow_routing == current_text[3]
            assert options.dates.start_date == current_text[4]
            assert options.dates.start_time == current_text[5]
            assert options.dates.report_start_date == current_text[6]
            assert options.dates.report_start_time == current_text[7]
            assert options.dates.end_date == current_text[8]
            assert options.dates.end_time == current_text[9]
            assert options.dates.dry_days == int(current_text[10])
            assert options.time_steps.wet_step == current_text[11]
            assert options.time_steps.dry_step == current_text[12]
            assert options.time_steps.routing_step == current_text[13]
            assert options.time_steps.report_step == current_text[14]
            if (str(current_text[15]).upper() != "NO"):
                assert options.allow_ponding
            else:
                assert not options.allow_ponding
            assert options.dynamic_wave.inertial_damping.name == current_text[16]
            assert options.dynamic_wave.variable_step == float(current_text[17])
            assert options.dynamic_wave.lengthening_step == int(current_text[18])
            assert options.dynamic_wave.min_surface_area == int(current_text[19])
            assert options.compatibility == int(current_text[20])




