# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.caller_id import CallerId


pytestmark = pytest.mark.asyncio

async def test_v2_phone_numbers_caller_ids_json_get(client):
    """Test case for v2_phone_numbers_caller_ids_json_get

    List caller ids
    """
    params = [('phone_number', 'phone_number_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/v2/phone_numbers/caller_ids.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

