from nose.tools import *
from ex49 import parser
from ex49 import lexicon



def testing_peek():
    '''testing the peek function.'''
    word_list = lexicon.scan('bear')
    assert_equal(parser.peek(word_list), 'noun')
    assert_equal(parser.peek(None), None)


def testing_match():
    '''testing the match function.'''
    word_list = lexicon.scan('bear')
    assert_equal(parser.match(word_list, 'noun'), ('noun', 'bear'))
    assert_equal(parser.match(word_list, 'direction'), None)
    assert_equal(parser.match(None, 'verb'), None)
    

def testing_skip():
    '''testing the skip function.'''
    word_list = lexicon.scan('bear kill princess')
    assert_equal(word_list, [('noun', 'bear'), ('verb', 'kill'), ('noun', 'princess')])
    parser.skip(word_list, 'noun')
    assert_equal(word_list, [('verb', 'kill'), ('noun', 'princess')])
    
    
def testing_parse_verb():
    '''testing the parse_verb function.'''
    word_list = lexicon.scan('kill at door')
    assert_equal(parser.parse_verb(word_list), ('verb', 'kill'))
    word_list = lexicon.scan('bear kill princess')
    # word_list is assigned with a value in this module, thus not preceeded by parser
    assert_raises(parser.ParseError, parser.parse_verb, word_list)
    
def testing_parse_object():
    '''testing the parse_object function.'''
    word_list = lexicon.scan('the princess')
    assert_equal(parser.parse_object(word_list), ('noun', 'princess'))
    word_list = lexicon.scan('the south')
    assert_equal(parser.parse_object(word_list), ('direction','south'))
    word_list = lexicon.scan('the kill')
    assert_raises(parser.ParseError, parser.parse_object, word_list)
    
def testing_parse_subject():
    '''testing the parse_subject function.'''
    word_list = lexicon.scan('kill princess')
    subj = ('noun', 'bear')    
    foo = parser.parse_subject(word_list, subj)
    assert_equal(foo.assign_tuple(), ('bear', 'kill', 'princess'))
    
def testing_parse_sentence():
    '''testing the parse_sentence function.'''
    word_list = lexicon.scan('the princess eat bear')
    foo = parser.parse_sentence(word_list)
    assert_equal(foo.assign_tuple(), ('princess', 'eat', 'bear'))
    word_list = lexicon.scan('it kill bear')
    foo = parser.parse_sentence(word_list)
    assert_equal(foo.assign_tuple(), ('player', 'kill', 'bear'))
    word_list = lexicon.scan('east it go')
    # here we don't need to assign to 'foo' as it goes straight to else
    # and doesn't return anything unlike the above
    assert_raises(parser.ParseError, parser.parse_sentence, word_list)
