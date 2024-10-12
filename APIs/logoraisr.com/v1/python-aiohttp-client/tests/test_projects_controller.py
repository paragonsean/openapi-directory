# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.project import Project
from openapi_server.models.project_request import ProjectRequest
from openapi_server.models.project_response import ProjectResponse


pytestmark = pytest.mark.asyncio

async def test_projects_create(client):
    """Test case for projects_create

    Create a new project.
    """
    body = {"process":{"rotate":28,"mirror":True,"processing_algorithm":"processing_algorithm","resize":"resize","flip":True,"crop":"crop"},"file_id":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","project_title":"project_title"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest-v1/projects/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_list(client):
    """Test case for projects_list

    Get user project list.
    """
    headers = { 
        'Accept': 'application/json',
        'Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-v1/projects/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_read(client):
    """Test case for projects_read

    Get project details.
    """
    headers = { 
        'Accept': 'application/json',
        'Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-v1/projects/{project_number}'.format(project_number='project_number_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

