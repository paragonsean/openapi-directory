# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.downloaded_product_resources_page import DownloadedProductResourcesPage
from openapi_server.models.downloaded_products_get200_response import DownloadedProductsGet200Response


pytestmark = pytest.mark.asyncio

async def test_downloaded_products_create(client):
    """Test case for downloaded_products_create

    
    """
    downloaded_product = openapi_server.DownloadedProductsGet200Response()
    params = [('api-version', '2016-01-01')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group}/providers/Microsoft.AzureBridge.Admin/activations/{activation_name}/downloadedProducts/{product_name}'.format(subscription_id='subscription_id_example', resource_group='resource_group_example', activation_name='activation_name_example', product_name='product_name_example'),
        headers=headers,
        json=downloaded_product,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_downloaded_products_delete(client):
    """Test case for downloaded_products_delete

    
    """
    params = [('api-version', '2016-01-01')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group}/providers/Microsoft.AzureBridge.Admin/activations/{activation_name}/downloadedProducts/{product_name}'.format(subscription_id='subscription_id_example', resource_group='resource_group_example', activation_name='activation_name_example', product_name='product_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_downloaded_products_get(client):
    """Test case for downloaded_products_get

    
    """
    params = [('api-version', '2016-01-01')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group}/providers/Microsoft.AzureBridge.Admin/activations/{activation_name}/downloadedProducts/{product_name}'.format(subscription_id='subscription_id_example', resource_group='resource_group_example', activation_name='activation_name_example', product_name='product_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_downloaded_products_list(client):
    """Test case for downloaded_products_list

    
    """
    params = [('api-version', '2016-01-01')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group}/providers/Microsoft.AzureBridge.Admin/activations/{activation_name}/downloadedProducts'.format(subscription_id='subscription_id_example', resource_group='resource_group_example', activation_name='activation_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

