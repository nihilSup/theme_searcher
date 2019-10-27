import string
from collections import Counter, defaultdict

tags_phrases = {
    'новости': ['деревья на Садовом кольце', 'добрый автобус', 'выставка IT-технологий'],
    'кухня': ['рецепт борща', 'яблочный пирог', 'тайская кухня'],
    'товары': ['Дети капитана Гранта', 'зимние шины', 'Тайская кухня'],
}


class Searcher(object):

    def __init__(self, tags_phrases):
        tags_index = defaultdict(set)
        phrase_index = defaultdict(set)
        for tag, phrases in tags_phrases.items():
            for phrase in phrases:
                # Proper way is to do lemmatization by nltk and spacy
                phrase = self._clear(phrase)
                tags_index[phrase].add(tag)
                for word in phrase.split():
                    phrase_index[word].add(phrase)
        self.tags_index = tags_index
        self.phrase_index = phrase_index

    def __call__(self, text):
        # one can use tokenize from nltk or spacy packages
        # one have to use lemmatization by nltk and spacy to handle
        # morphology
        text = self._clear(text)
        text_counter = Counter(word.lower() for word in text.split())
        phrases = set()
        for word in text_counter:
            try:
                new_phrases = self.phrase_index[word]
            except KeyError:
                continue
            else:
                phrases |= new_phrases
        tags = set()
        for phrase in phrases:
            # can be optimized if i build counter while constructing indexes or
            # cached
            ph_c = Counter(phrase.split())
            if self._contains(text_counter, ph_c):
                tags |= self.tags_index[phrase]
        return tags

    def _contains(self, container, contained):
        return all(container[k] >= contained[k] for k in contained)

    def _clear(self, text):

        table = str.maketrans('', '', string.punctuation)
        return text.translate(table).lower()
