# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData
from aiohttp import FormData
from aiohttp import FormData

from openapi_server.models.check_post200_response import CheckPost200Response
from openapi_server.models.languages_get200_response_inner import LanguagesGet200ResponseInner
from openapi_server.models.words_add_post200_response import WordsAddPost200Response
from openapi_server.models.words_delete_post200_response import WordsDeletePost200Response
from openapi_server.models.words_get200_response import WordsGet200Response


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_check_post(client):
    """Test case for check_post

    Check a text
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('text', 'text_example')
    data.add_field('data', 'data_example')
    data.add_field('language', 'language_example')
    data.add_field('username', 'username_example')
    data.add_field('api_key', 'api_key_example')
    data.add_field('dicts', 'dicts_example')
    data.add_field('mother_tongue', 'mother_tongue_example')
    data.add_field('preferred_variants', 'preferred_variants_example')
    data.add_field('enabled_rules', 'enabled_rules_example')
    data.add_field('disabled_rules', 'disabled_rules_example')
    data.add_field('enabled_categories', 'enabled_categories_example')
    data.add_field('disabled_categories', 'disabled_categories_example')
    data.add_field('enabled_only', False)
    data.add_field('level', 'level_example')
    response = await client.request(
        method='POST',
        path='/v2/check',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_languages_get(client):
    """Test case for languages_get

    Get a list of supported languages.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/languages',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_words_add_post(client):
    """Test case for words_add_post

    Add word to a dictionary
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('word', 'word_example')
    data.add_field('username', 'username_example')
    data.add_field('api_key', 'api_key_example')
    data.add_field('dict', 'dict_example')
    response = await client.request(
        method='POST',
        path='/v2/words/add',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_words_delete_post(client):
    """Test case for words_delete_post

    Remove word from a dictionary
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('word', 'word_example')
    data.add_field('username', 'username_example')
    data.add_field('api_key', 'api_key_example')
    data.add_field('dict', 'dict_example')
    response = await client.request(
        method='POST',
        path='/v2/words/delete',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_words_get(client):
    """Test case for words_get

    List words in dictionaries
    """
    params = [('offset', 56),
                    ('limit', 56),
                    ('username', 'username_example'),
                    ('apiKey', 'api_key_example'),
                    ('dicts', 'dicts_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/words',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

