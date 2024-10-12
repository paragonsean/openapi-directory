# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.electronic_address import ElectronicAddress
from openapi_server.models.invalid_argument import InvalidArgument
from openapi_server.models.not_found import NotFound
from openapi_server.models.unauthenticated import Unauthenticated


pytestmark = pytest.mark.asyncio

async def test_organisations_party_id_electronic_addresses_address_id_delete(client):
    """Test case for organisations_party_id_electronic_addresses_address_id_delete

    Delete an electronic address
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'api_key_example',
    }
    response = await client.request(
        method='DELETE',
        path='/organisations/{party_id}/electronic-addresses/{address_id}'.format(party_id='party_id_example', address_id='address_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_organisations_party_id_electronic_addresses_address_id_get(client):
    """Test case for organisations_party_id_electronic_addresses_address_id_get

    Retrieve an electronic address
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/organisations/{party_id}/electronic-addresses/{address_id}'.format(party_id='party_id_example', address_id='address_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_organisations_party_id_electronic_addresses_address_id_put(client):
    """Test case for organisations_party_id_electronic_addresses_address_id_put

    Update an electronic address
    """
    body = openapi_server.ElectronicAddress()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'api_key_example',
    }
    response = await client.request(
        method='PUT',
        path='/organisations/{party_id}/electronic-addresses/{address_id}'.format(party_id='party_id_example', address_id='address_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_organisations_party_id_electronic_addresses_get(client):
    """Test case for organisations_party_id_electronic_addresses_get

    Retrieve a list of electronic addresses
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/organisations/{party_id}/electronic-addresses'.format(party_id='party_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_organisations_party_id_electronic_addresses_post(client):
    """Test case for organisations_party_id_electronic_addresses_post

    Create an electronic address
    """
    body = openapi_server.ElectronicAddress()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'api_key_example',
    }
    response = await client.request(
        method='POST',
        path='/organisations/{party_id}/electronic-addresses'.format(party_id='party_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

