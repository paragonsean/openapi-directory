# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.post_user_info import PostUserInfo
from openapi_server.models.post_user_infos_list import PostUserInfosList


pytestmark = pytest.mark.asyncio

async def test_blogger_post_user_infos_get(client):
    """Test case for blogger_post_user_infos_get

    
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
                    ('maxComments', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/users/{user_id}/blogs/{blog_id}/posts/{post_id}'.format(user_id='user_id_example', blog_id='blog_id_example', post_id='post_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_blogger_post_user_infos_list(client):
    """Test case for blogger_post_user_infos_list

    
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
                    ('endDate', 'end_date_example'),
                    ('fetchBodies', True),
                    ('labels', 'labels_example'),
                    ('maxResults', 56),
                    ('orderBy', 'order_by_example'),
                    ('pageToken', 'page_token_example'),
                    ('startDate', 'start_date_example'),
                    ('status', ['status_example']),
                    ('view', 'view_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/users/{user_id}/blogs/{blog_id}/posts'.format(user_id='user_id_example', blog_id='blog_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

