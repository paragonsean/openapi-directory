# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.operation import Operation
from openapi_server.models.project_details import ProjectDetails
from openapi_server.models.project_list import ProjectList


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-yaml not supported by Connexion")
async def test_add_project(client):
    """Test case for add_project

    Add a project to LGTM
    """
    body = {"extraction":{"java":{"index":{"build_command":"./build.sh"}}}}
    params = [('repository', 'repository_example'),
                    ('language', ['language_example']),
                    ('mode', 'mode_example'),
                    ('commit', 'commit_example'),
                    ('date', '2013-10-20T19:20:30+01:00'),
                    ('worker-label', ['worker_label_example'])]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-yaml',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1.0/projects',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_project(client):
    """Test case for delete_project

    Delete project by numeric identifier
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1.0/projects/{project_id}'.format(project_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_project(client):
    """Test case for get_project

    Get project by numeric identifier
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1.0/projects/{project_id}'.format(project_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_project_by_url_identifier(client):
    """Test case for get_project_by_url_identifier

    Get project by URL identifier
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1.0/projects/{provider}/{org}/{name}'.format(provider='provider_example', org='org_example', name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_project_config(client):
    """Test case for get_project_config

    Get configuration for a project identified by numeric identifier
    """
    params = [('source', 'source_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1.0/projects/{project_id}/settings/analysis-configuration'.format(project_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_projects(client):
    """Test case for get_projects

    List projects
    """
    params = [('limit', 100),
                    ('start', 'start_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1.0/projects',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-yaml not supported by Connexion")
async def test_set_project_config(client):
    """Test case for set_project_config

    Set the administrator configuration for a project identified by numeric identifier
    """
    body = 'body_example'
    headers = { 
        'Accept': 'application/x-yaml',
        'Content-Type': 'application/x-yaml',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1.0/projects/{project_id}/settings/analysis-configuration'.format(project_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

