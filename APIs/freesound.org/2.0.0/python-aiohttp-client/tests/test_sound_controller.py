# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.sound import Sound


pytestmark = pytest.mark.asyncio

async def test_get_sound_by_id(client):
    """Test case for get_sound_by_id

    Details of a sound
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/apiv2/sounds/{sound_id}'.format(sound_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

