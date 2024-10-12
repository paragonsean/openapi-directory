# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.product_list_by_service_default_response import ProductListByServiceDefaultResponse
from openapi_server.models.tag_get_by_product200_response import TagGetByProduct200Response
from openapi_server.models.tag_list_by_product200_response import TagListByProduct200Response


pytestmark = pytest.mark.asyncio

async def test_tag_assign_to_product(client):
    """Test case for tag_assign_to_product

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/products/{product_id}/tags/{tag_id}'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', product_id='product_id_example', tag_id='tag_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tag_detach_from_product(client):
    """Test case for tag_detach_from_product

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/products/{product_id}/tags/{tag_id}'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', product_id='product_id_example', tag_id='tag_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tag_get_by_product(client):
    """Test case for tag_get_by_product

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/products/{product_id}/tags/{tag_id}'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', product_id='product_id_example', tag_id='tag_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tag_get_entity_state_by_product(client):
    """Test case for tag_get_entity_state_by_product

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='HEAD',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/products/{product_id}/tags/{tag_id}'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', product_id='product_id_example', tag_id='tag_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tag_list_by_product(client):
    """Test case for tag_list_by_product

    
    """
    params = [('$filter', 'filter_example'),
                    ('$top', 56),
                    ('$skip', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/products/{product_id}/tags'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', product_id='product_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

