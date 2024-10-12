# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.edit_user_alt1_request import EditUserAlt1Request
from openapi_server.models.user import User


pytestmark = pytest.mark.asyncio

async def test_edit_user(client):
    """Test case for edit_user

    Edit a user
    """
    body = openapi_server.EditUserAlt1Request()
    headers = { 
        'Accept': 'application/vnd.vimeo.user+json',
        'Content-Type': 'application/vnd.vimeo.user+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/users/{user_id}'.format(user_id=152184),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_edit_user_alt1(client):
    """Test case for edit_user_alt1

    Edit a user
    """
    body = openapi_server.EditUserAlt1Request()
    headers = { 
        'Accept': 'application/vnd.vimeo.user+json',
        'Content-Type': 'application/vnd.vimeo.user+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/me',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_user(client):
    """Test case for get_user

    Get a user
    """
    headers = { 
        'Accept': 'application/vnd.vimeo.user+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/users/{user_id}'.format(user_id=152184),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_user_alt1(client):
    """Test case for get_user_alt1

    Get a user
    """
    headers = { 
        'Accept': 'application/vnd.vimeo.user+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/me',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

