# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.async_operation_status import AsyncOperationStatus
from openapi_server.models.model_error_response import ModelErrorResponse


pytestmark = pytest.mark.asyncio

async def test_operations_get(client):
    """Test case for operations_get

    Get the status of an async operation.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/modelmanagement/v1.0/subscriptions/{subscription_id}/resourceGroups/{resource_group}/providers/Microsoft.MachineLearningServices/workspaces/{workspace}/operations/{id}'.format(subscription_id='subscription_id_example', resource_group='resource_group_example', workspace='workspace_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

