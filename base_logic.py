import collect as data_collect_func
import csv_func as csv_func
import pandas_collect as pd_coll

def operate():
    # touple_list=data_collect_func.get_data()
    # csv_func.export_data_to_csv("BAC.csv",touple_list)
    touple_list2=pd_coll.get_data()
    csv_func.export_data_to_csv("ADM.csv", touple_list2)
    print("done")

operate()