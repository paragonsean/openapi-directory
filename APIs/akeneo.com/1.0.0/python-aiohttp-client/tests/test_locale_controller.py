# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_locales_code200_response import GetLocalesCode200Response
from openapi_server.models.locales import Locales
from openapi_server.models.post_token400_response import PostToken400Response


pytestmark = pytest.mark.asyncio

async def test_get_locales(client):
    """Test case for get_locales

    Get a list of locales
    """
    params = [('search', 'search_example'),
                    ('page', 1),
                    ('limit', 10),
                    ('with_count', False)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/locales',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_locales_code(client):
    """Test case for get_locales_code

    Get a locale
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/locales/{code}'.format(code='code_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

