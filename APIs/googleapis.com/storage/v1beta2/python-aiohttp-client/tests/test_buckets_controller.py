# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bucket import Bucket
from openapi_server.models.buckets import Buckets


pytestmark = pytest.mark.asyncio

async def test_storage_buckets_delete(client):
    """Test case for storage_buckets_delete

    
    """
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example'),
                    ('ifMetagenerationMatch', 'if_metageneration_match_example'),
                    ('ifMetagenerationNotMatch', 'if_metageneration_not_match_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/storage/v1beta2/b/{bucket}'.format(bucket='bucket_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_storage_buckets_get(client):
    """Test case for storage_buckets_get

    
    """
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example'),
                    ('ifMetagenerationMatch', 'if_metageneration_match_example'),
                    ('ifMetagenerationNotMatch', 'if_metageneration_not_match_example'),
                    ('projection', 'projection_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/storage/v1beta2/b/{bucket}'.format(bucket='bucket_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_storage_buckets_insert(client):
    """Test case for storage_buckets_insert

    
    """
    body = {"defaultObjectAcl":[{"bucket":"bucket","generation":"generation","role":"role","kind":"storage#objectAccessControl","domain":"domain","entityId":"entityId","etag":"etag","id":"id","email":"email","entity":"entity","object":"object","selfLink":"selfLink"},{"bucket":"bucket","generation":"generation","role":"role","kind":"storage#objectAccessControl","domain":"domain","entityId":"entityId","etag":"etag","id":"id","email":"email","entity":"entity","object":"object","selfLink":"selfLink"}],"owner":{"entityId":"entityId","entity":"entity"},"metageneration":"metageneration","website":{"mainPageSuffix":"mainPageSuffix","notFoundPage":"notFoundPage"},"cors":[{"method":["method","method"],"origin":["origin","origin"],"responseHeader":["responseHeader","responseHeader"],"maxAgeSeconds":0},{"method":["method","method"],"origin":["origin","origin"],"responseHeader":["responseHeader","responseHeader"],"maxAgeSeconds":0}],"versioning":{"enabled":True},"kind":"storage#bucket","acl":[{"bucket":"bucket","role":"role","kind":"storage#bucketAccessControl","domain":"domain","entityId":"entityId","etag":"etag","id":"id","email":"email","entity":"entity","selfLink":"selfLink"},{"bucket":"bucket","role":"role","kind":"storage#bucketAccessControl","domain":"domain","entityId":"entityId","etag":"etag","id":"id","email":"email","entity":"entity","selfLink":"selfLink"}],"selfLink":"selfLink","lifecycle":{"rule":[{"condition":{"isLive":True,"numNewerVersions":1,"createdBefore":"2000-01-23","age":6},"action":{"type":"type"}},{"condition":{"isLive":True,"numNewerVersions":1,"createdBefore":"2000-01-23","age":6},"action":{"type":"type"}}]},"storageClass":"storageClass","name":"name","logging":{"logBucket":"logBucket","logObjectPrefix":"logObjectPrefix"},"etag":"etag","location":"location","timeCreated":"2000-01-23T04:56:07.000+00:00","id":"id"}
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example'),
                    ('project', 'project_example'),
                    ('projection', 'projection_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/storage/v1beta2/b',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_storage_buckets_list(client):
    """Test case for storage_buckets_list

    
    """
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example'),
                    ('project', 'project_example'),
                    ('maxResults', 56),
                    ('pageToken', 'page_token_example'),
                    ('projection', 'projection_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/storage/v1beta2/b',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_storage_buckets_patch(client):
    """Test case for storage_buckets_patch

    
    """
    body = {"defaultObjectAcl":[{"bucket":"bucket","generation":"generation","role":"role","kind":"storage#objectAccessControl","domain":"domain","entityId":"entityId","etag":"etag","id":"id","email":"email","entity":"entity","object":"object","selfLink":"selfLink"},{"bucket":"bucket","generation":"generation","role":"role","kind":"storage#objectAccessControl","domain":"domain","entityId":"entityId","etag":"etag","id":"id","email":"email","entity":"entity","object":"object","selfLink":"selfLink"}],"owner":{"entityId":"entityId","entity":"entity"},"metageneration":"metageneration","website":{"mainPageSuffix":"mainPageSuffix","notFoundPage":"notFoundPage"},"cors":[{"method":["method","method"],"origin":["origin","origin"],"responseHeader":["responseHeader","responseHeader"],"maxAgeSeconds":0},{"method":["method","method"],"origin":["origin","origin"],"responseHeader":["responseHeader","responseHeader"],"maxAgeSeconds":0}],"versioning":{"enabled":True},"kind":"storage#bucket","acl":[{"bucket":"bucket","role":"role","kind":"storage#bucketAccessControl","domain":"domain","entityId":"entityId","etag":"etag","id":"id","email":"email","entity":"entity","selfLink":"selfLink"},{"bucket":"bucket","role":"role","kind":"storage#bucketAccessControl","domain":"domain","entityId":"entityId","etag":"etag","id":"id","email":"email","entity":"entity","selfLink":"selfLink"}],"selfLink":"selfLink","lifecycle":{"rule":[{"condition":{"isLive":True,"numNewerVersions":1,"createdBefore":"2000-01-23","age":6},"action":{"type":"type"}},{"condition":{"isLive":True,"numNewerVersions":1,"createdBefore":"2000-01-23","age":6},"action":{"type":"type"}}]},"storageClass":"storageClass","name":"name","logging":{"logBucket":"logBucket","logObjectPrefix":"logObjectPrefix"},"etag":"etag","location":"location","timeCreated":"2000-01-23T04:56:07.000+00:00","id":"id"}
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example'),
                    ('ifMetagenerationMatch', 'if_metageneration_match_example'),
                    ('ifMetagenerationNotMatch', 'if_metageneration_not_match_example'),
                    ('projection', 'projection_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/storage/v1beta2/b/{bucket}'.format(bucket='bucket_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_storage_buckets_update(client):
    """Test case for storage_buckets_update

    
    """
    body = {"defaultObjectAcl":[{"bucket":"bucket","generation":"generation","role":"role","kind":"storage#objectAccessControl","domain":"domain","entityId":"entityId","etag":"etag","id":"id","email":"email","entity":"entity","object":"object","selfLink":"selfLink"},{"bucket":"bucket","generation":"generation","role":"role","kind":"storage#objectAccessControl","domain":"domain","entityId":"entityId","etag":"etag","id":"id","email":"email","entity":"entity","object":"object","selfLink":"selfLink"}],"owner":{"entityId":"entityId","entity":"entity"},"metageneration":"metageneration","website":{"mainPageSuffix":"mainPageSuffix","notFoundPage":"notFoundPage"},"cors":[{"method":["method","method"],"origin":["origin","origin"],"responseHeader":["responseHeader","responseHeader"],"maxAgeSeconds":0},{"method":["method","method"],"origin":["origin","origin"],"responseHeader":["responseHeader","responseHeader"],"maxAgeSeconds":0}],"versioning":{"enabled":True},"kind":"storage#bucket","acl":[{"bucket":"bucket","role":"role","kind":"storage#bucketAccessControl","domain":"domain","entityId":"entityId","etag":"etag","id":"id","email":"email","entity":"entity","selfLink":"selfLink"},{"bucket":"bucket","role":"role","kind":"storage#bucketAccessControl","domain":"domain","entityId":"entityId","etag":"etag","id":"id","email":"email","entity":"entity","selfLink":"selfLink"}],"selfLink":"selfLink","lifecycle":{"rule":[{"condition":{"isLive":True,"numNewerVersions":1,"createdBefore":"2000-01-23","age":6},"action":{"type":"type"}},{"condition":{"isLive":True,"numNewerVersions":1,"createdBefore":"2000-01-23","age":6},"action":{"type":"type"}}]},"storageClass":"storageClass","name":"name","logging":{"logBucket":"logBucket","logObjectPrefix":"logObjectPrefix"},"etag":"etag","location":"location","timeCreated":"2000-01-23T04:56:07.000+00:00","id":"id"}
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example'),
                    ('ifMetagenerationMatch', 'if_metageneration_match_example'),
                    ('ifMetagenerationNotMatch', 'if_metageneration_not_match_example'),
                    ('projection', 'projection_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/storage/v1beta2/b/{bucket}'.format(bucket='bucket_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

