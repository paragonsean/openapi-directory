# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.batch_input import BatchInput
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.language_batch_result import LanguageBatchResult


pytestmark = pytest.mark.asyncio

async def test_detect_language(client):
    """Test case for detect_language

    The API returns the detected language and a numeric score between 0 and 1.
    """
    input = {"documents":[{"id":"1","text":"Hello world"},{"id":"2","text":"Bonjour tout le monde"},{"id":"3","text":"La carretera estaba atascada. Había mucho tráfico el día de ayer."},{"id":"4","text":":) :( :D"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/languages',
        headers=headers,
        json=input,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

