# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.folder import Folder
from openapi_server.models.folders import Folders
from openapi_server.models.google_longrunning_operation import GoogleLongrunningOperation


pytestmark = pytest.mark.asyncio

async def test_storage_folders_delete(client):
    """Test case for storage_folders_delete

    
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
                    ('ifMetagenerationNotMatch', 'if_metageneration_not_match_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/storage/v1/b/{bucket}/folders/{folder}'.format(bucket='bucket_example', folder='folder_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_storage_folders_get(client):
    """Test case for storage_folders_get

    
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
                    ('ifMetagenerationNotMatch', 'if_metageneration_not_match_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/storage/v1/b/{bucket}/folders/{folder}'.format(bucket='bucket_example', folder='folder_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_storage_folders_insert(client):
    """Test case for storage_folders_insert

    
    """
    body = {"bucket":"bucket","metageneration":"metageneration","createTime":"2000-01-23T04:56:07.000+00:00","kind":"storage#folder","pendingRenameInfo":{"operationId":"operationId"},"name":"name","updateTime":"2000-01-23T04:56:07.000+00:00","id":"id","selfLink":"selfLink"}
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('uploadType', 'upload_type_example'),
                    ('userIp', 'user_ip_example'),
                    ('recursive', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/storage/v1/b/{bucket}/folders'.format(bucket='bucket_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_storage_folders_list(client):
    """Test case for storage_folders_list

    
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
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example'),
                    ('prefix', 'prefix_example'),
                    ('startOffset', 'start_offset_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/storage/v1/b/{bucket}/folders'.format(bucket='bucket_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_storage_folders_rename(client):
    """Test case for storage_folders_rename

    
    """
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('uploadType', 'upload_type_example'),
                    ('userIp', 'user_ip_example'),
                    ('ifSourceMetagenerationMatch', 'if_source_metageneration_match_example'),
                    ('ifSourceMetagenerationNotMatch', 'if_source_metageneration_not_match_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/storage/v1/b/{bucket}/folders/{source_folder}/renameTo/folders/{destination_folder}'.format(bucket='bucket_example', source_folder='source_folder_example', destination_folder='destination_folder_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

