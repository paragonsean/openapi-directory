# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.breadcrumbs_api_models_sanction_sanctioned_request import BreadcrumbsAPIModelsSanctionSanctionedRequest
from openapi_server.models.breadcrumbs_api_models_sanction_sanctioned_response import BreadcrumbsAPIModelsSanctionSanctionedResponse
from openapi_server.models.breadcrumbs_response_unauthorized_response import BreadcrumbsResponseUnauthorizedResponse
from openapi_server.models.breadcrumbs_response_unprocessable_response import BreadcrumbsResponseUnprocessableResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sanctioned_address_post(client):
    """Test case for sanctioned_address_post

    Verify if the addresses provided are in our sanctioned lists
    """
    body = [openapi_server.BreadcrumbsAPIModelsSanctionSanctionedRequest()]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'X-API-KEY': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/sanctioned_address',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

