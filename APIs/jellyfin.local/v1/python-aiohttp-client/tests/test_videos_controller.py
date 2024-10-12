# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.base_item_dto_query_result import BaseItemDtoQueryResult
from openapi_server.models.encoding_context import EncodingContext
from openapi_server.models.problem_details import ProblemDetails
from openapi_server.models.subtitle_delivery_method import SubtitleDeliveryMethod


pytestmark = pytest.mark.asyncio

async def test_delete_alternate_sources(client):
    """Test case for delete_alternate_sources

    Removes alternate video sources.
    """
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/Videos/{item_id}/AlternateSources'.format(item_id='item_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_additional_part(client):
    """Test case for get_additional_part

    Gets additional parts for a video.
    """
    params = [('userId', 'user_id_example')]
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Videos/{item_id}/AdditionalParts'.format(item_id='item_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_video_stream(client):
    """Test case for get_video_stream

    Gets a video stream.
    """
    params = [('container', 'container_example'),
                    ('static', True),
                    ('params', 'params_example'),
                    ('tag', 'tag_example'),
                    ('deviceProfileId', 'device_profile_id_example'),
                    ('playSessionId', 'play_session_id_example'),
                    ('segmentContainer', 'segment_container_example'),
                    ('segmentLength', 56),
                    ('minSegments', 56),
                    ('mediaSourceId', 'media_source_id_example'),
                    ('deviceId', 'device_id_example'),
                    ('audioCodec', 'audio_codec_example'),
                    ('enableAutoStreamCopy', True),
                    ('allowVideoStreamCopy', True),
                    ('allowAudioStreamCopy', True),
                    ('breakOnNonKeyFrames', True),
                    ('audioSampleRate', 56),
                    ('maxAudioBitDepth', 56),
                    ('audioBitRate', 56),
                    ('audioChannels', 56),
                    ('maxAudioChannels', 56),
                    ('profile', 'profile_example'),
                    ('level', 'level_example'),
                    ('framerate', 3.4),
                    ('maxFramerate', 3.4),
                    ('copyTimestamps', True),
                    ('startTimeTicks', 56),
                    ('width', 56),
                    ('height', 56),
                    ('videoBitRate', 56),
                    ('subtitleStreamIndex', 56),
                    ('subtitleMethod', openapi_server.SubtitleDeliveryMethod()),
                    ('maxRefFrames', 56),
                    ('maxVideoBitDepth', 56),
                    ('requireAvc', True),
                    ('deInterlace', True),
                    ('requireNonAnamorphic', True),
                    ('transcodingMaxAudioChannels', 56),
                    ('cpuCoreLimit', 56),
                    ('liveStreamId', 'live_stream_id_example'),
                    ('enableMpegtsM2TsMode', True),
                    ('videoCodec', 'video_codec_example'),
                    ('subtitleCodec', 'subtitle_codec_example'),
                    ('transcodeReasons', 'transcode_reasons_example'),
                    ('audioStreamIndex', 56),
                    ('videoStreamIndex', 56),
                    ('context', openapi_server.EncodingContext()),
                    ('streamOptions', {'key': 'stream_options_example'})]
    headers = { 
        'Accept': 'video/*',
    }
    response = await client.request(
        method='GET',
        path='/Videos/{item_id}/stream'.format(item_id='item_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_video_stream_by_container(client):
    """Test case for get_video_stream_by_container

    Gets a video stream.
    """
    params = [('static', True),
                    ('params', 'params_example'),
                    ('tag', 'tag_example'),
                    ('deviceProfileId', 'device_profile_id_example'),
                    ('playSessionId', 'play_session_id_example'),
                    ('segmentContainer', 'segment_container_example'),
                    ('segmentLength', 56),
                    ('minSegments', 56),
                    ('mediaSourceId', 'media_source_id_example'),
                    ('deviceId', 'device_id_example'),
                    ('audioCodec', 'audio_codec_example'),
                    ('enableAutoStreamCopy', True),
                    ('allowVideoStreamCopy', True),
                    ('allowAudioStreamCopy', True),
                    ('breakOnNonKeyFrames', True),
                    ('audioSampleRate', 56),
                    ('maxAudioBitDepth', 56),
                    ('audioBitRate', 56),
                    ('audioChannels', 56),
                    ('maxAudioChannels', 56),
                    ('profile', 'profile_example'),
                    ('level', 'level_example'),
                    ('framerate', 3.4),
                    ('maxFramerate', 3.4),
                    ('copyTimestamps', True),
                    ('startTimeTicks', 56),
                    ('width', 56),
                    ('height', 56),
                    ('videoBitRate', 56),
                    ('subtitleStreamIndex', 56),
                    ('subtitleMethod', openapi_server.SubtitleDeliveryMethod()),
                    ('maxRefFrames', 56),
                    ('maxVideoBitDepth', 56),
                    ('requireAvc', True),
                    ('deInterlace', True),
                    ('requireNonAnamorphic', True),
                    ('transcodingMaxAudioChannels', 56),
                    ('cpuCoreLimit', 56),
                    ('liveStreamId', 'live_stream_id_example'),
                    ('enableMpegtsM2TsMode', True),
                    ('videoCodec', 'video_codec_example'),
                    ('subtitleCodec', 'subtitle_codec_example'),
                    ('transcodeReasons', 'transcode_reasons_example'),
                    ('audioStreamIndex', 56),
                    ('videoStreamIndex', 56),
                    ('context', openapi_server.EncodingContext()),
                    ('streamOptions', {'key': 'stream_options_example'})]
    headers = { 
        'Accept': 'video/*',
    }
    response = await client.request(
        method='GET',
        path='/Videos/{item_id}/{stream_container}'.format(item_id='item_id_example', container='container_example', stream='stream_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_head_video_stream(client):
    """Test case for head_video_stream

    Gets a video stream.
    """
    params = [('container', 'container_example'),
                    ('static', True),
                    ('params', 'params_example'),
                    ('tag', 'tag_example'),
                    ('deviceProfileId', 'device_profile_id_example'),
                    ('playSessionId', 'play_session_id_example'),
                    ('segmentContainer', 'segment_container_example'),
                    ('segmentLength', 56),
                    ('minSegments', 56),
                    ('mediaSourceId', 'media_source_id_example'),
                    ('deviceId', 'device_id_example'),
                    ('audioCodec', 'audio_codec_example'),
                    ('enableAutoStreamCopy', True),
                    ('allowVideoStreamCopy', True),
                    ('allowAudioStreamCopy', True),
                    ('breakOnNonKeyFrames', True),
                    ('audioSampleRate', 56),
                    ('maxAudioBitDepth', 56),
                    ('audioBitRate', 56),
                    ('audioChannels', 56),
                    ('maxAudioChannels', 56),
                    ('profile', 'profile_example'),
                    ('level', 'level_example'),
                    ('framerate', 3.4),
                    ('maxFramerate', 3.4),
                    ('copyTimestamps', True),
                    ('startTimeTicks', 56),
                    ('width', 56),
                    ('height', 56),
                    ('videoBitRate', 56),
                    ('subtitleStreamIndex', 56),
                    ('subtitleMethod', openapi_server.SubtitleDeliveryMethod()),
                    ('maxRefFrames', 56),
                    ('maxVideoBitDepth', 56),
                    ('requireAvc', True),
                    ('deInterlace', True),
                    ('requireNonAnamorphic', True),
                    ('transcodingMaxAudioChannels', 56),
                    ('cpuCoreLimit', 56),
                    ('liveStreamId', 'live_stream_id_example'),
                    ('enableMpegtsM2TsMode', True),
                    ('videoCodec', 'video_codec_example'),
                    ('subtitleCodec', 'subtitle_codec_example'),
                    ('transcodeReasons', 'transcode_reasons_example'),
                    ('audioStreamIndex', 56),
                    ('videoStreamIndex', 56),
                    ('context', openapi_server.EncodingContext()),
                    ('streamOptions', {'key': 'stream_options_example'})]
    headers = { 
        'Accept': 'video/*',
    }
    response = await client.request(
        method='HEAD',
        path='/Videos/{item_id}/stream'.format(item_id='item_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_head_video_stream_by_container(client):
    """Test case for head_video_stream_by_container

    Gets a video stream.
    """
    params = [('static', True),
                    ('params', 'params_example'),
                    ('tag', 'tag_example'),
                    ('deviceProfileId', 'device_profile_id_example'),
                    ('playSessionId', 'play_session_id_example'),
                    ('segmentContainer', 'segment_container_example'),
                    ('segmentLength', 56),
                    ('minSegments', 56),
                    ('mediaSourceId', 'media_source_id_example'),
                    ('deviceId', 'device_id_example'),
                    ('audioCodec', 'audio_codec_example'),
                    ('enableAutoStreamCopy', True),
                    ('allowVideoStreamCopy', True),
                    ('allowAudioStreamCopy', True),
                    ('breakOnNonKeyFrames', True),
                    ('audioSampleRate', 56),
                    ('maxAudioBitDepth', 56),
                    ('audioBitRate', 56),
                    ('audioChannels', 56),
                    ('maxAudioChannels', 56),
                    ('profile', 'profile_example'),
                    ('level', 'level_example'),
                    ('framerate', 3.4),
                    ('maxFramerate', 3.4),
                    ('copyTimestamps', True),
                    ('startTimeTicks', 56),
                    ('width', 56),
                    ('height', 56),
                    ('videoBitRate', 56),
                    ('subtitleStreamIndex', 56),
                    ('subtitleMethod', openapi_server.SubtitleDeliveryMethod()),
                    ('maxRefFrames', 56),
                    ('maxVideoBitDepth', 56),
                    ('requireAvc', True),
                    ('deInterlace', True),
                    ('requireNonAnamorphic', True),
                    ('transcodingMaxAudioChannels', 56),
                    ('cpuCoreLimit', 56),
                    ('liveStreamId', 'live_stream_id_example'),
                    ('enableMpegtsM2TsMode', True),
                    ('videoCodec', 'video_codec_example'),
                    ('subtitleCodec', 'subtitle_codec_example'),
                    ('transcodeReasons', 'transcode_reasons_example'),
                    ('audioStreamIndex', 56),
                    ('videoStreamIndex', 56),
                    ('context', openapi_server.EncodingContext()),
                    ('streamOptions', {'key': 'stream_options_example'})]
    headers = { 
        'Accept': 'video/*',
    }
    response = await client.request(
        method='HEAD',
        path='/Videos/{item_id}/{stream_container}'.format(item_id='item_id_example', container='container_example', stream='stream_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_merge_versions(client):
    """Test case for merge_versions

    Merges videos into a single record.
    """
    params = [('ids', ['ids_example'])]
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/Videos/MergeVersions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

