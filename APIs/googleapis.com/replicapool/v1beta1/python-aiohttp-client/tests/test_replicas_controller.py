# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.replica import Replica
from openapi_server.models.replicas_delete_request import ReplicasDeleteRequest
from openapi_server.models.replicas_list_response import ReplicasListResponse


pytestmark = pytest.mark.asyncio

async def test_replicapool_replicas_delete(client):
    """Test case for replicapool_replicas_delete

    
    """
    body = {"abandonInstance":True}
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
        path='/replicapool/v1beta1/projects/{project_name}/zones/{zone}/pools/{pool_name}/replicas/{replica_name}'.format(project_name='project_name_example', zone='zone_example', pool_name='pool_name_example', replica_name='replica_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_replicapool_replicas_get(client):
    """Test case for replicapool_replicas_get

    
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
        path='/replicapool/v1beta1/projects/{project_name}/zones/{zone}/pools/{pool_name}/replicas/{replica_name}'.format(project_name='project_name_example', zone='zone_example', pool_name='pool_name_example', replica_name='replica_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_replicapool_replicas_list(client):
    """Test case for replicapool_replicas_list

    
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
        path='/replicapool/v1beta1/projects/{project_name}/zones/{zone}/pools/{pool_name}/replicas'.format(project_name='project_name_example', zone='zone_example', pool_name='pool_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_replicapool_replicas_restart(client):
    """Test case for replicapool_replicas_restart

    
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
        method='POST',
        path='/replicapool/v1beta1/projects/{project_name}/zones/{zone}/pools/{pool_name}/replicas/{replica_name}/restart'.format(project_name='project_name_example', zone='zone_example', pool_name='pool_name_example', replica_name='replica_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

