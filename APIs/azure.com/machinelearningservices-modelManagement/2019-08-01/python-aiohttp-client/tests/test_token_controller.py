# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.auth_token import AuthToken
from openapi_server.models.model_error_response import ModelErrorResponse


pytestmark = pytest.mark.asyncio

async def test_services_get_service_token_0(client):
    """Test case for services_get_service_token_0

    Generate Service Access Token.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/modelmanagement/v1.0/subscriptions/{subscription_id}/resourceGroups/{resource_group}/providers/Microsoft.MachineLearningServices/workspaces/{workspace}/services/{id}/token'.format(subscription_id='subscription_id_example', resource_group='resource_group_example', workspace='workspace_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

