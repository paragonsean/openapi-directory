# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_recognize_language_post(client):
    """Test case for recognize_language_post

    Recognize Language
    """
    headers = { 
        'Content-Type': 'application/x-www-form-urlencoded',
        'x_rapid_api_host': 'language-identification-prediction.p.rapidapi.com',
        'x_rapid_api_key': 'x_rapid_api_key_example',
    }
    data = {
        'text': 'text_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/recognize-language/',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

