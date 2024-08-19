# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.electronic_address_type import ElectronicAddressType
from openapi_server.models.not_found import NotFound
from openapi_server.models.unauthenticated import Unauthenticated


pytestmark = pytest.mark.asyncio

async def test_classifications_electronic_address_types_get(client):
    """Test case for classifications_electronic_address_types_get

    Retrieve a list of electronic address types
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/classifications/electronic-address-types',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

