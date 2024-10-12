# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_error import APIError
from openapi_server.models.evaluate import Evaluate
from openapi_server.models.found_faces import FoundFaces
from openapi_server.models.match_response import MatchResponse
from openapi_server.models.ocr import OCR


pytestmark = pytest.mark.asyncio

async def test_image_moderation_evaluate(client):
    """Test case for image_moderation_evaluate

    
    """
    params = [('CacheImage', True)]
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/contentmoderator/moderate/v1.0/ProcessImage/Evaluate',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_image_moderation_find_faces(client):
    """Test case for image_moderation_find_faces

    
    """
    params = [('CacheImage', True)]
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/contentmoderator/moderate/v1.0/ProcessImage/FindFaces',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_image_moderation_match(client):
    """Test case for image_moderation_match

    
    """
    params = [('listId', 'list_id_example'),
                    ('CacheImage', True)]
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/contentmoderator/moderate/v1.0/ProcessImage/Match',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_image_moderation_ocr(client):
    """Test case for image_moderation_ocr

    
    """
    params = [('language', 'language_example'),
                    ('CacheImage', True),
                    ('enhanced', False)]
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/contentmoderator/moderate/v1.0/ProcessImage/OCR',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

