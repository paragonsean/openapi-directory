# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_update_profile_requests import CreateUpdateProfileRequests
from openapi_server.models.document_response import DocumentResponse


pytestmark = pytest.mark.asyncio

async def test_create_new_customer_profilev2(client):
    """Test case for create_new_customer_profilev2

    Create new customer profile
    """
    body = openapi_server.CreateUpdateProfileRequests()
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
        path='/api/dataentities/Client/documents',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_customer_profile(client):
    """Test case for delete_customer_profile

    Delete customer profile
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
        path='/api/dataentities/Client/documents/{id}'.format(id='Client-b818cbda-e489-11e6-94f4-0ac138d2d42e'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_customer_profile(client):
    """Test case for update_customer_profile

    Update customer profile
    """
    body = openapi_server.CreateUpdateProfileRequests()
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
        path='/api/dataentities/Client/documents/{id}'.format(id='Client-b818cbda-e489-11e6-94f4-0ac138d2d42e'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

