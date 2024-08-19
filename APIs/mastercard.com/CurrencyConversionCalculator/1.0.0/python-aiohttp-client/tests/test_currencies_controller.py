# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.settlement_currency_request import SettlementCurrencyRequest


pytestmark = pytest.mark.asyncio

async def test_get_currency_rate_data_using_get(client):
    """Test case for get_currency_rate_data_using_get

    getCurrencyRateData
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='GET',
        path='/mcapi/settlement/currencyrate/settlement-currencies',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

