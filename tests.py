import unittest

from theme_searcher.searcher import Searcher


class TestSearcherIndexes(unittest.TestCase):
    def test_index_building(self):
        tags_phrases = {
            'кухня': ['рецепт борща', 'яблочный пирог', 'тайская кухня'],
            'товары': ['Дети капитана Гранта', 'зимние шины', 'Тайская кухня'],
        }
        s = Searcher(tags_phrases)
        self.assertDictEqual(s.tags_index, {'дети капитана гранта': {'товары'},
                                            'зимние шины': {'товары'},
                                            'рецепт борща': {'кухня'},
                                            'тайская кухня': {'кухня', 'товары'},
                                            'яблочный пирог': {'кухня'}})
        self.assertDictEqual(s.phrase_index, {'борща': {'рецепт борща'},
                                              'гранта': {'дети капитана гранта'},
                                              'дети': {'дети капитана гранта'},
                                              'зимние': {'зимние шины'},
                                              'капитана': {'дети капитана гранта'},
                                              'кухня': {'тайская кухня'},
                                              'пирог': {'яблочный пирог'},
                                              'рецепт': {'рецепт борща'},
                                              'тайская': {'тайская кухня'},
                                              'шины': {'зимние шины'},
                                              'яблочный': {'яблочный пирог'}})


class TestSearch(unittest.TestCase):
    def setUp(self):
        self.searcher = Searcher({
            'новости': ['деревья на Садовом кольце', 'добрый автобус', 'выставка IT-технологий'],
            'кухня': ['рецепт борща', 'яблочный пирог', 'тайская кухня'],
            'товары': ['Дети капитана Гранта', 'зимние шины', 'Тайская кухня', 'игрушка автобус дети'],
        })

    def test_empty(self):
        self.assertSetEqual(self.searcher(''), set())

    def test_simple_query(self):
        res = self.searcher('рецепт вкусного борща как у мамы')
        self.assertSetEqual(res, {'кухня'})

    def test_punct(self):
        res = self.searcher('выставка it-технологий "blabla"')
        self.assertSetEqual(res, {'новости'})

    def test_cross_query(self):
        res = self.searcher('где купить хорошие зимние шины для добрый автобус')
        self.assertSetEqual(res, {'новости', 'товары'})

    def test_upper(self):
        res = self.searcher('куда пойти на выставка it-технологий "Тайская кухня"')
        self.assertSetEqual(res, {'кухня', 'новости', 'товары'})
