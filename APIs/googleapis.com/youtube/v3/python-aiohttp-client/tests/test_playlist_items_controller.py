# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.playlist_item import PlaylistItem
from openapi_server.models.playlist_item_list_response import PlaylistItemListResponse


pytestmark = pytest.mark.asyncio

async def test_youtube_playlist_items_delete(client):
    """Test case for youtube_playlist_items_delete

    
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
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/youtube/v3/playlistItems',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_youtube_playlist_items_insert(client):
    """Test case for youtube_playlist_items_insert

    
    """
    body = {"snippet":{"playlistId":"playlistId","resourceId":{"playlistId":"playlistId","kind":"kind","videoId":"videoId","channelId":"channelId"},"publishedAt":"2000-01-23T04:56:07.000+00:00","description":"description","position":0,"thumbnails":{"standard":{"width":6,"url":"url","height":0},"high":{"width":6,"url":"url","height":0},"maxres":{"width":6,"url":"url","height":0},"medium":{"width":6,"url":"url","height":0}},"title":"title","channelId":"channelId","videoOwnerChannelId":"videoOwnerChannelId","channelTitle":"channelTitle","videoOwnerChannelTitle":"videoOwnerChannelTitle"},"kind":"youtube#playlistItem","etag":"etag","id":"id","contentDetails":{"note":"note","videoPublishedAt":"2000-01-23T04:56:07.000+00:00","videoId":"videoId","endAt":"endAt","startAt":"startAt"},"status":{"privacyStatus":"public"}}
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
                    ('part', ['part_example']),
                    ('onBehalfOfContentOwner', 'on_behalf_of_content_owner_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/youtube/v3/playlistItems',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_youtube_playlist_items_list(client):
    """Test case for youtube_playlist_items_list

    
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
                    ('part', ['part_example']),
                    ('id', ['id_example']),
                    ('maxResults', 56),
                    ('onBehalfOfContentOwner', 'on_behalf_of_content_owner_example'),
                    ('pageToken', 'page_token_example'),
                    ('playlistId', 'playlist_id_example'),
                    ('videoId', 'video_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/youtube/v3/playlistItems',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_youtube_playlist_items_update(client):
    """Test case for youtube_playlist_items_update

    
    """
    body = {"snippet":{"playlistId":"playlistId","resourceId":{"playlistId":"playlistId","kind":"kind","videoId":"videoId","channelId":"channelId"},"publishedAt":"2000-01-23T04:56:07.000+00:00","description":"description","position":0,"thumbnails":{"standard":{"width":6,"url":"url","height":0},"high":{"width":6,"url":"url","height":0},"maxres":{"width":6,"url":"url","height":0},"medium":{"width":6,"url":"url","height":0}},"title":"title","channelId":"channelId","videoOwnerChannelId":"videoOwnerChannelId","channelTitle":"channelTitle","videoOwnerChannelTitle":"videoOwnerChannelTitle"},"kind":"youtube#playlistItem","etag":"etag","id":"id","contentDetails":{"note":"note","videoPublishedAt":"2000-01-23T04:56:07.000+00:00","videoId":"videoId","endAt":"endAt","startAt":"startAt"},"status":{"privacyStatus":"public"}}
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
                    ('part', ['part_example']),
                    ('onBehalfOfContentOwner', 'on_behalf_of_content_owner_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/youtube/v3/playlistItems',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

