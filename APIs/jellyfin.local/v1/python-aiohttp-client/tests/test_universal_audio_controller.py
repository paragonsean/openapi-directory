# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_universal_audio_stream(client):
    """Test case for get_universal_audio_stream

    Gets an audio stream.
    """
    params = [('container', ['container_example']),
                    ('mediaSourceId', 'media_source_id_example'),
                    ('deviceId', 'device_id_example'),
                    ('userId', 'user_id_example'),
                    ('audioCodec', 'audio_codec_example'),
                    ('maxAudioChannels', 56),
                    ('transcodingAudioChannels', 56),
                    ('maxStreamingBitrate', 56),
                    ('audioBitRate', 56),
                    ('startTimeTicks', 56),
                    ('transcodingContainer', 'transcoding_container_example'),
                    ('transcodingProtocol', 'transcoding_protocol_example'),
                    ('maxAudioSampleRate', 56),
                    ('maxAudioBitDepth', 56),
                    ('enableRemoteMedia', True),
                    ('breakOnNonKeyFrames', True),
                    ('enableRedirection', True)]
    headers = { 
        'Accept': 'audio/*',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Audio/{item_id}/universal'.format(item_id='item_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_head_universal_audio_stream(client):
    """Test case for head_universal_audio_stream

    Gets an audio stream.
    """
    params = [('container', ['container_example']),
                    ('mediaSourceId', 'media_source_id_example'),
                    ('deviceId', 'device_id_example'),
                    ('userId', 'user_id_example'),
                    ('audioCodec', 'audio_codec_example'),
                    ('maxAudioChannels', 56),
                    ('transcodingAudioChannels', 56),
                    ('maxStreamingBitrate', 56),
                    ('audioBitRate', 56),
                    ('startTimeTicks', 56),
                    ('transcodingContainer', 'transcoding_container_example'),
                    ('transcodingProtocol', 'transcoding_protocol_example'),
                    ('maxAudioSampleRate', 56),
                    ('maxAudioBitDepth', 56),
                    ('enableRemoteMedia', True),
                    ('breakOnNonKeyFrames', True),
                    ('enableRedirection', True)]
    headers = { 
        'Accept': 'audio/*',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='HEAD',
        path='/Audio/{item_id}/universal'.format(item_id='item_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

