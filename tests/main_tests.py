import sys
import unittest

sys.path.append("..") # Fix to allow unittest to search for modules/paths in the parent folder
import src.main
### How to run these tests:
# From within *this* folder (i.e tests/) use
#
#       python -m main_tests    *OR*    python main_tests.py
#
# If running from the (parent) project folder use
#
#       python -m tests.main_tests *OR* python -m unittest discover tests "*_tests.py"
#
# See https://gideonbrimleaf.github.io/2021/01/26/relative-imports-python.html for reference


class Main_Tests(unittest.TestCase):
    def setUp(self) -> None:
        print("Tests set up")

    def test_intDoubler(self):
        self.assertEqual("004", src.main.intDoubler(2))

    def tearDown(self) -> None:
        print("Tests teardown")


# We need the following so it will execute the tests when we run the file in python
if __name__ == '__main__':
    unittest.main()