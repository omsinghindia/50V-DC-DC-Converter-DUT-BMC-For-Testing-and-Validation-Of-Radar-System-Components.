from src.config import DCDCSpecs
from src.dcdc_tester import DCDCConverterTester

def main():
    specs = DCDCSpecs()
    tester = DCDCConverterTester("SD50F401", specs)
    result = tester.run_all_tests()
    print("\nFinal Result:", result)

if __name__ == "__main__":
    main()
