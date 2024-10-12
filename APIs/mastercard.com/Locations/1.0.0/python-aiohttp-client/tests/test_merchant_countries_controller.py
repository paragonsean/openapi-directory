# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.countries_response import CountriesResponse
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_merchants_v1_country_get(client):
    """Test case for merchants_v1_country_get

    Returns countries that have Merchants offering the following services: accept contactless-enabled cards and devices, allow customers to add money to an eligible MasterCard or Maestro prepaid card, issue MasterCard Prepaid Travel cards, offer cash at checkout when paying with a Debit MasterCard or Maestro Card. 
    """
    params = [('details', 'acceptance.paypass')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/merchants/v1/country',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

