# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.live_stream import LiveStream
from openapi_server.models.live_stream_list_response import LiveStreamListResponse


pytestmark = pytest.mark.asyncio

async def test_youtube_live_streams_delete(client):
    """Test case for youtube_live_streams_delete

    
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
                    ('onBehalfOfContentOwner', 'on_behalf_of_content_owner_example'),
                    ('onBehalfOfContentOwnerChannel', 'on_behalf_of_content_owner_channel_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/youtube/v3/liveStreams',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_youtube_live_streams_insert(client):
    """Test case for youtube_live_streams_insert

    
    """
    body = {"snippet":{"publishedAt":"2000-01-23T04:56:07.000+00:00","description":"description","title":"title","channelId":"channelId","isDefaultStream":True},"kind":"youtube#liveStream","etag":"etag","id":"id","cdn":{"frameRate":"30fps","format":"format","ingestionType":"rtmp","ingestionInfo":{"ingestionAddress":"ingestionAddress","rtmpsIngestionAddress":"rtmpsIngestionAddress","backupIngestionAddress":"backupIngestionAddress","rtmpsBackupIngestionAddress":"rtmpsBackupIngestionAddress","streamName":"streamName"},"resolution":"240p"},"contentDetails":{"closedCaptionsIngestionUrl":"closedCaptionsIngestionUrl","isReusable":True},"status":{"healthStatus":{"lastUpdateTimeSeconds":"lastUpdateTimeSeconds","configurationIssues":[{"severity":"info","reason":"reason","description":"description","type":"gopSizeOver"},{"severity":"info","reason":"reason","description":"description","type":"gopSizeOver"}],"status":"good"},"streamStatus":"created"}}
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
        path='/youtube/v3/liveStreams',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_youtube_live_streams_list(client):
    """Test case for youtube_live_streams_list

    
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
        path='/youtube/v3/liveStreams',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_youtube_live_streams_update(client):
    """Test case for youtube_live_streams_update

    
    """
    body = {"snippet":{"publishedAt":"2000-01-23T04:56:07.000+00:00","description":"description","title":"title","channelId":"channelId","isDefaultStream":True},"kind":"youtube#liveStream","etag":"etag","id":"id","cdn":{"frameRate":"30fps","format":"format","ingestionType":"rtmp","ingestionInfo":{"ingestionAddress":"ingestionAddress","rtmpsIngestionAddress":"rtmpsIngestionAddress","backupIngestionAddress":"backupIngestionAddress","rtmpsBackupIngestionAddress":"rtmpsBackupIngestionAddress","streamName":"streamName"},"resolution":"240p"},"contentDetails":{"closedCaptionsIngestionUrl":"closedCaptionsIngestionUrl","isReusable":True},"status":{"healthStatus":{"lastUpdateTimeSeconds":"lastUpdateTimeSeconds","configurationIssues":[{"severity":"info","reason":"reason","description":"description","type":"gopSizeOver"},{"severity":"info","reason":"reason","description":"description","type":"gopSizeOver"}],"status":"good"},"streamStatus":"created"}}
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
        method='PUT',
        path='/youtube/v3/liveStreams',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

