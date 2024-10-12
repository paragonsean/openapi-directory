# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_aml_user_feature_result import ListAmlUserFeatureResult
from openapi_server.models.list_workspace_keys_result import ListWorkspaceKeysResult
from openapi_server.models.machine_learning_service_error import MachineLearningServiceError
from openapi_server.models.workspace import Workspace
from openapi_server.models.workspace_list_result import WorkspaceListResult
from openapi_server.models.workspace_update_parameters import WorkspaceUpdateParameters


pytestmark = pytest.mark.asyncio

async def test_workspace_features_list(client):
    """Test case for workspace_features_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.MachineLearningServices/workspaces/{workspace_name}/features'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', workspace_name='workspace_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workspaces_create_or_update(client):
    """Test case for workspaces_create_or_update

    
    """
    parameters = {"properties":{"applicationInsights":"applicationInsights","creationTime":"2000-01-23T04:56:07.000+00:00","keyVault":"keyVault","hbiWorkspace":False,"description":"description","provisioningState":"Unknown","storageAccount":"storageAccount","serviceProvisionedResourceGroup":"serviceProvisionedResourceGroup","encryption":{"keyVaultProperties":{"keyIdentifier":"keyIdentifier","identityClientId":"identityClientId","keyVaultArmId":"keyVaultArmId"},"status":"Enabled"},"containerRegistry":"containerRegistry","friendlyName":"friendlyName","discoveryUrl":"discoveryUrl","workspaceId":"workspaceId"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.MachineLearningServices/workspaces/{workspace_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', workspace_name='workspace_name_example'),
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
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.MachineLearningServices/workspaces/{workspace_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', workspace_name='workspace_name_example'),
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
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.MachineLearningServices/workspaces/{workspace_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', workspace_name='workspace_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workspaces_list_by_resource_group(client):
    """Test case for workspaces_list_by_resource_group

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$skiptoken', 'skiptoken_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.MachineLearningServices/workspaces'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workspaces_list_by_subscription(client):
    """Test case for workspaces_list_by_subscription

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$skiptoken', 'skiptoken_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.MachineLearningServices/workspaces'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workspaces_list_keys(client):
    """Test case for workspaces_list_keys

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.MachineLearningServices/workspaces/{workspace_name}/listKeys'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', workspace_name='workspace_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workspaces_resync_keys(client):
    """Test case for workspaces_resync_keys

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.MachineLearningServices/workspaces/{workspace_name}/resyncKeys'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', workspace_name='workspace_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workspaces_update(client):
    """Test case for workspaces_update

    
    """
    parameters = {"sku":{"tier":"tier","name":"name"},"properties":{"description":"description","friendlyName":"friendlyName"},"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.MachineLearningServices/workspaces/{workspace_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', workspace_name='workspace_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

