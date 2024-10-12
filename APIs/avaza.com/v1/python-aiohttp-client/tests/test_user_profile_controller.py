# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.user_list import UserList


pytestmark = pytest.mark.asyncio

async def test_user_profile_get(client):
    """Test case for user_profile_get

    Get Collection of Users who have roles in the current Avaza account.
    """
    params = [('Roles', 'roles_example'),
                    ('Tags', 'tags_example'),
                    ('CurrentUserOnly', True),
                    ('CompanyIDFK', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/UserProfile',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

