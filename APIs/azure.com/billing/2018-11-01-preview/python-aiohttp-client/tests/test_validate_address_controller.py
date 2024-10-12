# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.address import Address
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.validate_address_response import ValidateAddressResponse


pytestmark = pytest.mark.asyncio

async def test_addresses_validate(client):
    """Test case for addresses_validate

    
    """
    address = {"country":"country","firstName":"firstName","lastName":"lastName","city":"city","companyName":"companyName","postalCode":"postalCode","addressLine1":"addressLine1","addressLine2":"addressLine2","addressLine3":"addressLine3","region":"region"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/providers/Microsoft.Billing/validateAddress',
        headers=headers,
        json=address,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

