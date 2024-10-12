from typing import List, Dict
from aiohttp import web

from openapi_server.models.definition_search_results import DefinitionSearchResults
from openapi_server.models.word_object import WordObject
from openapi_server.models.word_of_the_day import WordOfTheDay
from openapi_server.models.word_search_results import WordSearchResults
from openapi_server import util


async def get_random_word(request: web.Request, has_dictionary_def=None, include_part_of_speech=None, exclude_part_of_speech=None, min_corpus_count=None, max_corpus_count=None, min_dictionary_count=None, max_dictionary_count=None, min_length=None, max_length=None) -> web.Response:
    """Returns a single random WordObject

    

    :param has_dictionary_def: Only return words with dictionary definitions
    :type has_dictionary_def: str
    :param include_part_of_speech: CSV part-of-speech values to include (allowable values are noun, adjective, verb, adverb, interjection, pronoun, preposition, abbreviation, affix, article, auxiliary-verb, conjunction, definite-article, family-name, given-name, idiom, imperative, noun-plural, noun-posessive, past-participle, phrasal-prefix, proper-noun, proper-noun-plural, proper-noun-posessive, suffix, verb-intransitive, verb-transitive)
    :type include_part_of_speech: str
    :param exclude_part_of_speech: CSV part-of-speech values to exclude (allowable values are noun, adjective, verb, adverb, interjection, pronoun, preposition, abbreviation, affix, article, auxiliary-verb, conjunction, definite-article, family-name, given-name, idiom, imperative, noun-plural, noun-posessive, past-participle, phrasal-prefix, proper-noun, proper-noun-plural, proper-noun-posessive, suffix, verb-intransitive, verb-transitive)
    :type exclude_part_of_speech: str
    :param min_corpus_count: Minimum corpus frequency for terms
    :type min_corpus_count: int
    :param max_corpus_count: Maximum corpus frequency for terms
    :type max_corpus_count: int
    :param min_dictionary_count: Minimum dictionary count
    :type min_dictionary_count: int
    :param max_dictionary_count: Maximum dictionary count
    :type max_dictionary_count: int
    :param min_length: Minimum word length
    :type min_length: int
    :param max_length: Maximum word length
    :type max_length: int

    """
    return web.Response(status=200)


async def get_random_words(request: web.Request, has_dictionary_def=None, include_part_of_speech=None, exclude_part_of_speech=None, min_corpus_count=None, max_corpus_count=None, min_dictionary_count=None, max_dictionary_count=None, min_length=None, max_length=None, sort_by=None, sort_order=None, limit=None) -> web.Response:
    """Returns an array of random WordObjects

    

    :param has_dictionary_def: Only return words with dictionary definitions
    :type has_dictionary_def: str
    :param include_part_of_speech: CSV part-of-speech values to include (allowable values are noun, adjective, verb, adverb, interjection, pronoun, preposition, abbreviation, affix, article, auxiliary-verb, conjunction, definite-article, family-name, given-name, idiom, imperative, noun-plural, noun-posessive, past-participle, phrasal-prefix, proper-noun, proper-noun-plural, proper-noun-posessive, suffix, verb-intransitive, verb-transitive)
    :type include_part_of_speech: str
    :param exclude_part_of_speech: CSV part-of-speech values to exclude (allowable values are noun, adjective, verb, adverb, interjection, pronoun, preposition, abbreviation, affix, article, auxiliary-verb, conjunction, definite-article, family-name, given-name, idiom, imperative, noun-plural, noun-posessive, past-participle, phrasal-prefix, proper-noun, proper-noun-plural, proper-noun-posessive, suffix, verb-intransitive, verb-transitive)
    :type exclude_part_of_speech: str
    :param min_corpus_count: Minimum corpus frequency for terms
    :type min_corpus_count: int
    :param max_corpus_count: Maximum corpus frequency for terms
    :type max_corpus_count: int
    :param min_dictionary_count: Minimum dictionary count
    :type min_dictionary_count: int
    :param max_dictionary_count: Maximum dictionary count
    :type max_dictionary_count: int
    :param min_length: Minimum word length
    :type min_length: int
    :param max_length: Maximum word length
    :type max_length: int
    :param sort_by: Attribute to sort by
    :type sort_by: str
    :param sort_order: Sort direction
    :type sort_order: str
    :param limit: Maximum number of results to return
    :type limit: int

    """
    return web.Response(status=200)


async def get_word_of_the_day(request: web.Request, _date=None) -> web.Response:
    """Returns a specific WordOfTheDay

    

    :param _date: Fetches by date in yyyy-MM-dd
    :type _date: str

    """
    return web.Response(status=200)


