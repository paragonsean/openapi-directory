# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.laying_body_resource_collection import LayingBodyResourceCollection


pytestmark = pytest.mark.asyncio

async def test_get_laying_bodies(client):
    """Test case for get_laying_bodies

    Returns all laying bodies.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/LayingBody',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

