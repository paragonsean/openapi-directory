# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.affiliation import Affiliation
from openapi_server.models.error_document import ErrorDocument
from openapi_server.models.user_document import UserDocument


pytestmark = pytest.mark.asyncio

async def test_delete_user(client):
    """Test case for delete_user

    Delete the user's account
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/user',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_user(client):
    """Test case for get_user

    Get the latest state information about the logged-in user
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/user',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_inherit_from_temp_user(client):
    """Test case for inherit_from_temp_user

    Copy listening data from a temporary user account to the logged-in user's account
    """
    params = [('temp_user', 56)]
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/user/inherit',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_following(client):
    """Test case for post_following

    Update the following status of the logged-in user for a particular aggregation
    """
    body = {"notif_rated":["notif_rated","notif_rated"],"following":False,"notif_following":["notif_following","notif_following"],"rating":6.0274563,"href":"href","id":"id","title":"title","daysSinceLastListen":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/following',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_update_stations(client):
    """Test case for update_stations

    Update the logged-in user's favorite station(s)
    """
    body = [56]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v2/stations',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

