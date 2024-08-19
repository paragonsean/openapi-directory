# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.invalid_argument import InvalidArgument
from openapi_server.models.license import License
from openapi_server.models.not_found import NotFound
from openapi_server.models.unauthenticated import Unauthenticated


pytestmark = pytest.mark.asyncio

async def test_individuals_party_id_licenses_get(client):
    """Test case for individuals_party_id_licenses_get

    Retrieve a list of licenses
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/individuals/{party_id}/licenses'.format(party_id='party_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_individuals_party_id_licenses_post(client):
    """Test case for individuals_party_id_licenses_post

    Create a license
    """
    body = openapi_server.License()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'api_key_example',
    }
    response = await client.request(
        method='POST',
        path='/individuals/{party_id}/licenses'.format(party_id='party_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_individuals_party_id_licenses_product_id_delete(client):
    """Test case for individuals_party_id_licenses_product_id_delete

    Delete a license
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'api_key_example',
    }
    response = await client.request(
        method='DELETE',
        path='/individuals/{party_id}/licenses/{product_id}'.format(party_id='party_id_example', product_id='product_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_individuals_party_id_licenses_product_id_get(client):
    """Test case for individuals_party_id_licenses_product_id_get

    Retrieve a license
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/individuals/{party_id}/licenses/{product_id}'.format(party_id='party_id_example', product_id='product_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_individuals_party_id_licenses_product_id_put(client):
    """Test case for individuals_party_id_licenses_product_id_put

    Update a license
    """
    body = openapi_server.License()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'api_key_example',
    }
    response = await client.request(
        method='PUT',
        path='/individuals/{party_id}/licenses/{product_id}'.format(party_id='party_id_example', product_id='product_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

