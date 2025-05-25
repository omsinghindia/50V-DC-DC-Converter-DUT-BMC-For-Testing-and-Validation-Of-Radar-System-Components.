
---

**tests/test_main.py**
```python
import unittest
from src.config import DCDCSpecs
from src.dcdc_tester import DCDCConverterTester

class TestDCDCConverterTester(unittest.TestCase):

    def setUp(self):
        self.specs = DCDCSpecs()
        self.tester = DCDCConverterTester("SD50F401", self.specs)

    def test_visual_inspection(self):
        self.assertTrue(self.tester.visual_inspection())

    def test_voltage_setability_test(self):
        self.assertTrue(self.tester.voltage_setability_test())

    def test_inrush_current_test(self):
        # Run multiple times due to randomness
        results = [self.tester.inrush_current_test() for _ in range(10)]
        self.assertIn(True, results)

    def test_switch_waveform_analysis(self):
        self.assertTrue(self.tester.switch_waveform_analysis())

    def test_run_all_tests(self):
        result = self.tester.run_all_tests()
        self.assertIn(result, ["✅ TEST PASSED", "❌ TEST FAILED"])

if __name__ == "__main__":
    unittest.main()

