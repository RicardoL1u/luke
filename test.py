from six import text_type
import unittest
# from transformers import BertTokenizer
from paddlenlp.transformers import RobertaTokenizer
# from transformers import LukeTokenizer
import LukeTokenizer
class TestToken(unittest.TestCase):
    def test_token(self):
        tokenizer = RobertaTokenizer.from_pretrained('roberta-wwm-ext')
        text = 'He was a player'
        tokens = tokenizer(text)
        print(text)
        print(tokens)
    def test_trans(self):
        tokenizer = LukeTokenizer.from_pretrained("studio-ousia/luke-base")
        text = "Beyoncé lives in Los Angeles."
        entity_spans = [(0, 7)]
        inputs = tokenizer(text, entity_spans=entity_spans, add_prefix_space=True, return_tensors="np")
        print(inputs)
if __name__ == '__main__':
    unittest.main()