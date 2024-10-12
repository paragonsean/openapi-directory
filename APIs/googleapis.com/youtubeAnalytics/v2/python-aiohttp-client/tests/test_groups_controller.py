# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.empty_response import EmptyResponse
from openapi_server.models.group import Group
from openapi_server.models.list_groups_response import ListGroupsResponse


pytestmark = pytest.mark.asyncio

async def test_youtube_analytics_groups_delete(client):
    """Test case for youtube_analytics_groups_delete

    
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
                    ('id', 'id_example'),
                    ('onBehalfOfContentOwner', 'on_behalf_of_content_owner_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/groups',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_youtube_analytics_groups_insert(client):
    """Test case for youtube_analytics_groups_insert

    
    """
    body = {"snippet":{"publishedAt":"publishedAt","title":"title"},"kind":"kind","etag":"etag","id":"id","errors":{"code":"BAD_REQUEST","requestId":"requestId","error":[{"argument":["argument","argument"],"code":"code","domain":"domain","locationType":"PATH","location":"location","debugInfo":"debugInfo","externalErrorMessage":"externalErrorMessage"},{"argument":["argument","argument"],"code":"code","domain":"domain","locationType":"PATH","location":"location","debugInfo":"debugInfo","externalErrorMessage":"externalErrorMessage"}]},"contentDetails":{"itemType":"itemType","itemCount":"itemCount"}}
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
                    ('onBehalfOfContentOwner', 'on_behalf_of_content_owner_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/groups',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_youtube_analytics_groups_list(client):
    """Test case for youtube_analytics_groups_list

    
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
                    ('id', 'id_example'),
                    ('mine', True),
                    ('onBehalfOfContentOwner', 'on_behalf_of_content_owner_example'),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/groups',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_youtube_analytics_groups_update(client):
    """Test case for youtube_analytics_groups_update

    
    """
    body = {"snippet":{"publishedAt":"publishedAt","title":"title"},"kind":"kind","etag":"etag","id":"id","errors":{"code":"BAD_REQUEST","requestId":"requestId","error":[{"argument":["argument","argument"],"code":"code","domain":"domain","locationType":"PATH","location":"location","debugInfo":"debugInfo","externalErrorMessage":"externalErrorMessage"},{"argument":["argument","argument"],"code":"code","domain":"domain","locationType":"PATH","location":"location","debugInfo":"debugInfo","externalErrorMessage":"externalErrorMessage"}]},"contentDetails":{"itemType":"itemType","itemCount":"itemCount"}}
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
                    ('onBehalfOfContentOwner', 'on_behalf_of_content_owner_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v2/groups',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

