# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.breadcrumbs_api_models_pathfinder_pathfinder_request import BreadcrumbsAPIModelsPathfinderPathfinderRequest
from openapi_server.models.breadcrumbs_api_models_pathfinder_pathfinder_response import BreadcrumbsAPIModelsPathfinderPathfinderResponse
from openapi_server.models.breadcrumbs_response_unauthorized_response import BreadcrumbsResponseUnauthorizedResponse
from openapi_server.models.breadcrumbs_response_unprocessable_response import BreadcrumbsResponseUnprocessableResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_pathfinder_post(client):
    """Test case for pathfinder_post

    Automatically find path between crypto addresses
    """
    body = openapi_server.BreadcrumbsAPIModelsPathfinderPathfinderRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'X-API-KEY': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/pathfinder',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

