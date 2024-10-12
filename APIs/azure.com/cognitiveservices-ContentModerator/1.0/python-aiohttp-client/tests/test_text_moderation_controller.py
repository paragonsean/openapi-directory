# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_error import APIError
from openapi_server.models.detected_language import DetectedLanguage
from openapi_server.models.screen import Screen


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_text_moderation_detect_language(client):
    """Test case for text_moderation_detect_language

    
    """
    text_content = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'text/plain',
        'content_type': 'content_type_example',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/contentmoderator/moderate/v1.0/ProcessText/DetectLanguage',
        headers=headers,
        json=text_content,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_text_moderation_screen_text(client):
    """Test case for text_moderation_screen_text

    Detect profanity and match against custom and shared blacklists
    """
    text_content = None
    params = [('language', 'language_example'),
                    ('autocorrect', False),
                    ('PII', False),
                    ('listId', 'list_id_example'),
                    ('classify', False)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'text/plain',
        'content_type': 'content_type_example',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/contentmoderator/moderate/v1.0/ProcessText/Screen/',
        headers=headers,
        json=text_content,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

