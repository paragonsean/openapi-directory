# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.hmac_key import HmacKey
from openapi_server.models.hmac_key_metadata import HmacKeyMetadata
from openapi_server.models.hmac_keys_metadata import HmacKeysMetadata
from openapi_server.models.service_account import ServiceAccount


pytestmark = pytest.mark.asyncio

async def test_storage_projects_hmac_keys_create(client):
    """Test case for storage_projects_hmac_keys_create

    
    """
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('uploadType', 'upload_type_example'),
                    ('userIp', 'user_ip_example'),
                    ('serviceAccountEmail', 'service_account_email_example'),
                    ('userProject', 'user_project_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/storage/v1/projects/{project_id}/hmacKeys'.format(project_id='project_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_storage_projects_hmac_keys_delete(client):
    """Test case for storage_projects_hmac_keys_delete

    
    """
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('uploadType', 'upload_type_example'),
                    ('userIp', 'user_ip_example'),
                    ('userProject', 'user_project_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/storage/v1/projects/{project_id}/hmacKeys/{access_id}'.format(project_id='project_id_example', access_id='access_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_storage_projects_hmac_keys_get(client):
    """Test case for storage_projects_hmac_keys_get

    
    """
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('uploadType', 'upload_type_example'),
                    ('userIp', 'user_ip_example'),
                    ('userProject', 'user_project_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/storage/v1/projects/{project_id}/hmacKeys/{access_id}'.format(project_id='project_id_example', access_id='access_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_storage_projects_hmac_keys_list(client):
    """Test case for storage_projects_hmac_keys_list

    
    """
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('uploadType', 'upload_type_example'),
                    ('userIp', 'user_ip_example'),
                    ('maxResults', 56),
                    ('pageToken', 'page_token_example'),
                    ('serviceAccountEmail', 'service_account_email_example'),
                    ('showDeletedKeys', True),
                    ('userProject', 'user_project_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/storage/v1/projects/{project_id}/hmacKeys'.format(project_id='project_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_storage_projects_hmac_keys_update(client):
    """Test case for storage_projects_hmac_keys_update

    
    """
    body = {"accessId":"accessId","serviceAccountEmail":"serviceAccountEmail","kind":"storage#hmacKeyMetadata","etag":"etag","timeCreated":"2000-01-23T04:56:07.000+00:00","id":"id","state":"state","projectId":"projectId","updated":"2000-01-23T04:56:07.000+00:00","selfLink":"selfLink"}
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('uploadType', 'upload_type_example'),
                    ('userIp', 'user_ip_example'),
                    ('userProject', 'user_project_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/storage/v1/projects/{project_id}/hmacKeys/{access_id}'.format(project_id='project_id_example', access_id='access_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_storage_projects_service_account_get(client):
    """Test case for storage_projects_service_account_get

    
    """
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('uploadType', 'upload_type_example'),
                    ('userIp', 'user_ip_example'),
                    ('userProject', 'user_project_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/storage/v1/projects/{project_id}/serviceAccount'.format(project_id='project_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

