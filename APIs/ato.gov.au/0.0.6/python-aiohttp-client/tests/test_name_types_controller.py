# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.name_type import NameType
from openapi_server.models.not_found import NotFound
from openapi_server.models.unauthenticated import Unauthenticated


pytestmark = pytest.mark.asyncio

async def test_classifications_name_types_get(client):
    """Test case for classifications_name_types_get

    Retrieve a list of name types
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/classifications/name-types',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

