# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.live_stream_response import LiveStreamResponse
from openapi_server.models.open_live_stream_dto import OpenLiveStreamDto
from openapi_server.models.playback_info_dto import PlaybackInfoDto
from openapi_server.models.playback_info_response import PlaybackInfoResponse
from openapi_server.models.problem_details import ProblemDetails


pytestmark = pytest.mark.asyncio

async def test_close_live_stream(client):
    """Test case for close_live_stream

    Closes a media source.
    """
    params = [('liveStreamId', 'live_stream_id_example')]
    headers = { 
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/LiveStreams/Close',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_bitrate_test_bytes(client):
    """Test case for get_bitrate_test_bytes

    Tests the network with a request with the size of the bitrate.
    """
    params = [('size', 102400)]
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Playback/BitrateTest',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_playback_info(client):
    """Test case for get_playback_info

    Gets live playback media info for an item.
    """
    params = [('userId', 'user_id_example')]
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Items/{item_id}/PlaybackInfo'.format(item_id='item_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_get_posted_playback_info(client):
    """Test case for get_posted_playback_info

    Gets live playback media info for an item.
    """
    body = {"AutoOpenLiveStream":True,"EnableDirectStream":True,"MediaSourceId":"MediaSourceId","MaxAudioChannels":6,"SubtitleStreamIndex":5,"MaxStreamingBitrate":1,"AllowVideoStreamCopy":True,"StartTimeTicks":5,"DeviceProfile":{"EnableSingleAlbumArtLimit":True,"ManufacturerUrl":"ManufacturerUrl","MusicStreamingTranscodingBitrate":9,"AlbumArtPn":"AlbumArtPn","TranscodingProfiles":[{"BreakOnNonKeyFrames":True,"Context":"Streaming","EnableSubtitlesInManifest":True,"CopyTimestamps":True,"MinSegments":2,"EnableMpegtsM2TsMode":True,"MaxAudioChannels":"MaxAudioChannels","VideoCodec":"VideoCodec","Container":"Container","EstimateContentLength":True,"SegmentLength":4,"TranscodeSeekInfo":"Auto","Protocol":"Protocol","AudioCodec":"AudioCodec"},{"BreakOnNonKeyFrames":True,"Context":"Streaming","EnableSubtitlesInManifest":True,"CopyTimestamps":True,"MinSegments":2,"EnableMpegtsM2TsMode":True,"MaxAudioChannels":"MaxAudioChannels","VideoCodec":"VideoCodec","Container":"Container","EstimateContentLength":True,"SegmentLength":4,"TranscodeSeekInfo":"Auto","Protocol":"Protocol","AudioCodec":"AudioCodec"}],"Identification":{"ManufacturerUrl":"ManufacturerUrl","ModelNumber":"ModelNumber","ModelUrl":"ModelUrl","ModelName":"ModelName","SerialNumber":"SerialNumber","FriendlyName":"FriendlyName","Headers":[{"Value":"Value","Match":"Equals","Name":"Name"},{"Value":"Value","Match":"Equals","Name":"Name"}],"Manufacturer":"Manufacturer","ModelDescription":"ModelDescription"},"MaxStreamingBitrate":7,"IgnoreTranscodeByteRangeRequests":True,"Name":"Name","ResponseProfiles":[{"Container":"Container","OrgPn":"OrgPn","VideoCodec":"VideoCodec","AudioCodec":"AudioCodec","Conditions":[{"Condition":"Equals","IsRequired":True,"Value":"Value","Property":"AudioChannels"},{"Condition":"Equals","IsRequired":True,"Value":"Value","Property":"AudioChannels"}],"MimeType":"MimeType"},{"Container":"Container","OrgPn":"OrgPn","VideoCodec":"VideoCodec","AudioCodec":"AudioCodec","Conditions":[{"Condition":"Equals","IsRequired":True,"Value":"Value","Property":"AudioChannels"},{"Condition":"Equals","IsRequired":True,"Value":"Value","Property":"AudioChannels"}],"MimeType":"MimeType"}],"ModelUrl":"ModelUrl","MaxStaticBitrate":5,"Manufacturer":"Manufacturer","ProtocolInfo":"ProtocolInfo","RequiresPlainVideoItems":True,"ModelDescription":"ModelDescription","MaxAlbumArtWidth":6,"ModelNumber":"ModelNumber","XmlRootAttributes":[{"Value":"Value","Name":"Name"},{"Value":"Value","Name":"Name"}],"ModelName":"ModelName","FriendlyName":"FriendlyName","MaxIconHeight":1,"RequiresPlainFolders":True,"EnableSingleSubtitleLimit":True,"SubtitleProfiles":[{"Container":"Container","Format":"Format","Language":"Language","DidlMode":"DidlMode","Method":"Encode"},{"Container":"Container","Format":"Format","Language":"Language","DidlMode":"DidlMode","Method":"Encode"}],"MaxAlbumArtHeight":0,"EnableAlbumArtInDidl":True,"EnableMSMediaReceiverRegistrar":True,"CodecProfiles":[{"Codec":"Codec","Container":"Container","Type":"Video","ApplyConditions":[{"Condition":"Equals","IsRequired":True,"Value":"Value","Property":"AudioChannels"},{"Condition":"Equals","IsRequired":True,"Value":"Value","Property":"AudioChannels"}],"Conditions":[{"Condition":"Equals","IsRequired":True,"Value":"Value","Property":"AudioChannels"},{"Condition":"Equals","IsRequired":True,"Value":"Value","Property":"AudioChannels"}]},{"Codec":"Codec","Container":"Container","Type":"Video","ApplyConditions":[{"Condition":"Equals","IsRequired":True,"Value":"Value","Property":"AudioChannels"},{"Condition":"Equals","IsRequired":True,"Value":"Value","Property":"AudioChannels"}],"Conditions":[{"Condition":"Equals","IsRequired":True,"Value":"Value","Property":"AudioChannels"},{"Condition":"Equals","IsRequired":True,"Value":"Value","Property":"AudioChannels"}]}],"SerialNumber":"SerialNumber","SupportedMediaTypes":"SupportedMediaTypes","SonyAggregationFlags":"SonyAggregationFlags","MaxIconWidth":5,"UserId":"UserId","TimelineOffsetSeconds":3,"ContainerProfiles":[{"Container":"Container","Type":"Audio","Conditions":[{"Condition":"Equals","IsRequired":True,"Value":"Value","Property":"AudioChannels"},{"Condition":"Equals","IsRequired":True,"Value":"Value","Property":"AudioChannels"}]},{"Container":"Container","Type":"Audio","Conditions":[{"Condition":"Equals","IsRequired":True,"Value":"Value","Property":"AudioChannels"},{"Condition":"Equals","IsRequired":True,"Value":"Value","Property":"AudioChannels"}]}],"DirectPlayProfiles":[{"Container":"Container","VideoCodec":"VideoCodec","AudioCodec":"AudioCodec"},{"Container":"Container","VideoCodec":"VideoCodec","AudioCodec":"AudioCodec"}],"MaxStaticMusicBitrate":2,"Id":"Id"},"AudioStreamIndex":0,"UserId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","AllowAudioStreamCopy":True,"LiveStreamId":"LiveStreamId","EnableTranscoding":True,"EnableDirectPlay":True}
    params = [('userId', 'user_id_example'),
                    ('maxStreamingBitrate', 56),
                    ('startTimeTicks', 56),
                    ('audioStreamIndex', 56),
                    ('subtitleStreamIndex', 56),
                    ('maxAudioChannels', 56),
                    ('mediaSourceId', 'media_source_id_example'),
                    ('liveStreamId', 'live_stream_id_example'),
                    ('autoOpenLiveStream', True),
                    ('enableDirectPlay', True),
                    ('enableDirectStream', True),
                    ('enableTranscoding', True),
                    ('allowVideoStreamCopy', True),
                    ('allowAudioStreamCopy', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/Items/{item_id}/PlaybackInfo'.format(item_id='item_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_open_live_stream(client):
    """Test case for open_live_stream

    Opens a media source.
    """
    body = {"DirectPlayProtocols":["File","File"],"EnableDirectStream":True,"MaxAudioChannels":6,"SubtitleStreamIndex":5,"ItemId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","MaxStreamingBitrate":1,"OpenToken":"OpenToken","StartTimeTicks":5,"DeviceProfile":{"EnableSingleAlbumArtLimit":True,"ManufacturerUrl":"ManufacturerUrl","MusicStreamingTranscodingBitrate":9,"AlbumArtPn":"AlbumArtPn","TranscodingProfiles":[{"BreakOnNonKeyFrames":True,"Context":"Streaming","EnableSubtitlesInManifest":True,"CopyTimestamps":True,"MinSegments":2,"EnableMpegtsM2TsMode":True,"MaxAudioChannels":"MaxAudioChannels","VideoCodec":"VideoCodec","Container":"Container","EstimateContentLength":True,"SegmentLength":4,"TranscodeSeekInfo":"Auto","Protocol":"Protocol","AudioCodec":"AudioCodec"},{"BreakOnNonKeyFrames":True,"Context":"Streaming","EnableSubtitlesInManifest":True,"CopyTimestamps":True,"MinSegments":2,"EnableMpegtsM2TsMode":True,"MaxAudioChannels":"MaxAudioChannels","VideoCodec":"VideoCodec","Container":"Container","EstimateContentLength":True,"SegmentLength":4,"TranscodeSeekInfo":"Auto","Protocol":"Protocol","AudioCodec":"AudioCodec"}],"Identification":{"ManufacturerUrl":"ManufacturerUrl","ModelNumber":"ModelNumber","ModelUrl":"ModelUrl","ModelName":"ModelName","SerialNumber":"SerialNumber","FriendlyName":"FriendlyName","Headers":[{"Value":"Value","Match":"Equals","Name":"Name"},{"Value":"Value","Match":"Equals","Name":"Name"}],"Manufacturer":"Manufacturer","ModelDescription":"ModelDescription"},"MaxStreamingBitrate":7,"IgnoreTranscodeByteRangeRequests":True,"Name":"Name","ResponseProfiles":[{"Container":"Container","OrgPn":"OrgPn","VideoCodec":"VideoCodec","AudioCodec":"AudioCodec","Conditions":[{"Condition":"Equals","IsRequired":True,"Value":"Value","Property":"AudioChannels"},{"Condition":"Equals","IsRequired":True,"Value":"Value","Property":"AudioChannels"}],"MimeType":"MimeType"},{"Container":"Container","OrgPn":"OrgPn","VideoCodec":"VideoCodec","AudioCodec":"AudioCodec","Conditions":[{"Condition":"Equals","IsRequired":True,"Value":"Value","Property":"AudioChannels"},{"Condition":"Equals","IsRequired":True,"Value":"Value","Property":"AudioChannels"}],"MimeType":"MimeType"}],"ModelUrl":"ModelUrl","MaxStaticBitrate":5,"Manufacturer":"Manufacturer","ProtocolInfo":"ProtocolInfo","RequiresPlainVideoItems":True,"ModelDescription":"ModelDescription","MaxAlbumArtWidth":6,"ModelNumber":"ModelNumber","XmlRootAttributes":[{"Value":"Value","Name":"Name"},{"Value":"Value","Name":"Name"}],"ModelName":"ModelName","FriendlyName":"FriendlyName","MaxIconHeight":1,"RequiresPlainFolders":True,"EnableSingleSubtitleLimit":True,"SubtitleProfiles":[{"Container":"Container","Format":"Format","Language":"Language","DidlMode":"DidlMode","Method":"Encode"},{"Container":"Container","Format":"Format","Language":"Language","DidlMode":"DidlMode","Method":"Encode"}],"MaxAlbumArtHeight":0,"EnableAlbumArtInDidl":True,"EnableMSMediaReceiverRegistrar":True,"CodecProfiles":[{"Codec":"Codec","Container":"Container","Type":"Video","ApplyConditions":[{"Condition":"Equals","IsRequired":True,"Value":"Value","Property":"AudioChannels"},{"Condition":"Equals","IsRequired":True,"Value":"Value","Property":"AudioChannels"}],"Conditions":[{"Condition":"Equals","IsRequired":True,"Value":"Value","Property":"AudioChannels"},{"Condition":"Equals","IsRequired":True,"Value":"Value","Property":"AudioChannels"}]},{"Codec":"Codec","Container":"Container","Type":"Video","ApplyConditions":[{"Condition":"Equals","IsRequired":True,"Value":"Value","Property":"AudioChannels"},{"Condition":"Equals","IsRequired":True,"Value":"Value","Property":"AudioChannels"}],"Conditions":[{"Condition":"Equals","IsRequired":True,"Value":"Value","Property":"AudioChannels"},{"Condition":"Equals","IsRequired":True,"Value":"Value","Property":"AudioChannels"}]}],"SerialNumber":"SerialNumber","SupportedMediaTypes":"SupportedMediaTypes","SonyAggregationFlags":"SonyAggregationFlags","MaxIconWidth":5,"UserId":"UserId","TimelineOffsetSeconds":3,"ContainerProfiles":[{"Container":"Container","Type":"Audio","Conditions":[{"Condition":"Equals","IsRequired":True,"Value":"Value","Property":"AudioChannels"},{"Condition":"Equals","IsRequired":True,"Value":"Value","Property":"AudioChannels"}]},{"Container":"Container","Type":"Audio","Conditions":[{"Condition":"Equals","IsRequired":True,"Value":"Value","Property":"AudioChannels"},{"Condition":"Equals","IsRequired":True,"Value":"Value","Property":"AudioChannels"}]}],"DirectPlayProfiles":[{"Container":"Container","VideoCodec":"VideoCodec","AudioCodec":"AudioCodec"},{"Container":"Container","VideoCodec":"VideoCodec","AudioCodec":"AudioCodec"}],"MaxStaticMusicBitrate":2,"Id":"Id"},"PlaySessionId":"PlaySessionId","AudioStreamIndex":0,"UserId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","EnableDirectPlay":True}
    params = [('openToken', 'open_token_example'),
                    ('userId', 'user_id_example'),
                    ('playSessionId', 'play_session_id_example'),
                    ('maxStreamingBitrate', 56),
                    ('startTimeTicks', 56),
                    ('audioStreamIndex', 56),
                    ('subtitleStreamIndex', 56),
                    ('maxAudioChannels', 56),
                    ('itemId', 'item_id_example'),
                    ('enableDirectPlay', True),
                    ('enableDirectStream', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/LiveStreams/Open',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

