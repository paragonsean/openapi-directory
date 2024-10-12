# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.conference_deaf_response import ConferenceDeafResponse
from openapi_server.models.conference_hangup_response import ConferenceHangupResponse
from openapi_server.models.conference_kick_response import ConferenceKickResponse
from openapi_server.models.conference_list_members_response import ConferenceListMembersResponse
from openapi_server.models.conference_list_response import ConferenceListResponse
from openapi_server.models.conference_mute_response import ConferenceMuteResponse
from openapi_server.models.conference_play_response import ConferencePlayResponse
from openapi_server.models.conference_record_start_response import ConferenceRecordStartResponse
from openapi_server.models.conference_record_stop_response import ConferenceRecordStopResponse
from openapi_server.models.conference_speak_response import ConferenceSpeakResponse
from openapi_server.models.conference_undeaf_response import ConferenceUndeafResponse
from openapi_server.models.conference_unmute_response import ConferenceUnmuteResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_v01_conference_deaf_post(client):
    """Test case for v01_conference_deaf_post

    /v0.1/ConferenceDeaf/
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'conference_name': 'conference_name_example',
        'member_id': 'member_id_example'
        }
    response = await client.request(
        method='POST',
        path='/rtckit/media/master/eqivo/readme-splash.png/v0.1/ConferenceDeaf/',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_v01_conference_hangup_post(client):
    """Test case for v01_conference_hangup_post

    /v0.1/ConferenceHangup/
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'conference_name': 'conference_name_example',
        'member_id': 'member_id_example'
        }
    response = await client.request(
        method='POST',
        path='/rtckit/media/master/eqivo/readme-splash.png/v0.1/ConferenceHangup/',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_v01_conference_kick_post(client):
    """Test case for v01_conference_kick_post

    /v0.1/ConferenceKick/
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'conference_name': 'conference_name_example',
        'member_id': 'member_id_example'
        }
    response = await client.request(
        method='POST',
        path='/rtckit/media/master/eqivo/readme-splash.png/v0.1/ConferenceKick/',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_v01_conference_list_members_post(client):
    """Test case for v01_conference_list_members_post

    /v0.1/ConferenceListMembers/
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'call_uuid_filter': 'call_uuid_filter_example',
        'conference_name': 'conference_name_example',
        'deaf_filter': False,
        'member_filter': 'member_filter_example',
        'muted_filter': False
        }
    response = await client.request(
        method='POST',
        path='/rtckit/media/master/eqivo/readme-splash.png/v0.1/ConferenceListMembers/',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_v01_conference_list_post(client):
    """Test case for v01_conference_list_post

    /v0.1/ConferenceList/
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'call_uuid_filter': 'call_uuid_filter_example',
        'deaf_filter': False,
        'member_filter': 'member_filter_example',
        'muted_filter': False
        }
    response = await client.request(
        method='POST',
        path='/rtckit/media/master/eqivo/readme-splash.png/v0.1/ConferenceList/',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_v01_conference_mute_post(client):
    """Test case for v01_conference_mute_post

    /v0.1/ConferenceMute/
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'conference_name': 'conference_name_example',
        'member_id': 'member_id_example'
        }
    response = await client.request(
        method='POST',
        path='/rtckit/media/master/eqivo/readme-splash.png/v0.1/ConferenceMute/',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_v01_conference_play_post(client):
    """Test case for v01_conference_play_post

    /v0.1/ConferencePlay/
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'conference_name': 'conference_name_example',
        'file_path': 'file_path_example',
        'member_id': 'member_id_example'
        }
    response = await client.request(
        method='POST',
        path='/rtckit/media/master/eqivo/readme-splash.png/v0.1/ConferencePlay/',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_v01_conference_record_start_post(client):
    """Test case for v01_conference_record_start_post

    /v0.1/ConferenceRecordStart/
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'conference_name': 'conference_name_example',
        'file_format': mp3,
        'file_name': '',
        'file_path': ''
        }
    response = await client.request(
        method='POST',
        path='/rtckit/media/master/eqivo/readme-splash.png/v0.1/ConferenceRecordStart/',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_v01_conference_record_stop_post(client):
    """Test case for v01_conference_record_stop_post

    /v0.1/ConferenceRecordStop/
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'conference_name': 'conference_name_example',
        'record_file': 'record_file_example'
        }
    response = await client.request(
        method='POST',
        path='/rtckit/media/master/eqivo/readme-splash.png/v0.1/ConferenceRecordStop/',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_v01_conference_speak_post(client):
    """Test case for v01_conference_speak_post

    /v0.1/ConferenceSpeak/
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'conference_name': 'conference_name_example',
        'member_id': 'member_id_example',
        'text': 'text_example'
        }
    response = await client.request(
        method='POST',
        path='/rtckit/media/master/eqivo/readme-splash.png/v0.1/ConferenceSpeak/',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_v01_conference_undeaf_post(client):
    """Test case for v01_conference_undeaf_post

    /v0.1/ConferenceUndeaf/
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'conference_name': 'conference_name_example',
        'member_id': 'member_id_example'
        }
    response = await client.request(
        method='POST',
        path='/rtckit/media/master/eqivo/readme-splash.png/v0.1/ConferenceUndeaf/',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_v01_conference_unmute_post(client):
    """Test case for v01_conference_unmute_post

    /v0.1/ConferenceUnmute/
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'conference_name': 'conference_name_example',
        'member_id': 'member_id_example'
        }
    response = await client.request(
        method='POST',
        path='/rtckit/media/master/eqivo/readme-splash.png/v0.1/ConferenceUnmute/',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

