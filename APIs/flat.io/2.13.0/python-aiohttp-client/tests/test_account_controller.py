# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.flat_error_response import FlatErrorResponse
from openapi_server.models.user_details import UserDetails


pytestmark = pytest.mark.asyncio

async def test_get_authenticated_user(client):
    """Test case for get_authenticated_user

    Get current user profile
    """
    params = [('onlyId', False)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/me',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

