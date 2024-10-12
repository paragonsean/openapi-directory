# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.user_dto import UserDTO


pytestmark = pytest.mark.asyncio

async def test_user_get(client):
    """Test case for user_get

    Get all Users detail This will return all properties related to User entity             
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/User',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_user_register_user(client):
    """Test case for user_register_user

    Register a new User             
    """
    params = [('UserId', 56),
                    ('AccountNumber', 'account_number_example'),
                    ('GymNumber', 'gym_number_example'),
                    ('ExternalEntityNumber', 'external_entity_number_example'),
                    ('Name', 'name_example'),
                    ('Number', 'number_example'),
                    ('IntroduceBy', 56),
                    ('Guardian', 56),
                    ('TypeId', 56)]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/User/registerUser',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_user_update_user(client):
    """Test case for user_update_user

    Update an exsisting User             
    """
    params = [('UserId', 56),
                    ('AccountNumber', 'account_number_example'),
                    ('GymNumber', 'gym_number_example'),
                    ('ExternalEntityNumber', 'external_entity_number_example'),
                    ('Name', 'name_example'),
                    ('Number', 'number_example'),
                    ('IntroduceBy', 56),
                    ('Guardian', 56),
                    ('TypeId', 56)]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/User/updateuser',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

