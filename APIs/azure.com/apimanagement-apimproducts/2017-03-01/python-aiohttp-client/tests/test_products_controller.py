# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.product_collection import ProductCollection
from openapi_server.models.product_contract import ProductContract
from openapi_server.models.product_list_default_response import ProductListDefaultResponse
from openapi_server.models.product_update_parameters import ProductUpdateParameters


pytestmark = pytest.mark.asyncio

async def test_product_create_or_update(client):
    """Test case for product_create_or_update

    
    """
    parameters = {"id":"id"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/products/{product_id}'.format(product_id='product_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_delete(client):
    """Test case for product_delete

    
    """
    params = [('deleteSubscriptions', True),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'if_match': 'if_match_example',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/products/{product_id}'.format(product_id='product_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_get(client):
    """Test case for product_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/products/{product_id}'.format(product_id='product_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_list(client):
    """Test case for product_list

    
    """
    params = [('$filter', 'filter_example'),
                    ('$top', 56),
                    ('$skip', 56),
                    ('expandGroups', True),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/products',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_update(client):
    """Test case for product_update

    
    """
    parameters = {"name":"name"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'if_match': 'if_match_example',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/products/{product_id}'.format(product_id='product_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

