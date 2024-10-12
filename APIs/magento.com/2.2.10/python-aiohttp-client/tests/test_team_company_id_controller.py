# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.company_team_repository_v1_create_post_request import CompanyTeamRepositoryV1CreatePostRequest
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_company_team_repository_v1_create_post(client):
    """Test case for company_team_repository_v1_create_post

    team/{companyId}
    """
    body = openapi_server.CompanyTeamRepositoryV1CreatePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/rest/default/V1/team/{company_id}'.format(company_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

