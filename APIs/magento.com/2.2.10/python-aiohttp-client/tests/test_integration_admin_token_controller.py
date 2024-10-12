# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.integration_admin_token_service_v1_create_admin_access_token_post_request import IntegrationAdminTokenServiceV1CreateAdminAccessTokenPostRequest


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_integration_admin_token_service_v1_create_admin_access_token_post(client):
    """Test case for integration_admin_token_service_v1_create_admin_access_token_post

    integration/admin/token
    """
    body = openapi_server.IntegrationAdminTokenServiceV1CreateAdminAccessTokenPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/rest/default/V1/integration/admin/token',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

