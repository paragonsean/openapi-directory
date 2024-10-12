# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.doctor import Doctor
from openapi_server.models.doctors_list200_response import DoctorsList200Response
from openapi_server.models.user_groups_list200_response import UserGroupsList200Response
from openapi_server.models.user_profile import UserProfile
from openapi_server.models.user_profiles_group import UserProfilesGroup
from openapi_server.models.users_list200_response import UsersList200Response


pytestmark = pytest.mark.asyncio

async def test_doctors_list(client):
    """Test case for doctors_list

    
    """
    params = [('cursor', 'cursor_example'),
                    ('page_size', 56),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/doctors',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_doctors_read(client):
    """Test case for doctors_read

    
    """
    params = [('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/doctors/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_user_groups_list(client):
    """Test case for user_groups_list

    
    """
    params = [('cursor', 'cursor_example'),
                    ('page_size', 56),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/user_groups',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_user_groups_read(client):
    """Test case for user_groups_read

    
    """
    params = [('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/user_groups/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_list(client):
    """Test case for users_list

    
    """
    params = [('cursor', 'cursor_example'),
                    ('page_size', 56),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/users',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_read(client):
    """Test case for users_read

    
    """
    params = [('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/users/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

