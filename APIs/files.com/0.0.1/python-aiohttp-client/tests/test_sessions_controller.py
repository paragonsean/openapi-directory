# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.session_entity import SessionEntity


pytestmark = pytest.mark.asyncio

async def test_delete_sessions(client):
    """Test case for delete_sessions

    Delete user session (log out)
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/rest/v1/sessions',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_post_sessions(client):
    """Test case for post_sessions

    Create user session (log in)
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('otp', 'otp_example')
    data.add_field('partial_session_id', 'partial_session_id_example')
    data.add_field('password', 'password_example')
    data.add_field('username', 'username_example')
    response = await client.request(
        method='POST',
        path='/api/rest/v1/sessions',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

