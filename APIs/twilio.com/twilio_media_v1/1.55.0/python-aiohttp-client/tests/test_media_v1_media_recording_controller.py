# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_media_recording_response import ListMediaRecordingResponse
from openapi_server.models.media_recording_enum_order import MediaRecordingEnumOrder
from openapi_server.models.media_recording_enum_status import MediaRecordingEnumStatus
from openapi_server.models.media_v1_media_recording import MediaV1MediaRecording


pytestmark = pytest.mark.asyncio

async def test_delete_media_recording(client):
    """Test case for delete_media_recording

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/MediaRecordings/{sid}'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_media_recording(client):
    """Test case for fetch_media_recording

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/MediaRecordings/{sid}'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_media_recording(client):
    """Test case for list_media_recording

    
    """
    params = [('Order', openapi_server.MediaRecordingEnumOrder()),
                    ('Status', openapi_server.MediaRecordingEnumStatus()),
                    ('ProcessorSid', 'processor_sid_example'),
                    ('SourceSid', 'source_sid_example'),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/MediaRecordings',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

