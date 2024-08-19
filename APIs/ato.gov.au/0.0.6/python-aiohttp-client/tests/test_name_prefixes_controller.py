# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.name_prefix import NamePrefix
from openapi_server.models.not_found import NotFound
from openapi_server.models.unauthenticated import Unauthenticated


pytestmark = pytest.mark.asyncio

async def test_classifications_name_prefixes_get(client):
    """Test case for classifications_name_prefixes_get

    Retrieve a list of name prefixes
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/classifications/name-prefixes',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

