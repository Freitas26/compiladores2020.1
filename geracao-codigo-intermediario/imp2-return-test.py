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

#testa fatorial de 15
    def test_fat(self):
        resp = "[1307674368000]"
        self.__test_pi_aut('examples/fat-func.imp2', resp)

#testa fibo de 15
    def test_fibo(self):
        resp = "[[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]]"
        self.__test_pi_aut('examples/fibo-func.imp2', resp)
        
if __name__ == '__main__':
    unittest.main()
