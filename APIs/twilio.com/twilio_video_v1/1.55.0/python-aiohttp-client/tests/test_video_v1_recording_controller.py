# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_recording_response import ListRecordingResponse
from openapi_server.models.recording_enum_status import RecordingEnumStatus
from openapi_server.models.recording_enum_type import RecordingEnumType
from openapi_server.models.video_v1_recording import VideoV1Recording


pytestmark = pytest.mark.asyncio

async def test_delete_recording(client):
    """Test case for delete_recording

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/Recordings/{sid}'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


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
        path='/v1/Recordings/{sid}'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_recording(client):
    """Test case for list_recording

    
    """
    params = [('Status', openapi_server.RecordingEnumStatus()),
                    ('SourceSid', 'source_sid_example'),
                    ('GroupingSid', ['grouping_sid_example']),
                    ('DateCreatedAfter', '2013-10-20T19:20:30+01:00'),
                    ('DateCreatedBefore', '2013-10-20T19:20:30+01:00'),
                    ('MediaType', openapi_server.RecordingEnumType()),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Recordings',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

