import os
import pandas as pd
from IPPlanning.ip_helper_generate import *
from IPPlanning.ip_helper_valid import *

class SubnetGenerator:
    
    def __init__(self):
        self.mask_list = []
        self.ip = ''
        self.src_path = None
        self.dst_path = None
        self.input = 'input.xlsx'
        self.output = 'output.xlsx'

    def SetInputFileName(self, input_value):
        self.input = input_value

    def SetOutputFileName(self, output_value):
        self.output = output_value

    @property
    def start_ip(self):
        return self.ip

    @start_ip.setter
    def start_ip(self, input_ip):
        valid_flag = ValidIP(input_ip)
        if valid_flag:
            self.ip = input_ip
        else:
            raise ValueError('invalid start_ip format. please try again')
    
    def GenerateExcel(self):
        src_path = os.path.join(os.path.join(os.getcwd(),'ExcelFolder_Generate'), self.input)
        dst_path = os.path.join(os.path.join(os.getcwd(),'ExcelFolder_Generate'), self.output)
        excel_data_df = pd.read_excel(src_path, sheet_name='Sheet1')
        mask_list = excel_data_df['masks'].tolist()
        self.mask_list = mask_list
        result_list = self.GeneratePlain()
        df_subnets = pd.DataFrame(data = {'subnets': result_list})

        # create excel writer object
        writer = pd.ExcelWriter(dst_path)
        # write dataframe to excel
        df_subnets.to_excel(writer)
        # save the excel
        writer.save()
        print('Input file is located at: *** {} ***\n\n'.format(src_path))
        print('Data is written successfully. Excel File can be found at: *** {} ***'.format(dst_path))

        
    def GeneratePlain(self):
        result_list = []
        if ValidIP(self.start_ip):
            next_block = self.start_ip
        else:
            raise ValueError('invalid start_ip format')
            
        for mask in self.mask_list:
            subnet, next_block = subnets(next_block, mask)
            result_list.append('{}/{}'.format(subnet, mask))
            
        return result_list
  
#SubnetCheck class starts here
class SubnetCheck:
    def __init__(self):
        self.ip_list = []
        self.filename = 'input.xlsx'

    @property
    def path(self):
        return os.path.join(os.path.join(os.getcwd(),'ExcelFolder_Validate'), self.filename)
    
    def ValidSubnet(self):
        ValidateList(self.ip_list)

    def CheckIPConflict(self):
        ValidateIPConflict(self.ip_list)

    def LoadExcel(self):
        excel_data_df = pd.read_excel(self.path, sheet_name='Sheet1')
        self.ip_list = excel_data_df['Subnets'].tolist()
        

















