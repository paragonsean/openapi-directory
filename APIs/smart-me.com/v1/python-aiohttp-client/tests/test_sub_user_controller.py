# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.sub_user_data import SubUserData


pytestmark = pytest.mark.asyncio

async def test_sub_user_delete(client):
    """Test case for sub_user_delete

    Delete a subuser
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/SubUser/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sub_user_get(client):
    """Test case for sub_user_get

    Get a sub user. The user must be assigend to the user that makes this call.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/SubUser/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sub_user_post(client):
    """Test case for sub_user_post

    Creates or updates a subuser.              To create a new user set no ID (empty)
    """
    body = {"NewPassword":"NewPassword","Email":"Email","Username":"Username","AccessEndDate":"2000-01-23T04:56:07.000+00:00","Id":"Id","PermissionLevel":"SelectedFolderAndSubfoldersMeters","AccessTimeStartDate":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/SubUser',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

