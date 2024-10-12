# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.language_detection import LanguageDetection
from openapi_server.models.language_predicted import LanguagePredicted
from openapi_server.models.post import Post
from openapi_server.models.post_predicted import PostPredicted
from openapi_server.models.topic_sentiment_output import TopicSentimentOutput
from openapi_server.models.validation_errors import ValidationErrors


pytestmark = pytest.mark.asyncio

async def test_communication(client):
    """Test case for communication

    Communication & Tonality
    """
    body = {"language":"en","id":"1","text":"I love the service"}
    params = [('all', False)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/communication',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ekman_emotion(client):
    """Test case for ekman_emotion

    Emotion Analysis
    """
    body = {"language":"en","id":"1","text":"I love the service"}
    params = [('all', False)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/ekman-emotion',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_emotion(client):
    """Test case for emotion

    Emotion Analysis
    """
    body = {"language":"en","id":"1","text":"I love the service"}
    params = [('all', False)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/emotion',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_language_detection(client):
    """Test case for language_detection

    Language Detection
    """
    body = {"id":"id","text":"text"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/language-detection',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_personality(client):
    """Test case for personality

    Personality Traits
    """
    body = {"language":"en","id":"1","text":"I love the service"}
    params = [('all', False)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/personality',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sentiment(client):
    """Test case for sentiment

    Sentiment Analysis
    """
    body = {"language":"en","id":"1","text":"I love the service"}
    params = [('all', False)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/sentiment',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_topic_sentiment(client):
    """Test case for topic_sentiment

    Extracts topics and sentiments and relates them.
    """
    body = {"language":"en","id":"1","text":"I love the service"}
    params = [('domain', 'domain_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/topic-sentiment',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

