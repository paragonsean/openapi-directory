# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.device_configuration import DeviceConfiguration
from openapi_server.models.extended_product import ExtendedProduct
from openapi_server.models.marketplace_product_log_update import MarketplaceProductLogUpdate
from openapi_server.models.product import Product
from openapi_server.models.product_list import ProductList
from openapi_server.models.product_log import ProductLog
from openapi_server.models.products_list_default_response import ProductsListDefaultResponse


pytestmark = pytest.mark.asyncio

async def test_products_get(client):
    """Test case for products_get

    
    """
    params = [('api-version', '2017-06-01')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group}/providers/Microsoft.AzureStack/registrations/{registration_name}/products/{product_name}'.format(subscription_id='subscription_id_example', resource_group='resource_group_example', registration_name='registration_name_example', product_name='product_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products_get_product(client):
    """Test case for products_get_product

    
    """
    device_configuration = {"identitySystem":"AzureAD","deviceVersion":"deviceVersion"}
    params = [('api-version', '2017-06-01')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group}/providers/Microsoft.AzureStack/registrations/{registration_name}/products/{product_name}/GetProduct'.format(subscription_id='subscription_id_example', resource_group='resource_group_example', registration_name='registration_name_example', product_name='product_name_example'),
        headers=headers,
        json=device_configuration,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products_get_products(client):
    """Test case for products_get_products

    
    """
    device_configuration = {"identitySystem":"AzureAD","deviceVersion":"deviceVersion"}
    params = [('api-version', '2017-06-01')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group}/providers/Microsoft.AzureStack/registrations/{registration_name}/products/_all/GetProducts'.format(subscription_id='subscription_id_example', resource_group='resource_group_example', registration_name='registration_name_example'),
        headers=headers,
        json=device_configuration,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products_list(client):
    """Test case for products_list

    
    """
    params = [('api-version', '2017-06-01')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group}/providers/Microsoft.AzureStack/registrations/{registration_name}/products'.format(subscription_id='subscription_id_example', resource_group='resource_group_example', registration_name='registration_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products_list_details(client):
    """Test case for products_list_details

    
    """
    params = [('api-version', '2017-06-01')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group}/providers/Microsoft.AzureStack/registrations/{registration_name}/products/{product_name}/listDetails'.format(subscription_id='subscription_id_example', resource_group='resource_group_example', registration_name='registration_name_example', product_name='product_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products_upload_log(client):
    """Test case for products_upload_log

    
    """
    marketplace_product_log_update = {"details":"details","error":"error","operation":"operation","status":"status"}
    params = [('api-version', '2017-06-01')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group}/providers/Microsoft.AzureStack/registrations/{registration_name}/products/{product_name}/uploadProductLog'.format(subscription_id='subscription_id_example', resource_group='resource_group_example', registration_name='registration_name_example', product_name='product_name_example'),
        headers=headers,
        json=marketplace_product_log_update,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

