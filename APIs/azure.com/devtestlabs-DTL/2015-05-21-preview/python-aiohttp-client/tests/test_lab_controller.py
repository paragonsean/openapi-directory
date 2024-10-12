# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.generate_upload_uri_parameter import GenerateUploadUriParameter
from openapi_server.models.generate_upload_uri_response import GenerateUploadUriResponse
from openapi_server.models.lab import Lab
from openapi_server.models.lab_virtual_machine import LabVirtualMachine
from openapi_server.models.response_with_continuation_lab import ResponseWithContinuationLab
from openapi_server.models.response_with_continuation_lab_vhd import ResponseWithContinuationLabVhd


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_lab_create_environment(client):
    """Test case for lab_create_environment

    
    """
    lab_virtual_machine = {"name":"name","location":"location","id":"id","type":"type","properties":{"createdByUserId":"createdByUserId","labVirtualNetworkId":"labVirtualNetworkId","notes":"notes","createdByUser":"createdByUser","fqdn":"fqdn","provisioningState":"provisioningState","userName":"userName","labSubnetName":"labSubnetName","artifactDeploymentStatus":{"deploymentStatus":"deploymentStatus","artifactsApplied":0,"totalArtifacts":6},"disallowPublicIpAddress":True,"password":"password","computeId":"computeId","isAuthenticationWithSshKey":True,"size":"size","sshKey":"sshKey","ownerObjectId":"ownerObjectId","osType":"osType","galleryImageReference":{"offer":"offer","osType":"osType","publisher":"publisher","sku":"sku","version":"version"},"artifacts":[{"artifactId":"artifactId","parameters":[{"name":"name","value":"value"},{"name":"name","value":"value"}]},{"artifactId":"artifactId","parameters":[{"name":"name","value":"value"},{"name":"name","value":"value"}]}],"customImageId":"customImageId"},"tags":{"key":"tags"}}
    params = [('api-version', '2015-05-21-preview')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{name}/createEnvironment'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', name='name_example'),
        headers=headers,
        json=lab_virtual_machine,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_lab_create_or_update_resource(client):
    """Test case for lab_create_or_update_resource

    
    """
    lab = {"name":"name","location":"location","id":"id","type":"type","properties":{"artifactsStorageAccount":"artifactsStorageAccount","createdDate":"2000-01-23T04:56:07.000+00:00","defaultStorageAccount":"defaultStorageAccount","vaultName":"vaultName","labStorageType":"Standard","storageAccounts":["storageAccounts","storageAccounts"],"defaultVirtualNetworkId":"defaultVirtualNetworkId","provisioningState":"provisioningState"},"tags":{"key":"tags"}}
    params = [('api-version', '2015-05-21-preview')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', name='name_example'),
        headers=headers,
        json=lab,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_lab_delete_resource(client):
    """Test case for lab_delete_resource

    
    """
    params = [('api-version', '2015-05-21-preview')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_lab_generate_upload_uri(client):
    """Test case for lab_generate_upload_uri

    
    """
    generate_upload_uri_parameter = {"blobName":"blobName"}
    params = [('api-version', '2015-05-21-preview')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{name}/generateUploadUri'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', name='name_example'),
        headers=headers,
        json=generate_upload_uri_parameter,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_lab_get_resource(client):
    """Test case for lab_get_resource

    
    """
    params = [('api-version', '2015-05-21-preview')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_lab_list_by_resource_group(client):
    """Test case for lab_list_by_resource_group

    
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
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_lab_list_by_subscription(client):
    """Test case for lab_list_by_subscription

    
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
        path='/subscriptions/{subscription_id}/providers/Microsoft.DevTestLab/labs'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_lab_list_vhds(client):
    """Test case for lab_list_vhds

    
    """
    params = [('api-version', '2015-05-21-preview')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{name}/listVhds'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_lab_patch_resource(client):
    """Test case for lab_patch_resource

    
    """
    lab = {"name":"name","location":"location","id":"id","type":"type","properties":{"artifactsStorageAccount":"artifactsStorageAccount","createdDate":"2000-01-23T04:56:07.000+00:00","defaultStorageAccount":"defaultStorageAccount","vaultName":"vaultName","labStorageType":"Standard","storageAccounts":["storageAccounts","storageAccounts"],"defaultVirtualNetworkId":"defaultVirtualNetworkId","provisioningState":"provisioningState"},"tags":{"key":"tags"}}
    params = [('api-version', '2015-05-21-preview')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', name='name_example'),
        headers=headers,
        json=lab,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

