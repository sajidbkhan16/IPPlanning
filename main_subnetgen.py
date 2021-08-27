from IPPlanning.Core import SubnetGenerator
import argparse

def main():
    parser = argparse.ArgumentParser(description='main staring ip from which subnets will be allocated')
    parser.add_argument('--start_ip', type=str, help='input IP in following format "192.168.0.0"', required=True)
    args = parser.parse_args()
    args.start_ip
    S = SubnetGenerator()
    S.start_ip = args.start_ip
    S.GenerateExcel()

if __name__ == "__main__":
    main()
