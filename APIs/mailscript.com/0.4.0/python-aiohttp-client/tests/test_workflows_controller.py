# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_workflow_request import AddWorkflowRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.get_all_workflows_response import GetAllWorkflowsResponse
from openapi_server.models.set_workflow_request import SetWorkflowRequest


pytestmark = pytest.mark.asyncio

async def test_add_workflow(client):
    """Test case for add_workflow

    Setup workflow
    """
    body = {"input":"input","name":"name","action":"action","active":True,"trigger":"trigger"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/workflows',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_workflow(client):
    """Test case for delete_workflow

    Delete a workflow
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/workflows/{workflow}'.format(workflow='workflow_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_workflows(client):
    """Test case for get_all_workflows

    Get all workflows you have access to
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/workflows',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_workflow(client):
    """Test case for set_workflow

    Set a property on a workflow
    """
    body = {"id":"id","pairs":[{"value":"value","key":"key"},{"value":"value","key":"key"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/workflows/set',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_workflow(client):
    """Test case for update_workflow

    Update an workflow
    """
    body = {"input":"input","name":"name","action":"action","active":True,"trigger":"trigger"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v2/workflows/{workflow}'.format(workflow='workflow_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

