# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bulk_restore_objects_request import BulkRestoreObjectsRequest
from openapi_server.models.channel import Channel
from openapi_server.models.compose_request import ComposeRequest
from openapi_server.models.google_longrunning_operation import GoogleLongrunningOperation
from openapi_server.models.object import Object
from openapi_server.models.objects import Objects
from openapi_server.models.policy import Policy
from openapi_server.models.rewrite_response import RewriteResponse
from openapi_server.models.test_iam_permissions_response import TestIamPermissionsResponse


pytestmark = pytest.mark.asyncio

async def test_storage_objects_bulk_restore(client):
    """Test case for storage_objects_bulk_restore

    
    """
    body = {"matchGlobs":["matchGlobs","matchGlobs"],"softDeletedAfterTime":"2000-01-23T04:56:07.000+00:00","copySourceAcl":True,"allowOverwrite":True,"softDeletedBeforeTime":"2000-01-23T04:56:07.000+00:00"}
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('uploadType', 'upload_type_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/storage/v1/b/{bucket}/o/bulkRestore'.format(bucket='bucket_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_storage_objects_compose(client):
    """Test case for storage_objects_compose

    
    """
    body = {"kind":"storage#composeRequest","destination":{"metadata":{"key":"metadata"},"temporaryHold":True,"acl":[{"generation":"generation","role":"role","kind":"storage#objectAccessControl","entityId":"entityId","projectTeam":{"projectNumber":"projectNumber","team":"team"},"selfLink":"selfLink","bucket":"bucket","domain":"domain","etag":"etag","id":"id","email":"email","entity":"entity","object":"object"},{"generation":"generation","role":"role","kind":"storage#objectAccessControl","entityId":"entityId","projectTeam":{"projectNumber":"projectNumber","team":"team"},"selfLink":"selfLink","bucket":"bucket","domain":"domain","etag":"etag","id":"id","email":"email","entity":"entity","object":"object"}],"customerEncryption":{"encryptionAlgorithm":"encryptionAlgorithm","keySha256":"keySha256"},"timeDeleted":"2000-01-23T04:56:07.000+00:00","storageClass":"storageClass","hardDeleteTime":"2000-01-23T04:56:07.000+00:00","md5Hash":"md5Hash","contentDisposition":"contentDisposition","contentEncoding":"contentEncoding","timeCreated":"2000-01-23T04:56:07.000+00:00","id":"id","contentType":"contentType","retention":{"mode":"mode","retainUntilTime":"2000-01-23T04:56:07.000+00:00"},"generation":"generation","owner":{"entityId":"entityId","entity":"entity"},"metageneration":"metageneration","kind":"storage#object","customTime":"2000-01-23T04:56:07.000+00:00","retentionExpirationTime":"2000-01-23T04:56:07.000+00:00","cacheControl":"cacheControl","kmsKeyName":"kmsKeyName","mediaLink":"mediaLink","selfLink":"selfLink","bucket":"bucket","eventBasedHold":True,"componentCount":0,"crc32c":"crc32c","size":"size","timeStorageClassUpdated":"2000-01-23T04:56:07.000+00:00","name":"name","contentLanguage":"contentLanguage","etag":"etag","softDeleteTime":"2000-01-23T04:56:07.000+00:00","updated":"2000-01-23T04:56:07.000+00:00"},"sourceObjects":[{"generation":"generation","name":"name","objectPreconditions":{"ifGenerationMatch":"ifGenerationMatch"}},{"generation":"generation","name":"name","objectPreconditions":{"ifGenerationMatch":"ifGenerationMatch"}}]}
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('uploadType', 'upload_type_example'),
                    ('userIp', 'user_ip_example'),
                    ('destinationPredefinedAcl', 'destination_predefined_acl_example'),
                    ('ifGenerationMatch', 'if_generation_match_example'),
                    ('ifMetagenerationMatch', 'if_metageneration_match_example'),
                    ('kmsKeyName', 'kms_key_name_example'),
                    ('userProject', 'user_project_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/storage/v1/b/{destination_bucket}/o/{destination_object}/compose'.format(destination_bucket='destination_bucket_example', destination_object='destination_object_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_storage_objects_copy(client):
    """Test case for storage_objects_copy

    
    """
    body = {"metadata":{"key":"metadata"},"temporaryHold":True,"acl":[{"generation":"generation","role":"role","kind":"storage#objectAccessControl","entityId":"entityId","projectTeam":{"projectNumber":"projectNumber","team":"team"},"selfLink":"selfLink","bucket":"bucket","domain":"domain","etag":"etag","id":"id","email":"email","entity":"entity","object":"object"},{"generation":"generation","role":"role","kind":"storage#objectAccessControl","entityId":"entityId","projectTeam":{"projectNumber":"projectNumber","team":"team"},"selfLink":"selfLink","bucket":"bucket","domain":"domain","etag":"etag","id":"id","email":"email","entity":"entity","object":"object"}],"customerEncryption":{"encryptionAlgorithm":"encryptionAlgorithm","keySha256":"keySha256"},"timeDeleted":"2000-01-23T04:56:07.000+00:00","storageClass":"storageClass","hardDeleteTime":"2000-01-23T04:56:07.000+00:00","md5Hash":"md5Hash","contentDisposition":"contentDisposition","contentEncoding":"contentEncoding","timeCreated":"2000-01-23T04:56:07.000+00:00","id":"id","contentType":"contentType","retention":{"mode":"mode","retainUntilTime":"2000-01-23T04:56:07.000+00:00"},"generation":"generation","owner":{"entityId":"entityId","entity":"entity"},"metageneration":"metageneration","kind":"storage#object","customTime":"2000-01-23T04:56:07.000+00:00","retentionExpirationTime":"2000-01-23T04:56:07.000+00:00","cacheControl":"cacheControl","kmsKeyName":"kmsKeyName","mediaLink":"mediaLink","selfLink":"selfLink","bucket":"bucket","eventBasedHold":True,"componentCount":0,"crc32c":"crc32c","size":"size","timeStorageClassUpdated":"2000-01-23T04:56:07.000+00:00","name":"name","contentLanguage":"contentLanguage","etag":"etag","softDeleteTime":"2000-01-23T04:56:07.000+00:00","updated":"2000-01-23T04:56:07.000+00:00"}
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('uploadType', 'upload_type_example'),
                    ('userIp', 'user_ip_example'),
                    ('destinationKmsKeyName', 'destination_kms_key_name_example'),
                    ('destinationPredefinedAcl', 'destination_predefined_acl_example'),
                    ('ifGenerationMatch', 'if_generation_match_example'),
                    ('ifGenerationNotMatch', 'if_generation_not_match_example'),
                    ('ifMetagenerationMatch', 'if_metageneration_match_example'),
                    ('ifMetagenerationNotMatch', 'if_metageneration_not_match_example'),
                    ('ifSourceGenerationMatch', 'if_source_generation_match_example'),
                    ('ifSourceGenerationNotMatch', 'if_source_generation_not_match_example'),
                    ('ifSourceMetagenerationMatch', 'if_source_metageneration_match_example'),
                    ('ifSourceMetagenerationNotMatch', 'if_source_metageneration_not_match_example'),
                    ('projection', 'projection_example'),
                    ('sourceGeneration', 'source_generation_example'),
                    ('userProject', 'user_project_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/storage/v1/b/{source_bucket}/o/{source_object}/copyTo/b/{destination_bucket}/o/{destination_object}'.format(source_bucket='source_bucket_example', source_object='source_object_example', destination_bucket='destination_bucket_example', destination_object='destination_object_example'),
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
                    ('uploadType', 'upload_type_example'),
                    ('userIp', 'user_ip_example'),
                    ('generation', 'generation_example'),
                    ('ifGenerationMatch', 'if_generation_match_example'),
                    ('ifGenerationNotMatch', 'if_generation_not_match_example'),
                    ('ifMetagenerationMatch', 'if_metageneration_match_example'),
                    ('ifMetagenerationNotMatch', 'if_metageneration_not_match_example'),
                    ('userProject', 'user_project_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/storage/v1/b/{bucket}/o/{object}'.format(bucket='bucket_example', object='object_example'),
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
                    ('uploadType', 'upload_type_example'),
                    ('userIp', 'user_ip_example'),
                    ('generation', 'generation_example'),
                    ('ifGenerationMatch', 'if_generation_match_example'),
                    ('ifGenerationNotMatch', 'if_generation_not_match_example'),
                    ('ifMetagenerationMatch', 'if_metageneration_match_example'),
                    ('ifMetagenerationNotMatch', 'if_metageneration_not_match_example'),
                    ('projection', 'projection_example'),
                    ('softDeleted', True),
                    ('userProject', 'user_project_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/storage/v1/b/{bucket}/o/{object}'.format(bucket='bucket_example', object='object_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_storage_objects_get_iam_policy(client):
    """Test case for storage_objects_get_iam_policy

    
    """
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('uploadType', 'upload_type_example'),
                    ('userIp', 'user_ip_example'),
                    ('generation', 'generation_example'),
                    ('userProject', 'user_project_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/storage/v1/b/{bucket}/o/{object}/iam'.format(bucket='bucket_example', object='object_example'),
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
                    ('uploadType', 'upload_type_example'),
                    ('userIp', 'user_ip_example'),
                    ('contentEncoding', 'content_encoding_example'),
                    ('ifGenerationMatch', 'if_generation_match_example'),
                    ('ifGenerationNotMatch', 'if_generation_not_match_example'),
                    ('ifMetagenerationMatch', 'if_metageneration_match_example'),
                    ('ifMetagenerationNotMatch', 'if_metageneration_not_match_example'),
                    ('kmsKeyName', 'kms_key_name_example'),
                    ('name', 'name_example'),
                    ('predefinedAcl', 'predefined_acl_example'),
                    ('projection', 'projection_example'),
                    ('userProject', 'user_project_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/octet-stream',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/storage/v1/b/{bucket}/o'.format(bucket='bucket_example'),
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
                    ('uploadType', 'upload_type_example'),
                    ('userIp', 'user_ip_example'),
                    ('delimiter', 'delimiter_example'),
                    ('endOffset', 'end_offset_example'),
                    ('includeFoldersAsPrefixes', True),
                    ('includeTrailingDelimiter', True),
                    ('matchGlob', 'match_glob_example'),
                    ('maxResults', 56),
                    ('pageToken', 'page_token_example'),
                    ('prefix', 'prefix_example'),
                    ('projection', 'projection_example'),
                    ('softDeleted', True),
                    ('startOffset', 'start_offset_example'),
                    ('userProject', 'user_project_example'),
                    ('versions', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/storage/v1/b/{bucket}/o'.format(bucket='bucket_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_storage_objects_patch(client):
    """Test case for storage_objects_patch

    
    """
    body = {"metadata":{"key":"metadata"},"temporaryHold":True,"acl":[{"generation":"generation","role":"role","kind":"storage#objectAccessControl","entityId":"entityId","projectTeam":{"projectNumber":"projectNumber","team":"team"},"selfLink":"selfLink","bucket":"bucket","domain":"domain","etag":"etag","id":"id","email":"email","entity":"entity","object":"object"},{"generation":"generation","role":"role","kind":"storage#objectAccessControl","entityId":"entityId","projectTeam":{"projectNumber":"projectNumber","team":"team"},"selfLink":"selfLink","bucket":"bucket","domain":"domain","etag":"etag","id":"id","email":"email","entity":"entity","object":"object"}],"customerEncryption":{"encryptionAlgorithm":"encryptionAlgorithm","keySha256":"keySha256"},"timeDeleted":"2000-01-23T04:56:07.000+00:00","storageClass":"storageClass","hardDeleteTime":"2000-01-23T04:56:07.000+00:00","md5Hash":"md5Hash","contentDisposition":"contentDisposition","contentEncoding":"contentEncoding","timeCreated":"2000-01-23T04:56:07.000+00:00","id":"id","contentType":"contentType","retention":{"mode":"mode","retainUntilTime":"2000-01-23T04:56:07.000+00:00"},"generation":"generation","owner":{"entityId":"entityId","entity":"entity"},"metageneration":"metageneration","kind":"storage#object","customTime":"2000-01-23T04:56:07.000+00:00","retentionExpirationTime":"2000-01-23T04:56:07.000+00:00","cacheControl":"cacheControl","kmsKeyName":"kmsKeyName","mediaLink":"mediaLink","selfLink":"selfLink","bucket":"bucket","eventBasedHold":True,"componentCount":0,"crc32c":"crc32c","size":"size","timeStorageClassUpdated":"2000-01-23T04:56:07.000+00:00","name":"name","contentLanguage":"contentLanguage","etag":"etag","softDeleteTime":"2000-01-23T04:56:07.000+00:00","updated":"2000-01-23T04:56:07.000+00:00"}
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('uploadType', 'upload_type_example'),
                    ('userIp', 'user_ip_example'),
                    ('generation', 'generation_example'),
                    ('ifGenerationMatch', 'if_generation_match_example'),
                    ('ifGenerationNotMatch', 'if_generation_not_match_example'),
                    ('ifMetagenerationMatch', 'if_metageneration_match_example'),
                    ('ifMetagenerationNotMatch', 'if_metageneration_not_match_example'),
                    ('overrideUnlockedRetention', True),
                    ('predefinedAcl', 'predefined_acl_example'),
                    ('projection', 'projection_example'),
                    ('userProject', 'user_project_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/storage/v1/b/{bucket}/o/{object}'.format(bucket='bucket_example', object='object_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_storage_objects_restore(client):
    """Test case for storage_objects_restore

    
    """
    body = {"metadata":{"key":"metadata"},"temporaryHold":True,"acl":[{"generation":"generation","role":"role","kind":"storage#objectAccessControl","entityId":"entityId","projectTeam":{"projectNumber":"projectNumber","team":"team"},"selfLink":"selfLink","bucket":"bucket","domain":"domain","etag":"etag","id":"id","email":"email","entity":"entity","object":"object"},{"generation":"generation","role":"role","kind":"storage#objectAccessControl","entityId":"entityId","projectTeam":{"projectNumber":"projectNumber","team":"team"},"selfLink":"selfLink","bucket":"bucket","domain":"domain","etag":"etag","id":"id","email":"email","entity":"entity","object":"object"}],"customerEncryption":{"encryptionAlgorithm":"encryptionAlgorithm","keySha256":"keySha256"},"timeDeleted":"2000-01-23T04:56:07.000+00:00","storageClass":"storageClass","hardDeleteTime":"2000-01-23T04:56:07.000+00:00","md5Hash":"md5Hash","contentDisposition":"contentDisposition","contentEncoding":"contentEncoding","timeCreated":"2000-01-23T04:56:07.000+00:00","id":"id","contentType":"contentType","retention":{"mode":"mode","retainUntilTime":"2000-01-23T04:56:07.000+00:00"},"generation":"generation","owner":{"entityId":"entityId","entity":"entity"},"metageneration":"metageneration","kind":"storage#object","customTime":"2000-01-23T04:56:07.000+00:00","retentionExpirationTime":"2000-01-23T04:56:07.000+00:00","cacheControl":"cacheControl","kmsKeyName":"kmsKeyName","mediaLink":"mediaLink","selfLink":"selfLink","bucket":"bucket","eventBasedHold":True,"componentCount":0,"crc32c":"crc32c","size":"size","timeStorageClassUpdated":"2000-01-23T04:56:07.000+00:00","name":"name","contentLanguage":"contentLanguage","etag":"etag","softDeleteTime":"2000-01-23T04:56:07.000+00:00","updated":"2000-01-23T04:56:07.000+00:00"}
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('uploadType', 'upload_type_example'),
                    ('userIp', 'user_ip_example'),
                    ('copySourceAcl', True),
                    ('generation', 'generation_example'),
                    ('ifGenerationMatch', 'if_generation_match_example'),
                    ('ifGenerationNotMatch', 'if_generation_not_match_example'),
                    ('ifMetagenerationMatch', 'if_metageneration_match_example'),
                    ('ifMetagenerationNotMatch', 'if_metageneration_not_match_example'),
                    ('projection', 'projection_example'),
                    ('userProject', 'user_project_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/storage/v1/b/{bucket}/o/{object}/restore'.format(bucket='bucket_example', object='object_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_storage_objects_rewrite(client):
    """Test case for storage_objects_rewrite

    
    """
    body = {"metadata":{"key":"metadata"},"temporaryHold":True,"acl":[{"generation":"generation","role":"role","kind":"storage#objectAccessControl","entityId":"entityId","projectTeam":{"projectNumber":"projectNumber","team":"team"},"selfLink":"selfLink","bucket":"bucket","domain":"domain","etag":"etag","id":"id","email":"email","entity":"entity","object":"object"},{"generation":"generation","role":"role","kind":"storage#objectAccessControl","entityId":"entityId","projectTeam":{"projectNumber":"projectNumber","team":"team"},"selfLink":"selfLink","bucket":"bucket","domain":"domain","etag":"etag","id":"id","email":"email","entity":"entity","object":"object"}],"customerEncryption":{"encryptionAlgorithm":"encryptionAlgorithm","keySha256":"keySha256"},"timeDeleted":"2000-01-23T04:56:07.000+00:00","storageClass":"storageClass","hardDeleteTime":"2000-01-23T04:56:07.000+00:00","md5Hash":"md5Hash","contentDisposition":"contentDisposition","contentEncoding":"contentEncoding","timeCreated":"2000-01-23T04:56:07.000+00:00","id":"id","contentType":"contentType","retention":{"mode":"mode","retainUntilTime":"2000-01-23T04:56:07.000+00:00"},"generation":"generation","owner":{"entityId":"entityId","entity":"entity"},"metageneration":"metageneration","kind":"storage#object","customTime":"2000-01-23T04:56:07.000+00:00","retentionExpirationTime":"2000-01-23T04:56:07.000+00:00","cacheControl":"cacheControl","kmsKeyName":"kmsKeyName","mediaLink":"mediaLink","selfLink":"selfLink","bucket":"bucket","eventBasedHold":True,"componentCount":0,"crc32c":"crc32c","size":"size","timeStorageClassUpdated":"2000-01-23T04:56:07.000+00:00","name":"name","contentLanguage":"contentLanguage","etag":"etag","softDeleteTime":"2000-01-23T04:56:07.000+00:00","updated":"2000-01-23T04:56:07.000+00:00"}
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('uploadType', 'upload_type_example'),
                    ('userIp', 'user_ip_example'),
                    ('destinationKmsKeyName', 'destination_kms_key_name_example'),
                    ('destinationPredefinedAcl', 'destination_predefined_acl_example'),
                    ('ifGenerationMatch', 'if_generation_match_example'),
                    ('ifGenerationNotMatch', 'if_generation_not_match_example'),
                    ('ifMetagenerationMatch', 'if_metageneration_match_example'),
                    ('ifMetagenerationNotMatch', 'if_metageneration_not_match_example'),
                    ('ifSourceGenerationMatch', 'if_source_generation_match_example'),
                    ('ifSourceGenerationNotMatch', 'if_source_generation_not_match_example'),
                    ('ifSourceMetagenerationMatch', 'if_source_metageneration_match_example'),
                    ('ifSourceMetagenerationNotMatch', 'if_source_metageneration_not_match_example'),
                    ('maxBytesRewrittenPerCall', 'max_bytes_rewritten_per_call_example'),
                    ('projection', 'projection_example'),
                    ('rewriteToken', 'rewrite_token_example'),
                    ('sourceGeneration', 'source_generation_example'),
                    ('userProject', 'user_project_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/storage/v1/b/{source_bucket}/o/{source_object}/rewriteTo/b/{destination_bucket}/o/{destination_object}'.format(source_bucket='source_bucket_example', source_object='source_object_example', destination_bucket='destination_bucket_example', destination_object='destination_object_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_storage_objects_set_iam_policy(client):
    """Test case for storage_objects_set_iam_policy

    
    """
    body = {"resourceId":"resourceId","kind":"storage#policy","bindings":[{"condition":{"expression":"expression","description":"description","location":"location","title":"title"},"role":"role","members":["members","members"]},{"condition":{"expression":"expression","description":"description","location":"location","title":"title"},"role":"role","members":["members","members"]}],"etag":"etag","version":0}
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('uploadType', 'upload_type_example'),
                    ('userIp', 'user_ip_example'),
                    ('generation', 'generation_example'),
                    ('userProject', 'user_project_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/storage/v1/b/{bucket}/o/{object}/iam'.format(bucket='bucket_example', object='object_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_storage_objects_test_iam_permissions(client):
    """Test case for storage_objects_test_iam_permissions

    
    """
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('uploadType', 'upload_type_example'),
                    ('userIp', 'user_ip_example'),
                    ('permissions', ['permissions_example']),
                    ('generation', 'generation_example'),
                    ('userProject', 'user_project_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/storage/v1/b/{bucket}/o/{object}/iam/testPermissions'.format(bucket='bucket_example', object='object_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_storage_objects_update(client):
    """Test case for storage_objects_update

    
    """
    body = {"metadata":{"key":"metadata"},"temporaryHold":True,"acl":[{"generation":"generation","role":"role","kind":"storage#objectAccessControl","entityId":"entityId","projectTeam":{"projectNumber":"projectNumber","team":"team"},"selfLink":"selfLink","bucket":"bucket","domain":"domain","etag":"etag","id":"id","email":"email","entity":"entity","object":"object"},{"generation":"generation","role":"role","kind":"storage#objectAccessControl","entityId":"entityId","projectTeam":{"projectNumber":"projectNumber","team":"team"},"selfLink":"selfLink","bucket":"bucket","domain":"domain","etag":"etag","id":"id","email":"email","entity":"entity","object":"object"}],"customerEncryption":{"encryptionAlgorithm":"encryptionAlgorithm","keySha256":"keySha256"},"timeDeleted":"2000-01-23T04:56:07.000+00:00","storageClass":"storageClass","hardDeleteTime":"2000-01-23T04:56:07.000+00:00","md5Hash":"md5Hash","contentDisposition":"contentDisposition","contentEncoding":"contentEncoding","timeCreated":"2000-01-23T04:56:07.000+00:00","id":"id","contentType":"contentType","retention":{"mode":"mode","retainUntilTime":"2000-01-23T04:56:07.000+00:00"},"generation":"generation","owner":{"entityId":"entityId","entity":"entity"},"metageneration":"metageneration","kind":"storage#object","customTime":"2000-01-23T04:56:07.000+00:00","retentionExpirationTime":"2000-01-23T04:56:07.000+00:00","cacheControl":"cacheControl","kmsKeyName":"kmsKeyName","mediaLink":"mediaLink","selfLink":"selfLink","bucket":"bucket","eventBasedHold":True,"componentCount":0,"crc32c":"crc32c","size":"size","timeStorageClassUpdated":"2000-01-23T04:56:07.000+00:00","name":"name","contentLanguage":"contentLanguage","etag":"etag","softDeleteTime":"2000-01-23T04:56:07.000+00:00","updated":"2000-01-23T04:56:07.000+00:00"}
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('uploadType', 'upload_type_example'),
                    ('userIp', 'user_ip_example'),
                    ('generation', 'generation_example'),
                    ('ifGenerationMatch', 'if_generation_match_example'),
                    ('ifGenerationNotMatch', 'if_generation_not_match_example'),
                    ('ifMetagenerationMatch', 'if_metageneration_match_example'),
                    ('ifMetagenerationNotMatch', 'if_metageneration_not_match_example'),
                    ('overrideUnlockedRetention', True),
                    ('predefinedAcl', 'predefined_acl_example'),
                    ('projection', 'projection_example'),
                    ('userProject', 'user_project_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/storage/v1/b/{bucket}/o/{object}'.format(bucket='bucket_example', object='object_example'),
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
                    ('uploadType', 'upload_type_example'),
                    ('userIp', 'user_ip_example'),
                    ('delimiter', 'delimiter_example'),
                    ('endOffset', 'end_offset_example'),
                    ('includeTrailingDelimiter', True),
                    ('maxResults', 56),
                    ('pageToken', 'page_token_example'),
                    ('prefix', 'prefix_example'),
                    ('projection', 'projection_example'),
                    ('startOffset', 'start_offset_example'),
                    ('userProject', 'user_project_example'),
                    ('versions', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/storage/v1/b/{bucket}/o/watch'.format(bucket='bucket_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

