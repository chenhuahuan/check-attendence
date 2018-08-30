
import datetime
from dateutil.relativedelta import *
import XlsManager
import collections




def get_date_str_timestamp(fmt="%Y-%m-%d %H:%M:%S", **kwargs):
    n_days = datetime.datetime.today()+relativedelta(minutes = kwargs['minutes'])
    return str(n_days.strftime(fmt))


def read_dict_list(xls_obj):
  #  dict_list = xls_obj.read_xls_to_dict_list(sheet_name= '每日统计', key_rows= 3)
    dict_list = read_xls_to_dict_list_attendence(xls_obj.rdbook,sheet_name= '每日统计', key_rows= 2)
    return dict_list


def read_xls_to_dict_list_attendence(rdbook_obj, sheetx=0, sheet_name=None, key_rows=0):
    if sheet_name:
        sheet = rdbook_obj.sheet_by_name(sheet_name)
    else:
        sheet = rdbook_obj.sheet_by_index(sheetx)

    # read header values into the list
    keys_common = [sheet.cell(key_rows, col_index).value for col_index in range(7)]

    dict_list = []
    for row_index in range(1, sheet.nrows):
        d = {keys_common[col_index]: sheet.cell(row_index, col_index).value
             for col_index in range(7)}
        d['打卡时间1'] = sheet.cell(row_index, 7).value
        d['打卡结果1'] = sheet.cell(row_index, 8).value
        d['打卡时间2'] = sheet.cell(row_index, 9).value
        d['打卡结果2'] = sheet.cell(row_index, 10).value

        dict_list.append(d)

    return dict_list

def get_attendence_time_stat(dict_list):

    BREAK_HOURS = 1.5
    staffs = set()
    overall_total_attendence_hours = 0
    overall_total_attendence_count = 0
    total_attendence_hours_per_staff = collections.defaultdict(int)
    average_attendence_hours_dict = {}
    count_dict = collections.defaultdict(int)



    for dic in dict_list:

        # 剔除休息班次的item
        if dic['班次'] == '休息' or dic ['班次'] != 'B 09:00-18:00 ' or dic['班次'] == '':
            continue

        # 筛选打卡结果至少包含 “{正常，[早退，迟到]}的记录”，只有这种情况，才认为当天上班的情况是可以列为有效统计的
        # 其余的情况，比如请假，外勤，漏打卡，缺卡等各种情况的组合，人为因素太难把控，容易给平均工时带来干扰
        if (dic['打卡结果1'] == '正常' and dic['打卡结果2'] == '正常') or (dic['打卡结果1'] == '正常' and '早退' in dic['打卡结果2']) or ('迟到' in dic['打卡结果1'] and dic['打卡结果2'] == '正常'):
            print(interval_hours_without_date(dic['打卡时间1'], dic['打卡时间2']))
            interval_hours = interval_hours_without_date(dic['打卡时间1'], dic['打卡时间2'], BREAK_HOURS)

            staffs.add(dic['姓名'])
            count_dict[dic['姓名']] += 1
            # 单个员工总工作时长
            total_attendence_hours_per_staff[dic['姓名']] += interval_hours

            # 总体员工正常考勤打卡次数
            overall_total_attendence_count += 1
            # 全体员工总工作时长
            overall_total_attendence_hours += interval_hours

    print(staffs)
    print(dict(total_attendence_hours_per_staff))
    print(dict(count_dict))

    print('###' * 4)
    print('Average for each staff:')
    for staff in staffs:
        print("{} : {}".format(staff,total_attendence_hours_per_staff[staff] / count_dict[staff]))



    print('部门平均时间: {}'.format(overall_total_attendence_hours/overall_total_attendence_count))

    return overall_total_attendence_hours/overall_total_attendence_count




def interval_hours_without_date(begin_time_str, end_time_str, break_hours = 1.5):

    if ':' in begin_time_str and ':' in end_time_str:
        start_dt = datetime.datetime.strptime(begin_time_str, "%H:%M")
        end_dt = datetime.datetime.strptime(end_time_str, "%H:%M")
    else:
        raise Exception("Not a correct string for time format ")

    interval = end_dt - start_dt
    return (interval.days*24*3600 + interval.seconds - 1.5*3600) / 3600



def get_average_attendence_hours(dict_list):
    average_hours = get_attendence_time_stat(dict_list)
    return average_hours



if __name__=='__main__':
    test = XlsManager.XlsManager('深圳市铱云云计算有限公司_考勤报表_20180701-20180731(1).xls')

    dict_list = read_dict_list(test)
    dict_list = dict_list[2:]

    get_average_attendence_hours(dict_list)

    # a = test.read_xls_cell(5,8,sheet_name= '每日统计')
    # print(a)