# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.escalation_policy_info_list import EscalationPolicyInfoList
from openapi_server.models.escalation_policy_list import EscalationPolicyList


pytestmark = pytest.mark.asyncio

async def test_api_public_v1_policies_get(client):
    """Test case for api_public_v1_policies_get

    Get escalation policy info
    """
    headers = { 
        'Accept': 'application/json',
        'x_vo_api_id': 'x_vo_api_id_example',
        'x_vo_api_key': 'x_vo_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api-public/v1/policies',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_public_v1_team_team_policies_get(client):
    """Test case for api_public_v1_team_team_policies_get

    Retrieve a list of escalation policies for a team
    """
    headers = { 
        'Accept': 'application/json',
        'x_vo_api_id': 'x_vo_api_id_example',
        'x_vo_api_key': 'x_vo_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api-public/v1/team/{team}/policies'.format(team='team_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

