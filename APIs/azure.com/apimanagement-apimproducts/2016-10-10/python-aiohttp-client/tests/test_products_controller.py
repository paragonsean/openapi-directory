# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.product_collection import ProductCollection
from openapi_server.models.product_contract import ProductContract
from openapi_server.models.product_update_parameters import ProductUpdateParameters
from openapi_server.models.products_list_by_service_default_response import ProductsListByServiceDefaultResponse


pytestmark = pytest.mark.asyncio

async def test_products_create_or_update(client):
    """Test case for products_create_or_update

    
    """
    parameters = {"subscriptionsLimit":6,"subscriptionRequired":True,"terms":"terms","approvalRequired":True,"name":"name","description":"description","id":"id","state":"NotPublished"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/products/{product_id}'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', product_id='product_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products_delete(client):
    """Test case for products_delete

    
    """
    params = [('deleteSubscriptions', True),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'if_match': 'if_match_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/products/{product_id}'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', product_id='product_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products_get(client):
    """Test case for products_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/products/{product_id}'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', product_id='product_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products_list_by_service(client):
    """Test case for products_list_by_service

    
    """
    params = [('$filter', 'filter_example'),
                    ('$top', 56),
                    ('$skip', 56),
                    ('expandGroups', True),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/products'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products_update(client):
    """Test case for products_update

    
    """
    parameters = {"subscriptionsLimit":0,"subscriptionRequired":True,"terms":"terms","approvalRequired":True,"name":"name","description":"description","state":"NotPublished"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'if_match': 'if_match_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/products/{product_id}'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', product_id='product_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

