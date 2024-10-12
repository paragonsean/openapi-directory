# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.numbers_errors import NumbersErrors
from openapi_server.models.success import Success


pytestmark = pytest.mark.asyncio

async def test_get_random_numbers(client):
    """Test case for get_random_numbers

    
    """
    params = [('gameCode', 'game_code_example'),
                    ('highest', 56),
                    ('lowest', 56),
                    ('count', 56),
                    ('unique', True)]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'api_key_example',
        'api_secret': 'api_secret_example',
        'api_ticket': 'api_ticket_example',
    }
    response = await client.request(
        method='GET',
        path='/v2/numbers/generate/integers',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

