# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_public_v1_oncall_current_get200_response import ApiPublicV1OncallCurrentGet200Response
from openapi_server.models.on_call_and_overrides import OnCallAndOverrides
from openapi_server.models.take_request import TakeRequest
from openapi_server.models.take_result import TakeResult
from openapi_server.models.team_schedule import TeamSchedule
from openapi_server.models.user_schedule import UserSchedule


pytestmark = pytest.mark.asyncio

async def test_api_public_v1_oncall_current_get(client):
    """Test case for api_public_v1_oncall_current_get

    Get an organization's on-call users
    """
    headers = { 
        'Accept': 'application/json',
        'x_vo_api_id': 'x_vo_api_id_example',
        'x_vo_api_key': 'x_vo_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api-public/v1/oncall/current',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_api_public_v1_policies_policy_oncall_user_patch(client):
    """Test case for api_public_v1_policies_policy_oncall_user_patch

    Create an on-call override (take on-call)
    """
    body = openapi_server.TakeRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_vo_api_id': 'x_vo_api_id_example',
        'x_vo_api_key': 'x_vo_api_key_example',
    }
    response = await client.request(
        method='PATCH',
        path='/api-public/v1/policies/{policy}/oncall/user'.format(policy='policy_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_public_v1_team_team_oncall_schedule_get(client):
    """Test case for api_public_v1_team_team_oncall_schedule_get

    Get a team's on-call schedule
    """
    params = [('daysForward', 14.0),
                    ('daysSkip', 0.0),
                    ('step', 0.0)]
    headers = { 
        'Accept': 'application/json',
        'x_vo_api_id': 'x_vo_api_id_example',
        'x_vo_api_key': 'x_vo_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api-public/v1/team/{team}/oncall/schedule'.format(team='team_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_api_public_v1_team_team_oncall_user_patch(client):
    """Test case for api_public_v1_team_team_oncall_user_patch

    Create an on-call override (take on-call)
    """
    body = openapi_server.TakeRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_vo_api_id': 'x_vo_api_id_example',
        'x_vo_api_key': 'x_vo_api_key_example',
    }
    response = await client.request(
        method='PATCH',
        path='/api-public/v1/team/{team}/oncall/user'.format(team='team_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_public_v1_user_user_oncall_schedule_get(client):
    """Test case for api_public_v1_user_user_oncall_schedule_get

    Get a user's on-call schedule
    """
    params = [('daysForward', 14.0),
                    ('daysSkip', 0.0),
                    ('step', 0.0)]
    headers = { 
        'Accept': 'application/json',
        'x_vo_api_id': 'x_vo_api_id_example',
        'x_vo_api_key': 'x_vo_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api-public/v1/user/{user}/oncall/schedule'.format(user='user_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_public_v2_team_team_oncall_schedule_get(client):
    """Test case for api_public_v2_team_team_oncall_schedule_get

    Get a team's on-call schedule
    """
    params = [('daysForward', 14.0),
                    ('daysSkip', 0.0),
                    ('step', 0.0)]
    headers = { 
        'Accept': 'application/json',
        'x_vo_api_id': 'x_vo_api_id_example',
        'x_vo_api_key': 'x_vo_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api-public/v2/team/{team}/oncall/schedule'.format(team='team_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_public_v2_user_user_oncall_schedule_get(client):
    """Test case for api_public_v2_user_user_oncall_schedule_get

    Get a user's on-call schedule
    """
    params = [('daysForward', 14.0),
                    ('daysSkip', 0.0),
                    ('step', 0.0)]
    headers = { 
        'Accept': 'application/json',
        'x_vo_api_id': 'x_vo_api_id_example',
        'x_vo_api_key': 'x_vo_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api-public/v2/user/{user}/oncall/schedule'.format(user='user_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

