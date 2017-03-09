import core
import unittest


def testDefine(word):
    return core.define(word)


def testSynonym(word):
    return core.synonym(word)


def testAntonym(word):
    return core.antonym(word)


class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(testDefine('python'),
                         {'Noun': ['large Old World boas',
                                   'a soothsaying spirit or a person who is possessed by such a spirit',
                                   '(Greek mythology) dragon killed by Apollo at Delphi']})
        self.assertEqual(testSynonym('happy'), ['cheerful',
                                                'contented', 'overjoyed', 'ecstatic', 'elated'])

        self.assertEqual(testAntonym('happy'), ['melancholy',
                                                'upset', 'disappointed', 'sorrowful', 'unfriendly'])


if __name__ == '__main__':
    unittest.main()
