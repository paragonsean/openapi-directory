# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.intent_predict_request import IntentPredictRequest
from openapi_server.models.intent_predict_response import IntentPredictResponse
from openapi_server.models.prediction_error_response import PredictionErrorResponse
from openapi_server.models.sentiment_predict_request import SentimentPredictRequest
from openapi_server.models.sentiment_predict_response import SentimentPredictResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_intent_multipart(client):
    """Test case for intent_multipart

    Prediction for Intent
    """
    body = {"modelId":"WJH4YCA7YX4PCWVNCYNWYHBMY4","sampleId":"sampleId","document":"I can't tell you how much fun it was","numResults":3}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/language/intent',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sentiment_multipart(client):
    """Test case for sentiment_multipart

    Prediction for Sentiment
    """
    body = {"modelId":"WJH4YCA7YX4PCWVNCYNWYHBMY4","sampleId":"sampleId","document":"I can't tell you how much fun it was","numResults":3}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/language/sentiment',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

