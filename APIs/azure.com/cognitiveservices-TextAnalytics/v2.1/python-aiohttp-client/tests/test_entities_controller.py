# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.entities_batch_result import EntitiesBatchResult
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.multi_language_batch_input import MultiLanguageBatchInput


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_entities(client):
    """Test case for entities

    The API returns a list of recognized entities in a given document.
    """
    multi_language_batch_input = {"documents":[{"language":"language","id":"id","text":"text"},{"language":"language","id":"id","text":"text"}]}
    params = [('showStats', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/entities',
        headers=headers,
        json=multi_language_batch_input,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

