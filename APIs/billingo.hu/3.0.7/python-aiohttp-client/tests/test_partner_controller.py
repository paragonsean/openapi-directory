# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.client_error_response import ClientErrorResponse
from openapi_server.models.partner import Partner
from openapi_server.models.partner_list import PartnerList
from openapi_server.models.partner_upsert import PartnerUpsert
from openapi_server.models.server_error_response import ServerErrorResponse
from openapi_server.models.validation_error_response import ValidationErrorResponse


pytestmark = pytest.mark.asyncio

async def test_create_partner(client):
    """Test case for create_partner

    Create a partner
    """
    body = {"emails":["emails","emails"],"account_number":"account_number","address":{"country_code":"","address":"address","city":"city","post_code":"post_code"},"phone":"phone","general_ledger_number":"general_ledger_number","iban":"iban","name":"name","taxcode":"taxcode","swift":"swift"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v3/partners',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_partner(client):
    """Test case for delete_partner

    Delete a partner
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v3/partners/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_partner(client):
    """Test case for get_partner

    Retrieve a partner
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/partners/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_partner(client):
    """Test case for list_partner

    List all partners
    """
    params = [('page', 56),
                    ('per_page', 25)]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/partners',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_partner(client):
    """Test case for update_partner

    Update a partner
    """
    body = {"emails":["emails","emails"],"account_number":"account_number","address":{"country_code":"","address":"address","city":"city","post_code":"post_code"},"phone":"phone","general_ledger_number":"general_ledger_number","iban":"iban","name":"name","taxcode":"taxcode","swift":"swift"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v3/partners/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

