# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.phrase_response_version import PhraseResponseVersion


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_add_phrases(client):
    """Test case for add_phrases

    Add sentiment-bearing phrases
    """
    sentiment_phrases = None
    params = [('config_id', 'config_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/phrases.{content_type}'.format(content_type='content_type_example'),
        headers=headers,
        json=sentiment_phrases,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_delete_phrases(client):
    """Test case for delete_phrases

    Remove sentiment-bearing phrases
    """
    sentiment_phrase_ids = ['sentiment_phrase_ids_example']
    params = [('config_id', 'config_id_example')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/phrases.{content_type}'.format(content_type='content_type_example'),
        headers=headers,
        json=sentiment_phrase_ids,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_phrases(client):
    """Test case for get_phrases

    Retrieve sentiment-bearing phrases
    """
    params = [('config_id', 'config_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/phrases.{content_type}'.format(content_type='content_type_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_update_phrases(client):
    """Test case for update_phrases

    Updates sentiment-bearing phrases
    """
    sentiment_phrases = None
    params = [('config_id', 'config_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/phrases.{content_type}'.format(content_type='content_type_example'),
        headers=headers,
        json=sentiment_phrases,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

