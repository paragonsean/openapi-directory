# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_project_status_for_project_request import CreateProjectStatusForProjectRequest
from openapi_server.models.delete_attachment200_response import DeleteAttachment200Response
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.get_project_status200_response import GetProjectStatus200Response
from openapi_server.models.get_project_statuses_for_project200_response import GetProjectStatusesForProject200Response


pytestmark = pytest.mark.asyncio

async def test_create_project_status_for_project(client):
    """Test case for create_project_status_for_project

    Create a project status
    """
    body = openapi_server.CreateProjectStatusForProjectRequest()
    params = [('opt_pretty', true),
                    ('opt_fields', ['[\"followers\",\"assignee\"]'])]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/projects/{project_gid}/project_statuses'.format(project_gid='1331'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_project_status(client):
    """Test case for delete_project_status

    Delete a project status
    """
    params = [('opt_pretty', true),
                    ('opt_fields', ['[\"followers\",\"assignee\"]'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/1.0/project_statuses/{project_status_gid}'.format(project_status_gid='321654'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_project_status(client):
    """Test case for get_project_status

    Get a project status
    """
    params = [('opt_pretty', true),
                    ('opt_fields', ['[\"followers\",\"assignee\"]'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/1.0/project_statuses/{project_status_gid}'.format(project_status_gid='321654'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_project_statuses_for_project(client):
    """Test case for get_project_statuses_for_project

    Get statuses from a project
    """
    params = [('opt_pretty', true),
                    ('opt_fields', ['[\"followers\",\"assignee\"]']),
                    ('limit', 50),
                    ('offset', 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/1.0/projects/{project_gid}/project_statuses'.format(project_gid='1331'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

