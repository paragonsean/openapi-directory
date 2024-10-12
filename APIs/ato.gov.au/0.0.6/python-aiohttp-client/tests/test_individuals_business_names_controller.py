# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.business_name import BusinessName
from openapi_server.models.invalid_argument import InvalidArgument
from openapi_server.models.not_found import NotFound
from openapi_server.models.unauthenticated import Unauthenticated


pytestmark = pytest.mark.asyncio

async def test_individuals_party_id_business_names_get(client):
    """Test case for individuals_party_id_business_names_get

    Retrieve a list of business names
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/individuals/{party_id}/business-names'.format(party_id='party_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_individuals_party_id_business_names_post(client):
    """Test case for individuals_party_id_business_names_post

    Create a business name
    """
    body = openapi_server.BusinessName()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'api_key_example',
    }
    response = await client.request(
        method='POST',
        path='/individuals/{party_id}/business-names'.format(party_id='party_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_individuals_party_id_business_names_product_id_delete(client):
    """Test case for individuals_party_id_business_names_product_id_delete

    Delete a business name
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'api_key_example',
    }
    response = await client.request(
        method='DELETE',
        path='/individuals/{party_id}/business-names/{product_id}'.format(party_id='party_id_example', product_id='product_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_individuals_party_id_business_names_product_id_get(client):
    """Test case for individuals_party_id_business_names_product_id_get

    Retrieve a business name
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/individuals/{party_id}/business-names/{product_id}'.format(party_id='party_id_example', product_id='product_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_individuals_party_id_business_names_product_id_put(client):
    """Test case for individuals_party_id_business_names_product_id_put

    Update a business name
    """
    body = openapi_server.BusinessName()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'api_key_example',
    }
    response = await client.request(
        method='PUT',
        path='/individuals/{party_id}/business-names/{product_id}'.format(party_id='party_id_example', product_id='product_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

