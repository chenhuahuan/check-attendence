
import datetime
from dateutil.relativedelta import *
import XlsManager





def get_date_str_timestamp(fmt="%Y-%m-%d %H:%M:%S", **kwargs):
    n_days = datetime.datetime.today()+relativedelta(minutes = kwargs['minutes'])
    return str(n_days.strftime(fmt))


def read_dict_list(xls_obj):

  #  dict_list = xls_obj.read_xls_to_dict_list(sheet_name= '每日统计', key_rows= 3)
    dict_list = xls_obj.read_xls_to_dict_list_attendence(sheet_name= '每日统计', key_rows= 2)



    return dict_list


def scree_attendence_time(dict_list):

    ATTENDENCE_MORNING = '09:00'
    ATTENDENCE_EVENING = '18:00'
    ATTENDENCE_TIME = '考勤时间'
    PUNCH_TIME = '打卡时间'

    for dic in dict_list:
        if dic[ATTENDENCE_TIME]:
            return








def average_hours(begin_time_str, end_time_str ):

    if ':' not in begin_time_str:
        start_dt = datetime.datetime.strptime(begin_time_str, "%Y-%m-%d")
    else:
        start_dt = datetime.datetime.strptime(begin_time_str, "%Y-%m-%d %H:%M:%S")

    if ':' not in end_time_str:
        end_dt = datetime.datetime.strptime(end_time_str, "%Y-%m-%d")
    else:
        end_dt = datetime.datetime.strptime(end_time_str, "%Y-%m-%d %H:%M:%S")


    return average_hours



if __name__=='__main__':
    test = XlsManager.XlsManager('C:\\Users\\huan\\PycharmProjects\\test\深圳市铱云云计算有限公司_考勤报表_20180701-20180731(1).xls')

    dict_list = read_dict_list(test)
    dict_list = dict_list[2:]
    for dic in dict_list:
        print(dic)

    # a = test.read_xls_cell(5,8,sheet_name= '每日统计')
    # print(a)