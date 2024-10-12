# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.tenant_access_get200_response import TenantAccessGet200Response
from openapi_server.models.tenant_access_get_default_response import TenantAccessGetDefaultResponse
from openapi_server.models.tenant_access_update_request import TenantAccessUpdateRequest


pytestmark = pytest.mark.asyncio

async def test_tenant_access_get(client):
    """Test case for tenant_access_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/tenant/{access_name}'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', subscription_id='subscription_id_example', access_name='access_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tenant_access_get_entity_tag(client):
    """Test case for tenant_access_get_entity_tag

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='HEAD',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/tenant/{access_name}'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', subscription_id='subscription_id_example', access_name='access_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tenant_access_regenerate_primary_key(client):
    """Test case for tenant_access_regenerate_primary_key

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/tenant/{access_name}/regeneratePrimaryKey'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', subscription_id='subscription_id_example', access_name='access_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tenant_access_regenerate_secondary_key(client):
    """Test case for tenant_access_regenerate_secondary_key

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/tenant/{access_name}/regenerateSecondaryKey'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', subscription_id='subscription_id_example', access_name='access_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tenant_access_update(client):
    """Test case for tenant_access_update

    
    """
    parameters = openapi_server.TenantAccessUpdateRequest()
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'if_match': 'if_match_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/tenant/{access_name}'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', access_name='access_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

