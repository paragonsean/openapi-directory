# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_types_by_id(client):
    """Test case for get_types_by_id

    getTypesById()
    """
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/types/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

