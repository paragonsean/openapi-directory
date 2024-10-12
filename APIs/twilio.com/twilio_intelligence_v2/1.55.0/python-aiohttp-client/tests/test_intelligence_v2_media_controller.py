# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.intelligence_v2_transcript_media import IntelligenceV2TranscriptMedia


pytestmark = pytest.mark.asyncio

async def test_fetch_media(client):
    """Test case for fetch_media

    
    """
    params = [('Redacted', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/Transcripts/{sid}/Media'.format(sid='sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

