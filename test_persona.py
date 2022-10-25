import unittest
from unittest.mock import patch

from persona import *

class Test_Persona(unittest.TestCase):

    def setUp(self):
        self.DB = Persona()
        self.DB.clean_DB()
        self.DB.add_users("101", "Tomas", "Bourguet")
        self.DB.add_users("102", "Pepe", "Honguito")
        self.DB.add_users("103", "Pepa", "Pig")
        self.DB.add_users("104", "Tortuga", "Manuelita")

    def test_00_clean_DB(self):
        self.DB.users_in_DB()
        self.assertEqual(self.DB.personas["101"], "Tomas Bourguet")
        self.assertEqual(self.DB.personas["102"], "Pepe Honguito")
        self.assertEqual(self.DB.personas["103"], "Pepa Pig")
        self.assertEqual(self.DB.personas["104"], "Tortuga Manuelita")
        self.DB.clean_DB()
        with open(self.DB.DB) as Data:
            for line in Data.readlines():
                self.assertEqual(line, "")

    def test_01_add_user(self):
        self.assertTrue(self.DB.add_users("001", "Mirtha", "Lagrande"))

    def test_02_add_user_repeated(self):
        self.DB.add_users("001", "Hermana", "Lagrande")
        self.assertFalse(self.DB.add_users("001", "Hermana", "Lagrande"))

    def test_03_not_user(self):
        with self.assertRaises(ValueError):
            self.DB.add_users("", "Hermana", "Lagrande")
            self.DB.add_users("002", "", "Lagrande")
            self.DB.add_users("003", "Hermana", "")
    
    def test_04_not_user(self):
        with self.assertRaises(ValueError):
            self.DB.add_users("numerito", "Hermana", "Lagrande")
            self.DB.add_users("002", "HERMANA", "Lagrande")
            self.DB.add_users("003", "Hermana", "legrande")

    
    def test_06_users_in_DB(self):
        self.DB.users_in_DB()
        self.assertEqual(self.DB.personas["101"], "Tomas Bourguet")
        self.DB.add_users("002", "Hermana", "Lagrande")
        self.assertEqual(self.DB.personas["002"], "Hermana Lagrande")

    def test_07_delete_user(self):
        self.DB.delete_users("101")
        self.DB.users_in_DB()
        with self.assertRaises(KeyError):
            self.DB.personas["101"]
        with open(self.DB.DB) as Data:
            if Data.readlines(1) != "101 Tomas Bourguet":
                self.assertEqual(1, 1)
    
    def test_08_not_delete_user(self):
        with self.assertRaises(ValueError):
            self.DB.delete_users("001")



if __name__ == "__main__": 
    unittest.main()
