# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.entities_response import EntitiesResponse
from openapi_server.models.lemmatize_response import LemmatizeResponse
from openapi_server.models.request import Request
from openapi_server.models.sentiment_response import SentimentResponse
from openapi_server.models.topic_response import TopicResponse


pytestmark = pytest.mark.asyncio

async def test_correction_get(client):
    """Test case for correction_get

    Performs text correction (diacritization) on the given document
    """
    params = [('id', 'id_example'),
                    ('text', 'text_example'),
                    ('url', 'url_example'),
                    ('extractor', 'extractor_example'),
                    ('language', 'language_example'),
                    ('returnTextInfo', True)]
    headers = { 
        'Accept': 'application/json',
        'user_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/s1/correction',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_correction_post(client):
    """Test case for correction_post

    Performs text correction (diacritization) on the given document
    """
    body = {"returnTextInfo":True,"options":"{}","extractor":"default","language":"language","id":"id","text":"text","url":"url"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'user_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/s1/correction',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_entities_get(client):
    """Test case for entities_get

    Performs named-entity recognition on the given document
    """
    params = [('id', 'id_example'),
                    ('text', 'text_example'),
                    ('url', 'url_example'),
                    ('extractor', 'extractor_example'),
                    ('language', 'language_example'),
                    ('returnTextInfo', True)]
    headers = { 
        'Accept': 'application/json',
        'user_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/s1/entities',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_entities_post(client):
    """Test case for entities_post

    Performs named-entity recognition on the given document
    """
    body = {"returnTextInfo":True,"options":"{}","extractor":"default","language":"language","id":"id","text":"text","url":"url"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'user_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/s1/entities',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_lemmatize_get(client):
    """Test case for lemmatize_get

    Performs lemmatization on the given document
    """
    params = [('id', 'id_example'),
                    ('text', 'text_example'),
                    ('url', 'url_example'),
                    ('extractor', 'extractor_example'),
                    ('language', 'language_example'),
                    ('returnTextInfo', True)]
    headers = { 
        'Accept': 'application/json',
        'user_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/s1/lemmatize',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_lemmatize_post(client):
    """Test case for lemmatize_post

    Performs lemmatization on the given document
    """
    body = {"returnTextInfo":True,"options":"{}","extractor":"default","language":"language","id":"id","text":"text","url":"url"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'user_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/s1/lemmatize',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sentiment_get(client):
    """Test case for sentiment_get

    Performs sentiment analysis on the given document
    """
    params = [('id', 'id_example'),
                    ('text', 'text_example'),
                    ('url', 'url_example'),
                    ('extractor', 'extractor_example'),
                    ('language', 'language_example'),
                    ('returnTextInfo', True)]
    headers = { 
        'Accept': 'application/json',
        'user_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/s1/sentiment',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sentiment_post(client):
    """Test case for sentiment_post

    Performs sentiment analysis on the given document
    """
    body = {"returnTextInfo":True,"options":"{}","extractor":"default","language":"language","id":"id","text":"text","url":"url"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'user_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/s1/sentiment',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_topic_get(client):
    """Test case for topic_get

    Performs topic detection on the given document
    """
    params = [('id', 'id_example'),
                    ('text', 'text_example'),
                    ('url', 'url_example'),
                    ('extractor', 'extractor_example'),
                    ('language', 'language_example'),
                    ('returnTextInfo', True)]
    headers = { 
        'Accept': 'application/json',
        'user_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/s1/topic',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_topic_post(client):
    """Test case for topic_post

    Performs topic detection on the given document
    """
    body = {"returnTextInfo":True,"options":"{}","extractor":"default","language":"language","id":"id","text":"text","url":"url"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'user_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/s1/topic',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

