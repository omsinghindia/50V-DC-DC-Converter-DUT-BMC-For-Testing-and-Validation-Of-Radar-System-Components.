class DCDCSpecs:
    def __init__(self):
        self.V_in_min = 26
        self.V_in_max = 42
        self.f_switch = 250_000  # Hz
        self.f_tolerance = 0.20
        self.efficiency_min = 0.65
        self.I_inrush_max = 6  # Amps
        self.I_inrush_duration = (0.5, 3.5)  # ms
        self.output_voltage = {
            1: 5,
            2: 6,
            3: 15,
            4: -15
        }
        self.current_limits = {
            "output": (3.0, 0.2),
            "input": (1.5, 0.5)
        }

