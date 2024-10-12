# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_address_request import AddAddressRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.get_all_addresses_response import GetAllAddressesResponse


pytestmark = pytest.mark.asyncio

async def test_add_address(client):
    """Test case for add_address

    Claim a new Mailscript address
    """
    body = {"address":"address"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/addresses',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_address(client):
    """Test case for delete_address

    Delete a mailscript address
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/addresses/{address}'.format(address='address_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_addresses(client):
    """Test case for get_all_addresses

    Get all addresses you have access to
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/addresses',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

