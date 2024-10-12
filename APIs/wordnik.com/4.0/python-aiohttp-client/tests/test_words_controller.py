# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.definition_search_results import DefinitionSearchResults
from openapi_server.models.word_object import WordObject
from openapi_server.models.word_of_the_day import WordOfTheDay
from openapi_server.models.word_search_results import WordSearchResults


pytestmark = pytest.mark.asyncio

async def test_get_random_word(client):
    """Test case for get_random_word

    Returns a single random WordObject
    """
    params = [('hasDictionaryDef', 'true'),
                    ('includePartOfSpeech', 'include_part_of_speech_example'),
                    ('excludePartOfSpeech', 'exclude_part_of_speech_example'),
                    ('minCorpusCount', 0),
                    ('maxCorpusCount', -1),
                    ('minDictionaryCount', 1),
                    ('maxDictionaryCount', -1),
                    ('minLength', 5),
                    ('maxLength', -1)]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/v4/words.json/randomWord',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_random_words(client):
    """Test case for get_random_words

    Returns an array of random WordObjects
    """
    params = [('hasDictionaryDef', 'true'),
                    ('includePartOfSpeech', 'include_part_of_speech_example'),
                    ('excludePartOfSpeech', 'exclude_part_of_speech_example'),
                    ('minCorpusCount', 0),
                    ('maxCorpusCount', -1),
                    ('minDictionaryCount', 1),
                    ('maxDictionaryCount', -1),
                    ('minLength', 5),
                    ('maxLength', -1),
                    ('sortBy', 'sort_by_example'),
                    ('sortOrder', 'sort_order_example'),
                    ('limit', 10)]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/v4/words.json/randomWords',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_word_of_the_day(client):
    """Test case for get_word_of_the_day

    Returns a specific WordOfTheDay
    """
    params = [('date', '_date_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/v4/words.json/wordOfTheDay',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reverse_dictionary(client):
    """Test case for reverse_dictionary

    Reverse dictionary search
    """
    params = [('query', 'query_example'),
                    ('findSenseForWord', 'find_sense_for_word_example'),
                    ('includeSourceDictionaries', 'include_source_dictionaries_example'),
                    ('excludeSourceDictionaries', 'exclude_source_dictionaries_example'),
                    ('includePartOfSpeech', 'include_part_of_speech_example'),
                    ('excludePartOfSpeech', 'exclude_part_of_speech_example'),
                    ('minCorpusCount', 5),
                    ('maxCorpusCount', -1),
                    ('minLength', 1),
                    ('maxLength', -1),
                    ('expandTerms', 'expand_terms_example'),
                    ('includeTags', false),
                    ('sortBy', 'sort_by_example'),
                    ('sortOrder', 'sort_order_example'),
                    ('skip', '0'),
                    ('limit', 10)]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/v4/words.json/reverseDictionary',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_words(client):
    """Test case for search_words

    Searches words
    """
    params = [('allowRegex', 'false'),
                    ('caseSensitive', 'true'),
                    ('includePartOfSpeech', 'include_part_of_speech_example'),
                    ('excludePartOfSpeech', 'exclude_part_of_speech_example'),
                    ('minCorpusCount', 5),
                    ('maxCorpusCount', -1),
                    ('minDictionaryCount', 1),
                    ('maxDictionaryCount', -1),
                    ('minLength', 1),
                    ('maxLength', -1),
                    ('skip', 0),
                    ('limit', 10)]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/v4/words.json/search/{query}'.format(query='query_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

