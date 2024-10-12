# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.company_data_team_interface import CompanyDataTeamInterface
from openapi_server.models.company_team_repository_v1_create_post_request import CompanyTeamRepositoryV1CreatePostRequest
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_company_team_repository_v1_delete_by_id_delete(client):
    """Test case for company_team_repository_v1_delete_by_id_delete

    team/{teamId}
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/default/V1/team/{team_id}'.format(team_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_company_team_repository_v1_get_get(client):
    """Test case for company_team_repository_v1_get_get

    team/{teamId}
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/default/V1/team/{team_id}'.format(team_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_company_team_repository_v1_save_put(client):
    """Test case for company_team_repository_v1_save_put

    team/{teamId}
    """
    body = openapi_server.CompanyTeamRepositoryV1CreatePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/rest/default/V1/team/{team_id}'.format(team_id='team_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

