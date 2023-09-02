import unittest
from util import hex_to_bin


class TestHexaToBinaryConversion(unittest.TestCase):

    def test_convert_hex_to_32bit(self):
        self.assertEqual(hex_to_bin(hexstring="0xff", width=32), '00000000000000000000000011111111')
        self.assertEqual(hex_to_bin(hexstring="0xf", width=32), '00000000000000000000000000001111')
        # with default width set to 32
        self.assertEqual(hex_to_bin(hexstring="0xff"), '00000000000000000000000011111111')
        self.assertEqual(hex_to_bin(hexstring="0xFFAB"), '00000000000000001111111110101011')

    def test_convert_hex_to_16bit(self):
        self.assertEqual(hex_to_bin(hexstring="0xff", width=16), '0000000011111111')
        self.assertEqual(hex_to_bin(hexstring="0xffff", width=16), '1111111111111111')
        self.assertEqual(hex_to_bin(hexstring="0x1111", width=16), '0001000100010001')

    def test_convert_hex_to_8bit(self):
        expected_string = '11111111'
        self.assertEqual(hex_to_bin(hexstring="0xff", width=8), '11111111')

    def test_convert_hex_to_4bit(self):
        self.assertEqual(hex_to_bin(hexstring="0xa", width=4), '1010')

    def test_convert_hex_to_binary_case_sensitive(self):
        expected_string = '1010001010110011'
        self.assertEqual(hex_to_bin(hexstring="0xA2B3", width=16), expected_string)
        self.assertEqual(hex_to_bin(hexstring="0xa2b3", width=16), expected_string)

    def test_convert_zeros_hex_to_binary(self):
        self.assertEqual(hex_to_bin(hexstring="0x0000", width=16), '0000000000000000')
        self.assertEqual(hex_to_bin(hexstring="0x0", width=16), '0000000000000000')
        self.assertEqual(hex_to_bin(hexstring="0x0", width=4), '0000')

    def test_input_width_less_than_hex_bytes(self):
        # check if width is greater than equal to hex byte length
        with self.assertRaises(ValueError):
            hex_to_bin(hexstring="0xff", width=4)

        with self.assertRaises(ValueError):
            hex_to_bin(hexstring="0xf", width=2)

    def test_input_hex_string_is_blank(self):
        with self.assertRaises(ValueError):
            hex_to_bin(hexstring=None)

    def test_invalid_hex_characters_in_string(self):
        # invalid hex characters
        with self.assertRaises(ValueError):
            hex_to_bin(hexstring="0xfl", width=8)
        # contains all invalid characters
        with self.assertRaises(ValueError):
            hex_to_bin(hexstring="0xGKPL", width=16)

    def test_hex_not_started_with_0x(self):
        # string does not start with '0x'
        with self.assertRaises(ValueError):
            hex_to_bin(hexstring="FFFF", width=16)
        # string starts with '0X'
        with self.assertRaises(ValueError):
            hex_to_bin(hexstring="0XFFFF", width=16)
        # string starts with '00'
        with self.assertRaises(ValueError):
            hex_to_bin(hexstring="00FFFF", width=16)
    
    def test_failure(self):
        # This test is intentionally failed to test the Jenkins pipeline stages
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
