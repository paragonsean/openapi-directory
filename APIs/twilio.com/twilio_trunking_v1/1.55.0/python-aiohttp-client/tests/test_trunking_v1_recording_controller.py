# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.recording_enum_recording_mode import RecordingEnumRecordingMode
from openapi_server.models.recording_enum_recording_trim import RecordingEnumRecordingTrim
from openapi_server.models.trunking_v1_trunk_recording import TrunkingV1TrunkRecording


pytestmark = pytest.mark.asyncio

async def test_fetch_recording(client):
    """Test case for fetch_recording

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Trunks/{trunk_sid}/Recording'.format(trunk_sid='trunk_sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_recording(client):
    """Test case for update_recording

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'mode': openapi_server.RecordingEnumRecordingMode(),
        'trim': openapi_server.RecordingEnumRecordingTrim()
        }
    response = await client.request(
        method='POST',
        path='/v1/Trunks/{trunk_sid}/Recording'.format(trunk_sid='trunk_sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

