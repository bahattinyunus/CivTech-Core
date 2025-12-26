import unittest
import civtech_core

class TestCivTechCore(unittest.TestCase):
    def test_version_exists(self):
        self.assertTrue(hasattr(civtech_core, "__version__"))
    
    def test_version_return(self):
        self.assertIn("System Online", civtech_core.version())

if __name__ == "__main__":
    unittest.main()
