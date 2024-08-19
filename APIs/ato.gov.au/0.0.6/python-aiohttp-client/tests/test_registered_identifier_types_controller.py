# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.not_found import NotFound
from openapi_server.models.registered_identifier_type import RegisteredIdentifierType
from openapi_server.models.unauthenticated import Unauthenticated


pytestmark = pytest.mark.asyncio

async def test_classifications_registered_identifier_types_get(client):
    """Test case for classifications_registered_identifier_types_get

    Retrieve a list of registered identifier types
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/classifications/registered-identifier-types',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

