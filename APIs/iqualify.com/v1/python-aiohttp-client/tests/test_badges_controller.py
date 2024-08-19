# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.awarded_response import AwardedResponse
from openapi_server.models.badge import Badge
from openapi_server.models.error import Error
from openapi_server.models.user_badge import UserBadge


pytestmark = pytest.mark.asyncio

async def test_offerings_offering_id_badges_get(client):
    """Test case for offerings_offering_id_badges_get

    Find offering badges
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/offerings/{offering_id}/badges'.format(offering_id='offering_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_offerings_offering_id_users_user_email_badges_award_post(client):
    """Test case for offerings_offering_id_users_user_email_badges_award_post

    Award badge
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/offerings/{offering_id}/users/{user_email}/badges/award'.format(offering_id='offering_id_example', user_email='user_email_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_user_email_badges_get(client):
    """Test case for users_user_email_badges_get

    Find user's badges
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/users/{user_email}/badges'.format(user_email='user_email_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

