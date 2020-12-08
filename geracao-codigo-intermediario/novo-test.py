import unittest
import tatsu
from impiler import Impiler
from pi import run

class TestPiAut(unittest.TestCase):
    def setUp(self):
        imp_grammar_h = open('imp2.ebnf')
        imp_grammar = imp_grammar_h.read()
        imp_grammar_h.close()
        self.parser = tatsu.compile(imp_grammar)

    def __test_pi_aut(self, file_name,resp):
        source_h = open(file_name)
        source = source_h.read()
        source_h.close()
        pi_ast = self.parser.parse(source, semantics=Impiler())
        (trace, step, out, dt) = run(pi_ast, color=False)
        self.assertEqual(str(out), resp)

    def test_exp(self):
        resp ="texto"
        self.__test_pi_aut('exp-test0.imp2', resp)
        
if __name__ == '__main__':
    unittest.main()
