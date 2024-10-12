# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.container_of_workflow_scheme_associations import ContainerOfWorkflowSchemeAssociations
from openapi_server.models.workflow_scheme_project_association import WorkflowSchemeProjectAssociation


pytestmark = pytest.mark.asyncio

async def test_assign_scheme_to_project(client):
    """Test case for assign_scheme_to_project

    Assign workflow scheme to project
    """
    body = {"workflowSchemeId":"workflowSchemeId","projectId":"projectId"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/rest/api/3/workflowscheme/project',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_workflow_scheme_project_associations(client):
    """Test case for get_workflow_scheme_project_associations

    Get workflow scheme project associations
    """
    params = [('projectId', [56])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/workflowscheme/project',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

