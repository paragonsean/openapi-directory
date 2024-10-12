from typing import List, Dict
from aiohttp import web

from openapi_server.models.audio_file import AudioFile
from openapi_server.models.bigram import Bigram
from openapi_server.models.definition import Definition
from openapi_server.models.example import Example
from openapi_server.models.example_search_results import ExampleSearchResults
from openapi_server.models.frequency_summary import FrequencySummary
from openapi_server.models.related import Related
from openapi_server.models.syllable import Syllable
from openapi_server.models.text_pron import TextPron
from openapi_server import util


async def get_audio(request: web.Request, word, use_canonical=None, limit=None) -> web.Response:
    """Fetches audio metadata for a word.

    The metadata includes a time-expiring fileUrl which allows reading the audio file directly from the API.  Currently only audio pronunciations from the American Heritage Dictionary in mp3 format are supported.

    :param word: Word to get audio for.
    :type word: str
    :param use_canonical: If true will try to return the correct word root (&#39;cats&#39; -&gt; &#39;cat&#39;). If false returns exactly what was requested.
    :type use_canonical: str
    :param limit: Maximum number of results to return
    :type limit: int

    """
    return web.Response(status=200)


async def get_definitions(request: web.Request, word, limit=None, part_of_speech=None, include_related=None, source_dictionaries=None, use_canonical=None, include_tags=None) -> web.Response:
    """Return definitions for a word

    

    :param word: Word to return definitions for
    :type word: str
    :param limit: Maximum number of results to return
    :type limit: int
    :param part_of_speech: CSV list of part-of-speech types
    :type part_of_speech: str
    :param include_related: Return related words with definitions
    :type include_related: str
    :param source_dictionaries: Source dictionary to return definitions from.  If &#39;all&#39; is received, results are returned from all sources. If multiple values are received (e.g. &#39;century,wiktionary&#39;), results are returned from the first specified dictionary that has definitions. If left blank, results are returned from the first dictionary that has definitions. By default, dictionaries are searched in this order: ahd-5, wiktionary, webster, century, wordnet
    :type source_dictionaries: List[str]
    :param use_canonical: If true will try to return the correct word root (&#39;cats&#39; -&gt; &#39;cat&#39;). If false returns exactly what was requested.
    :type use_canonical: str
    :param include_tags: Return a closed set of XML tags in response
    :type include_tags: str

    """
    return web.Response(status=200)


async def get_etymologies(request: web.Request, word, use_canonical=None) -> web.Response:
    """Fetches etymology data

    

    :param word: Word to return
    :type word: str
    :param use_canonical: If true will try to return the correct word root (&#39;cats&#39; -&gt; &#39;cat&#39;). If false returns exactly what was requested.
    :type use_canonical: str

    """
    return web.Response(status=200)


async def get_examples(request: web.Request, word, include_duplicates=None, use_canonical=None, skip=None, limit=None) -> web.Response:
    """Returns examples for a word

    

    :param word: Word to return examples for
    :type word: str
    :param include_duplicates: Show duplicate examples from different sources
    :type include_duplicates: str
    :param use_canonical: If true will try to return the correct word root (&#39;cats&#39; -&gt; &#39;cat&#39;). If false returns exactly what was requested.
    :type use_canonical: str
    :param skip: Results to skip
    :type skip: int
    :param limit: Maximum number of results to return
    :type limit: int

    """
    return web.Response(status=200)


async def get_hyphenation(request: web.Request, word, use_canonical=None, source_dictionary=None, limit=None) -> web.Response:
    """Returns syllable information for a word

    

    :param word: Word to get syllables for
    :type word: str
    :param use_canonical: If true will try to return a correct word root (&#39;cats&#39; -&gt; &#39;cat&#39;). If false returns exactly what was requested.
    :type use_canonical: str
    :param source_dictionary: Get from a single dictionary. Valid options: ahd-5, century, wiktionary, webster, and wordnet.
    :type source_dictionary: str
    :param limit: Maximum number of results to return
    :type limit: int

    """
    return web.Response(status=200)


async def get_phrases(request: web.Request, word, limit=None, wlmi=None, use_canonical=None) -> web.Response:
    """Fetches bi-gram phrases for a word

    

    :param word: Word to fetch phrases for
    :type word: str
    :param limit: Maximum number of results to return
    :type limit: int
    :param wlmi: Minimum WLMI for the phrase
    :type wlmi: int
    :param use_canonical: If true will try to return the correct word root (&#39;cats&#39; -&gt; &#39;cat&#39;). If false returns exactly what was requested.
    :type use_canonical: str

    """
    return web.Response(status=200)


async def get_related_words(request: web.Request, word, use_canonical=None, relationship_types=None, limit_per_relationship_type=None) -> web.Response:
    """Given a word as a string, returns relationships from the Word Graph

    

    :param word: Word to fetch relationships for
    :type word: str
    :param use_canonical: If true will try to return the correct word root (&#39;cats&#39; -&gt; &#39;cat&#39;). If false returns exactly what was requested.
    :type use_canonical: str
    :param relationship_types: Limits the total results per type of relationship type
    :type relationship_types: str
    :param limit_per_relationship_type: Restrict to the supplied relationship types
    :type limit_per_relationship_type: int

    """
    return web.Response(status=200)


async def get_scrabble_score(request: web.Request, word) -> web.Response:
    """Returns the Scrabble score for a word

    

    :param word: Word to get scrabble score for.
    :type word: str

    """
    return web.Response(status=200)


async def get_text_pronunciations(request: web.Request, word, use_canonical=None, source_dictionary=None, type_format=None, limit=None) -> web.Response:
    """Returns text pronunciations for a given word

    

    :param word: Word to get pronunciations for
    :type word: str
    :param use_canonical: If true will try to return a correct word root (&#39;cats&#39; -&gt; &#39;cat&#39;). If false returns exactly what was requested.
    :type use_canonical: str
    :param source_dictionary: Get from a single dictionary
    :type source_dictionary: str
    :param type_format: Text pronunciation type
    :type type_format: str
    :param limit: Maximum number of results to return
    :type limit: int

    """
    return web.Response(status=200)


async def get_top_example(request: web.Request, word, use_canonical=None) -> web.Response:
    """Returns a top example for a word

    

    :param word: Word to fetch examples for
    :type word: str
    :param use_canonical: If true will try to return the correct word root (&#39;cats&#39; -&gt; &#39;cat&#39;). If false returns exactly what was requested.
    :type use_canonical: str

    """
    return web.Response(status=200)


async def get_word_frequency(request: web.Request, word, use_canonical=None, start_year=None, end_year=None) -> web.Response:
    """Returns word usage over time

    

    :param word: Word to return
    :type word: str
    :param use_canonical: If true will try to return the correct word root (&#39;cats&#39; -&gt; &#39;cat&#39;). If false returns exactly what was requested.
    :type use_canonical: str
    :param start_year: Starting Year
    :type start_year: int
    :param end_year: Ending Year
    :type end_year: int

    """
    return web.Response(status=200)
