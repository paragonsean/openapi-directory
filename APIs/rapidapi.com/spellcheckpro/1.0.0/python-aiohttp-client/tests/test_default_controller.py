# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.check_spelling_russian_request import CheckSpellingRussianRequest


pytestmark = pytest.mark.asyncio

async def test_check_spelling_russian(client):
    """Test case for check_spelling_russian

    Check Spelling (Russian)
    """
    body = {"lang_code":"ru","text":"Добрый вее!"}
    headers = { 
        'Content-Type': 'application/json',
        'x_rapid_api_key': '',
    }
    response = await client.request(
        method='POST',
        path='/check_spelling',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

