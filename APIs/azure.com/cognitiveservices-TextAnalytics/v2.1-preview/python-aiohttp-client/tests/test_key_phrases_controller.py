# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.key_phrase_batch_result import KeyPhraseBatchResult
from openapi_server.models.multi_language_batch_input import MultiLanguageBatchInput


pytestmark = pytest.mark.asyncio

async def test_key_phrases(client):
    """Test case for key_phrases

    The API returns a list of strings denoting the key talking points in the input text.
    """
    input = {"documents":[{"id":"1","language":"en","text":"Hello world. This is some input text that I love."},{"id":"2","language":"fr","text":"Bonjour tout le monde"},{"id":"3","language":"es","text":"La carretera estaba atascada. Había mucho tráfico el día de ayer."}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/keyPhrases',
        headers=headers,
        json=input,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

