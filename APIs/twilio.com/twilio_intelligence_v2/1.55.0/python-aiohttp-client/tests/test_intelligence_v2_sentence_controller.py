# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_sentence_response import ListSentenceResponse


pytestmark = pytest.mark.asyncio

async def test_list_sentence(client):
    """Test case for list_sentence

    
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
        path='/v2/Transcripts/{transcript_sid}/Sentences'.format(transcript_sid='transcript_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

