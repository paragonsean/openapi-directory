# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_v1_suggest_get200_response import ApiV1SuggestGet200Response


pytestmark = pytest.mark.asyncio

async def test_api_v1_suggest_get(client):
    """Test case for api_v1_suggest_get

    Get .at domain name suggestions
    """
    params = [('term', 'mydomain')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/suggest',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

