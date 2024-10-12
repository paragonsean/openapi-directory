# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.artifact_source import ArtifactSource
from openapi_server.models.cloud_error import CloudError
from openapi_server.models.response_with_continuation_artifact_source import ResponseWithContinuationArtifactSource


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_artifact_source_create_or_update_resource(client):
    """Test case for artifact_source_create_or_update_resource

    
    """
    artifact_source = {"name":"name","location":"location","id":"id","type":"type","properties":{"folderPath":"folderPath","securityToken":"securityToken","sourceType":"VsoGit","displayName":"displayName","provisioningState":"provisioningState","branchRef":"branchRef","uri":"uri","status":"Enabled"},"tags":{"key":"tags"}}
    params = [('api-version', '2015-05-21-preview')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{lab_name}/artifactsources/{name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_name='lab_name_example', name='name_example'),
        headers=headers,
        json=artifact_source,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_artifact_source_delete_resource(client):
    """Test case for artifact_source_delete_resource

    
    """
    params = [('api-version', '2015-05-21-preview')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{lab_name}/artifactsources/{name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_name='lab_name_example', name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_artifact_source_get_resource(client):
    """Test case for artifact_source_get_resource

    
    """
    params = [('api-version', '2015-05-21-preview')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{lab_name}/artifactsources/{name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_name='lab_name_example', name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_artifact_source_list(client):
    """Test case for artifact_source_list

    
    """
    params = [('$filter', 'filter_example'),
                    ('$top', 56),
                    ('$orderBy', 'order_by_example'),
                    ('api-version', '2015-05-21-preview')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{lab_name}/artifactsources'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_name='lab_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_artifact_source_patch_resource(client):
    """Test case for artifact_source_patch_resource

    
    """
    artifact_source = {"name":"name","location":"location","id":"id","type":"type","properties":{"folderPath":"folderPath","securityToken":"securityToken","sourceType":"VsoGit","displayName":"displayName","provisioningState":"provisioningState","branchRef":"branchRef","uri":"uri","status":"Enabled"},"tags":{"key":"tags"}}
    params = [('api-version', '2015-05-21-preview')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{lab_name}/artifactsources/{name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_name='lab_name_example', name='name_example'),
        headers=headers,
        json=artifact_source,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

