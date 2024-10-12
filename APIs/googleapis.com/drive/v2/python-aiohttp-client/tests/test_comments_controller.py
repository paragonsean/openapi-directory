# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.comment import Comment
from openapi_server.models.comment_list import CommentList


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
        path='/drive/v2/files/{file_id}/comments/{comment_id}'.format(file_id='file_id_example', comment_id='comment_id_example'),
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
        path='/drive/v2/files/{file_id}/comments/{comment_id}'.format(file_id='file_id_example', comment_id='comment_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_drive_comments_insert(client):
    """Test case for drive_comments_insert

    
    """
    body = {"author":{"permissionId":"permissionId","emailAddress":"emailAddress","isAuthenticatedUser":True,"displayName":"displayName","kind":"drive#user","picture":{"url":"url"}},"kind":"drive#comment","content":"content","htmlContent":"htmlContent","selfLink":"selfLink","createdDate":"2000-01-23T04:56:07.000+00:00","deleted":True,"replies":[{"createdDate":"2000-01-23T04:56:07.000+00:00","deleted":True,"author":{"permissionId":"permissionId","emailAddress":"emailAddress","isAuthenticatedUser":True,"displayName":"displayName","kind":"drive#user","picture":{"url":"url"}},"kind":"drive#commentReply","modifiedDate":"2000-01-23T04:56:07.000+00:00","replyId":"replyId","verb":"verb","content":"content","htmlContent":"htmlContent"},{"createdDate":"2000-01-23T04:56:07.000+00:00","deleted":True,"author":{"permissionId":"permissionId","emailAddress":"emailAddress","isAuthenticatedUser":True,"displayName":"displayName","kind":"drive#user","picture":{"url":"url"}},"kind":"drive#commentReply","modifiedDate":"2000-01-23T04:56:07.000+00:00","replyId":"replyId","verb":"verb","content":"content","htmlContent":"htmlContent"}],"anchor":"anchor","fileTitle":"fileTitle","context":{"type":"type","value":"value"},"modifiedDate":"2000-01-23T04:56:07.000+00:00","commentId":"commentId","fileId":"fileId","status":"status"}
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
        path='/drive/v2/files/{file_id}/comments'.format(file_id='file_id_example'),
        headers=headers,
        json=body,
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
                    ('maxResults', 56),
                    ('pageToken', 'page_token_example'),
                    ('updatedMin', 'updated_min_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/drive/v2/files/{file_id}/comments'.format(file_id='file_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_drive_comments_patch(client):
    """Test case for drive_comments_patch

    
    """
    body = {"author":{"permissionId":"permissionId","emailAddress":"emailAddress","isAuthenticatedUser":True,"displayName":"displayName","kind":"drive#user","picture":{"url":"url"}},"kind":"drive#comment","content":"content","htmlContent":"htmlContent","selfLink":"selfLink","createdDate":"2000-01-23T04:56:07.000+00:00","deleted":True,"replies":[{"createdDate":"2000-01-23T04:56:07.000+00:00","deleted":True,"author":{"permissionId":"permissionId","emailAddress":"emailAddress","isAuthenticatedUser":True,"displayName":"displayName","kind":"drive#user","picture":{"url":"url"}},"kind":"drive#commentReply","modifiedDate":"2000-01-23T04:56:07.000+00:00","replyId":"replyId","verb":"verb","content":"content","htmlContent":"htmlContent"},{"createdDate":"2000-01-23T04:56:07.000+00:00","deleted":True,"author":{"permissionId":"permissionId","emailAddress":"emailAddress","isAuthenticatedUser":True,"displayName":"displayName","kind":"drive#user","picture":{"url":"url"}},"kind":"drive#commentReply","modifiedDate":"2000-01-23T04:56:07.000+00:00","replyId":"replyId","verb":"verb","content":"content","htmlContent":"htmlContent"}],"anchor":"anchor","fileTitle":"fileTitle","context":{"type":"type","value":"value"},"modifiedDate":"2000-01-23T04:56:07.000+00:00","commentId":"commentId","fileId":"fileId","status":"status"}
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
        path='/drive/v2/files/{file_id}/comments/{comment_id}'.format(file_id='file_id_example', comment_id='comment_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_drive_comments_update(client):
    """Test case for drive_comments_update

    
    """
    body = {"author":{"permissionId":"permissionId","emailAddress":"emailAddress","isAuthenticatedUser":True,"displayName":"displayName","kind":"drive#user","picture":{"url":"url"}},"kind":"drive#comment","content":"content","htmlContent":"htmlContent","selfLink":"selfLink","createdDate":"2000-01-23T04:56:07.000+00:00","deleted":True,"replies":[{"createdDate":"2000-01-23T04:56:07.000+00:00","deleted":True,"author":{"permissionId":"permissionId","emailAddress":"emailAddress","isAuthenticatedUser":True,"displayName":"displayName","kind":"drive#user","picture":{"url":"url"}},"kind":"drive#commentReply","modifiedDate":"2000-01-23T04:56:07.000+00:00","replyId":"replyId","verb":"verb","content":"content","htmlContent":"htmlContent"},{"createdDate":"2000-01-23T04:56:07.000+00:00","deleted":True,"author":{"permissionId":"permissionId","emailAddress":"emailAddress","isAuthenticatedUser":True,"displayName":"displayName","kind":"drive#user","picture":{"url":"url"}},"kind":"drive#commentReply","modifiedDate":"2000-01-23T04:56:07.000+00:00","replyId":"replyId","verb":"verb","content":"content","htmlContent":"htmlContent"}],"anchor":"anchor","fileTitle":"fileTitle","context":{"type":"type","value":"value"},"modifiedDate":"2000-01-23T04:56:07.000+00:00","commentId":"commentId","fileId":"fileId","status":"status"}
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
        method='PUT',
        path='/drive/v2/files/{file_id}/comments/{comment_id}'.format(file_id='file_id_example', comment_id='comment_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

