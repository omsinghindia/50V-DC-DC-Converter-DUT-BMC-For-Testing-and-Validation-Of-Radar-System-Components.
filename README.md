# 50V-DC-DC-Converter-DUT-BMC-For-Testing-and-Validation-Of-Radar-System-Components.
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NISAR DC-DC Converter Test Framework</title>
    <style>
        body { font-family: Arial, sans-serif; line-height: 1.6; padding: 20px; }
        h1, h2 { color: #2c3e50; }
        code { background: #f4f4f4; padding: 2px 6px; border-radius: 4px; }
        pre { background: #f4f4f4; padding: 10px; border-left: 3px solid #3498db; overflow-x: auto; }
        ul { margin-bottom: 1em; }
    </style>
</head>
<body>
    <h1>NISAR DC-DC Converter Test Framework</h1>
    <p>This project implements an advanced and modular test framework for validating package-level DC-DC converters used in ISRO's NISAR satellite project, specifically the SD50F401 (Power Card) and SD50F302 (Control Card).</p>

    <h2>📦 Features</h2>
    <ul>
        <li>Visual inspection simulation</li>
        <li>TM/TC interface validation</li>
        <li>Voltage setability and regulation tests</li>
        <li>Inrush current and transient response analysis</li>
        <li>Output current limit verification</li>
        <li>Stability, waveform, and isolation checks</li>
        <li>Modular design for extensibility and lab integration</li>
    </ul>

    <h2>🚀 Getting Started</h2>
    <h3>Clone Repository</h3>
    <pre><code>git clone https://github.com/&lt;your-username&gt;/nisar-dcdc-test.git
cd nisar-dcdc-test</code></pre>

    <h3>Install Dependencies</h3>
    <pre><code>pip install -r requirements.txt</code></pre>

    <h3>Run Demo</h3>
    <pre><code>python examples/run_demo.py</code></pre>

    <h2>🧪 Project Structure</h2>
    <pre><code>nisar-dcdc-test/
├── src/
│   ├── config.py            # Converter specifications
│   ├── logger.py            # Logging utility
│   └── dcdc_tester.py       # Main test class
├── tests/
│   └── test_main.py         # Unit tests
├── examples/
│   └── run_demo.py          # Demo script
├── README.md
├── requirements.txt
└── LICENSE</code></pre>

    <h2>📄 License</h2>
    <p>This project is licensed under the MIT License.</p>
</body>
</html>
