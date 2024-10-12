# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_locations_response import ListLocationsResponse
from openapi_server.models.list_operations_response import ListOperationsResponse
from openapi_server.models.operation import Operation
from openapi_server.models.run_pipeline_request import RunPipelineRequest


pytestmark = pytest.mark.asyncio

async def test_lifesciences_projects_locations_list(client):
    """Test case for lifesciences_projects_locations_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2beta/{name}/locations'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_lifesciences_projects_locations_operations_cancel(client):
    """Test case for lifesciences_projects_locations_operations_cancel

    
    """
    body = None
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2beta/{namecance}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_lifesciences_projects_locations_operations_get(client):
    """Test case for lifesciences_projects_locations_operations_get

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2beta/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_lifesciences_projects_locations_operations_list(client):
    """Test case for lifesciences_projects_locations_operations_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2beta/{name}/operations'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_lifesciences_projects_locations_pipelines_run(client):
    """Test case for lifesciences_projects_locations_pipelines_run

    
    """
    body = {"pipeline":{"encryptedEnvironment":{"cipherText":"cipherText","keyName":"keyName"},"environment":{"key":"environment"},"resources":{"virtualMachine":{"disks":[{"sizeGb":1,"name":"name","sourceImage":"sourceImage","type":"type"},{"sizeGb":1,"name":"name","sourceImage":"sourceImage","type":"type"}],"volumes":[{"persistentDisk":{"sizeGb":5,"sourceImage":"sourceImage","type":"type"},"volume":"volume","nfsMount":{"target":"target"},"existingDisk":{"disk":"disk"}},{"persistentDisk":{"sizeGb":5,"sourceImage":"sourceImage","type":"type"},"volume":"volume","nfsMount":{"target":"target"},"existingDisk":{"disk":"disk"}}],"cpuPlatform":"cpuPlatform","serviceAccount":{"scopes":["scopes","scopes"],"email":"email"},"labels":{"key":"labels"},"network":{"subnetwork":"subnetwork","usePrivateAddress":True,"network":"network"},"nvidiaDriverVersion":"nvidiaDriverVersion","dockerCacheImages":["dockerCacheImages","dockerCacheImages"],"preemptible":True,"accelerators":[{"count":"count","type":"type"},{"count":"count","type":"type"}],"reservation":"reservation","bootImage":"bootImage","bootDiskSizeGb":6,"enableStackdriverMonitoring":True,"machineType":"machineType"},"regions":["regions","regions"],"zones":["zones","zones"]},"actions":[{"encryptedEnvironment":{"cipherText":"cipherText","keyName":"keyName"},"disableStandardErrorCapture":True,"publishExposedPorts":True,"credentials":{"cipherText":"cipherText","keyName":"keyName"},"runInBackground":True,"mounts":[{"path":"path","disk":"disk","readOnly":True},{"path":"path","disk":"disk","readOnly":True}],"alwaysRun":True,"ignoreExitStatus":True,"blockExternalNetwork":True,"disableImagePrefetch":True,"timeout":"timeout","labels":{"key":"labels"},"portMappings":{"key":0},"environment":{"key":"environment"},"imageUri":"imageUri","containerName":"containerName","enableFuse":True,"entrypoint":"entrypoint","pidNamespace":"pidNamespace","commands":["commands","commands"]},{"encryptedEnvironment":{"cipherText":"cipherText","keyName":"keyName"},"disableStandardErrorCapture":True,"publishExposedPorts":True,"credentials":{"cipherText":"cipherText","keyName":"keyName"},"runInBackground":True,"mounts":[{"path":"path","disk":"disk","readOnly":True},{"path":"path","disk":"disk","readOnly":True}],"alwaysRun":True,"ignoreExitStatus":True,"blockExternalNetwork":True,"disableImagePrefetch":True,"timeout":"timeout","labels":{"key":"labels"},"portMappings":{"key":0},"environment":{"key":"environment"},"imageUri":"imageUri","containerName":"containerName","enableFuse":True,"entrypoint":"entrypoint","pidNamespace":"pidNamespace","commands":["commands","commands"]}],"timeout":"timeout"},"pubSubTopic":"pubSubTopic","labels":{"key":"labels"}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2beta/{parent}/pipelines:run'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

