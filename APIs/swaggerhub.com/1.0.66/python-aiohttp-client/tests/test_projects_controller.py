# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.project import Project
from openapi_server.models.project_member_list import ProjectMemberList
from openapi_server.models.projects_json import ProjectsJson


pytestmark = pytest.mark.asyncio

async def test_add_spec_to_project_v2(client):
    """Test case for add_spec_to_project_v2

    Add an API or domain to a project
    """
    headers = { 
        'TokenSecured': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/projects/{owner}/{project_id}/{spec_type}/{name}'.format(owner='owner_example', project_id='project_id_example', spec_type='spec_type_example', name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_create_project(client):
    """Test case for create_project

    Create a project in an organization
    """
    project_request = openapi_server.Project()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'TokenSecured': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/projects/{owner}'.format(owner='owner_example'),
        headers=headers,
        json=project_request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_project_v2(client):
    """Test case for delete_project_v2

    Delete a project
    """
    headers = { 
        'TokenSecured': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/projects/{owner}/{project_id}'.format(owner='owner_example', project_id='project_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_org_projects_v2(client):
    """Test case for get_org_projects_v2

    Get all projects of an organization
    """
    params = [('nameOnly', False),
                    ('page', 0),
                    ('limit', 10),
                    ('order', ASC)]
    headers = { 
        'Accept': 'application/json',
        'TokenSecured': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/projects/{owner}'.format(owner='owner_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_project_members_v2(client):
    """Test case for get_project_members_v2

    Get project members
    """
    headers = { 
        'Accept': 'application/json',
        'TokenSecured': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/projects/{owner}/{project_id}/members'.format(owner='owner_example', project_id='project_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_project_v2(client):
    """Test case for get_project_v2

    Get project information
    """
    headers = { 
        'Accept': 'application/json',
        'TokenSecured': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/projects/{owner}/{project_id}'.format(owner='owner_example', project_id='project_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_user_projects(client):
    """Test case for get_user_projects

    Get all projects that a user has access to
    """
    params = [('nameOnly', False),
                    ('page', 0),
                    ('limit', 10),
                    ('sort', NAME),
                    ('order', ASC)]
    headers = { 
        'Accept': 'application/json',
        'TokenSecured': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/projects',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_save_project_v2(client):
    """Test case for save_project_v2

    Update a project
    """
    project_request = openapi_server.Project()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'TokenSecured': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/projects/{owner}/{project_id}'.format(owner='owner_example', project_id='project_id_example'),
        headers=headers,
        json=project_request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_project_members_v2(client):
    """Test case for update_project_members_v2

    Update a project's members list
    """
    project_member_list = {"members":[{"name":"alex","type":"USER"},{"name":"core-developers","type":"TEAM"}]}
    headers = { 
        'Content-Type': 'application/json',
        'TokenSecured': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/projects/{owner}/{project_id}/members'.format(owner='owner_example', project_id='project_id_example'),
        headers=headers,
        json=project_member_list,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

