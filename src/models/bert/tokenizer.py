import transformers

import src.models.bert.parameters

class Tokenizer:

    def __init__(self):

        self.__parameters = src.models.bert.parameters.Parameters()

    def __call__(self):

        # Tokenizer
        return transformers.BertTokenizerFast.from_pretrained(
            pretrained_model_name_or_path=self.__parameters.pretrained_model_name)
