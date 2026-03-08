import unittest
import os
from vishal_info import MobileInfo, lookup, quick_lookup

class TestMobileInfo(unittest.TestCase):
    
    def setUp(self):
        self.api_key = os.getenv('VISHAI_API_KEY', 'Errnkeor01')
        self.valid_mobile = "7068715523"
        self.invalid_mobile = "123"
    
    def test_init_with_key(self):
        info = MobileInfo(api_key="test")
        self.assertEqual(info.api_key, "test")
    
    def test_validate_mobile_valid(self):
        info = MobileInfo(api_key="test")
        cleaned = info._validate_mobile(self.valid_mobile)
        self.assertEqual(cleaned, self.valid_mobile)
    
    def test_validate_mobile_invalid(self):
        info = MobileInfo(api_key="test")
        with self.assertRaises(ValueError):
            info._validate_mobile(self.invalid_mobile)
    
    def test_format_address(self):
        info = MobileInfo(api_key="test")
        test_addr = "S/O Shyam Lal!!40 Genda Kaboola!!Genda Kabola Jhansi!Uttar Pradesh!284302"
        expected = "S/O Shyam Lal, 40 Genda Kaboola, Genda Kabola Jhansi, Uttar Pradesh, 284302"
        self.assertEqual(info.format_address(test_addr), expected)
    
    def test_actual_api_call(self):
        """This test actually calls the API - use with caution"""
        if self.api_key:
            info = MobileInfo(api_key=self.api_key)
            data = info.get_info(self.valid_mobile)
            self.assertIsNotNone(data)
    
    def test_lookup_function(self):
        if self.api_key:
            data = lookup(self.valid_mobile, api_key=self.api_key)
            self.assertIsNotNone(data)

if __name__ == '__main__':
    unittest.main()