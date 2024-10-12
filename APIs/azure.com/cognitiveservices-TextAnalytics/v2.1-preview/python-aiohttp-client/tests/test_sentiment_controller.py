# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.multi_language_batch_input import MultiLanguageBatchInput
from openapi_server.models.sentiment_batch_result import SentimentBatchResult


pytestmark = pytest.mark.asyncio

async def test_sentiment(client):
    """Test case for sentiment

    The API returns a numeric score between 0 and 1.
    """
    input = {"documents":[{"id":"1","language":"en","text":"Hello world. This is some input text that I love."},{"id":"2","language":"fr","text":"Bonjour tout le monde"},{"id":"3","language":"es","text":"La carretera estaba atascada. Había mucho tráfico el día de ayer."}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/sentiment',
        headers=headers,
        json=input,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

