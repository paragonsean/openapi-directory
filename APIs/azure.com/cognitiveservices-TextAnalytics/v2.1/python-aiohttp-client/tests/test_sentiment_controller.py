# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.multi_language_batch_input import MultiLanguageBatchInput
from openapi_server.models.sentiment_batch_result import SentimentBatchResult


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sentiment(client):
    """Test case for sentiment

    The API returns a numeric score between 0 and 1.
    """
    multi_language_batch_input = {"documents":[{"language":"language","id":"id","text":"text"},{"language":"language","id":"id","text":"text"}]}
    params = [('showStats', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/sentiment',
        headers=headers,
        json=multi_language_batch_input,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

