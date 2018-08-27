
import datetime

def interval_hours(begin_time_str, end_time_str ):

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

    interval = end_dt - start_dt

    return (interval.days*24*3600 + interval.seconds) / 3600

def interval_hours_without_date(begin_time_str, end_time_str ):

    start_dt = datetime.datetime.strptime(begin_time_str, "%H:%M")
    end_dt = datetime.datetime.strptime(end_time_str, "%H:%M")

    interval = end_dt - start_dt
    return (interval.days*24*3600 + interval.seconds) / 3600


delta = interval_hours("2018-07-12 09:10", "2018-07-13 19:00")
print(delta)

delta2 = interval_hours_without_date("09:00", "19:00")
print(delta2)