# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.activity_pub import ActivityPub


pytestmark = pytest.mark.asyncio

async def test_activitypub_person(client):
    """Test case for activitypub_person

    Returns the Person actor for a user
    """
    headers = { 
        'Accept': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/activitypub/user-id/{user_id}'.format(user_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_activitypub_person_inbox(client):
    """Test case for activitypub_person_inbox

    Send to the inbox
    """
    headers = { 
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/activitypub/user-id/{user_id}/inbox'.format(user_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

