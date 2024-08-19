# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.breadcrumbs_api_models_node_node_request import BreadcrumbsAPIModelsNodeNodeRequest
from openapi_server.models.breadcrumbs_api_models_node_node_response import BreadcrumbsAPIModelsNodeNodeResponse
from openapi_server.models.breadcrumbs_response_unauthorized_response import BreadcrumbsResponseUnauthorizedResponse
from openapi_server.models.breadcrumbs_response_unprocessable_response import BreadcrumbsResponseUnprocessableResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_node_post(client):
    """Test case for node_post

    Shows the incoming and outgoing transactions from blockchain address
    """
    body = openapi_server.BreadcrumbsAPIModelsNodeNodeRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'X-API-KEY': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/node',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

