# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cuepoint import Cuepoint
from openapi_server.models.live_broadcast import LiveBroadcast
from openapi_server.models.live_broadcast_list_response import LiveBroadcastListResponse


pytestmark = pytest.mark.asyncio

async def test_youtube_live_broadcasts_bind(client):
    """Test case for youtube_live_broadcasts_bind

    
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
                    ('part', ['part_example']),
                    ('onBehalfOfContentOwner', 'on_behalf_of_content_owner_example'),
                    ('onBehalfOfContentOwnerChannel', 'on_behalf_of_content_owner_channel_example'),
                    ('streamId', 'stream_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/youtube/v3/liveBroadcasts/bind',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_youtube_live_broadcasts_delete(client):
    """Test case for youtube_live_broadcasts_delete

    
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
        path='/youtube/v3/liveBroadcasts',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_youtube_live_broadcasts_insert(client):
    """Test case for youtube_live_broadcasts_insert

    
    """
    body = {"snippet":{"actualStartTime":"2000-01-23T04:56:07.000+00:00","isDefaultBroadcast":True,"publishedAt":"2000-01-23T04:56:07.000+00:00","liveChatId":"liveChatId","scheduledStartTime":"2000-01-23T04:56:07.000+00:00","scheduledEndTime":"2000-01-23T04:56:07.000+00:00","actualEndTime":"2000-01-23T04:56:07.000+00:00","description":"description","thumbnails":{"standard":{"width":6,"url":"url","height":0},"high":{"width":6,"url":"url","height":0},"maxres":{"width":6,"url":"url","height":0},"medium":{"width":6,"url":"url","height":0}},"title":"title","channelId":"channelId"},"monetizationDetails":{"cuepointSchedule":{"pauseAdsUntil":"pauseAdsUntil","scheduleStrategy":"scheduleStrategyUnspecified","repeatIntervalSecs":6,"enabled":True}},"kind":"youtube#liveBroadcast","etag":"etag","id":"id","contentDetails":{"monitorStream":{"enableMonitorStream":True,"embedHtml":"embedHtml","broadcastStreamDelayMs":0},"recordFromStart":True,"boundStreamId":"boundStreamId","enableDvr":True,"enableLowLatency":True,"stereoLayout":"stereoLayoutUnspecified","boundStreamLastUpdateTimeMs":"2000-01-23T04:56:07.000+00:00","startWithSlate":True,"closedCaptionsType":"closedCaptionsTypeUnspecified","enableEmbed":True,"enableAutoStop":True,"enableContentEncryption":True,"enableAutoStart":True,"latencyPreference":"latencyPreferenceUnspecified","projection":"projectionUnspecified","enableClosedCaptions":True,"mesh":"mesh"},"statistics":{"concurrentViewers":"concurrentViewers"},"status":{"liveBroadcastPriority":"liveBroadcastPriorityUnspecified","recordingStatus":"liveBroadcastRecordingStatusUnspecified","selfDeclaredMadeForKids":True,"privacyStatus":"public","lifeCycleStatus":"lifeCycleStatusUnspecified","madeForKids":True}}
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
        path='/youtube/v3/liveBroadcasts',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_youtube_live_broadcasts_insert_cuepoint(client):
    """Test case for youtube_live_broadcasts_insert_cuepoint

    
    """
    body = {"walltimeMs":"walltimeMs","durationSecs":0,"cueType":"cueTypeUnspecified","etag":"etag","insertionOffsetTimeMs":"insertionOffsetTimeMs","id":"id"}
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
                    ('onBehalfOfContentOwnerChannel', 'on_behalf_of_content_owner_channel_example'),
                    ('part', ['part_example'])]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/youtube/v3/liveBroadcasts/cuepoint',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_youtube_live_broadcasts_list(client):
    """Test case for youtube_live_broadcasts_list

    
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
                    ('broadcastStatus', 'broadcast_status_example'),
                    ('broadcastType', 'broadcast_type_example'),
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
        path='/youtube/v3/liveBroadcasts',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_youtube_live_broadcasts_transition(client):
    """Test case for youtube_live_broadcasts_transition

    
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
                    ('broadcastStatus', 'broadcast_status_example'),
                    ('id', 'id_example'),
                    ('part', ['part_example']),
                    ('onBehalfOfContentOwner', 'on_behalf_of_content_owner_example'),
                    ('onBehalfOfContentOwnerChannel', 'on_behalf_of_content_owner_channel_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/youtube/v3/liveBroadcasts/transition',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_youtube_live_broadcasts_update(client):
    """Test case for youtube_live_broadcasts_update

    
    """
    body = {"snippet":{"actualStartTime":"2000-01-23T04:56:07.000+00:00","isDefaultBroadcast":True,"publishedAt":"2000-01-23T04:56:07.000+00:00","liveChatId":"liveChatId","scheduledStartTime":"2000-01-23T04:56:07.000+00:00","scheduledEndTime":"2000-01-23T04:56:07.000+00:00","actualEndTime":"2000-01-23T04:56:07.000+00:00","description":"description","thumbnails":{"standard":{"width":6,"url":"url","height":0},"high":{"width":6,"url":"url","height":0},"maxres":{"width":6,"url":"url","height":0},"medium":{"width":6,"url":"url","height":0}},"title":"title","channelId":"channelId"},"monetizationDetails":{"cuepointSchedule":{"pauseAdsUntil":"pauseAdsUntil","scheduleStrategy":"scheduleStrategyUnspecified","repeatIntervalSecs":6,"enabled":True}},"kind":"youtube#liveBroadcast","etag":"etag","id":"id","contentDetails":{"monitorStream":{"enableMonitorStream":True,"embedHtml":"embedHtml","broadcastStreamDelayMs":0},"recordFromStart":True,"boundStreamId":"boundStreamId","enableDvr":True,"enableLowLatency":True,"stereoLayout":"stereoLayoutUnspecified","boundStreamLastUpdateTimeMs":"2000-01-23T04:56:07.000+00:00","startWithSlate":True,"closedCaptionsType":"closedCaptionsTypeUnspecified","enableEmbed":True,"enableAutoStop":True,"enableContentEncryption":True,"enableAutoStart":True,"latencyPreference":"latencyPreferenceUnspecified","projection":"projectionUnspecified","enableClosedCaptions":True,"mesh":"mesh"},"statistics":{"concurrentViewers":"concurrentViewers"},"status":{"liveBroadcastPriority":"liveBroadcastPriorityUnspecified","recordingStatus":"liveBroadcastRecordingStatusUnspecified","selfDeclaredMadeForKids":True,"privacyStatus":"public","lifeCycleStatus":"lifeCycleStatusUnspecified","madeForKids":True}}
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
        path='/youtube/v3/liveBroadcasts',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

