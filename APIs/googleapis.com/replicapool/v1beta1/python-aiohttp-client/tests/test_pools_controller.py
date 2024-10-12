# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.pool import Pool
from openapi_server.models.pools_delete_request import PoolsDeleteRequest
from openapi_server.models.pools_list_response import PoolsListResponse
from openapi_server.models.template import Template


pytestmark = pytest.mark.asyncio

async def test_replicapool_pools_delete(client):
    """Test case for replicapool_pools_delete

    
    """
    body = {"abandonInstances":["abandonInstances","abandonInstances"]}
    params = [('alt', json),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/replicapool/v1beta1/projects/{project_name}/zones/{zone}/pools/{pool_name}'.format(project_name='project_name_example', zone='zone_example', pool_name='pool_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_replicapool_pools_get(client):
    """Test case for replicapool_pools_get

    
    """
    params = [('alt', json),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/replicapool/v1beta1/projects/{project_name}/zones/{zone}/pools/{pool_name}'.format(project_name='project_name_example', zone='zone_example', pool_name='pool_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_replicapool_pools_insert(client):
    """Test case for replicapool_pools_insert

    
    """
    body = {"autoRestart":True,"template":{"healthChecks":[{"path":"path","port":5,"checkIntervalSec":6,"host":"host","name":"name","description":"description","unhealthyThreshold":2,"healthyThreshold":1,"timeoutSec":5},{"path":"path","port":5,"checkIntervalSec":6,"host":"host","name":"name","description":"description","unhealthyThreshold":2,"healthyThreshold":1,"timeoutSec":5}],"action":{"timeoutMilliSeconds":3,"envVariables":[{"hidden":True,"name":"name","value":"value"},{"hidden":True,"name":"name","value":"value"}],"commands":["commands","commands"]},"vmParams":{"canIpForward":True,"metadata":{"fingerPrint":"fingerPrint","items":[{"value":"value","key":"key"},{"value":"value","key":"key"}]},"networkInterfaces":[{"networkIp":"networkIp","accessConfigs":[{"natIp":"natIp","name":"name","type":"type"},{"natIp":"natIp","name":"name","type":"type"}],"network":"network"},{"networkIp":"networkIp","accessConfigs":[{"natIp":"natIp","name":"name","type":"type"},{"natIp":"natIp","name":"name","type":"type"}],"network":"network"}],"serviceAccounts":[{"scopes":["scopes","scopes"],"email":"email"},{"scopes":["scopes","scopes"],"email":"email"}],"disksToAttach":[{"attachment":{"index":2,"deviceName":"deviceName"},"source":"source"},{"attachment":{"index":2,"deviceName":"deviceName"},"source":"source"}],"onHostMaintenance":"onHostMaintenance","disksToCreate":[{"attachment":{"index":2,"deviceName":"deviceName"},"autoDelete":True,"boot":True,"initializeParams":{"diskType":"diskType","sourceImage":"sourceImage","diskSizeGb":"diskSizeGb"}},{"attachment":{"index":2,"deviceName":"deviceName"},"autoDelete":True,"boot":True,"initializeParams":{"diskType":"diskType","sourceImage":"sourceImage","diskSizeGb":"diskSizeGb"}}],"description":"description","baseInstanceName":"baseInstanceName","machineType":"machineType","tags":{"fingerPrint":"fingerPrint","items":["items","items"]}},"version":"version"},"healthChecks":[{"path":"path","port":5,"checkIntervalSec":6,"host":"host","name":"name","description":"description","unhealthyThreshold":2,"healthyThreshold":1,"timeoutSec":5},{"path":"path","port":5,"checkIntervalSec":6,"host":"host","name":"name","description":"description","unhealthyThreshold":2,"healthyThreshold":1,"timeoutSec":5}],"initialNumReplicas":7,"description":"description","baseInstanceName":"baseInstanceName","targetPools":["targetPools","targetPools"],"type":"type","labels":[{"value":"value","key":"key"},{"value":"value","key":"key"}],"selfLink":"selfLink","numReplicas":9,"targetPool":"targetPool","currentNumReplicas":0,"name":"name","resourceViews":["resourceViews","resourceViews"]}
    params = [('alt', json),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/replicapool/v1beta1/projects/{project_name}/zones/{zone}/pools'.format(project_name='project_name_example', zone='zone_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_replicapool_pools_list(client):
    """Test case for replicapool_pools_list

    
    """
    params = [('alt', json),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example'),
                    ('maxResults', 500),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/replicapool/v1beta1/projects/{project_name}/zones/{zone}/pools'.format(project_name='project_name_example', zone='zone_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_replicapool_pools_resize(client):
    """Test case for replicapool_pools_resize

    
    """
    params = [('alt', json),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example'),
                    ('numReplicas', 56)]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/replicapool/v1beta1/projects/{project_name}/zones/{zone}/pools/{pool_name}/resize'.format(project_name='project_name_example', zone='zone_example', pool_name='pool_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_replicapool_pools_updatetemplate(client):
    """Test case for replicapool_pools_updatetemplate

    
    """
    body = {"healthChecks":[{"path":"path","port":5,"checkIntervalSec":6,"host":"host","name":"name","description":"description","unhealthyThreshold":2,"healthyThreshold":1,"timeoutSec":5},{"path":"path","port":5,"checkIntervalSec":6,"host":"host","name":"name","description":"description","unhealthyThreshold":2,"healthyThreshold":1,"timeoutSec":5}],"action":{"timeoutMilliSeconds":3,"envVariables":[{"hidden":True,"name":"name","value":"value"},{"hidden":True,"name":"name","value":"value"}],"commands":["commands","commands"]},"vmParams":{"canIpForward":True,"metadata":{"fingerPrint":"fingerPrint","items":[{"value":"value","key":"key"},{"value":"value","key":"key"}]},"networkInterfaces":[{"networkIp":"networkIp","accessConfigs":[{"natIp":"natIp","name":"name","type":"type"},{"natIp":"natIp","name":"name","type":"type"}],"network":"network"},{"networkIp":"networkIp","accessConfigs":[{"natIp":"natIp","name":"name","type":"type"},{"natIp":"natIp","name":"name","type":"type"}],"network":"network"}],"serviceAccounts":[{"scopes":["scopes","scopes"],"email":"email"},{"scopes":["scopes","scopes"],"email":"email"}],"disksToAttach":[{"attachment":{"index":2,"deviceName":"deviceName"},"source":"source"},{"attachment":{"index":2,"deviceName":"deviceName"},"source":"source"}],"onHostMaintenance":"onHostMaintenance","disksToCreate":[{"attachment":{"index":2,"deviceName":"deviceName"},"autoDelete":True,"boot":True,"initializeParams":{"diskType":"diskType","sourceImage":"sourceImage","diskSizeGb":"diskSizeGb"}},{"attachment":{"index":2,"deviceName":"deviceName"},"autoDelete":True,"boot":True,"initializeParams":{"diskType":"diskType","sourceImage":"sourceImage","diskSizeGb":"diskSizeGb"}}],"description":"description","baseInstanceName":"baseInstanceName","machineType":"machineType","tags":{"fingerPrint":"fingerPrint","items":["items","items"]}},"version":"version"}
    params = [('alt', json),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/replicapool/v1beta1/projects/{project_name}/zones/{zone}/pools/{pool_name}/updateTemplate'.format(project_name='project_name_example', zone='zone_example', pool_name='pool_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

