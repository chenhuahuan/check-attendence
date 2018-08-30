import unittest
import check_attendence


class TestFunc(unittest.TestCase):

    def test_interval_hours_without_date(self):

        begin_time_str = '09:00'
        end_time_str = '18:00'
        break_hours = 1.5
        expected_hours = 7.5

        actual_hours = check_attendence.interval_hours_without_date(begin_time_str,end_time_str,break_hours)
        self.assertEqual(actual_hours,expected_hours)




if __name__ == '__main__':
    unittest.main()