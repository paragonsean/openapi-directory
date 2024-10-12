# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.language_batch_input import LanguageBatchInput
from openapi_server.models.language_batch_result import LanguageBatchResult


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_detect_language(client):
    """Test case for detect_language

    The API returns the detected language and a numeric score between 0 and 1.
    """
    language_batch_input = {"documents":[{"countryHint":"countryHint","id":"id","text":"text"},{"countryHint":"countryHint","id":"id","text":"text"}]}
    params = [('showStats', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/languages',
        headers=headers,
        json=language_batch_input,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

