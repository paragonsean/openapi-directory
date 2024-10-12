# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_current_user_throttle200_response import GetCurrentUserThrottle200Response
from openapi_server.models.user import User


pytestmark = pytest.mark.asyncio

async def test_current_user(client):
    """Test case for current_user

    Get information about the current user
    """
    headers = { 
        'Accept': 'application/json',
        'HeaderSignature': 'special-key',
        'QueryKey': 'special-key',
        'HeaderKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/user',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_current_user_throttle(client):
    """Test case for get_current_user_throttle

    Get the user's data rate limit and current activity level.
    """
    headers = { 
        'Accept': 'application/json',
        'HeaderSignature': 'special-key',
        'QueryKey': 'special-key',
        'HeaderKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/{username}/throttle'.format(username='username_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

