# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.workspace import Workspace
from openapi_server.models.workspace_list_result import WorkspaceListResult
from openapi_server.models.workspace_update import WorkspaceUpdate


pytestmark = pytest.mark.asyncio

async def test_workspaces_create_or_update(client):
    """Test case for workspaces_create_or_update

    
    """
    parameters = {"sku":{"tier":"tier","name":"name"},"properties":{"uiDefinitionUri":"uiDefinitionUri","managedResourceGroupId":"managedResourceGroupId","authorizations":[{"roleDefinitionId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","principalId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"},{"roleDefinitionId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","principalId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}],"provisioningState":"Accepted","parameters":{"enableNoPublicIp":{"value":True},"loadBalancerId":{"type":"Bool","value":"value"},"resourceTags":{"value":"{}"},"loadBalancerBackendPoolName":{"type":"Bool","value":"value"},"vnetAddressPrefix":{"type":"Bool","value":"value"},"relayNamespaceName":{"type":"Bool","value":"value"},"customVirtualNetworkId":{"type":"Bool","value":"value"},"storageAccountName":{"type":"Bool","value":"value"},"customPrivateSubnetName":{"type":"Bool","value":"value"},"amlWorkspaceId":{"type":"Bool","value":"value"},"storageAccountSkuName":{"type":"Bool","value":"value"},"customPublicSubnetName":{"type":"Bool","value":"value"}}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Databricks/workspaces/{workspace_name}'.format(resource_group_name='resource_group_name_example', workspace_name='workspace_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workspaces_delete(client):
    """Test case for workspaces_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Databricks/workspaces/{workspace_name}'.format(resource_group_name='resource_group_name_example', workspace_name='workspace_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workspaces_get(client):
    """Test case for workspaces_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Databricks/workspaces/{workspace_name}'.format(resource_group_name='resource_group_name_example', workspace_name='workspace_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workspaces_list_by_resource_group(client):
    """Test case for workspaces_list_by_resource_group

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Databricks/workspaces'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workspaces_list_by_subscription(client):
    """Test case for workspaces_list_by_subscription

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Databricks/workspaces'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workspaces_update(client):
    """Test case for workspaces_update

    
    """
    parameters = {"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Databricks/workspaces/{workspace_name}'.format(resource_group_name='resource_group_name_example', workspace_name='workspace_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

