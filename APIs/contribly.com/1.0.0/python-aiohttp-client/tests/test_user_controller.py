# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.linked_profile import LinkedProfile
from openapi_server.models.user import User


pytestmark = pytest.mark.asyncio

async def test_users_get(client):
    """Test case for users_get

    List users
    """
    params = [('assignment', 'assignment_example'),
                    ('country', 'country_example'),
                    ('minimumContributions', 3.4),
                    ('linkedProfile', 'linked_profile_example'),
                    ('ownedBy', 'owned_by_example'),
                    ('submittedBefore', '2013-10-20T19:20:30+01:00'),
                    ('submittedAfter', '2013-10-20T19:20:30+01:00'),
                    ('username', 'username_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/1/users',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_id_get(client):
    """Test case for users_id_get

    Retrieve a single user by id
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/1/users/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_id_linked_type_get(client):
    """Test case for users_id_linked_type_get

    Retrieve a users linked profile by type
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/1/users/{id}/linked/{type}'.format(id='id_example', type='type_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

