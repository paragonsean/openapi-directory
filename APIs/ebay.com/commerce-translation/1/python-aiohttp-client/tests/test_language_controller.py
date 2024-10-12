# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.translate400_response import Translate400Response
from openapi_server.models.translate_request import TranslateRequest
from openapi_server.models.translate_response import TranslateResponse


pytestmark = pytest.mark.asyncio

async def test_translate(client):
    """Test case for translate

    
    """
    body = {"from":"from","text":["text","text"],"to":"to","translationContext":"translationContext"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/commerce/translation/v1/translate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

