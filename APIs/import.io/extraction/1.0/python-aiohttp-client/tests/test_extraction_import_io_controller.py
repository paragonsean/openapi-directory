# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_error import APIError
from openapi_server.models.query_response import QueryResponse


pytestmark = pytest.mark.asyncio

async def test_extractor_extractor_id_get(client):
    """Test case for extractor_extractor_id_get

    Query by extractor endpoint, adhoc runs only.
    """
    params = [('url', 'url_example')]
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/extractor/{extractor_id}'.format(extractor_id='extractor_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

