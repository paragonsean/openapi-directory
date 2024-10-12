# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.language_list import LanguageList


pytestmark = pytest.mark.asyncio

async def test_util_languages_get(client):
    """Test case for util_languages_get

    
    """
    params = [('pageSize', 'page_size_example'),
                    ('page', 'page_example')]
    headers = { 
        'Accept': 'application/json',
        'partner_id': 'special-key',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/partner/util/languages',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

