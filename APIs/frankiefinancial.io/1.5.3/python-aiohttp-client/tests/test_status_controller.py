# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_object import ErrorObject
from openapi_server.models.puppy_object import PuppyObject


pytestmark = pytest.mark.asyncio

async def test_status_check(client):
    """Test case for status_check

    Service Status
    """
    params = [('askingNicely', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/compliance/v1.2/ruok',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

