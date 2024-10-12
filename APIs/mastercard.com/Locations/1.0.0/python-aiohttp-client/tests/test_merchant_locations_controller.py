# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.merchants_response import MerchantsResponse


pytestmark = pytest.mark.asyncio

async def test_merchants_v1_merchant_get(client):
    """Test case for merchants_v1_merchant_get

    Returns merchant location information for merchants offering the following services: accept contactless-enabled cards and devices, allow customers to add money to an eligible MasterCard or Maestro prepaid card, issue MasterCard Prepaid Travel cards, participate in the MasterCard Easy Savings program, and offer cash at checkout when paying with a Debit MasterCard or Maestro Card. 
    """
    params = [('Details', 'acceptance.paypass'),
                    ('PageOffset', 0),
                    ('PageLength', 5),
                    ('Category', 'features.cashback'),
                    ('AddressLine1', '42 Elm Street'),
                    ('AddressLine2', 'Suite 101'),
                    ('City', 'New York'),
                    ('CountrySubdivision', 'NY'),
                    ('PostalCode', '11001'),
                    ('Country', 'USA'),
                    ('Latitude', 38.53463),
                    ('Longitude', -90.286781),
                    ('DistanceUnit', 'MILE'),
                    ('Radius', 25),
                    ('OfferMerchantID', '34760')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/merchants/v1/merchant',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

