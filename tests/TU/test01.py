import unittest
import os
from src.main import validate_xml_with_xsd


class TestSomme(unittest.TestCase):
    def test_somme(self):
        current_directory = os.getcwd()
        print(f"Le répertoire courant est: {current_directory}")
        self.assertEqual(validate_xml_with_xsd("files\\f01.xml", "files\\f01.xsd"), True)
        self.assertEqual(validate_xml_with_xsd("files\\f01.xml", "files\\f02.xsd"), False)
        self.assertEqual(validate_xml_with_xsd("files\\f01.xml", "files\\f03.xsd"), False)
        self.assertEqual(validate_xml_with_xsd("files\\f02.xml", "files\\f01.xsd"), False)
        self.assertEqual(validate_xml_with_xsd("files\\f02.xml", "files\\f02.xsd"), False)
        self.assertEqual(validate_xml_with_xsd("files\\f02.xml", "files\\f03.xsd"), False)
        self.assertEqual(validate_xml_with_xsd("files\\f03.xml", "files\\f01.xsd"), False)
        self.assertEqual(validate_xml_with_xsd("files\\f03.xml", "files\\f02.xsd"), False)
        self.assertEqual(validate_xml_with_xsd("files\\f03.xml", "files\\f03.xsd"), False)


if __name__ == '__main__':
    unittest.main()
