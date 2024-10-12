# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.comment_reply import CommentReply
from openapi_server.models.comment_reply_list import CommentReplyList


pytestmark = pytest.mark.asyncio

async def test_drive_replies_delete(client):
    """Test case for drive_replies_delete

    
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
        path='/drive/v2/files/{file_id}/comments/{comment_id}/replies/{reply_id}'.format(file_id='file_id_example', comment_id='comment_id_example', reply_id='reply_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_drive_replies_get(client):
    """Test case for drive_replies_get

    
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
        path='/drive/v2/files/{file_id}/comments/{comment_id}/replies/{reply_id}'.format(file_id='file_id_example', comment_id='comment_id_example', reply_id='reply_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_drive_replies_insert(client):
    """Test case for drive_replies_insert

    
    """
    body = {"createdDate":"2000-01-23T04:56:07.000+00:00","deleted":True,"author":{"permissionId":"permissionId","emailAddress":"emailAddress","isAuthenticatedUser":True,"displayName":"displayName","kind":"drive#user","picture":{"url":"url"}},"kind":"drive#commentReply","modifiedDate":"2000-01-23T04:56:07.000+00:00","replyId":"replyId","verb":"verb","content":"content","htmlContent":"htmlContent"}
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
        path='/drive/v2/files/{file_id}/comments/{comment_id}/replies'.format(file_id='file_id_example', comment_id='comment_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_drive_replies_list(client):
    """Test case for drive_replies_list

    
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
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/drive/v2/files/{file_id}/comments/{comment_id}/replies'.format(file_id='file_id_example', comment_id='comment_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_drive_replies_patch(client):
    """Test case for drive_replies_patch

    
    """
    body = {"createdDate":"2000-01-23T04:56:07.000+00:00","deleted":True,"author":{"permissionId":"permissionId","emailAddress":"emailAddress","isAuthenticatedUser":True,"displayName":"displayName","kind":"drive#user","picture":{"url":"url"}},"kind":"drive#commentReply","modifiedDate":"2000-01-23T04:56:07.000+00:00","replyId":"replyId","verb":"verb","content":"content","htmlContent":"htmlContent"}
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
        path='/drive/v2/files/{file_id}/comments/{comment_id}/replies/{reply_id}'.format(file_id='file_id_example', comment_id='comment_id_example', reply_id='reply_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_drive_replies_update(client):
    """Test case for drive_replies_update

    
    """
    body = {"createdDate":"2000-01-23T04:56:07.000+00:00","deleted":True,"author":{"permissionId":"permissionId","emailAddress":"emailAddress","isAuthenticatedUser":True,"displayName":"displayName","kind":"drive#user","picture":{"url":"url"}},"kind":"drive#commentReply","modifiedDate":"2000-01-23T04:56:07.000+00:00","replyId":"replyId","verb":"verb","content":"content","htmlContent":"htmlContent"}
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
        path='/drive/v2/files/{file_id}/comments/{comment_id}/replies/{reply_id}'.format(file_id='file_id_example', comment_id='comment_id_example', reply_id='reply_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

