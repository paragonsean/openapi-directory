# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.word_alterations_dto import WordAlterationsDTO


pytestmark = pytest.mark.asyncio

async def test_alterations_get(client):
    """Test case for alterations_get

    Download alterations from runtime.
    """
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/alterations',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_alterations_replace(client):
    """Test case for alterations_replace

    Replace alterations data.
    """
    word_alterations = {"wordAlterations":[{"alterations":["alterations","alterations"]},{"alterations":["alterations","alterations"]}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/alterations',
        headers=headers,
        json=word_alterations,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

