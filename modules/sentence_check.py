"""
    @Author => Aman Raj
    @Encoding => UTF-8
    @File Created => 01/02/2023
"""

import sys
import os
import joblib
sys.path.append('./preprocessor.py')
from .preprocessor import PreProcessor
from .basic import path

class SentenceCheck(object):
    def __init__(self) -> None:
        MODEL = os.path.join(path(os.path.abspath(os.path.dirname(__file__))), 'bin', 'models')

        DECODER = os.path.join(path(os.path.abspath(os.path.dirname(__file__))), 'bin', 'decoders')

        TRANSFORMERS = os.path.join(path(os.path.abspath(os.path.dirname(__file__))), 'bin', 'transformers')

        self.PATH = {
            'sentiment': {
                'model': os.path.join(MODEL, "sentiment.pkl"), # r'models\experimental\models\sentiment.pkl'
                'decode': os.path.join(DECODER, 'sentiment.decode'),# r'models\experimental\decoders\sentiment.decode',
                'transformer': os.path.join(TRANSFORMERS, 'sentiment.transform') # r'models\experimental\transformers\sentiment.transform'
            },

            'humor': {
                'model': os.path.join(MODEL, "humor.pkl"),#r'models\experimental\models\humor.pkl',
                'decode': None,
                'transformer': os.path.join(TRANSFORMERS, 'humor.transform')#r'models\experimental\transformers\humor.transform'
            },

            'news': {
                'model': os.path.join(MODEL, "news.pkl"), #r'models\experimental\models\news.pkl',
                'decode': os.path.join(DECODER, 'news.decode'), # r'models\experimental\decoders\news.decode',
                'transformer': os.path.join(TRANSFORMERS, 'news.transform') # r'E:\keras\tf_projects\clock\models\experimental\transformers\news.transform'
            },

            'spam': {
                'model': os.path.join(MODEL, "spam.pkl"), #r'models\experimental\models\spam.pkl',
                'decode': None,
                'transformer': os.path.join(TRANSFORMERS, 'spam.transform')# r'models\experimental\transformers\spam.transform'
            },

            'Language-Detector': {
                'model': os.path.join(MODEL, "language_detector.pkl"),# r'models\experimental\models\language_detector.pkl',
                'decode': None,
                'transformer': None
            }
        }
        self.LOAD = {
            'sentiment': {
                'model': self._loader(self.PATH['sentiment']['model']),
                'decoder': self._loader(self.PATH['sentiment']['decode']),
                'transformer': self._loader(self.PATH['sentiment']['transformer'])
            },

            'humor': {
                'model': self._loader(self.PATH['humor']['model']),
                'transformer': self._loader(self.PATH['humor']['transformer'])
            },

            'news': {
                'model': self._loader(self.PATH['news']['model']),
                'decoder': self._loader(self.PATH['news']['decode']),
                'transformer': self._loader(self.PATH['news']['transformer'])
            },

            'spam': {
                'model': self._loader(self.PATH['spam']['model']),                'transformer': self._loader(self.PATH['spam']['transformer'])
            },
            'Language-Detector': {
                'model': self._loader(self.PATH['Language-Detector']['model'])
            }
        }

    def _loader(self, path:str):
        return joblib.load(path)


    def _decode(self, x, decoder):

        for i, j in decoder.items():
            if x == i:
                return j

    def _model(self, x, model, transformer, decoder, decoding:bool=True):
        clean_ = PreProcessor(path=os.path.join(path(os.path.abspath(os.path.dirname(__file__))), 'bin', 'others'))(x)
        transform_ = transformer.transform([clean_])
        predicted_value = int(model.predict(transform_))
        if decoding:
            decoded = self._decode(predicted_value, decoder)
            return decoded
        else:
            return predicted_value

    def _cleaner(self, x):
        pre = PreProcessor(path=os.path.join(path(os.path.abspath(os.path.dirname(__file__))), 'bin', 'others'))
        x = pre._digit(x)
        x = pre(x)

        return str(x)

    def _function(self, text:str, __news__:bool=False, return_dict=True):
        MODEL = os.path.join(path(os.path.abspath(os.path.dirname(__file__))), 'bin', 'models')

        text = str(text).lower()
        sentiment = self.LOAD['sentiment']
        humor = self.LOAD['humor']
        news = self.LOAD['news']
        spam = self.LOAD['spam']

        sentiment_ = self._model(x=text, model=sentiment['model'], decoder=sentiment['decoder'], transformer=sentiment['transformer'])

        news_ = self._model(x=text, model=news['model'], decoder=news['decoder'], transformer=news['transformer'])

        humor_ = self._model(x=text, model=humor['model'], decoder=None, transformer=humor['transformer'], decoding=False)

        spam_ = self._model(x=text, model=spam['model'], decoder=None, transformer=spam['transformer'], decoding=False)

        __lang__ = self._loader(os.path.join(MODEL, "language_detector.pkl"))
        __lang__ = __lang__.predict([self._cleaner(text)])
        __lang__ = str(__lang__[0]).lower()

        _humor_ = bool(humor_)
        _spam_ = bool(spam_)

        if sentiment_ == 'Neutral' or sentiment_ == 'Positive' or sentiment_ == 'Irrelevant':
            _sentiment_ = True
        else:
            _sentiment_ = False

        if __news__:
            if news_ == 'fake':
                _news_ = False
            else:
                _news_ = True
        else:
            _news_ = None



        if return_dict:
            return {
                'text': text,
                'sentiment': _sentiment_,
                'news': _news_,
                'humor': _humor_,
                'spam': _spam_,
                'language': __lang__
            }
        else:
            return [
                _sentiment_, _news_, _humor_, _spam_, __lang__
            ]


        #{0: 'Irrelevant', 1: 'Negative', 2: 'Neutral', 3: 'Positive'}
        #{0: 'fake', 1: 'real'}

    def __call__(self, text:str, news:bool=False, return_dict:bool=True):

        return self._function(
            text=text,
            __news__=news,
            return_dict=return_dict
        )


# if __name__ == '__main__':
#     x = SentenceCheck()
#     print(x("Do not lose sight of the fact."))
