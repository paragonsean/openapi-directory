# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.customer_data_group_interface import CustomerDataGroupInterface
from openapi_server.models.customer_group_repository_v1_save_post_request import CustomerGroupRepositoryV1SavePostRequest
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_customer_group_repository_v1_save_post(client):
    """Test case for customer_group_repository_v1_save_post

    customerGroups
    """
    body = openapi_server.CustomerGroupRepositoryV1SavePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/rest/default/V1/customerGroups',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

