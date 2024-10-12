# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.check_get200_response import CheckGet200Response
from openapi_server.models.check_get_default_response import CheckGetDefaultResponse


pytestmark = pytest.mark.asyncio

async def test_check_get(client):
    """Test case for check_get

    Get Fortnite game status
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/check',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

