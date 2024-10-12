# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.check_name_request import CheckNameRequest
from openapi_server.models.check_name_response import CheckNameResponse
from openapi_server.models.create_workspace_collection_request import CreateWorkspaceCollectionRequest
from openapi_server.models.error import Error
from openapi_server.models.migrate_workspace_collection_request import MigrateWorkspaceCollectionRequest
from openapi_server.models.update_workspace_collection_request import UpdateWorkspaceCollectionRequest
from openapi_server.models.workspace_collection import WorkspaceCollection
from openapi_server.models.workspace_collection_access_key import WorkspaceCollectionAccessKey
from openapi_server.models.workspace_collection_access_keys import WorkspaceCollectionAccessKeys
from openapi_server.models.workspace_collection_list import WorkspaceCollectionList


pytestmark = pytest.mark.asyncio

async def test_workspace_collections_check_name_availability(client):
    """Test case for workspace_collections_check_name_availability

    
    """
    body = {"name":"name","type":"Microsoft.PowerBI/workspaceCollections"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/providers/Microsoft.PowerBI/locations/{location}/checkNameAvailability'.format(subscription_id='subscription_id_example', location='location_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workspace_collections_create(client):
    """Test case for workspace_collections_create

    
    """
    body = {"location":"location","sku":{"tier":"Standard","name":"S1"},"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.PowerBI/workspaceCollections/{workspace_collection_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', workspace_collection_name='workspace_collection_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workspace_collections_delete(client):
    """Test case for workspace_collections_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.PowerBI/workspaceCollections/{workspace_collection_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', workspace_collection_name='workspace_collection_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workspace_collections_get_access_keys(client):
    """Test case for workspace_collections_get_access_keys

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.PowerBI/workspaceCollections/{workspace_collection_name}/listKeys'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', workspace_collection_name='workspace_collection_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workspace_collections_get_by_name(client):
    """Test case for workspace_collections_get_by_name

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.PowerBI/workspaceCollections/{workspace_collection_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', workspace_collection_name='workspace_collection_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workspace_collections_list_by_resource_group(client):
    """Test case for workspace_collections_list_by_resource_group

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.PowerBI/workspaceCollections'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workspace_collections_list_by_subscription(client):
    """Test case for workspace_collections_list_by_subscription

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.PowerBI/workspaceCollections'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workspace_collections_migrate(client):
    """Test case for workspace_collections_migrate

    
    """
    body = {"targetResourceGroup":"targetResourceGroup","resources":["resources","resources"]}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/moveResources'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workspace_collections_regenerate_key(client):
    """Test case for workspace_collections_regenerate_key

    
    """
    body = {"keyName":"key1"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.PowerBI/workspaceCollections/{workspace_collection_name}/regenerateKey'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', workspace_collection_name='workspace_collection_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workspace_collections_update(client):
    """Test case for workspace_collections_update

    
    """
    body = {"sku":{"tier":"Standard","name":"S1"},"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.PowerBI/workspaceCollections/{workspace_collection_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', workspace_collection_name='workspace_collection_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

