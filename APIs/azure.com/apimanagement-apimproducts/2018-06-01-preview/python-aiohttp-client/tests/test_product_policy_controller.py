# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.product_list_by_service_default_response import ProductListByServiceDefaultResponse
from openapi_server.models.product_policy_get200_response import ProductPolicyGet200Response
from openapi_server.models.product_policy_list_by_product200_response import ProductPolicyListByProduct200Response


pytestmark = pytest.mark.asyncio

async def test_product_policy_create_or_update(client):
    """Test case for product_policy_create_or_update

    
    """
    parameters = openapi_server.ProductPolicyGet200Response()
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'if_match': 'if_match_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/products/{product_id}/policies/{policy_id}'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', product_id='product_id_example', policy_id='policy_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_policy_delete(client):
    """Test case for product_policy_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'if_match': 'if_match_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/products/{product_id}/policies/{policy_id}'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', product_id='product_id_example', policy_id='policy_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_policy_get(client):
    """Test case for product_policy_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/products/{product_id}/policies/{policy_id}'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', product_id='product_id_example', policy_id='policy_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_policy_get_entity_tag(client):
    """Test case for product_policy_get_entity_tag

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='HEAD',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/products/{product_id}/policies/{policy_id}'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', product_id='product_id_example', policy_id='policy_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_policy_list_by_product(client):
    """Test case for product_policy_list_by_product

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/products/{product_id}/policies'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', product_id='product_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

