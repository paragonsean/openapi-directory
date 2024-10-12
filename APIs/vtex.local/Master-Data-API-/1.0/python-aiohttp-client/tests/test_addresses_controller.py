# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_update_address_requests import CreateUpdateAddressRequests
from openapi_server.models.document_response import DocumentResponse


pytestmark = pytest.mark.asyncio

async def test_create_new_customer_address(client):
    """Test case for create_new_customer_address

    Create new customer address
    """
    body = openapi_server.CreateUpdateAddressRequests()
    params = [('_schema', 'schema')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/dataentities/Address/documents',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_customer_address(client):
    """Test case for delete_customer_address

    Delete customer address
    """
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/dataentities/Address/documents/{id}'.format(id='Client-b818cbda-e489-11e6-94f4-0ac138d2d42e'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_customer_address(client):
    """Test case for update_customer_address

    Update customer address
    """
    body = openapi_server.CreateUpdateAddressRequests()
    params = [('_schema', 'schema')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/dataentities/Address/documents/{id}'.format(id='Client-b818cbda-e489-11e6-94f4-0ac138d2d42e'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

