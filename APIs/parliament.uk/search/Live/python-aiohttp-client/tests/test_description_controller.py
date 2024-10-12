# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_description_get(client):
    """Test case for description_get

    OpenSearch description document
    """
    headers = { 
        'Accept': 'application/opensearchdescription+xml',
    }
    response = await client.request(
        method='GET',
        path='/search/description',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

