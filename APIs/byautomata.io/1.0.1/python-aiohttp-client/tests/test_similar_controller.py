# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.similar_get200_response import SimilarGet200Response


pytestmark = pytest.mark.asyncio

async def test_similar_get(client):
    """Test case for similar_get

    Send a company website to receive a list of companies related to them.
    """
    params = [('link', 'link_example'),
                    ('page', '0')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/similar',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

