# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.check_get_default_response import CheckGetDefaultResponse
from openapi_server.models.user_plateform_username_get200_response import UserPlateformUsernameGet200Response


pytestmark = pytest.mark.asyncio

async def test_user_plateform_username_get(client):
    """Test case for user_plateform_username_get

    Get a user by username
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/user/{plateform}/{username}'.format(plateform='plateform_example', username='username_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

