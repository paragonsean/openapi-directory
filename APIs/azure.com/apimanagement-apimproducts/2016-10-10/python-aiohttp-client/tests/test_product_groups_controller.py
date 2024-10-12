# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.product_groups_list_by_products200_response import ProductGroupsListByProducts200Response
from openapi_server.models.products_list_by_service_default_response import ProductsListByServiceDefaultResponse


pytestmark = pytest.mark.asyncio

async def test_product_groups_create(client):
    """Test case for product_groups_create

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/products/{product_id}/groups/{group_id}'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', product_id='product_id_example', group_id='group_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_groups_delete(client):
    """Test case for product_groups_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/products/{product_id}/groups/{group_id}'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', product_id='product_id_example', group_id='group_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_groups_list_by_products(client):
    """Test case for product_groups_list_by_products

    
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
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/products/{product_id}/groups'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', product_id='product_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

