# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bots_info_error_schema import BotsInfoErrorSchema
from openapi_server.models.bots_info_schema import BotsInfoSchema


pytestmark = pytest.mark.asyncio

async def test_bots_info(client):
    """Test case for bots_info

    
    """
    params = [('token', 'token_example'),
                    ('bot', 'bot_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/bots.info',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

