# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.language import Language
from openapi_server.models.store import Store


pytestmark = pytest.mark.asyncio

async def test_store_info_json_get(client):
    """Test case for store_info_json_get

    Retrieve Store Information.
    """
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/store/info.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_store_languages_json_get(client):
    """Test case for store_languages_json_get

    Retrieve Store Languages.
    """
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/store/languages.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

