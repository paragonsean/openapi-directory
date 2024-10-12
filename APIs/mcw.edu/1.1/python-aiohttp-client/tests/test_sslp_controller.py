# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.mapped_sslp import MappedSSLP


pytestmark = pytest.mark.asyncio

async def test_get_mapped_sslpby_position_using_get(client):
    """Test case for get_mapped_sslpby_position_using_get

    Returns a list SSLP for given position and assembly map
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/rgdws/sslps/mapped/{chr}/{start}/{stop}/{map_key}'.format(chr='chr_example', start=56, stop=56, map_key=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

