# coding: utf-8

import pytest
import json
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


pytestmark = pytest.mark.asyncio

async def test_get_audio(client):
    """Test case for get_audio

    Fetches audio metadata for a word.
    """
    params = [('useCanonical', false),
                    ('limit', 50)]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/v4/word.json/{word}/audio'.format(word='word_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_definitions(client):
    """Test case for get_definitions

    Return definitions for a word
    """
    params = [('limit', 200),
                    ('partOfSpeech', 'part_of_speech_example'),
                    ('includeRelated', 'false'),
                    ('sourceDictionaries', ['source_dictionaries_example']),
                    ('useCanonical', false),
                    ('includeTags', false)]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/v4/word.json/{word}/definitions'.format(word='word_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_etymologies(client):
    """Test case for get_etymologies

    Fetches etymology data
    """
    params = [('useCanonical', false)]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/v4/word.json/{word}/etymologies'.format(word='word_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_examples(client):
    """Test case for get_examples

    Returns examples for a word
    """
    params = [('includeDuplicates', false),
                    ('useCanonical', false),
                    ('skip', 0),
                    ('limit', 5)]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/v4/word.json/{word}/examples'.format(word='word_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_hyphenation(client):
    """Test case for get_hyphenation

    Returns syllable information for a word
    """
    params = [('useCanonical', false),
                    ('sourceDictionary', 'source_dictionary_example'),
                    ('limit', 50)]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/v4/word.json/{word}/hyphenation'.format(word='word_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_phrases(client):
    """Test case for get_phrases

    Fetches bi-gram phrases for a word
    """
    params = [('limit', 5),
                    ('wlmi', 0),
                    ('useCanonical', false)]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/v4/word.json/{word}/phrases'.format(word='word_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_related_words(client):
    """Test case for get_related_words

    Given a word as a string, returns relationships from the Word Graph
    """
    params = [('useCanonical', false),
                    ('relationshipTypes', 'relationship_types_example'),
                    ('limitPerRelationshipType', 10)]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/v4/word.json/{word}/relatedWords'.format(word='word_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_scrabble_score(client):
    """Test case for get_scrabble_score

    Returns the Scrabble score for a word
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/v4/word.json/{word}/scrabbleScore'.format(word='word_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_text_pronunciations(client):
    """Test case for get_text_pronunciations

    Returns text pronunciations for a given word
    """
    params = [('useCanonical', false),
                    ('sourceDictionary', 'source_dictionary_example'),
                    ('typeFormat', 'type_format_example'),
                    ('limit', 50)]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/v4/word.json/{word}/pronunciations'.format(word='word_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_top_example(client):
    """Test case for get_top_example

    Returns a top example for a word
    """
    params = [('useCanonical', false)]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/v4/word.json/{word}/topExample'.format(word='word_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_word_frequency(client):
    """Test case for get_word_frequency

    Returns word usage over time
    """
    params = [('useCanonical', false),
                    ('startYear', 1800),
                    ('endYear', 2012)]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/v4/word.json/{word}/frequency'.format(word='word_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

