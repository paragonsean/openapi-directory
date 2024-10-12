# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.wimstatus200_response import Wimstatus200Response


pytestmark = pytest.mark.asyncio

async def test_wimstatus(client):
    """Test case for wimstatus

    WiM Proess Informtion
    """
    params = [('vid', 'vid_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2.0/wim/status',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

