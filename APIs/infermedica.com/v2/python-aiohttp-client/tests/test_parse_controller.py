# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.parse_request import ParseRequest
from openapi_server.models.parse_response import ParseResponse


pytestmark = pytest.mark.asyncio

async def test_get_mentions(client):
    """Test case for get_mentions

    Find mentions of observations in given text
    """
    body = {"correct_spelling":True,"include_tokens":True,"context":["context","context"],"concept_types":["symptom","symptom"],"text":"text"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/parse',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

