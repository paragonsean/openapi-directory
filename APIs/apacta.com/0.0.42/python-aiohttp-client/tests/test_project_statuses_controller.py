# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bad_request_response import BadRequestResponse
from openapi_server.models.bulk_action_request_body import BulkActionRequestBody
from openapi_server.models.create_success_response import CreateSuccessResponse
from openapi_server.models.empty_success_response import EmptySuccessResponse
from openapi_server.models.error_not_found import ErrorNotFound
from openapi_server.models.error_validation import ErrorValidation
from openapi_server.models.forbidden_error import ForbiddenError
from openapi_server.models.project_statuses_get200_response import ProjectStatusesGet200Response
from openapi_server.models.project_statuses_post_request import ProjectStatusesPostRequest
from openapi_server.models.project_statuses_project_status_id_get200_response import ProjectStatusesProjectStatusIdGet200Response
from openapi_server.models.projects_has_projects_with_custom_statuses_get200_response import ProjectsHasProjectsWithCustomStatusesGet200Response


pytestmark = pytest.mark.asyncio

async def test_project_statuses_bulk_delete_delete(client):
    """Test case for project_statuses_bulk_delete_delete

    Bulk delete project statuses
    """
    body = {"id":["id","id"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/project_statuses/bulkDelete',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_statuses_get(client):
    """Test case for project_statuses_get

    Get list of project statuses
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/project_statuses',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_statuses_post(client):
    """Test case for project_statuses_post

    Create a new project status
    """
    body = openapi_server.ProjectStatusesPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/project_statuses',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_statuses_project_status_id_delete(client):
    """Test case for project_statuses_project_status_id_delete

    Delete a project status
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/project_statuses/{project_status_id}'.format(project_status_id='project_status_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_statuses_project_status_id_get(client):
    """Test case for project_statuses_project_status_id_get

    Get a single project status
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/project_statuses/{project_status_id}'.format(project_status_id='project_status_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_statuses_project_status_id_put(client):
    """Test case for project_statuses_project_status_id_put

    Edit a project status
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/project_statuses/{project_status_id}'.format(project_status_id='project_status_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_has_projects_with_custom_statuses_get(client):
    """Test case for projects_has_projects_with_custom_statuses_get

    Check if the company has projects with custom statuses
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/projects/has_projects_with_custom_statuses',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