async def reverse_dictionary(request: web.Request, query, find_sense_for_word=None, include_source_dictionaries=None, exclude_source_dictionaries=None, include_part_of_speech=None, exclude_part_of_speech=None, min_corpus_count=None, max_corpus_count=None, min_length=None, max_length=None, expand_terms=None, include_tags=None, sort_by=None, sort_order=None, skip=None, limit=None) -> web.Response:
    """Reverse dictionary search

    

    :param query: Search term
    :type query: str
    :param find_sense_for_word: Restricts words and finds closest sense
    :type find_sense_for_word: str
    :param include_source_dictionaries: Only include these comma-delimited source dictionaries
    :type include_source_dictionaries: str
    :param exclude_source_dictionaries: Exclude these comma-delimited source dictionaries
    :type exclude_source_dictionaries: str
    :param include_part_of_speech: Only include these comma-delimited parts of speech (allowable values are noun, adjective, verb, adverb, interjection, pronoun, preposition, abbreviation, affix, article, auxiliary-verb, conjunction, definite-article, family-name, given-name, idiom, imperative, noun-plural, noun-posessive, past-participle, phrasal-prefix, proper-noun, proper-noun-plural, proper-noun-posessive, suffix, verb-intransitive, verb-transitive)
    :type include_part_of_speech: str
    :param exclude_part_of_speech: Exclude these comma-delimited parts of speech (allowable values are noun, adjective, verb, adverb, interjection, pronoun, preposition, abbreviation, affix, article, auxiliary-verb, conjunction, definite-article, family-name, given-name, idiom, imperative, noun-plural, noun-posessive, past-participle, phrasal-prefix, proper-noun, proper-noun-plural, proper-noun-posessive, suffix, verb-intransitive, verb-transitive)
    :type exclude_part_of_speech: str
    :param min_corpus_count: Minimum corpus frequency for terms
    :type min_corpus_count: int
    :param max_corpus_count: Maximum corpus frequency for terms
    :type max_corpus_count: int
    :param min_length: Minimum word length
    :type min_length: int
    :param max_length: Maximum word length
    :type max_length: int
    :param expand_terms: Expand terms
    :type expand_terms: str
    :param include_tags: Return a closed set of XML tags in response
    :type include_tags: str
    :param sort_by: Attribute to sort by
    :type sort_by: str
    :param sort_order: Sort direction
    :type sort_order: str
    :param skip: Results to skip
    :type skip: str
    :param limit: Maximum number of results to return
    :type limit: int

    """
    return web.Response(status=200)


async def search_words(request: web.Request, query, allow_regex=None, case_sensitive=None, include_part_of_speech=None, exclude_part_of_speech=None, min_corpus_count=None, max_corpus_count=None, min_dictionary_count=None, max_dictionary_count=None, min_length=None, max_length=None, skip=None, limit=None) -> web.Response:
    """Searches words

    

    :param query: Search query
    :type query: str
    :param allow_regex: Search term is a Regular Expression
    :type allow_regex: str
    :param case_sensitive: Search case sensitive
    :type case_sensitive: str
    :param include_part_of_speech: Only include these comma-delimited parts of speech (allowable values are noun, adjective, verb, adverb, interjection, pronoun, preposition, abbreviation, affix, article, auxiliary-verb, conjunction, definite-article, family-name, given-name, idiom, imperative, noun-plural, noun-posessive, past-participle, phrasal-prefix, proper-noun, proper-noun-plural, proper-noun-posessive, suffix, verb-intransitive, verb-transitive)
    :type include_part_of_speech: str
    :param exclude_part_of_speech: Exclude these comma-delimited parts of speech (allowable values are noun, adjective, verb, adverb, interjection, pronoun, preposition, abbreviation, affix, article, auxiliary-verb, conjunction, definite-article, family-name, given-name, idiom, imperative, noun-plural, noun-posessive, past-participle, phrasal-prefix, proper-noun, proper-noun-plural, proper-noun-posessive, suffix, verb-intransitive, verb-transitive)
    :type exclude_part_of_speech: str
    :param min_corpus_count: Minimum corpus frequency for terms
    :type min_corpus_count: int
    :param max_corpus_count: Maximum corpus frequency for terms
    :type max_corpus_count: int
    :param min_dictionary_count: Minimum number of dictionary entries for words returned
    :type min_dictionary_count: int
    :param max_dictionary_count: Maximum dictionary definition count
    :type max_dictionary_count: int
    :param min_length: Minimum word length
    :type min_length: int
    :param max_length: Maximum word length
    :type max_length: int
    :param skip: Results to skip
    :type skip: int
    :param limit: Maximum number of results to return
    :type limit: int

    """
    return web.Response(status=200)
