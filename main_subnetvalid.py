from IPPlanning.Core import SubnetCheck

def main():
    
    S = SubnetCheck()
    print('Path of the file on which these checks are being performed is located at:*** {} ***\n\n'.format(S.path))
    S.LoadExcel()
    S.ValidSubnet()
    S.CheckIPConflict()

if __name__ == '__main__':
    main()
