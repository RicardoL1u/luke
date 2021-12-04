from six import text_type
import unittest
# from transformers import BertTokenizer
from transformers import RobertaTokenizer
# from transformers import LukeTokenizer
from utils import add_end_docstrings
from LukeTokenizer import ENCODE_KWARGS_DOCSTRING,ENCODE_PLUS_ADDITIONAL_KWARGS_DOCSTRING,INIT_TOKENIZER_DOCSTRING
import LukeTokenizer

#funA 作为装饰器函数
def funA(fn):
    print("C语言中文网")
    fn() # 执行传入的fn参数
    print("http://c.biancheng.net")
    return "装饰器函数的返回值"
@funA
def funB():
    print("学习 Python")

def funC():
    print("test callable")

class TestToken(unittest.TestCase):
    # def test_token(self):
    #     tokenizer = RobertaTokenizer.from_pretrained('roberta-wwm-ext')
    #     text = 'He was a player'
    #     tokens = tokenizer(text)
    #     print(text)
    #     print(tokens)
    # def test_trans(self):
    #     tokenizer = LukeTokenizer.from_pretrained("studio-ousia/luke-base")
    #     text = "Beyoncé lives in Los Angeles."
    #     entity_spans = [(0, 7)]
    #     inputs = tokenizer(text, entity_spans=entity_spans, add_prefix_space=True, return_tensors="np")
    #     print(inputs)
    # def test_dec(self):
    #     print(funB)
    # def test_func(self):
    #     print(add_end_docstrings(ENCODE_KWARGS_DOCSTRING, ENCODE_PLUS_ADDITIONAL_KWARGS_DOCSTRING))
        # print(ENCODE_PLUS_ADDITIONAL_KWARGS_DOCSTRING)
    def test_paddleluke(self):
        tokenizer = LukeTokenizer.LukeTokenizer.from_pretrained("./files/")
        print(tokenizer)
if __name__ == '__main__':
    unittest.main()