# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.client_capabilities_dto import ClientCapabilitiesDto
from openapi_server.models.general_command import GeneralCommand
from openapi_server.models.general_command_type import GeneralCommandType
from openapi_server.models.name_id_pair import NameIdPair
from openapi_server.models.play_command import PlayCommand
from openapi_server.models.playstate_command import PlaystateCommand
from openapi_server.models.session_info import SessionInfo


pytestmark = pytest.mark.asyncio

async def test_add_user_to_session(client):
    """Test case for add_user_to_session

    Adds an additional user to a session.
    """
    headers = { 
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/Sessions/{session_id}/User/{user_id}'.format(session_id='session_id_example', user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_display_content(client):
    """Test case for display_content

    Instructs a session to browse to an item or view.
    """
    params = [('itemType', 'item_type_example'),
                    ('itemId', 'item_id_example'),
                    ('itemName', 'item_name_example')]
    headers = { 
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/Sessions/{session_id}/Viewing'.format(session_id='session_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_auth_providers(client):
    """Test case for get_auth_providers

    Get all auth providers.
    """
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Auth/Providers',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_password_reset_providers(client):
    """Test case for get_password_reset_providers

    Get all password reset providers.
    """
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Auth/PasswordResetProviders',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_sessions(client):
    """Test case for get_sessions

    Gets a list of sessions.
    """
    params = [('controllableByUserId', 'controllable_by_user_id_example'),
                    ('deviceId', 'device_id_example'),
                    ('activeWithinSeconds', 56)]
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Sessions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_play(client):
    """Test case for play

    Instructs a session to play an item.
    """
    params = [('playCommand', openapi_server.PlayCommand()),
                    ('itemIds', ['item_ids_example']),
                    ('startPositionTicks', 56)]
    headers = { 
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/Sessions/{session_id}/Playing'.format(session_id='session_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_capabilities(client):
    """Test case for post_capabilities

    Updates capabilities for a device.
    """
    params = [('id', 'id_example'),
                    ('playableMediaTypes', ['playable_media_types_example']),
                    ('supportedCommands', [openapi_server.GeneralCommandType()]),
                    ('supportsMediaControl', False),
                    ('supportsSync', False),
                    ('supportsPersistentIdentifier', True)]
    headers = { 
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/Sessions/Capabilities',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_post_full_capabilities(client):
    """Test case for post_full_capabilities

    Updates capabilities for a device.
    """
    body = {"IconUrl":"IconUrl","DeviceProfile":{"EnableSingleAlbumArtLimit":True,"ManufacturerUrl":"ManufacturerUrl","MusicStreamingTranscodingBitrate":9,"AlbumArtPn":"AlbumArtPn","TranscodingProfiles":[{"BreakOnNonKeyFrames":True,"Context":"Streaming","EnableSubtitlesInManifest":True,"CopyTimestamps":True,"MinSegments":2,"EnableMpegtsM2TsMode":True,"MaxAudioChannels":"MaxAudioChannels","VideoCodec":"VideoCodec","Container":"Container","EstimateContentLength":True,"SegmentLength":4,"TranscodeSeekInfo":"Auto","Protocol":"Protocol","AudioCodec":"AudioCodec"},{"BreakOnNonKeyFrames":True,"Context":"Streaming","EnableSubtitlesInManifest":True,"CopyTimestamps":True,"MinSegments":2,"EnableMpegtsM2TsMode":True,"MaxAudioChannels":"MaxAudioChannels","VideoCodec":"VideoCodec","Container":"Container","EstimateContentLength":True,"SegmentLength":4,"TranscodeSeekInfo":"Auto","Protocol":"Protocol","AudioCodec":"AudioCodec"}],"Identification":{"ManufacturerUrl":"ManufacturerUrl","ModelNumber":"ModelNumber","ModelUrl":"ModelUrl","ModelName":"ModelName","SerialNumber":"SerialNumber","FriendlyName":"FriendlyName","Headers":[{"Value":"Value","Match":"Equals","Name":"Name"},{"Value":"Value","Match":"Equals","Name":"Name"}],"Manufacturer":"Manufacturer","ModelDescription":"ModelDescription"},"MaxStreamingBitrate":7,"IgnoreTranscodeByteRangeRequests":True,"Name":"Name","ResponseProfiles":[{"Container":"Container","OrgPn":"OrgPn","VideoCodec":"VideoCodec","AudioCodec":"AudioCodec","Conditions":[{"Condition":"Equals","IsRequired":True,"Value":"Value","Property":"AudioChannels"},{"Condition":"Equals","IsRequired":True,"Value":"Value","Property":"AudioChannels"}],"MimeType":"MimeType"},{"Container":"Container","OrgPn":"OrgPn","VideoCodec":"VideoCodec","AudioCodec":"AudioCodec","Conditions":[{"Condition":"Equals","IsRequired":True,"Value":"Value","Property":"AudioChannels"},{"Condition":"Equals","IsRequired":True,"Value":"Value","Property":"AudioChannels"}],"MimeType":"MimeType"}],"ModelUrl":"ModelUrl","MaxStaticBitrate":5,"Manufacturer":"Manufacturer","ProtocolInfo":"ProtocolInfo","RequiresPlainVideoItems":True,"ModelDescription":"ModelDescription","MaxAlbumArtWidth":6,"ModelNumber":"ModelNumber","XmlRootAttributes":[{"Value":"Value","Name":"Name"},{"Value":"Value","Name":"Name"}],"ModelName":"ModelName","FriendlyName":"FriendlyName","MaxIconHeight":1,"RequiresPlainFolders":True,"EnableSingleSubtitleLimit":True,"SubtitleProfiles":[{"Container":"Container","Format":"Format","Language":"Language","DidlMode":"DidlMode","Method":"Encode"},{"Container":"Container","Format":"Format","Language":"Language","DidlMode":"DidlMode","Method":"Encode"}],"MaxAlbumArtHeight":0,"EnableAlbumArtInDidl":True,"EnableMSMediaReceiverRegistrar":True,"CodecProfiles":[{"Codec":"Codec","Container":"Container","Type":"Video","ApplyConditions":[{"Condition":"Equals","IsRequired":True,"Value":"Value","Property":"AudioChannels"},{"Condition":"Equals","IsRequired":True,"Value":"Value","Property":"AudioChannels"}],"Conditions":[{"Condition":"Equals","IsRequired":True,"Value":"Value","Property":"AudioChannels"},{"Condition":"Equals","IsRequired":True,"Value":"Value","Property":"AudioChannels"}]},{"Codec":"Codec","Container":"Container","Type":"Video","ApplyConditions":[{"Condition":"Equals","IsRequired":True,"Value":"Value","Property":"AudioChannels"},{"Condition":"Equals","IsRequired":True,"Value":"Value","Property":"AudioChannels"}],"Conditions":[{"Condition":"Equals","IsRequired":True,"Value":"Value","Property":"AudioChannels"},{"Condition":"Equals","IsRequired":True,"Value":"Value","Property":"AudioChannels"}]}],"SerialNumber":"SerialNumber","SupportedMediaTypes":"SupportedMediaTypes","SonyAggregationFlags":"SonyAggregationFlags","MaxIconWidth":5,"UserId":"UserId","TimelineOffsetSeconds":3,"ContainerProfiles":[{"Container":"Container","Type":"Audio","Conditions":[{"Condition":"Equals","IsRequired":True,"Value":"Value","Property":"AudioChannels"},{"Condition":"Equals","IsRequired":True,"Value":"Value","Property":"AudioChannels"}]},{"Container":"Container","Type":"Audio","Conditions":[{"Condition":"Equals","IsRequired":True,"Value":"Value","Property":"AudioChannels"},{"Condition":"Equals","IsRequired":True,"Value":"Value","Property":"AudioChannels"}]}],"DirectPlayProfiles":[{"Container":"Container","VideoCodec":"VideoCodec","AudioCodec":"AudioCodec"},{"Container":"Container","VideoCodec":"VideoCodec","AudioCodec":"AudioCodec"}],"MaxStaticMusicBitrate":2,"Id":"Id"},"PlayableMediaTypes":["PlayableMediaTypes","PlayableMediaTypes"],"SupportedCommands":["MoveUp","MoveUp"],"SupportsContentUploading":True,"SupportsMediaControl":True,"SupportsPersistentIdentifier":True,"AppStoreUrl":"AppStoreUrl","SupportsSync":True,"MessageCallbackUrl":"MessageCallbackUrl"}
    params = [('id', 'id_example')]
    headers = { 
        'Content-Type': 'application/*+json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/Sessions/Capabilities/Full',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_user_from_session(client):
    """Test case for remove_user_from_session

    Removes an additional user from a session.
    """
    headers = { 
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/Sessions/{session_id}/User/{user_id}'.format(session_id='session_id_example', user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_report_session_ended(client):
    """Test case for report_session_ended

    Reports that a session has ended.
    """
    headers = { 
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/Sessions/Logout',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_report_viewing(client):
    """Test case for report_viewing

    Reports that a session is viewing an item.
    """
    params = [('sessionId', 'session_id_example'),
                    ('itemId', 'item_id_example')]
    headers = { 
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/Sessions/Viewing',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_send_full_general_command(client):
    """Test case for send_full_general_command

    Issues a full general command to a client.
    """
    body = {"Arguments":{"key":"Arguments"},"ControllingUserId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","Name":"MoveUp"}
    headers = { 
        'Content-Type': 'application/*+json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/Sessions/{session_id}/Command'.format(session_id='session_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_send_general_command(client):
    """Test case for send_general_command

    Issues a general command to a client.
    """
    headers = { 
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/Sessions/{session_id}/Command/{command}'.format(session_id='session_id_example', command=openapi_server.GeneralCommandType()),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_send_message_command(client):
    """Test case for send_message_command

    Issues a command to a client to display a message to the user.
    """
    params = [('text', 'text_example'),
                    ('header', 'header_example'),
                    ('timeoutMs', 56)]
    headers = { 
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/Sessions/{session_id}/Message'.format(session_id='session_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_send_playstate_command(client):
    """Test case for send_playstate_command

    Issues a playstate command to a client.
    """
    params = [('seekPositionTicks', 56),
                    ('controllingUserId', 'controlling_user_id_example')]
    headers = { 
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/Sessions/{session_id}/Playing/{command}'.format(session_id='session_id_example', command=openapi_server.PlaystateCommand()),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_send_system_command(client):
    """Test case for send_system_command

    Issues a system command to a client.
    """
    headers = { 
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/Sessions/{session_id}/System/{command}'.format(session_id='session_id_example', command=openapi_server.GeneralCommandType()),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

