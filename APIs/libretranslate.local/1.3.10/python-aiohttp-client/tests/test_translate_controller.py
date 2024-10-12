# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.detections_inner import DetectionsInner
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.error_slow_down import ErrorSlowDown
from openapi_server.models.languages_inner import LanguagesInner
from openapi_server.models.translate import Translate
from openapi_server.models.translate_file import TranslateFile


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_detect_post(client):
    """Test case for detect_post

    Detect the language of a single text
    """
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    response = await client.request(
        method='POST',
        path='/detect',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_languages_get(client):
    """Test case for languages_get

    Retrieve list of supported languages
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/languages',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_translate_file_post(client):
    """Test case for translate_file_post

    Translate file from a language to another
    """
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'multipart/form-data',
    }
    response = await client.request(
        method='POST',
        path='/translate_file',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_translate_post(client):
    """Test case for translate_post

    Translate text from a language to another
    """
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    response = await client.request(
        method='POST',
        path='/translate',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

