# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bucket_access_control import BucketAccessControl
from openapi_server.models.bucket_access_controls import BucketAccessControls


pytestmark = pytest.mark.asyncio

async def test_storage_bucket_access_controls_delete(client):
    """Test case for storage_bucket_access_controls_delete

    
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
        path='/storage/v1/b/{bucket}/acl/{entity}'.format(bucket='bucket_example', entity='entity_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_storage_bucket_access_controls_get(client):
    """Test case for storage_bucket_access_controls_get

    
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
        path='/storage/v1/b/{bucket}/acl/{entity}'.format(bucket='bucket_example', entity='entity_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_storage_bucket_access_controls_insert(client):
    """Test case for storage_bucket_access_controls_insert

    
    """
    body = {"bucket":"bucket","role":"role","kind":"storage#bucketAccessControl","domain":"domain","entityId":"entityId","etag":"etag","id":"id","projectTeam":{"projectNumber":"projectNumber","team":"team"},"email":"email","entity":"entity","selfLink":"selfLink"}
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
        method='POST',
        path='/storage/v1/b/{bucket}/acl'.format(bucket='bucket_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_storage_bucket_access_controls_list(client):
    """Test case for storage_bucket_access_controls_list

    
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
        path='/storage/v1/b/{bucket}/acl'.format(bucket='bucket_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_storage_bucket_access_controls_patch(client):
    """Test case for storage_bucket_access_controls_patch

    
    """
    body = {"bucket":"bucket","role":"role","kind":"storage#bucketAccessControl","domain":"domain","entityId":"entityId","etag":"etag","id":"id","projectTeam":{"projectNumber":"projectNumber","team":"team"},"email":"email","entity":"entity","selfLink":"selfLink"}
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
        method='PATCH',
        path='/storage/v1/b/{bucket}/acl/{entity}'.format(bucket='bucket_example', entity='entity_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_storage_bucket_access_controls_update(client):
    """Test case for storage_bucket_access_controls_update

    
    """
    body = {"bucket":"bucket","role":"role","kind":"storage#bucketAccessControl","domain":"domain","entityId":"entityId","etag":"etag","id":"id","projectTeam":{"projectNumber":"projectNumber","team":"team"},"email":"email","entity":"entity","selfLink":"selfLink"}
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
        path='/storage/v1/b/{bucket}/acl/{entity}'.format(bucket='bucket_example', entity='entity_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

