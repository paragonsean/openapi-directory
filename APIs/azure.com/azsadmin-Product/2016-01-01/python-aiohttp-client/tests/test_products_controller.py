# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.product_resource import ProductResource
from openapi_server.models.product_resources_page import ProductResourcesPage
from openapi_server.models.products_download200_response import ProductsDownload200Response


pytestmark = pytest.mark.asyncio

async def test_products_download(client):
    """Test case for products_download

    
    """
    params = [('api-version', '2016-01-01')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group}/providers/Microsoft.AzureBridge.Admin/activations/{activation_name}/products/{product_name}/download'.format(subscription_id='subscription_id_example', resource_group='resource_group_example', activation_name='activation_name_example', product_name='product_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products_get(client):
    """Test case for products_get

    
    """
    params = [('api-version', '2016-01-01')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group}/providers/Microsoft.AzureBridge.Admin/activations/{activation_name}/products/{product_name}'.format(subscription_id='subscription_id_example', resource_group='resource_group_example', activation_name='activation_name_example', product_name='product_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products_list(client):
    """Test case for products_list

    
    """
    params = [('api-version', '2016-01-01')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group}/providers/Microsoft.AzureBridge.Admin/activations/{activation_name}/products'.format(subscription_id='subscription_id_example', resource_group='resource_group_example', activation_name='activation_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

