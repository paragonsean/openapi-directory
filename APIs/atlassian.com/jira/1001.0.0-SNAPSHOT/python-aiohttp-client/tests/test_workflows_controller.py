# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_workflow_details import CreateWorkflowDetails
from openapi_server.models.deprecated_workflow import DeprecatedWorkflow
from openapi_server.models.error_collection import ErrorCollection
from openapi_server.models.page_bean_workflow import PageBeanWorkflow
from openapi_server.models.workflow_ids import WorkflowIDs


pytestmark = pytest.mark.asyncio

async def test_create_workflow(client):
    """Test case for create_workflow

    Create workflow
    """
    body = {"name":"name","description":"description","statuses":[{"id":"id","properties":{"key":"properties"}},{"id":"id","properties":{"key":"properties"}}],"transitions":[{"name":"name","description":"description","screen":"","from":["from","from"],"rules":"","to":"to","type":"global","properties":{"key":"properties"}},{"name":"name","description":"description","screen":"","from":["from","from"],"rules":"","to":"to","type":"global","properties":{"key":"properties"}}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/rest/api/3/workflow',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_inactive_workflow(client):
    """Test case for delete_inactive_workflow

    Delete inactive workflow
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/api/3/workflow/{entity_id}'.format(entity_id='entity_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_workflows(client):
    """Test case for get_all_workflows

    Get all workflows
    """
    params = [('workflowName', 'workflow_name_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/workflow',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_workflows_paginated(client):
    """Test case for get_workflows_paginated

    Get workflows paginated
    """
    params = [('startAt', 0),
                    ('maxResults', 50),
                    ('workflowName', ['workflow_name_example']),
                    ('expand', 'expand_example'),
                    ('queryString', 'query_string_example'),
                    ('orderBy', 'order_by_example'),
                    ('isActive', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/workflow/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

