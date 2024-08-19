# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.country_subdivision_response import CountrySubdivisionResponse
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_merchants_v1_countrysubdivision_get(client):
    """Test case for merchants_v1_countrysubdivision_get

    Returns country subdivisions that have Merchants offering the following services: accept contactless-enabled cards and devices, allow customers to add money to an eligible MasterCard or Maestro prepaid card, issue MasterCard Prepaid Travel cards, offer cash at checkout when paying with a Debit MasterCard or Maestro Card. A country subdivision is a segment within a country (ex  state or province).  Please note country subdivisions are only available for the US and Canada. 
    """
    params = [('details', 'topup.repower'),
                    ('country', 'USA')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/merchants/v1/countrysubdivision',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

