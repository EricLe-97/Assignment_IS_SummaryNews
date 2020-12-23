import pandas as pd
import os

def readExcelFile(file_name,file_sheet,categories_list):
    df = pd.read_excel(file_name, sheet_name = file_sheet)
    for i in range(len(df)):
        Id = df.loc[i,"Id"]
        if( str(Id) in list(categories_list.keys())):
            categories_list[str(Id)].append(df.loc[i,"category"])
    return categories_list

def readCsvFile (data_dir,categories_list): 
    for (dirpath, dirnames, filenames) in os.walk(data_dir):
        for filename in filenames:
            if filename.startswith('chinh_tri'):
                dataframe = pd.read_csv(dirpath+"/"+filename)
                for i in dataframe["category"]:
                    categories_list['0'].append(i)
            if filename.startswith('the_thao'):
                dataframe = pd.read_csv(dirpath+"/"+filename)
                for i in dataframe["category"]:
                    categories_list['1'].append(i)
            if filename.startswith('giao_duc'):
                dataframe = pd.read_csv(dirpath+"/"+filename)
                for i in dataframe["category"]:
                    categories_list['2'].append(i)
            if filename.startswith('giai_tri'):
                dataframe = pd.read_csv(dirpath+"/"+filename)
                for i in dataframe["category"]:
                    categories_list['3'].append(i)
            if filename.startswith('cong_nghe'):
                dataframe = pd.read_csv(dirpath+"/"+filename)
                for i in dataframe["category"]:
                    categories_list['4'].append(i)
            if filename.startswith('kinh_te'):
                dataframe = pd.read_csv(dirpath+"/"+filename)
                for i in dataframe["category"]:
                    categories_list['5'].append(i)
            if filename.startswith('phap_luat'):
                dataframe = pd.read_csv(dirpath+"/"+filename)
                for i in dataframe["category"]:
                    categories_list['6'].append(i)
            if filename.startswith('dien_anh'):
                dataframe = pd.read_csv(dirpath+"/"+filename)
                for i in dataframe["category"]:
                    categories_list['7'].append(i)
            if filename.startswith('covid_19'):
                dataframe = pd.read_csv(dirpath+"/"+filename)
                for i in dataframe["category"]:
                    categories_list['8'].append(i)

    return categories_list
