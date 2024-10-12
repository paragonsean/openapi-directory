# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.availability import Availability
from openapi_server.models.problem import Problem


pytestmark = pytest.mark.asyncio

async def test_feed_availability_get(client):
    """Test case for feed_availability_get

    Gets availability of featured feed content for the apps by wiki domain.
    """
    headers = { 
        'Accept': 'application/problem+json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest_v1/feed/availability',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

