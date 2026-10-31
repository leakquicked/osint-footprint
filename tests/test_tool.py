import importlib.util,pathlib,unittest
p=pathlib.Path(__file__).resolve().parents[1]/"osint_footprint.py"
s=importlib.util.spec_from_file_location("tool",p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
class Tests(unittest.TestCase):
 def test_empty(self): self.assertEqual(m.analyze_text(""),[])
 def test_result_shape(self):
  result=m.analyze_text("ordinary safe text")
  self.assertIsInstance(result,list)
  for item in result: self.assertIn("severity",item)
if __name__=="__main__": unittest.main()
