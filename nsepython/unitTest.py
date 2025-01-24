import unittest
from datetime import datetime
import pytz
from rahu import running_status,open_interest_spurts,nse_custom_function_secfno

class TestRunningStatus(unittest.TestCase):
    def setUp(self):
        # Define the timezone
        self.india_tz = pytz.timezone("Asia/Calcutta")

    def test_running_status_during_market_hours(self):
        # Simulate time during market hours (10:00 AM IST)
        mock_time = datetime(2025, 1, 24, 10, 0, 0, tzinfo=self.india_tz)
        self.assertTrue(running_status(mock_time))

    def test_running_status_before_market_open(self):
        # Simulate time before market hours (8:00 AM IST)
        mock_time = datetime(2025, 1, 24, 8, 0, 0, tzinfo=self.india_tz)
        self.assertFalse(running_status(mock_time))

    def test_running_status_after_market_close(self):
        # Simulate time after market hours (4:00 PM IST)
        mock_time = datetime(2025, 1, 24, 16, 0, 0, tzinfo=self.india_tz)
        self.assertFalse(running_status(mock_time))

    def test_running_status_at_market_open(self):
        # Simulate time exactly at market open (9:15 AM IST)
        mock_time = datetime(2025, 1, 24, 9, 15, 0, tzinfo=self.india_tz)
        self.assertFalse(running_status(mock_time))  # Exact boundary is not considered "inside"

    def test_running_status_at_market_close(self):
        # Simulate time exactly at market close (3:30 PM IST)
        mock_time = datetime(2025, 1, 24, 15, 30, 0, tzinfo=self.india_tz)
        self.assertTrue(running_status(mock_time))  # Exact boundary is not considered "inside"

    def test_get_open_interest_spurts(self):
        print(open_interest_spurts())
        
    def test_nse_custom_function_secfno(self):
        print(nse_custom_function_secfno(["RELIANCE"]))

if __name__ == "__main__":
    unittest.main()
