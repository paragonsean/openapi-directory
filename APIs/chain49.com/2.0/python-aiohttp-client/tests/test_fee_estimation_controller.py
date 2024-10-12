# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_estimate_fee_v2200_response import GetEstimateFeeV2200Response


pytestmark = pytest.mark.asyncio

async def test_get_estimate_fee_v2(client):
    """Test case for get_estimate_fee_v2

    Estimate transaction fee V2
    """
    headers = { 
        'Accept': 'application/json',
        'X-RapidAPI-Host': 'special-key',
        'X-API-Key': 'special-key',
        'X-RapidAPI-Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/{blockchain}/v2/estimatefee/{confirmation_target}'.format(blockchain='bitcoin', confirmation_target=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

