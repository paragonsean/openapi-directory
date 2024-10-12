# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.tenant_access_get_default_response import TenantAccessGetDefaultResponse
from openapi_server.models.tenant_configuration_deploy200_response import TenantConfigurationDeploy200Response
from openapi_server.models.tenant_configuration_deploy_request import TenantConfigurationDeployRequest
from openapi_server.models.tenant_configuration_save_request import TenantConfigurationSaveRequest


pytestmark = pytest.mark.asyncio

async def test_tenant_configuration_deploy(client):
    """Test case for tenant_configuration_deploy

    
    """
    parameters = openapi_server.TenantConfigurationDeployRequest()
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/tenant/{configuration_name}/deploy'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', subscription_id='subscription_id_example', configuration_name='configuration_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tenant_configuration_save(client):
    """Test case for tenant_configuration_save

    
    """
    parameters = openapi_server.TenantConfigurationSaveRequest()
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/tenant/{configuration_name}/save'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', subscription_id='subscription_id_example', configuration_name='configuration_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tenant_configuration_validate(client):
    """Test case for tenant_configuration_validate

    
    """
    parameters = openapi_server.TenantConfigurationDeployRequest()
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/tenant/{configuration_name}/validate'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', subscription_id='subscription_id_example', configuration_name='configuration_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

