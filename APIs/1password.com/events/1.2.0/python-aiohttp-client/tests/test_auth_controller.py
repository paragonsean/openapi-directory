# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.introspection import Introspection
from openapi_server.models.introspection_v2 import IntrospectionV2


pytestmark = pytest.mark.asyncio

async def test_get_auth_introspect(client):
    """Test case for get_auth_introspect

    Performs introspection of the provided Bearer JWT token
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/auth/introspect',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_auth_introspect_v2(client):
    """Test case for get_auth_introspect_v2

    Performs introspection of the provided Bearer JWT token
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/auth/introspect',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

