# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.comment import Comment
from openapi_server.models.comment_list import CommentList


pytestmark = pytest.mark.asyncio

async def test_drive_comments_create(client):
    """Test case for drive_comments_create

    
    """
    body = {"modifiedTime":"2000-01-23T04:56:07.000+00:00","deleted":True,"replies":[{"modifiedTime":"2000-01-23T04:56:07.000+00:00","deleted":True,"author":{"permissionId":"permissionId","emailAddress":"emailAddress","displayName":"displayName","kind":"drive#user","me":True,"photoLink":"photoLink"},"kind":"drive#reply","action":"action","createdTime":"2000-01-23T04:56:07.000+00:00","id":"id","content":"content","htmlContent":"htmlContent"},{"modifiedTime":"2000-01-23T04:56:07.000+00:00","deleted":True,"author":{"permissionId":"permissionId","emailAddress":"emailAddress","displayName":"displayName","kind":"drive#user","me":True,"photoLink":"photoLink"},"kind":"drive#reply","action":"action","createdTime":"2000-01-23T04:56:07.000+00:00","id":"id","content":"content","htmlContent":"htmlContent"}],"author":{"permissionId":"permissionId","emailAddress":"emailAddress","displayName":"displayName","kind":"drive#user","me":True,"photoLink":"photoLink"},"kind":"drive#comment","anchor":"anchor","createdTime":"2000-01-23T04:56:07.000+00:00","id":"id","content":"content","quotedFileContent":{"mimeType":"mimeType","value":"value"},"htmlContent":"htmlContent","resolved":True}
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
        path='/drive/v3/files/{file_id}/comments'.format(file_id='file_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_drive_comments_delete(client):
    """Test case for drive_comments_delete

    
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
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/drive/v3/files/{file_id}/comments/{comment_id}'.format(file_id='file_id_example', comment_id='comment_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_drive_comments_get(client):
    """Test case for drive_comments_get

    
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
                    ('includeDeleted', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/drive/v3/files/{file_id}/comments/{comment_id}'.format(file_id='file_id_example', comment_id='comment_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_drive_comments_list(client):
    """Test case for drive_comments_list

    
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
                    ('includeDeleted', True),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example'),
                    ('startModifiedTime', 'start_modified_time_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/drive/v3/files/{file_id}/comments'.format(file_id='file_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_drive_comments_update(client):
    """Test case for drive_comments_update

    
    """
    body = {"modifiedTime":"2000-01-23T04:56:07.000+00:00","deleted":True,"replies":[{"modifiedTime":"2000-01-23T04:56:07.000+00:00","deleted":True,"author":{"permissionId":"permissionId","emailAddress":"emailAddress","displayName":"displayName","kind":"drive#user","me":True,"photoLink":"photoLink"},"kind":"drive#reply","action":"action","createdTime":"2000-01-23T04:56:07.000+00:00","id":"id","content":"content","htmlContent":"htmlContent"},{"modifiedTime":"2000-01-23T04:56:07.000+00:00","deleted":True,"author":{"permissionId":"permissionId","emailAddress":"emailAddress","displayName":"displayName","kind":"drive#user","me":True,"photoLink":"photoLink"},"kind":"drive#reply","action":"action","createdTime":"2000-01-23T04:56:07.000+00:00","id":"id","content":"content","htmlContent":"htmlContent"}],"author":{"permissionId":"permissionId","emailAddress":"emailAddress","displayName":"displayName","kind":"drive#user","me":True,"photoLink":"photoLink"},"kind":"drive#comment","anchor":"anchor","createdTime":"2000-01-23T04:56:07.000+00:00","id":"id","content":"content","quotedFileContent":{"mimeType":"mimeType","value":"value"},"htmlContent":"htmlContent","resolved":True}
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
        method='PATCH',
        path='/drive/v3/files/{file_id}/comments/{comment_id}'.format(file_id='file_id_example', comment_id='comment_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

