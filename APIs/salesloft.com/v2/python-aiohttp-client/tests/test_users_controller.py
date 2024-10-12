# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.user import User


pytestmark = pytest.mark.asyncio

async def test_v2_users_id_json_get(client):
    """Test case for v2_users_id_json_get

    Fetch a user
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/v2/users/{id_jso}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_v2_users_id_json_put(client):
    """Test case for v2_users_id_json_put

    Update a user
    """
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'active': True,
        'group_id': 56,
        'role_id': 'role_id_example',
        'work_country': 'work_country_example'
        }
    response = await client.request(
        method='PUT',
        path='/v2/users/{id_jso}'.format(id='id_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v2_users_json_get(client):
    """Test case for v2_users_json_get

    List users
    """
    params = [('ids', [56]),
                    ('guid', ['guid_example']),
                    ('group_id', ['group_id_example']),
                    ('role_id', ['role_id_example']),
                    ('search', 'search_example'),
                    ('active', True),
                    ('visible_only', True),
                    ('per_page', 56),
                    ('page', 56),
                    ('include_paging_counts', True),
                    ('has_crm_user', True),
                    ('work_country', ['work_country_example']),
                    ('sort_by', 'sort_by_example'),
                    ('sort_direction', 'sort_direction_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/v2/users.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

