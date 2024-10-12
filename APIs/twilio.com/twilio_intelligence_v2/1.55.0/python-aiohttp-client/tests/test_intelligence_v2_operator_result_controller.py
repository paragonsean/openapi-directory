# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.intelligence_v2_transcript_operator_result import IntelligenceV2TranscriptOperatorResult
from openapi_server.models.list_operator_result_response import ListOperatorResultResponse


pytestmark = pytest.mark.asyncio

async def test_fetch_operator_result(client):
    """Test case for fetch_operator_result

    
    """
    params = [('Redacted', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/Transcripts/{transcript_sid}/OperatorResults/{operator_sid}'.format(transcript_sid='transcript_sid_example', operator_sid='operator_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_operator_result(client):
    """Test case for list_operator_result

    
    """
    params = [('Redacted', True),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/Transcripts/{transcript_sid}/OperatorResults'.format(transcript_sid='transcript_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

