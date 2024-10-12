# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.empty_response import EmptyResponse
from openapi_server.models.group_item import GroupItem
from openapi_server.models.list_group_items_response import ListGroupItemsResponse


pytestmark = pytest.mark.asyncio

async def test_youtube_analytics_group_items_delete(client):
    """Test case for youtube_analytics_group_items_delete

    
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
        path='/v2/groupItems',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_youtube_analytics_group_items_insert(client):
    """Test case for youtube_analytics_group_items_insert

    
    """
    body = {"resource":{"kind":"kind","id":"id"},"kind":"kind","groupId":"groupId","etag":"etag","id":"id","errors":{"code":"BAD_REQUEST","requestId":"requestId","error":[{"argument":["argument","argument"],"code":"code","domain":"domain","locationType":"PATH","location":"location","debugInfo":"debugInfo","externalErrorMessage":"externalErrorMessage"},{"argument":["argument","argument"],"code":"code","domain":"domain","locationType":"PATH","location":"location","debugInfo":"debugInfo","externalErrorMessage":"externalErrorMessage"}]}}
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
        path='/v2/groupItems',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_youtube_analytics_group_items_list(client):
    """Test case for youtube_analytics_group_items_list

    
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
                    ('groupId', 'group_id_example'),
                    ('onBehalfOfContentOwner', 'on_behalf_of_content_owner_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/groupItems',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

