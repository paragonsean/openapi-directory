# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.merchant_ids import MerchantIds


pytestmark = pytest.mark.asyncio

async def test_get_merchant_identifiers(client):
    """Test case for get_merchant_identifiers

    Returns merchant descriptor and locator information based on the criteria you provide.  Information returned includes merchant DBA name, merchant category code (MCC), street address, city, state, postal code, country, and sales channels.
    """
    params = [('merchant_id', 'DOLIUMPTYLTDWELSHPOOLWA'),
                    ('type', 'ExactMatch')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/merchant-id/v2/merchant-ids',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

