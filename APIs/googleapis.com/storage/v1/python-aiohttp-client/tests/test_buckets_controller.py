# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bucket import Bucket
from openapi_server.models.buckets import Buckets
from openapi_server.models.policy import Policy
from openapi_server.models.test_iam_permissions_response import TestIamPermissionsResponse


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
                    ('uploadType', 'upload_type_example'),
                    ('userIp', 'user_ip_example'),
                    ('ifMetagenerationMatch', 'if_metageneration_match_example'),
                    ('ifMetagenerationNotMatch', 'if_metageneration_not_match_example'),
                    ('userProject', 'user_project_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/storage/v1/b/{bucket}'.format(bucket='bucket_example'),
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
                    ('uploadType', 'upload_type_example'),
                    ('userIp', 'user_ip_example'),
                    ('ifMetagenerationMatch', 'if_metageneration_match_example'),
                    ('ifMetagenerationNotMatch', 'if_metageneration_not_match_example'),
                    ('projection', 'projection_example'),
                    ('userProject', 'user_project_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/storage/v1/b/{bucket}'.format(bucket='bucket_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_storage_buckets_get_iam_policy(client):
    """Test case for storage_buckets_get_iam_policy

    
    """
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('uploadType', 'upload_type_example'),
                    ('userIp', 'user_ip_example'),
                    ('optionsRequestedPolicyVersion', 56),
                    ('userProject', 'user_project_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/storage/v1/b/{bucket}/iam'.format(bucket='bucket_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_storage_buckets_insert(client):
    """Test case for storage_buckets_insert

    
    """
    body = {"cors":[{"method":["method","method"],"origin":["origin","origin"],"responseHeader":["responseHeader","responseHeader"],"maxAgeSeconds":0},{"method":["method","method"],"origin":["origin","origin"],"responseHeader":["responseHeader","responseHeader"],"maxAgeSeconds":0}],"versioning":{"enabled":True},"locationType":"locationType","satisfiesPZS":True,"acl":[{"bucket":"bucket","role":"role","kind":"storage#bucketAccessControl","domain":"domain","entityId":"entityId","etag":"etag","id":"id","projectTeam":{"projectNumber":"projectNumber","team":"team"},"email":"email","entity":"entity","selfLink":"selfLink"},{"bucket":"bucket","role":"role","kind":"storage#bucketAccessControl","domain":"domain","entityId":"entityId","etag":"etag","id":"id","projectTeam":{"projectNumber":"projectNumber","team":"team"},"email":"email","entity":"entity","selfLink":"selfLink"}],"billing":{"requesterPays":True},"lifecycle":{"rule":[{"condition":{"matchesSuffix":["matchesSuffix","matchesSuffix"],"isLive":True,"numNewerVersions":5,"daysSinceCustomTime":1,"createdBefore":"2000-01-23","customTimeBefore":"2000-01-23","noncurrentTimeBefore":"2000-01-23","age":6,"matchesPrefix":["matchesPrefix","matchesPrefix"],"matchesStorageClass":["matchesStorageClass","matchesStorageClass"],"daysSinceNoncurrentTime":5,"matchesPattern":"matchesPattern"},"action":{"storageClass":"storageClass","type":"type"}},{"condition":{"matchesSuffix":["matchesSuffix","matchesSuffix"],"isLive":True,"numNewerVersions":5,"daysSinceCustomTime":1,"createdBefore":"2000-01-23","customTimeBefore":"2000-01-23","noncurrentTimeBefore":"2000-01-23","age":6,"matchesPrefix":["matchesPrefix","matchesPrefix"],"matchesStorageClass":["matchesStorageClass","matchesStorageClass"],"daysSinceNoncurrentTime":5,"matchesPattern":"matchesPattern"},"action":{"storageClass":"storageClass","type":"type"}}]},"storageClass":"storageClass","autoclass":{"toggleTime":"2000-01-23T04:56:07.000+00:00","terminalStorageClass":"terminalStorageClass","enabled":True,"terminalStorageClassUpdateTime":"2000-01-23T04:56:07.000+00:00"},"objectRetention":{"mode":"mode"},"encryption":{"defaultKmsKeyName":"defaultKmsKeyName"},"iamConfiguration":{"bucketPolicyOnly":{"enabled":True,"lockedTime":"2000-01-23T04:56:07.000+00:00"},"uniformBucketLevelAccess":{"enabled":True,"lockedTime":"2000-01-23T04:56:07.000+00:00"},"publicAccessPrevention":"publicAccessPrevention"},"timeCreated":"2000-01-23T04:56:07.000+00:00","id":"id","retentionPolicy":{"effectiveTime":"2000-01-23T04:56:07.000+00:00","isLocked":True,"retentionPeriod":"retentionPeriod"},"defaultObjectAcl":[{"generation":"generation","role":"role","kind":"storage#objectAccessControl","entityId":"entityId","projectTeam":{"projectNumber":"projectNumber","team":"team"},"selfLink":"selfLink","bucket":"bucket","domain":"domain","etag":"etag","id":"id","email":"email","entity":"entity","object":"object"},{"generation":"generation","role":"role","kind":"storage#objectAccessControl","entityId":"entityId","projectTeam":{"projectNumber":"projectNumber","team":"team"},"selfLink":"selfLink","bucket":"bucket","domain":"domain","etag":"etag","id":"id","email":"email","entity":"entity","object":"object"}],"owner":{"entityId":"entityId","entity":"entity"},"customPlacementConfig":{"dataLocations":["dataLocations","dataLocations"]},"metageneration":"metageneration","website":{"mainPageSuffix":"mainPageSuffix","notFoundPage":"notFoundPage"},"kind":"storage#bucket","projectNumber":"projectNumber","labels":{"key":"labels"},"selfLink":"selfLink","rpo":"rpo","hierarchicalNamespace":{"enabled":True},"defaultEventBasedHold":True,"name":"name","logging":{"logBucket":"logBucket","logObjectPrefix":"logObjectPrefix"},"etag":"etag","location":"location","softDeletePolicy":{"retentionDurationSeconds":"retentionDurationSeconds","effectiveTime":"2000-01-23T04:56:07.000+00:00"},"updated":"2000-01-23T04:56:07.000+00:00"}
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('uploadType', 'upload_type_example'),
                    ('userIp', 'user_ip_example'),
                    ('project', 'project_example'),
                    ('enableObjectRetention', True),
                    ('predefinedAcl', 'predefined_acl_example'),
                    ('predefinedDefaultObjectAcl', 'predefined_default_object_acl_example'),
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
        path='/storage/v1/b',
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
                    ('uploadType', 'upload_type_example'),
                    ('userIp', 'user_ip_example'),
                    ('project', 'project_example'),
                    ('maxResults', 56),
                    ('pageToken', 'page_token_example'),
                    ('prefix', 'prefix_example'),
                    ('projection', 'projection_example'),
                    ('userProject', 'user_project_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/storage/v1/b',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_storage_buckets_lock_retention_policy(client):
    """Test case for storage_buckets_lock_retention_policy

    
    """
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('uploadType', 'upload_type_example'),
                    ('userIp', 'user_ip_example'),
                    ('ifMetagenerationMatch', 'if_metageneration_match_example'),
                    ('userProject', 'user_project_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/storage/v1/b/{bucket}/lockRetentionPolicy'.format(bucket='bucket_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_storage_buckets_patch(client):
    """Test case for storage_buckets_patch

    
    """
    body = {"cors":[{"method":["method","method"],"origin":["origin","origin"],"responseHeader":["responseHeader","responseHeader"],"maxAgeSeconds":0},{"method":["method","method"],"origin":["origin","origin"],"responseHeader":["responseHeader","responseHeader"],"maxAgeSeconds":0}],"versioning":{"enabled":True},"locationType":"locationType","satisfiesPZS":True,"acl":[{"bucket":"bucket","role":"role","kind":"storage#bucketAccessControl","domain":"domain","entityId":"entityId","etag":"etag","id":"id","projectTeam":{"projectNumber":"projectNumber","team":"team"},"email":"email","entity":"entity","selfLink":"selfLink"},{"bucket":"bucket","role":"role","kind":"storage#bucketAccessControl","domain":"domain","entityId":"entityId","etag":"etag","id":"id","projectTeam":{"projectNumber":"projectNumber","team":"team"},"email":"email","entity":"entity","selfLink":"selfLink"}],"billing":{"requesterPays":True},"lifecycle":{"rule":[{"condition":{"matchesSuffix":["matchesSuffix","matchesSuffix"],"isLive":True,"numNewerVersions":5,"daysSinceCustomTime":1,"createdBefore":"2000-01-23","customTimeBefore":"2000-01-23","noncurrentTimeBefore":"2000-01-23","age":6,"matchesPrefix":["matchesPrefix","matchesPrefix"],"matchesStorageClass":["matchesStorageClass","matchesStorageClass"],"daysSinceNoncurrentTime":5,"matchesPattern":"matchesPattern"},"action":{"storageClass":"storageClass","type":"type"}},{"condition":{"matchesSuffix":["matchesSuffix","matchesSuffix"],"isLive":True,"numNewerVersions":5,"daysSinceCustomTime":1,"createdBefore":"2000-01-23","customTimeBefore":"2000-01-23","noncurrentTimeBefore":"2000-01-23","age":6,"matchesPrefix":["matchesPrefix","matchesPrefix"],"matchesStorageClass":["matchesStorageClass","matchesStorageClass"],"daysSinceNoncurrentTime":5,"matchesPattern":"matchesPattern"},"action":{"storageClass":"storageClass","type":"type"}}]},"storageClass":"storageClass","autoclass":{"toggleTime":"2000-01-23T04:56:07.000+00:00","terminalStorageClass":"terminalStorageClass","enabled":True,"terminalStorageClassUpdateTime":"2000-01-23T04:56:07.000+00:00"},"objectRetention":{"mode":"mode"},"encryption":{"defaultKmsKeyName":"defaultKmsKeyName"},"iamConfiguration":{"bucketPolicyOnly":{"enabled":True,"lockedTime":"2000-01-23T04:56:07.000+00:00"},"uniformBucketLevelAccess":{"enabled":True,"lockedTime":"2000-01-23T04:56:07.000+00:00"},"publicAccessPrevention":"publicAccessPrevention"},"timeCreated":"2000-01-23T04:56:07.000+00:00","id":"id","retentionPolicy":{"effectiveTime":"2000-01-23T04:56:07.000+00:00","isLocked":True,"retentionPeriod":"retentionPeriod"},"defaultObjectAcl":[{"generation":"generation","role":"role","kind":"storage#objectAccessControl","entityId":"entityId","projectTeam":{"projectNumber":"projectNumber","team":"team"},"selfLink":"selfLink","bucket":"bucket","domain":"domain","etag":"etag","id":"id","email":"email","entity":"entity","object":"object"},{"generation":"generation","role":"role","kind":"storage#objectAccessControl","entityId":"entityId","projectTeam":{"projectNumber":"projectNumber","team":"team"},"selfLink":"selfLink","bucket":"bucket","domain":"domain","etag":"etag","id":"id","email":"email","entity":"entity","object":"object"}],"owner":{"entityId":"entityId","entity":"entity"},"customPlacementConfig":{"dataLocations":["dataLocations","dataLocations"]},"metageneration":"metageneration","website":{"mainPageSuffix":"mainPageSuffix","notFoundPage":"notFoundPage"},"kind":"storage#bucket","projectNumber":"projectNumber","labels":{"key":"labels"},"selfLink":"selfLink","rpo":"rpo","hierarchicalNamespace":{"enabled":True},"defaultEventBasedHold":True,"name":"name","logging":{"logBucket":"logBucket","logObjectPrefix":"logObjectPrefix"},"etag":"etag","location":"location","softDeletePolicy":{"retentionDurationSeconds":"retentionDurationSeconds","effectiveTime":"2000-01-23T04:56:07.000+00:00"},"updated":"2000-01-23T04:56:07.000+00:00"}
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('uploadType', 'upload_type_example'),
                    ('userIp', 'user_ip_example'),
                    ('ifMetagenerationMatch', 'if_metageneration_match_example'),
                    ('ifMetagenerationNotMatch', 'if_metageneration_not_match_example'),
                    ('predefinedAcl', 'predefined_acl_example'),
                    ('predefinedDefaultObjectAcl', 'predefined_default_object_acl_example'),
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
        path='/storage/v1/b/{bucket}'.format(bucket='bucket_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_storage_buckets_set_iam_policy(client):
    """Test case for storage_buckets_set_iam_policy

    
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
                    ('userProject', 'user_project_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/storage/v1/b/{bucket}/iam'.format(bucket='bucket_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_storage_buckets_test_iam_permissions(client):
    """Test case for storage_buckets_test_iam_permissions

    
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
                    ('userProject', 'user_project_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/storage/v1/b/{bucket}/iam/testPermissions'.format(bucket='bucket_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_storage_buckets_update(client):
    """Test case for storage_buckets_update

    
    """
    body = {"cors":[{"method":["method","method"],"origin":["origin","origin"],"responseHeader":["responseHeader","responseHeader"],"maxAgeSeconds":0},{"method":["method","method"],"origin":["origin","origin"],"responseHeader":["responseHeader","responseHeader"],"maxAgeSeconds":0}],"versioning":{"enabled":True},"locationType":"locationType","satisfiesPZS":True,"acl":[{"bucket":"bucket","role":"role","kind":"storage#bucketAccessControl","domain":"domain","entityId":"entityId","etag":"etag","id":"id","projectTeam":{"projectNumber":"projectNumber","team":"team"},"email":"email","entity":"entity","selfLink":"selfLink"},{"bucket":"bucket","role":"role","kind":"storage#bucketAccessControl","domain":"domain","entityId":"entityId","etag":"etag","id":"id","projectTeam":{"projectNumber":"projectNumber","team":"team"},"email":"email","entity":"entity","selfLink":"selfLink"}],"billing":{"requesterPays":True},"lifecycle":{"rule":[{"condition":{"matchesSuffix":["matchesSuffix","matchesSuffix"],"isLive":True,"numNewerVersions":5,"daysSinceCustomTime":1,"createdBefore":"2000-01-23","customTimeBefore":"2000-01-23","noncurrentTimeBefore":"2000-01-23","age":6,"matchesPrefix":["matchesPrefix","matchesPrefix"],"matchesStorageClass":["matchesStorageClass","matchesStorageClass"],"daysSinceNoncurrentTime":5,"matchesPattern":"matchesPattern"},"action":{"storageClass":"storageClass","type":"type"}},{"condition":{"matchesSuffix":["matchesSuffix","matchesSuffix"],"isLive":True,"numNewerVersions":5,"daysSinceCustomTime":1,"createdBefore":"2000-01-23","customTimeBefore":"2000-01-23","noncurrentTimeBefore":"2000-01-23","age":6,"matchesPrefix":["matchesPrefix","matchesPrefix"],"matchesStorageClass":["matchesStorageClass","matchesStorageClass"],"daysSinceNoncurrentTime":5,"matchesPattern":"matchesPattern"},"action":{"storageClass":"storageClass","type":"type"}}]},"storageClass":"storageClass","autoclass":{"toggleTime":"2000-01-23T04:56:07.000+00:00","terminalStorageClass":"terminalStorageClass","enabled":True,"terminalStorageClassUpdateTime":"2000-01-23T04:56:07.000+00:00"},"objectRetention":{"mode":"mode"},"encryption":{"defaultKmsKeyName":"defaultKmsKeyName"},"iamConfiguration":{"bucketPolicyOnly":{"enabled":True,"lockedTime":"2000-01-23T04:56:07.000+00:00"},"uniformBucketLevelAccess":{"enabled":True,"lockedTime":"2000-01-23T04:56:07.000+00:00"},"publicAccessPrevention":"publicAccessPrevention"},"timeCreated":"2000-01-23T04:56:07.000+00:00","id":"id","retentionPolicy":{"effectiveTime":"2000-01-23T04:56:07.000+00:00","isLocked":True,"retentionPeriod":"retentionPeriod"},"defaultObjectAcl":[{"generation":"generation","role":"role","kind":"storage#objectAccessControl","entityId":"entityId","projectTeam":{"projectNumber":"projectNumber","team":"team"},"selfLink":"selfLink","bucket":"bucket","domain":"domain","etag":"etag","id":"id","email":"email","entity":"entity","object":"object"},{"generation":"generation","role":"role","kind":"storage#objectAccessControl","entityId":"entityId","projectTeam":{"projectNumber":"projectNumber","team":"team"},"selfLink":"selfLink","bucket":"bucket","domain":"domain","etag":"etag","id":"id","email":"email","entity":"entity","object":"object"}],"owner":{"entityId":"entityId","entity":"entity"},"customPlacementConfig":{"dataLocations":["dataLocations","dataLocations"]},"metageneration":"metageneration","website":{"mainPageSuffix":"mainPageSuffix","notFoundPage":"notFoundPage"},"kind":"storage#bucket","projectNumber":"projectNumber","labels":{"key":"labels"},"selfLink":"selfLink","rpo":"rpo","hierarchicalNamespace":{"enabled":True},"defaultEventBasedHold":True,"name":"name","logging":{"logBucket":"logBucket","logObjectPrefix":"logObjectPrefix"},"etag":"etag","location":"location","softDeletePolicy":{"retentionDurationSeconds":"retentionDurationSeconds","effectiveTime":"2000-01-23T04:56:07.000+00:00"},"updated":"2000-01-23T04:56:07.000+00:00"}
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('uploadType', 'upload_type_example'),
                    ('userIp', 'user_ip_example'),
                    ('ifMetagenerationMatch', 'if_metageneration_match_example'),
                    ('ifMetagenerationNotMatch', 'if_metageneration_not_match_example'),
                    ('predefinedAcl', 'predefined_acl_example'),
                    ('predefinedDefaultObjectAcl', 'predefined_default_object_acl_example'),
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
        path='/storage/v1/b/{bucket}'.format(bucket='bucket_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

