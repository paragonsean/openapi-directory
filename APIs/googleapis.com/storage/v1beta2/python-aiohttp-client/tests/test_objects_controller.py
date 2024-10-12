# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.channel import Channel
from openapi_server.models.compose_request import ComposeRequest
from openapi_server.models.object import Object
from openapi_server.models.objects import Objects


pytestmark = pytest.mark.asyncio

async def test_storage_objects_compose(client):
    """Test case for storage_objects_compose

    
    """
    body = {"kind":"storage#composeRequest","destination":{"generation":"generation","owner":{"entityId":"entityId","entity":"entity"},"metadata":{"key":"metadata"},"metageneration":"metageneration","kind":"storage#object","acl":[{"bucket":"bucket","generation":"generation","role":"role","kind":"storage#objectAccessControl","domain":"domain","entityId":"entityId","etag":"etag","id":"id","email":"email","entity":"entity","object":"object","selfLink":"selfLink"},{"bucket":"bucket","generation":"generation","role":"role","kind":"storage#objectAccessControl","domain":"domain","entityId":"entityId","etag":"etag","id":"id","email":"email","entity":"entity","object":"object","selfLink":"selfLink"}],"cacheControl":"cacheControl","mediaLink":"mediaLink","selfLink":"selfLink","bucket":"bucket","timeDeleted":"2000-01-23T04:56:07.000+00:00","componentCount":0,"storageClass":"storageClass","crc32c":"crc32c","md5Hash":"md5Hash","size":"size","contentDisposition":"contentDisposition","name":"name","contentEncoding":"contentEncoding","contentLanguage":"contentLanguage","etag":"etag","id":"id","contentType":"contentType","updated":"2000-01-23T04:56:07.000+00:00"},"sourceObjects":[{"generation":"generation","name":"name","objectPreconditions":{"ifGenerationMatch":"ifGenerationMatch"}},{"generation":"generation","name":"name","objectPreconditions":{"ifGenerationMatch":"ifGenerationMatch"}}]}
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example'),
                    ('ifGenerationMatch', 'if_generation_match_example'),
                    ('ifMetagenerationMatch', 'if_metageneration_match_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/storage/v1beta2/b/{destination_bucket}/o/{destination_object}/compose'.format(destination_bucket='destination_bucket_example', destination_object='destination_object_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_storage_objects_copy(client):
    """Test case for storage_objects_copy

    
    """
    body = {"generation":"generation","owner":{"entityId":"entityId","entity":"entity"},"metadata":{"key":"metadata"},"metageneration":"metageneration","kind":"storage#object","acl":[{"bucket":"bucket","generation":"generation","role":"role","kind":"storage#objectAccessControl","domain":"domain","entityId":"entityId","etag":"etag","id":"id","email":"email","entity":"entity","object":"object","selfLink":"selfLink"},{"bucket":"bucket","generation":"generation","role":"role","kind":"storage#objectAccessControl","domain":"domain","entityId":"entityId","etag":"etag","id":"id","email":"email","entity":"entity","object":"object","selfLink":"selfLink"}],"cacheControl":"cacheControl","mediaLink":"mediaLink","selfLink":"selfLink","bucket":"bucket","timeDeleted":"2000-01-23T04:56:07.000+00:00","componentCount":0,"storageClass":"storageClass","crc32c":"crc32c","md5Hash":"md5Hash","size":"size","contentDisposition":"contentDisposition","name":"name","contentEncoding":"contentEncoding","contentLanguage":"contentLanguage","etag":"etag","id":"id","contentType":"contentType","updated":"2000-01-23T04:56:07.000+00:00"}
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example'),
                    ('ifGenerationMatch', 'if_generation_match_example'),
                    ('ifGenerationNotMatch', 'if_generation_not_match_example'),
                    ('ifMetagenerationMatch', 'if_metageneration_match_example'),
                    ('ifMetagenerationNotMatch', 'if_metageneration_not_match_example'),
                    ('ifSourceGenerationMatch', 'if_source_generation_match_example'),
                    ('ifSourceGenerationNotMatch', 'if_source_generation_not_match_example'),
                    ('ifSourceMetagenerationMatch', 'if_source_metageneration_match_example'),
                    ('ifSourceMetagenerationNotMatch', 'if_source_metageneration_not_match_example'),
                    ('projection', 'projection_example'),
                    ('sourceGeneration', 'source_generation_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/storage/v1beta2/b/{source_bucket}/o/{source_object}/copyTo/b/{destination_bucket}/o/{destination_object}'.format(source_bucket='source_bucket_example', source_object='source_object_example', destination_bucket='destination_bucket_example', destination_object='destination_object_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_storage_objects_delete(client):
    """Test case for storage_objects_delete

    
    """
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example'),
                    ('generation', 'generation_example'),
                    ('ifGenerationMatch', 'if_generation_match_example'),
                    ('ifGenerationNotMatch', 'if_generation_not_match_example'),
                    ('ifMetagenerationMatch', 'if_metageneration_match_example'),
                    ('ifMetagenerationNotMatch', 'if_metageneration_not_match_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/storage/v1beta2/b/{bucket}/o/{object}'.format(bucket='bucket_example', object='object_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_storage_objects_get(client):
    """Test case for storage_objects_get

    
    """
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example'),
                    ('generation', 'generation_example'),
                    ('ifGenerationMatch', 'if_generation_match_example'),
                    ('ifGenerationNotMatch', 'if_generation_not_match_example'),
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
        path='/storage/v1beta2/b/{bucket}/o/{object}'.format(bucket='bucket_example', object='object_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/octet-stream not supported by Connexion")
async def test_storage_objects_insert(client):
    """Test case for storage_objects_insert

    
    """
    body = openapi_server.Object()
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example'),
                    ('ifGenerationMatch', 'if_generation_match_example'),
                    ('ifGenerationNotMatch', 'if_generation_not_match_example'),
                    ('ifMetagenerationMatch', 'if_metageneration_match_example'),
                    ('ifMetagenerationNotMatch', 'if_metageneration_not_match_example'),
                    ('name', 'name_example'),
                    ('projection', 'projection_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/octet-stream',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/storage/v1beta2/b/{bucket}/o'.format(bucket='bucket_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_storage_objects_list(client):
    """Test case for storage_objects_list

    
    """
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example'),
                    ('delimiter', 'delimiter_example'),
                    ('maxResults', 56),
                    ('pageToken', 'page_token_example'),
                    ('prefix', 'prefix_example'),
                    ('projection', 'projection_example'),
                    ('versions', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/storage/v1beta2/b/{bucket}/o'.format(bucket='bucket_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_storage_objects_patch(client):
    """Test case for storage_objects_patch

    
    """
    body = {"generation":"generation","owner":{"entityId":"entityId","entity":"entity"},"metadata":{"key":"metadata"},"metageneration":"metageneration","kind":"storage#object","acl":[{"bucket":"bucket","generation":"generation","role":"role","kind":"storage#objectAccessControl","domain":"domain","entityId":"entityId","etag":"etag","id":"id","email":"email","entity":"entity","object":"object","selfLink":"selfLink"},{"bucket":"bucket","generation":"generation","role":"role","kind":"storage#objectAccessControl","domain":"domain","entityId":"entityId","etag":"etag","id":"id","email":"email","entity":"entity","object":"object","selfLink":"selfLink"}],"cacheControl":"cacheControl","mediaLink":"mediaLink","selfLink":"selfLink","bucket":"bucket","timeDeleted":"2000-01-23T04:56:07.000+00:00","componentCount":0,"storageClass":"storageClass","crc32c":"crc32c","md5Hash":"md5Hash","size":"size","contentDisposition":"contentDisposition","name":"name","contentEncoding":"contentEncoding","contentLanguage":"contentLanguage","etag":"etag","id":"id","contentType":"contentType","updated":"2000-01-23T04:56:07.000+00:00"}
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example'),
                    ('generation', 'generation_example'),
                    ('ifGenerationMatch', 'if_generation_match_example'),
                    ('ifGenerationNotMatch', 'if_generation_not_match_example'),
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
        path='/storage/v1beta2/b/{bucket}/o/{object}'.format(bucket='bucket_example', object='object_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_storage_objects_update(client):
    """Test case for storage_objects_update

    
    """
    body = {"generation":"generation","owner":{"entityId":"entityId","entity":"entity"},"metadata":{"key":"metadata"},"metageneration":"metageneration","kind":"storage#object","acl":[{"bucket":"bucket","generation":"generation","role":"role","kind":"storage#objectAccessControl","domain":"domain","entityId":"entityId","etag":"etag","id":"id","email":"email","entity":"entity","object":"object","selfLink":"selfLink"},{"bucket":"bucket","generation":"generation","role":"role","kind":"storage#objectAccessControl","domain":"domain","entityId":"entityId","etag":"etag","id":"id","email":"email","entity":"entity","object":"object","selfLink":"selfLink"}],"cacheControl":"cacheControl","mediaLink":"mediaLink","selfLink":"selfLink","bucket":"bucket","timeDeleted":"2000-01-23T04:56:07.000+00:00","componentCount":0,"storageClass":"storageClass","crc32c":"crc32c","md5Hash":"md5Hash","size":"size","contentDisposition":"contentDisposition","name":"name","contentEncoding":"contentEncoding","contentLanguage":"contentLanguage","etag":"etag","id":"id","contentType":"contentType","updated":"2000-01-23T04:56:07.000+00:00"}
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example'),
                    ('generation', 'generation_example'),
                    ('ifGenerationMatch', 'if_generation_match_example'),
                    ('ifGenerationNotMatch', 'if_generation_not_match_example'),
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
        path='/storage/v1beta2/b/{bucket}/o/{object}'.format(bucket='bucket_example', object='object_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_storage_objects_watch_all(client):
    """Test case for storage_objects_watch_all

    
    """
    body = {"resourceId":"resourceId","address":"address","payload":True,"kind":"api#channel","expiration":"expiration","id":"id","resourceUri":"resourceUri","params":{"key":"params"},"type":"type","token":"token"}
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example'),
                    ('delimiter', 'delimiter_example'),
                    ('maxResults', 56),
                    ('pageToken', 'page_token_example'),
                    ('prefix', 'prefix_example'),
                    ('projection', 'projection_example'),
                    ('versions', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/storage/v1beta2/b/{bucket}/o/watch'.format(bucket='bucket_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

