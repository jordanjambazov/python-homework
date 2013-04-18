import unittest

from solution import Person


class PersonTests(unittest.TestCase):
    def setUp(self):
        self.jordan = Person('Jordan', 1993, 'M')
        self.momchil = Person('Momchil', 1993, 'M')
        self.july = Person('July', 1963, 'F')
        self.anton = Person('Anton', 1966, 'M')
        self.iva = Person('Iva', 1983, 'F')
        self.nikol = Person('Nikol', 2002, 'F')
        self.boris = Person('Boris', 1999, 'M')

        self.july.add_child(self.iva)
        self.july.add_child(self.momchil)
        self.july.add_child(self.jordan)

        self.anton.add_child(self.momchil)
        self.anton.add_child(self.jordan)

        self.nikol.add_parent(self.iva)

    def test_iva_is_child_of_july(self):
        self.assertIn(self.iva, self.july.children())
        self.assertIn(self.iva, self.july.children(gender='F'))

    def test_iva_is_not_male_child_of_july(self):
        self.assertNotIn(self.iva, self.july.children(gender='M'))

    def test_jordan_and_momchil_are_children_of_anton_and_july(self):
        self.assertIn(self.jordan, self.july.children(gender='M'))
        self.assertIn(self.momchil, self.july.children(gender='M'))
        self.assertIn(self.jordan, self.anton.children())
        self.assertIn(self.momchil, self.anton.children())

    def test_jordan_and_momchil_are_not_female_children_of_anton(self):
        self.assertNotIn(self.jordan, self.anton.children(gender='F'))
        self.assertNotIn(self.momchil, self.anton.children(gender='F'))

    def test_iva_is_not_child_of_anton(self):
        self.assertNotIn(self.iva, self.anton.children())

    def test_nikol_is_child_of_iva(self):
        self.assertIn(self.nikol, self.iva.children())

    def test_iva_is_mother_of_nikol(self):
        self.assertEqual(self.iva, self.nikol.mother)

    def test_iva_is_not_father_of_nikol(self):
        self.assertNotEqual(self.iva, self.nikol.father)

    def test_parent_not_too_young(self):
        self.assertNotIn(self.boris, self.iva.children())

    def test_jordan_and_momchil_are_brothers(self):
        self.assertIn(self.jordan, self.momchil.get_brothers())
        self.assertIn(self.momchil, self.jordan.get_brothers())

    def test_iva_is_sister_of_jordan_and_momchil(self):
        self.assertIn(self.iva, self.momchil.get_sisters())
        self.assertIn(self.iva, self.jordan.get_sisters())

    def test_jordan_is_brother_of_iva(self):
        self.assertIn(self.jordan, self.iva.get_brothers())
        self.assertNotIn(self.jordan, self.iva.get_sisters())

    def test_jordan_is_direct_successor_of_anton_and_july(self):
        self.assertTrue(self.anton.is_direct_successor(self.jordan))
        self.assertTrue(self.july.is_direct_successor(self.jordan))

    def test_nikol_is_not_direct_successor_of_momchil(self):
        self.assertFalse(self.nikol.is_direct_successor(self.momchil))
        self.assertFalse(self.momchil.is_direct_successor(self.nikol))

if __name__ == '__main__':
    unittest.main()
