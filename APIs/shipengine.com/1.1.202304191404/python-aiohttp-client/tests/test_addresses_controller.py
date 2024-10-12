# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.address_to_validate import AddressToValidate
from openapi_server.models.address_validation_result import AddressValidationResult
from openapi_server.models.error_response_body import ErrorResponseBody
from openapi_server.models.parse_address_request_body import ParseAddressRequestBody
from openapi_server.models.parse_address_response_body import ParseAddressResponseBody


pytestmark = pytest.mark.asyncio

async def test_parse_address(client):
    """Test case for parse_address

    Parse an address
    """
    body = {"address":{"address_residential_indicator":true,"country_code":"US"},"text":"Margie McMiller at 3800 North Lamar suite 200 in austin, tx.  The zip code there is 78652."}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/addresses/recognize',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_validate_address(client):
    """Test case for validate_address

    Validate An Address
    """
    body = [{"address_line1":"500 South Buena Vista Street","city_locality":"Burbank","company_name":"The Walt Disney Company","country_code":"US","name":"Mickey and Minnie Mouse","phone":"714-781-4565","postal_code":91521,"state_province":"CA"}]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/addresses/validate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

