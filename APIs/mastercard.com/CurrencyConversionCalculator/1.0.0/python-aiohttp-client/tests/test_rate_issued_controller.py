# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.settlement_rate_issued_request import SettlementRateIssuedRequest


pytestmark = pytest.mark.asyncio

async def test_is_rate_issued_using_get(client):
    """Test case for is_rate_issued_using_get

    Determine if the settlement rate has been issued.
    """
    params = [('date', '_date_example')]
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='GET',
        path='/mcapi/settlement/currencyrate/conversion-rate-issued',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

