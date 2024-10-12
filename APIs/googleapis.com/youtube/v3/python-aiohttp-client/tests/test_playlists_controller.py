# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.playlist import Playlist
from openapi_server.models.playlist_list_response import PlaylistListResponse


pytestmark = pytest.mark.asyncio

async def test_youtube_playlists_delete(client):
    """Test case for youtube_playlists_delete

    
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
        path='/youtube/v3/playlists',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_youtube_playlists_insert(client):
    """Test case for youtube_playlists_insert

    
    """
    body = {"snippet":{"defaultLanguage":"defaultLanguage","publishedAt":"2000-01-23T04:56:07.000+00:00","localized":{"description":"description","title":"title"},"thumbnailVideoId":"thumbnailVideoId","description":"description","thumbnails":{"standard":{"width":6,"url":"url","height":0},"high":{"width":6,"url":"url","height":0},"maxres":{"width":6,"url":"url","height":0},"medium":{"width":6,"url":"url","height":0}},"title":"title","channelId":"channelId","channelTitle":"channelTitle","tags":["tags","tags"]},"localizations":{"key":{"description":"description","title":"title"}},"kind":"youtube#playlist","etag":"etag","id":"id","contentDetails":{"itemCount":0},"player":{"embedHtml":"embedHtml"},"status":{"privacyStatus":"public"}}
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
                    ('onBehalfOfContentOwner', 'on_behalf_of_content_owner_example'),
                    ('onBehalfOfContentOwnerChannel', 'on_behalf_of_content_owner_channel_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/youtube/v3/playlists',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_youtube_playlists_list(client):
    """Test case for youtube_playlists_list

    
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
                    ('channelId', 'channel_id_example'),
                    ('hl', 'hl_example'),
                    ('id', ['id_example']),
                    ('maxResults', 56),
                    ('mine', True),
                    ('onBehalfOfContentOwner', 'on_behalf_of_content_owner_example'),
                    ('onBehalfOfContentOwnerChannel', 'on_behalf_of_content_owner_channel_example'),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/youtube/v3/playlists',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_youtube_playlists_update(client):
    """Test case for youtube_playlists_update

    
    """
    body = {"snippet":{"defaultLanguage":"defaultLanguage","publishedAt":"2000-01-23T04:56:07.000+00:00","localized":{"description":"description","title":"title"},"thumbnailVideoId":"thumbnailVideoId","description":"description","thumbnails":{"standard":{"width":6,"url":"url","height":0},"high":{"width":6,"url":"url","height":0},"maxres":{"width":6,"url":"url","height":0},"medium":{"width":6,"url":"url","height":0}},"title":"title","channelId":"channelId","channelTitle":"channelTitle","tags":["tags","tags"]},"localizations":{"key":{"description":"description","title":"title"}},"kind":"youtube#playlist","etag":"etag","id":"id","contentDetails":{"itemCount":0},"player":{"embedHtml":"embedHtml"},"status":{"privacyStatus":"public"}}
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
        path='/youtube/v3/playlists',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

