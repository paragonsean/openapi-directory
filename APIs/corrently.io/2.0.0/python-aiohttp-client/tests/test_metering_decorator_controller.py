# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.metering_get200_response import MeteringGet200Response
from openapi_server.models.metering_post200_response import MeteringPost200Response
from openapi_server.models.metering_post_request import MeteringPostRequest


pytestmark = pytest.mark.asyncio

async def test_metering_get(client):
    """Test case for metering_get

    Meter Reading
    """
    params = [('account', 'account_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2.0/metering/reading',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_metering_post(client):
    """Test case for metering_post

    Meter Reading
    """
    body = openapi_server.MeteringPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2.0/metering/reading',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

