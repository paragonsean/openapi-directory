# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.auth_keys import AuthKeys
from openapi_server.models.model_error_response import ModelErrorResponse
from openapi_server.models.regenerate_service_keys_request import RegenerateServiceKeysRequest


pytestmark = pytest.mark.asyncio

async def test_services_list_service_keys_0(client):
    """Test case for services_list_service_keys_0

    Lists Service keys.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/modelmanagement/v1.0/subscriptions/{subscription_id}/resourceGroups/{resource_group}/providers/Microsoft.MachineLearningServices/workspaces/{workspace}/services/{id}/listkeys'.format(subscription_id='subscription_id_example', resource_group='resource_group_example', workspace='workspace_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_services_regenerate_service_keys_0(client):
    """Test case for services_regenerate_service_keys_0

    Regenerate Service Keys.
    """
    request = {"keyValue":"keyValue","keyType":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/modelmanagement/v1.0/subscriptions/{subscription_id}/resourceGroups/{resource_group}/providers/Microsoft.MachineLearningServices/workspaces/{workspace}/services/{id}/regenerateKeys'.format(subscription_id='subscription_id_example', resource_group='resource_group_example', workspace='workspace_example', id='id_example'),
        headers=headers,
        json=request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

