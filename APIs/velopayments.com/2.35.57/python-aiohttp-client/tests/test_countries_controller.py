# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.inline_response401 import InlineResponse401
from openapi_server.models.payment_channel_rules_response import PaymentChannelRulesResponse
from openapi_server.models.supported_countries_response import SupportedCountriesResponse
from openapi_server.models.supported_countries_response_v2 import SupportedCountriesResponseV2


pytestmark = pytest.mark.asyncio

async def test_list_payment_channel_rules_v1(client):
    """Test case for list_payment_channel_rules_v1

    List Payment Channel Country Rules
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/paymentChannelRules',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_supported_countries_v1(client):
    """Test case for list_supported_countries_v1

    List Supported Countries
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/supportedCountries',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_supported_countries_v2(client):
    """Test case for list_supported_countries_v2

    List Supported Countries
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/supportedCountries',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

