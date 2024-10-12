# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_sentences_from_book200_response import GetSentencesFromBook200Response
from openapi_server.models.get_specific_sentence200_response import GetSpecificSentence200Response


pytestmark = pytest.mark.asyncio

async def test_get_sentences(client):
    """Test case for get_sentences

    A random sentence
    """
    params = [('limit', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/sentences',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_sentences_from_book(client):
    """Test case for get_sentences_from_book

    Random sentences from a specific book
    """
    params = [('limit', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/books/{id}/sentences'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_specific_sentence(client):
    """Test case for get_specific_sentence

    A specific sentence
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/sentences/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

