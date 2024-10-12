# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_realm_attack_detection_brute_force_users_delete(client):
    """Test case for realm_attack_detection_brute_force_users_delete

    Clear any user login failures for all users   This can release temporary disabled users
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/{realm}/attack-detection/brute-force/users'.format(realm='realm_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_attack_detection_brute_force_users_user_id_delete(client):
    """Test case for realm_attack_detection_brute_force_users_user_id_delete

    Clear any user login failures for the user   This can release temporary disabled user
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/{realm}/attack-detection/brute-force/users/{user_id}'.format(realm='realm_example', user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_attack_detection_brute_force_users_user_id_get(client):
    """Test case for realm_attack_detection_brute_force_users_user_id_get

    Get status of a username in brute force detection
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/attack-detection/brute-force/users/{user_id}'.format(realm='realm_example', user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

