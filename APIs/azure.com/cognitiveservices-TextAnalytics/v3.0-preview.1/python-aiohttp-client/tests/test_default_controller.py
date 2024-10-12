# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.entities_result import EntitiesResult
from openapi_server.models.entity_linking_result import EntityLinkingResult
from openapi_server.models.key_phrase_result import KeyPhraseResult
from openapi_server.models.language_batch_input import LanguageBatchInput
from openapi_server.models.language_result import LanguageResult
from openapi_server.models.multi_language_batch_input import MultiLanguageBatchInput
from openapi_server.models.sentiment_response import SentimentResponse
from openapi_server.models.text_analytics_error import TextAnalyticsError


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_entities_linking(client):
    """Test case for entities_linking

    Linked entities from a well-known knowledge base
    """
    input = {"documents":[{"language":"language","id":"id","text":"text"},{"language":"language","id":"id","text":"text"}]}
    params = [('model-version', 'model_version_example'),
                    ('showStats', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/entities/linking',
        headers=headers,
        json=input,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_entities_recognition_general(client):
    """Test case for entities_recognition_general

    Named Entity Recognition
    """
    input = {"documents":[{"language":"language","id":"id","text":"text"},{"language":"language","id":"id","text":"text"}]}
    params = [('model-version', 'model_version_example'),
                    ('showStats', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/entities/recognition/general',
        headers=headers,
        json=input,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_entities_recognition_pii(client):
    """Test case for entities_recognition_pii

    Entities containing personal information
    """
    input = {"documents":[{"language":"language","id":"id","text":"text"},{"language":"language","id":"id","text":"text"}]}
    params = [('model-version', 'model_version_example'),
                    ('showStats', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/entities/recognition/pii',
        headers=headers,
        json=input,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_key_phrases(client):
    """Test case for key_phrases

    Key Phrases
    """
    input = {"documents":[{"language":"language","id":"id","text":"text"},{"language":"language","id":"id","text":"text"}]}
    params = [('model-version', 'model_version_example'),
                    ('showStats', True)]
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
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_languages(client):
    """Test case for languages

    Detect Language
    """
    input = {"documents":[{"countryHint":"countryHint","id":"id","text":"text"},{"countryHint":"countryHint","id":"id","text":"text"}]}
    params = [('model-version', 'model_version_example'),
                    ('showStats', True)]
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
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sentiment(client):
    """Test case for sentiment

    Sentiment
    """
    input = {"documents":[{"language":"language","id":"id","text":"text"},{"language":"language","id":"id","text":"text"}]}
    params = [('model-version', 'model_version_example'),
                    ('showStats', True)]
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
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

