# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.language_wrapped import LanguageWrapped


pytestmark = pytest.mark.asyncio

async def test_resources_languages_id_json_get(client):
    """Test case for resources_languages_id_json_get

    Get Language by ID
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/resources/languages/{id_jso}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_resources_languages_json_get(client):
    """Test case for resources_languages_json_get

    Get Languages
    """
    params = [('max', 56),
                    ('offset', 56),
                    ('sort', 'sort_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/resources/languages.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

