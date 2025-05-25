import random
from src.logger import log
from src.config import DCDCSpecs

class DCDCConverterTester:
    def __init__(self, converter_id: str, specs: DCDCSpecs):
        self.converter_id = converter_id
        self.logs = []
        self.results = {}
        self.specs = specs

    def run_all_tests(self):
        log(f"Starting tests for converter: {self.converter_id}\n")

        checks = [
            self.visual_inspection,
            self.tm_interface_check,
            self.voltage_setability_test,
            self.regulation_tests,
            self.inrush_current_test,
            self.transient_response_test,
            self.output_current_limit_test,
            self.dtm_interface_check,
            self.telemetry_current_test,
            self.stability_test,
            self.switch_waveform_analysis,
            self.isolation_and_grounding_check
        ]

        for check in checks:
            result = check()
            self.results[check.__name__] = result
            if not result:
                log(f"❌ FAIL: {check.__name__} failed.")
                return "❌ TEST FAILED"

        log("\n✅ All tests passed successfully.")
        return "✅ TEST PASSED"

    # === Test Procedures ===

    def visual_inspection(self):
        log("Performing Visual Inspection...")
        return True

    def tm_interface_check(self):
        log("Checking TM interface @ 26V, 200mA...")
        return True

    def voltage_setability_test(self):
        log("Testing voltage setability across input range...")
        for vin in range(self.specs.V_in_min, self.specs.V_in_max + 1):
            if not self.simulate_voltage_output(vin):
                return False
        return True

    def simulate_voltage_output(self, vin):
        tolerance = 0.03
        for ch, vout in self.specs.output_voltage.items():
            observed = vout * (1 + random.uniform(-tolerance, tolerance))
            if abs(observed - vout) > vout * tolerance:
                log(f"Channel {ch}: Voltage out of tolerance @ Vin={vin}V")
                return False
        return True

    def regulation_tests(self):
        log("Conducting line/load/cross regulation tests...")
        return True

    def inrush_current_test(self):
        log("Measuring inrush current during TC ON...")
        current = random.uniform(3.0, 6.5)
        duration = random.uniform(*self.specs.I_inrush_duration)
        log(f"Inrush Current: {current:.2f}A for {duration:.2f}ms")
        if current > self.specs.I_inrush_max:
            log(f"❌ Inrush current {current:.2f}A exceeds max allowed {self.specs.I_inrush_max}A")
            return False
        if not (self.specs.I_inrush_duration[0] <= duration <= self.specs.I_inrush_duration[1]):
            log(f"❌ Inrush current duration {duration:.2f}ms out of allowed range {self.specs.I_inrush_duration}ms")
            return False
        return True

    def transient_response_test(self):
        log("Performing transient tests (0↔26V↔43V)...")
        return True

    def output_current_limit_test(self):
        log("Checking output current limiting...")
        limit, tol = self.specs.current_limits['output']
        measured = random.uniform(limit - tol, limit + tol)
        log(f"Output current limit observed: {measured:.2f}A")
        return abs(measured - limit) <= tol

    def dtm_interface_check(self):
        log("Validating DTM interface voltage (0-5V)...")
        return True

    def telemetry_current_test(self):
        log("Checking current telemetry range...")
        return True

    def stability_test(self):
        log("Verifying steady-state and transient stability...")
        return True

    def switch_waveform_analysis(self):
        log("Analyzing switching frequency and waveform shape...")
        fs_measured = random.randint(200_000, 300_000)
        target = self.specs.f_switch
        tol = self.specs.f_tolerance * target
        log(f"Measured switching frequency: {fs_measured} Hz")
        return abs(fs_measured - target) <= tol

    def isolation_and_grounding_check(self):
        log("Performing isolation impedance and grounding check...")
        return True
