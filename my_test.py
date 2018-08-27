
import datetime

def delta_hours(begin_time_str, end_time_str ):

    if ':' not in begin_time_str:
        start_dt = datetime.datetime.strptime(begin_time_str, "%Y-%m-%d")
    elif begin_time_str.count(':') == 1:
        start_dt = datetime.datetime.strptime(begin_time_str, "%Y-%m-%d %H:%M")
    elif begin_time_str.count(':') == 2:
        start_dt = datetime.datetime.strptime(begin_time_str, "%Y-%m-%d %H:%M:%S")

    if ':' not in end_time_str:
        end_dt = datetime.datetime.strptime(end_time_str, "%Y-%m-%d")
    elif end_time_str.count(':') == 1:
        end_dt = datetime.datetime.strptime(end_time_str, "%Y-%m-%d %H:%M")
    elif end_time_str.count(':') == 2:
        end_dt = datetime.datetime.strptime(end_time_str, "%Y-%m-%d %H:%M:%S")
    else:
        raise Exception("NOT Correct format!")

    delta = end_dt - start_dt
    return delta


delta = delta_hours("2018-07-12 09:00", "2018-07-13 19:00")
print(delta)