# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_live_stream_request import CreateLiveStreamRequest
from openapi_server.models.create_playback_id_request import CreatePlaybackIDRequest
from openapi_server.models.create_playback_id_response import CreatePlaybackIDResponse
from openapi_server.models.create_simulcast_target_request import CreateSimulcastTargetRequest
from openapi_server.models.disable_live_stream_response import DisableLiveStreamResponse
from openapi_server.models.enable_live_stream_response import EnableLiveStreamResponse
from openapi_server.models.get_live_stream_playback_id_response import GetLiveStreamPlaybackIDResponse
from openapi_server.models.list_live_streams_response import ListLiveStreamsResponse
from openapi_server.models.live_stream_response import LiveStreamResponse
from openapi_server.models.live_stream_status import LiveStreamStatus
from openapi_server.models.signal_live_stream_complete_response import SignalLiveStreamCompleteResponse
from openapi_server.models.simulcast_target_response import SimulcastTargetResponse
from openapi_server.models.update_live_stream_embedded_subtitles_request import UpdateLiveStreamEmbeddedSubtitlesRequest
from openapi_server.models.update_live_stream_generated_subtitles_request import UpdateLiveStreamGeneratedSubtitlesRequest
from openapi_server.models.update_live_stream_request import UpdateLiveStreamRequest


pytestmark = pytest.mark.asyncio

