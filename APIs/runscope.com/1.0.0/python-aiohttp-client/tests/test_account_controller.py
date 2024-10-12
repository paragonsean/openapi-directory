# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.account import Account
from openapi_server.models.account_get200_response import AccountGet200Response
from openapi_server.models.agent import Agent
from openapi_server.models.error import Error
from openapi_server.models.teams_team_id_integrations_get200_response import TeamsTeamIdIntegrationsGet200Response


pytestmark = pytest.mark.asyncio

async def test_account_get(client):
    """Test case for account_get

    Account Resource
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/account',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_team_id_agents_get(client):
    """Test case for teams_team_id_agents_get

    Team agents list
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/teams/{team_id}/agents'.format(team_id='team_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_team_id_integrations_get(client):
    """Test case for teams_team_id_integrations_get

    Team integrations list
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/teams/{team_id}/integrations'.format(team_id='team_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_team_id_people_get(client):
    """Test case for teams_team_id_people_get

    Teams Resource
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/teams/{team_id}/people'.format(team_id='team_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

