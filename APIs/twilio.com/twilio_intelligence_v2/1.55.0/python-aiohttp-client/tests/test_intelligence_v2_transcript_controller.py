# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.intelligence_v2_transcript import IntelligenceV2Transcript
from openapi_server.models.list_transcript_response import ListTranscriptResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_transcript(client):
    """Test case for create_transcript

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'channel': None,
        'customer_key': 'customer_key_example',
        'media_start_time': '2013-10-20T19:20:30+01:00',
        'service_sid': 'service_sid_example'
        }
    response = await client.request(
        method='POST',
        path='/v2/Transcripts',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_transcript(client):
    """Test case for delete_transcript

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/Transcripts/{sid}'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_transcript(client):
    """Test case for fetch_transcript

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/Transcripts/{sid}'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_transcript(client):
    """Test case for list_transcript

    
    """
    params = [('ServiceSid', 'service_sid_example'),
                    ('BeforeStartTime', 'before_start_time_example'),
                    ('AfterStartTime', 'after_start_time_example'),
                    ('BeforeDateCreated', 'before_date_created_example'),
                    ('AfterDateCreated', 'after_date_created_example'),
                    ('Status', 'status_example'),
                    ('LanguageCode', 'language_code_example'),
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
        path='/v2/Transcripts',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

