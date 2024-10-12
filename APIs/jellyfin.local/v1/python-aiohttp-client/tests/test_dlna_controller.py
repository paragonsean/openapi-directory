# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.device_profile import DeviceProfile
from openapi_server.models.device_profile_info import DeviceProfileInfo
from openapi_server.models.problem_details import ProblemDetails


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_create_profile(client):
    """Test case for create_profile

    Creates a profile.
    """
    body = {"EnableSingleAlbumArtLimit":True,"ManufacturerUrl":"ManufacturerUrl","MusicStreamingTranscodingBitrate":9,"AlbumArtPn":"AlbumArtPn","TranscodingProfiles":[{"BreakOnNonKeyFrames":True,"Context":"Streaming","EnableSubtitlesInManifest":True,"CopyTimestamps":True,"MinSegments":2,"EnableMpegtsM2TsMode":True,"MaxAudioChannels":"MaxAudioChannels","VideoCodec":"VideoCodec","Container":"Container","EstimateContentLength":True,"SegmentLength":4,"TranscodeSeekInfo":"Auto","Protocol":"Protocol","AudioCodec":"AudioCodec"},{"BreakOnNonKeyFrames":True,"Context":"Streaming","EnableSubtitlesInManifest":True,"CopyTimestamps":True,"MinSegments":2,"EnableMpegtsM2TsMode":True,"MaxAudioChannels":"MaxAudioChannels","VideoCodec":"VideoCodec","Container":"Container","EstimateContentLength":True,"SegmentLength":4,"TranscodeSeekInfo":"Auto","Protocol":"Protocol","AudioCodec":"AudioCodec"}],"Identification":{"ManufacturerUrl":"ManufacturerUrl","ModelNumber":"ModelNumber","ModelUrl":"ModelUrl","ModelName":"ModelName","SerialNumber":"SerialNumber","FriendlyName":"FriendlyName","Headers":[{"Value":"Value","Match":"Equals","Name":"Name"},{"Value":"Value","Match":"Equals","Name":"Name"}],"Manufacturer":"Manufacturer","ModelDescription":"ModelDescription"},"MaxStreamingBitrate":7,"IgnoreTranscodeByteRangeRequests":True,"Name":"Name","ResponseProfiles":[{"Container":"Container","OrgPn":"OrgPn","VideoCodec":"VideoCodec","AudioCodec":"AudioCodec","Conditions":[{"Condition":"Equals","IsRequired":True,"Value":"Value","Property":"AudioChannels"},{"Condition":"Equals","IsRequired":True,"Value":"Value","Property":"AudioChannels"}],"MimeType":"MimeType"},{"Container":"Container","OrgPn":"OrgPn","VideoCodec":"VideoCodec","AudioCodec":"AudioCodec","Conditions":[{"Condition":"Equals","IsRequired":True,"Value":"Value","Property":"AudioChannels"},{"Condition":"Equals","IsRequired":True,"Value":"Value","Property":"AudioChannels"}],"MimeType":"MimeType"}],"ModelUrl":"ModelUrl","MaxStaticBitrate":5,"Manufacturer":"Manufacturer","ProtocolInfo":"ProtocolInfo","RequiresPlainVideoItems":True,"ModelDescription":"ModelDescription","MaxAlbumArtWidth":6,"ModelNumber":"ModelNumber","XmlRootAttributes":[{"Value":"Value","Name":"Name"},{"Value":"Value","Name":"Name"}],"ModelName":"ModelName","FriendlyName":"FriendlyName","MaxIconHeight":1,"RequiresPlainFolders":True,"EnableSingleSubtitleLimit":True,"SubtitleProfiles":[{"Container":"Container","Format":"Format","Language":"Language","DidlMode":"DidlMode","Method":"Encode"},{"Container":"Container","Format":"Format","Language":"Language","DidlMode":"DidlMode","Method":"Encode"}],"MaxAlbumArtHeight":0,"EnableAlbumArtInDidl":True,"EnableMSMediaReceiverRegistrar":True,"CodecProfiles":[{"Codec":"Codec","Container":"Container","Type":"Video","ApplyConditions":[{"Condition":"Equals","IsRequired":True,"Value":"Value","Property":"AudioChannels"},{"Condition":"Equals","IsRequired":True,"Value":"Value","Property":"AudioChannels"}],"Conditions":[{"Condition":"Equals","IsRequired":True,"Value":"Value","Property":"AudioChannels"},{"Condition":"Equals","IsRequired":True,"Value":"Value","Property":"AudioChannels"}]},{"Codec":"Codec","Container":"Container","Type":"Video","ApplyConditions":[{"Condition":"Equals","IsRequired":True,"Value":"Value","Property":"AudioChannels"},{"Condition":"Equals","IsRequired":True,"Value":"Value","Property":"AudioChannels"}],"Conditions":[{"Condition":"Equals","IsRequired":True,"Value":"Value","Property":"AudioChannels"},{"Condition":"Equals","IsRequired":True,"Value":"Value","Property":"AudioChannels"}]}],"SerialNumber":"SerialNumber","SupportedMediaTypes":"SupportedMediaTypes","SonyAggregationFlags":"SonyAggregationFlags","MaxIconWidth":5,"UserId":"UserId","TimelineOffsetSeconds":3,"ContainerProfiles":[{"Container":"Container","Type":"Audio","Conditions":[{"Condition":"Equals","IsRequired":True,"Value":"Value","Property":"AudioChannels"},{"Condition":"Equals","IsRequired":True,"Value":"Value","Property":"AudioChannels"}]},{"Container":"Container","Type":"Audio","Conditions":[{"Condition":"Equals","IsRequired":True,"Value":"Value","Property":"AudioChannels"},{"Condition":"Equals","IsRequired":True,"Value":"Value","Property":"AudioChannels"}]}],"DirectPlayProfiles":[{"Container":"Container","VideoCodec":"VideoCodec","AudioCodec":"AudioCodec"},{"Container":"Container","VideoCodec":"VideoCodec","AudioCodec":"AudioCodec"}],"MaxStaticMusicBitrate":2,"Id":"Id"}
    headers = { 
        'Content-Type': 'application/*+json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/Dlna/Profiles',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_profile(client):
    """Test case for delete_profile

    Deletes a profile.
    """
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/Dlna/Profiles/{profile_id}'.format(profile_id='profile_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_default_profile(client):
    """Test case for get_default_profile

    Gets the default profile.
    """
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Dlna/Profiles/Default',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_profile(client):
    """Test case for get_profile

    Gets a single profile.
    """
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Dlna/Profiles/{profile_id}'.format(profile_id='profile_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_profile_infos(client):
    """Test case for get_profile_infos

    Get profile infos.
    """
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Dlna/ProfileInfos',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_update_profile(client):
    """Test case for update_profile

    Updates a profile.
    """
    body = {"EnableSingleAlbumArtLimit":True,"ManufacturerUrl":"ManufacturerUrl","MusicStreamingTranscodingBitrate":9,"AlbumArtPn":"AlbumArtPn","TranscodingProfiles":[{"BreakOnNonKeyFrames":True,"Context":"Streaming","EnableSubtitlesInManifest":True,"CopyTimestamps":True,"MinSegments":2,"EnableMpegtsM2TsMode":True,"MaxAudioChannels":"MaxAudioChannels","VideoCodec":"VideoCodec","Container":"Container","EstimateContentLength":True,"SegmentLength":4,"TranscodeSeekInfo":"Auto","Protocol":"Protocol","AudioCodec":"AudioCodec"},{"BreakOnNonKeyFrames":True,"Context":"Streaming","EnableSubtitlesInManifest":True,"CopyTimestamps":True,"MinSegments":2,"EnableMpegtsM2TsMode":True,"MaxAudioChannels":"MaxAudioChannels","VideoCodec":"VideoCodec","Container":"Container","EstimateContentLength":True,"SegmentLength":4,"TranscodeSeekInfo":"Auto","Protocol":"Protocol","AudioCodec":"AudioCodec"}],"Identification":{"ManufacturerUrl":"ManufacturerUrl","ModelNumber":"ModelNumber","ModelUrl":"ModelUrl","ModelName":"ModelName","SerialNumber":"SerialNumber","FriendlyName":"FriendlyName","Headers":[{"Value":"Value","Match":"Equals","Name":"Name"},{"Value":"Value","Match":"Equals","Name":"Name"}],"Manufacturer":"Manufacturer","ModelDescription":"ModelDescription"},"MaxStreamingBitrate":7,"IgnoreTranscodeByteRangeRequests":True,"Name":"Name","ResponseProfiles":[{"Container":"Container","OrgPn":"OrgPn","VideoCodec":"VideoCodec","AudioCodec":"AudioCodec","Conditions":[{"Condition":"Equals","IsRequired":True,"Value":"Value","Property":"AudioChannels"},{"Condition":"Equals","IsRequired":True,"Value":"Value","Property":"AudioChannels"}],"MimeType":"MimeType"},{"Container":"Container","OrgPn":"OrgPn","VideoCodec":"VideoCodec","AudioCodec":"AudioCodec","Conditions":[{"Condition":"Equals","IsRequired":True,"Value":"Value","Property":"AudioChannels"},{"Condition":"Equals","IsRequired":True,"Value":"Value","Property":"AudioChannels"}],"MimeType":"MimeType"}],"ModelUrl":"ModelUrl","MaxStaticBitrate":5,"Manufacturer":"Manufacturer","ProtocolInfo":"ProtocolInfo","RequiresPlainVideoItems":True,"ModelDescription":"ModelDescription","MaxAlbumArtWidth":6,"ModelNumber":"ModelNumber","XmlRootAttributes":[{"Value":"Value","Name":"Name"},{"Value":"Value","Name":"Name"}],"ModelName":"ModelName","FriendlyName":"FriendlyName","MaxIconHeight":1,"RequiresPlainFolders":True,"EnableSingleSubtitleLimit":True,"SubtitleProfiles":[{"Container":"Container","Format":"Format","Language":"Language","DidlMode":"DidlMode","Method":"Encode"},{"Container":"Container","Format":"Format","Language":"Language","DidlMode":"DidlMode","Method":"Encode"}],"MaxAlbumArtHeight":0,"EnableAlbumArtInDidl":True,"EnableMSMediaReceiverRegistrar":True,"CodecProfiles":[{"Codec":"Codec","Container":"Container","Type":"Video","ApplyConditions":[{"Condition":"Equals","IsRequired":True,"Value":"Value","Property":"AudioChannels"},{"Condition":"Equals","IsRequired":True,"Value":"Value","Property":"AudioChannels"}],"Conditions":[{"Condition":"Equals","IsRequired":True,"Value":"Value","Property":"AudioChannels"},{"Condition":"Equals","IsRequired":True,"Value":"Value","Property":"AudioChannels"}]},{"Codec":"Codec","Container":"Container","Type":"Video","ApplyConditions":[{"Condition":"Equals","IsRequired":True,"Value":"Value","Property":"AudioChannels"},{"Condition":"Equals","IsRequired":True,"Value":"Value","Property":"AudioChannels"}],"Conditions":[{"Condition":"Equals","IsRequired":True,"Value":"Value","Property":"AudioChannels"},{"Condition":"Equals","IsRequired":True,"Value":"Value","Property":"AudioChannels"}]}],"SerialNumber":"SerialNumber","SupportedMediaTypes":"SupportedMediaTypes","SonyAggregationFlags":"SonyAggregationFlags","MaxIconWidth":5,"UserId":"UserId","TimelineOffsetSeconds":3,"ContainerProfiles":[{"Container":"Container","Type":"Audio","Conditions":[{"Condition":"Equals","IsRequired":True,"Value":"Value","Property":"AudioChannels"},{"Condition":"Equals","IsRequired":True,"Value":"Value","Property":"AudioChannels"}]},{"Container":"Container","Type":"Audio","Conditions":[{"Condition":"Equals","IsRequired":True,"Value":"Value","Property":"AudioChannels"},{"Condition":"Equals","IsRequired":True,"Value":"Value","Property":"AudioChannels"}]}],"DirectPlayProfiles":[{"Container":"Container","VideoCodec":"VideoCodec","AudioCodec":"AudioCodec"},{"Container":"Container","VideoCodec":"VideoCodec","AudioCodec":"AudioCodec"}],"MaxStaticMusicBitrate":2,"Id":"Id"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/Dlna/Profiles/{profile_id}'.format(profile_id='profile_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

