# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.commitment import Commitment
from openapi_server.models.commitment_request import CommitmentRequest
from openapi_server.models.user import User


pytestmark = pytest.mark.asyncio

async def test_users_post(client):
    """Test case for users_post

    Create a User
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/users',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_users_user_id_commitments_post(client):
    """Test case for users_user_id_commitments_post

    Assign points to a User
    """
    commitment_request = openapi_server.CommitmentRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/users/{user_id}/commitments'.format(user_id='user_id_example'),
        headers=headers,
        json=commitment_request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

