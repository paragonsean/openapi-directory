# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.user_request_entity import UserRequestEntity


pytestmark = pytest.mark.asyncio

async def test_delete_user_requests_id(client):
    """Test case for delete_user_requests_id

    Delete User Request
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/rest/v1/user_requests/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_user_requests(client):
    """Test case for get_user_requests

    List User Requests
    """
    params = [('cursor', 'cursor_example'),
                    ('per_page', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/user_requests',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_user_requests_id(client):
    """Test case for get_user_requests_id

    Show User Request
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/user_requests/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_post_user_requests(client):
    """Test case for post_user_requests

    Create User Request
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('details', 'details_example')
    data.add_field('email', 'email_example')
    data.add_field('name', 'name_example')
    response = await client.request(
        method='POST',
        path='/api/rest/v1/user_requests',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