async def test_create_live_stream(client):
    """Test case for create_live_stream

    Create a live stream
    """
    body = {"generated_subtitles":[{"language_code":"en","name":"name","passthrough":"passthrough","transcription_vocabulary_ids":["transcription_vocabulary_ids","transcription_vocabulary_ids"]},{"language_code":"en","name":"name","passthrough":"passthrough","transcription_vocabulary_ids":["transcription_vocabulary_ids","transcription_vocabulary_ids"]}],"reconnect_slate_url":"reconnect_slate_url","audio_only":True,"embedded_subtitles":[{"language_code":"en","name":"name","passthrough":"passthrough","language_channel":"cc1"},{"language_code":"en","name":"name","passthrough":"passthrough","language_channel":"cc1"}],"test":True,"playback_policy":["public","public"],"use_slate_for_standard_latency":False,"max_continuous_duration":3514,"reconnect_window":1084.9421,"latency_mode":"low","passthrough":"passthrough","reduced_latency":True,"new_asset_settings":{"input":[{"generated_subtitles":[{"language_code":"en","name":"name","passthrough":"passthrough"},{"language_code":"en","name":"name","passthrough":"passthrough"}],"language_code":"language_code","overlay_settings":{"horizontal_margin":"horizontal_margin","vertical_align":"top","horizontal_align":"left","width":"width","opacity":"opacity","height":"height","vertical_margin":"vertical_margin"},"start_time":6.027456183070403,"text_type":"subtitles","end_time":0.8008281904610115,"name":"name","passthrough":"passthrough","closed_captions":True,"type":"video","url":"url"},{"generated_subtitles":[{"language_code":"en","name":"name","passthrough":"passthrough"},{"language_code":"en","name":"name","passthrough":"passthrough"}],"language_code":"language_code","overlay_settings":{"horizontal_margin":"horizontal_margin","vertical_align":"top","horizontal_align":"left","width":"width","opacity":"opacity","height":"height","vertical_margin":"vertical_margin"},"start_time":6.027456183070403,"text_type":"subtitles","end_time":0.8008281904610115,"name":"name","passthrough":"passthrough","closed_captions":True,"type":"video","url":"url"}],"test":True,"max_resolution_tier":"1080p","encoding_tier":"smart","normalize_audio":False,"passthrough":"passthrough","playback_policy":["public","public"],"master_access":"none","mp4_support":"none","per_title_encode":True},"simulcast_targets":[{"passthrough":"passthrough","stream_key":"stream_key","url":"url"},{"passthrough":"passthrough","stream_key":"stream_key","url":"url"}],"low_latency":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/video/v1/live-streams',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_live_stream_playback_id(client):
    """Test case for create_live_stream_playback_id

    Create a live stream playback ID
    """
    body = {"policy":"public"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/video/v1/live-streams/{live_stream_id}/playback-ids'.format(live_stream_id='live_stream_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_live_stream_simulcast_target(client):
    """Test case for create_live_stream_simulcast_target

    Create a live stream simulcast target
    """
    body = {"passthrough":"passthrough","stream_key":"stream_key","url":"url"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/video/v1/live-streams/{live_stream_id}/simulcast-targets'.format(live_stream_id='live_stream_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_live_stream(client):
    """Test case for delete_live_stream

    Delete a live stream
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/video/v1/live-streams/{live_stream_id}'.format(live_stream_id='live_stream_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_live_stream_playback_id(client):
    """Test case for delete_live_stream_playback_id

    Delete a live stream playback ID
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/video/v1/live-streams/{live_stream_id}/playback-ids/{playback_id}'.format(live_stream_id='live_stream_id_example', playback_id='playback_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_live_stream_simulcast_target(client):
    """Test case for delete_live_stream_simulcast_target

    Delete a Live Stream Simulcast Target
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/video/v1/live-streams/{live_stream_id}/simulcast-targets/{simulcast_target_id}'.format(live_stream_id='live_stream_id_example', simulcast_target_id='simulcast_target_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_disable_live_stream(client):
    """Test case for disable_live_stream

    Disable a live stream
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/video/v1/live-streams/{live_stream_id}/disable'.format(live_stream_id='live_stream_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enable_live_stream(client):
    """Test case for enable_live_stream

    Enable a live stream
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/video/v1/live-streams/{live_stream_id}/enable'.format(live_stream_id='live_stream_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_live_stream(client):
    """Test case for get_live_stream

    Retrieve a live stream
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/video/v1/live-streams/{live_stream_id}'.format(live_stream_id='live_stream_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_live_stream_playback_id(client):
    """Test case for get_live_stream_playback_id

    Retrieve a live stream playback ID
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/video/v1/live-streams/{live_stream_id}/playback-ids/{playback_id}'.format(live_stream_id='live_stream_id_example', playback_id='playback_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_live_stream_simulcast_target(client):
    """Test case for get_live_stream_simulcast_target

    Retrieve a Live Stream Simulcast Target
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/video/v1/live-streams/{live_stream_id}/simulcast-targets/{simulcast_target_id}'.format(live_stream_id='live_stream_id_example', simulcast_target_id='simulcast_target_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_live_streams(client):
    """Test case for list_live_streams

    List live streams
    """
    params = [('limit', 25),
                    ('page', 1),
                    ('stream_key', 'stream_key_example'),
                    ('status', openapi_server.LiveStreamStatus())]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/video/v1/live-streams',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reset_stream_key(client):
    """Test case for reset_stream_key

    Reset a live stream's stream key
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/video/v1/live-streams/{live_stream_id}/reset-stream-key'.format(live_stream_id='live_stream_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_signal_live_stream_complete(client):
    """Test case for signal_live_stream_complete

    Signal a live stream is finished
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/video/v1/live-streams/{live_stream_id}/complete'.format(live_stream_id='live_stream_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_live_stream(client):
    """Test case for update_live_stream

    Update a live stream
    """
    body = {"reconnect_slate_url":"reconnect_slate_url","reconnect_window":1084.9421,"latency_mode":"low","passthrough":"passthrough","use_slate_for_standard_latency":False,"max_continuous_duration":3514}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PATCH',
        path='/video/v1/live-streams/{live_stream_id}'.format(live_stream_id='live_stream_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_live_stream_embedded_subtitles(client):
    """Test case for update_live_stream_embedded_subtitles

    Update a live stream's embedded subtitles
    """
    body = {"embedded_subtitles":[{"language_code":"en","name":"name","passthrough":"passthrough","language_channel":"cc1"},{"language_code":"en","name":"name","passthrough":"passthrough","language_channel":"cc1"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/video/v1/live-streams/{live_stream_id}/embedded-subtitles'.format(live_stream_id='live_stream_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_live_stream_generated_subtitles(client):
    """Test case for update_live_stream_generated_subtitles

    Update a live stream's generated subtitles
    """
    body = {"generated_subtitles":[{"language_code":"en","name":"name","passthrough":"passthrough","transcription_vocabulary_ids":["transcription_vocabulary_ids","transcription_vocabulary_ids"]},{"language_code":"en","name":"name","passthrough":"passthrough","transcription_vocabulary_ids":["transcription_vocabulary_ids","transcription_vocabulary_ids"]}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/video/v1/live-streams/{live_stream_id}/generated-subtitles'.format(live_stream_id='live_stream_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

