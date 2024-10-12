# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.product_api_create_or_update200_response import ProductApiCreateOrUpdate200Response
from openapi_server.models.product_api_list_by_product200_response import ProductApiListByProduct200Response
from openapi_server.models.product_list_default_response import ProductListDefaultResponse


pytestmark = pytest.mark.asyncio

async def test_product_api_create_or_update(client):
    """Test case for product_api_create_or_update

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/products/{product_id}/apis/{api_id}'.format(product_id='product_id_example', api_id='api_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_api_delete(client):
    """Test case for product_api_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/products/{product_id}/apis/{api_id}'.format(product_id='product_id_example', api_id='api_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_api_list_by_product(client):
    """Test case for product_api_list_by_product

    
    """
    params = [('$filter', 'filter_example'),
                    ('$top', 56),
                    ('$skip', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/products/{product_id}/apis'.format(product_id='product_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

