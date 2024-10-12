# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData
from aiohttp import FormData
from aiohttp import FormData

from openapi_server.models.collaborator import Collaborator
from openapi_server.models.collaborator_data import CollaboratorData
from openapi_server.models.collaborator_error import CollaboratorError
from openapi_server.models.deployment import Deployment
from openapi_server.models.deployment_data import DeploymentData
from openapi_server.models.deployment_error import DeploymentError
from openapi_server.models.jwt import JWT
from openapi_server.models.not_found import NotFound
from openapi_server.models.project import Project
from openapi_server.models.project_copy_check_request import ProjectCopyCheckRequest
from openapi_server.models.project_copy_request import ProjectCopyRequest
from openapi_server.models.project_data import ProjectData
from openapi_server.models.project_error import ProjectError
from openapi_server.models.project_file import ProjectFile
from openapi_server.models.project_file_error import ProjectFileError
from openapi_server.models.server import Server
from openapi_server.models.server_action import ServerAction
from openapi_server.models.server_action_data import ServerActionData
from openapi_server.models.server_action_error import ServerActionError
from openapi_server.models.server_data import ServerData
from openapi_server.models.server_error import ServerError
from openapi_server.models.server_run_statistics import ServerRunStatistics
from openapi_server.models.server_run_statistics_data import ServerRunStatisticsData
from openapi_server.models.server_run_statistics_error import ServerRunStatisticsError
from openapi_server.models.server_statistics import ServerStatistics
from openapi_server.models.server_statistics_data import ServerStatisticsData
from openapi_server.models.server_statistics_error import ServerStatisticsError
from openapi_server.models.server_status import ServerStatus
from openapi_server.models.ssh_tunnel import SshTunnel
from openapi_server.models.ssh_tunnel_data import SshTunnelData
from openapi_server.models.ssh_tunnel_error import SshTunnelError


pytestmark = pytest.mark.asyncio

async def test_project_copy(client):
    """Test case for project_copy

    Copy a project to your own account.
    """
    project_copy_data = openapi_server.ProjectCopyRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{namespace}/projects/project-copy'.format(namespace='namespace_example'),
        headers=headers,
        json=project_copy_data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_copy_check(client):
    """Test case for project_copy_check

    Check if you are able to copy a project to your account.
    """
    project_copy_data = openapi_server.ProjectCopyCheckRequest()
    headers = { 
        'Content-Type': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='HEAD',
        path='/v1/{namespace}/projects/project-copy-check'.format(namespace='namespace_example'),
        headers=headers,
        json=project_copy_data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_collaborators_create(client):
    """Test case for projects_collaborators_create

    Create project collaborators
    """
    collaborator_data = {"owner":True,"permissions":"read_project","member":"member"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{namespace}/projects/{project}/collaborators'.format(project='project_example', namespace='namespace_example'),
        headers=headers,
        json=collaborator_data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_collaborators_delete(client):
    """Test case for projects_collaborators_delete

    Delete a project collaborator
    """
    headers = { 
        'Accept': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/{namespace}/projects/{project}/collaborators/{collaborator}'.format(project='project_example', namespace='namespace_example', collaborator='collaborator_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_collaborators_list(client):
    """Test case for projects_collaborators_list

    Get project collaborators
    """
    params = [('limit', 'limit_example'),
                    ('offset', 'offset_example'),
                    ('ordering', 'ordering_example')]
    headers = { 
        'Accept': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{namespace}/projects/{project}/collaborators'.format(project='project_example', namespace='namespace_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_collaborators_read(client):
    """Test case for projects_collaborators_read

    Get a project collaborator
    """
    headers = { 
        'Accept': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{namespace}/projects/{project}/collaborators/{collaborator}'.format(project='project_example', namespace='namespace_example', collaborator='collaborator_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_collaborators_update(client):
    """Test case for projects_collaborators_update

    Update project collaborator
    """
    collaborator_data = {"owner":True,"permissions":"read_project","member":"member"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/{namespace}/projects/{project}/collaborators/{collaborator}'.format(project='project_example', namespace='namespace_example', collaborator='collaborator_example'),
        headers=headers,
        json=collaborator_data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_create(client):
    """Test case for projects_create

    Create a new project
    """
    project_data = {"private":True,"name":"name","description":"description"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{namespace}/projects'.format(namespace='namespace_example'),
        headers=headers,
        json=project_data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_delete(client):
    """Test case for projects_delete

    Delete a project
    """
    headers = { 
        'Accept': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/{namespace}/projects/{project}'.format(namespace='namespace_example', project='project_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_deployment_delete(client):
    """Test case for projects_deployment_delete

    Delete a deployment
    """
    headers = { 
        'Accept': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/{namespace}/projects/{project}/deployments/{deployment}'.format(project='project_example', namespace='namespace_example', deployment='deployment_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_deployments_create(client):
    """Test case for projects_deployments_create

    Create a new deployment
    """
    deployment_data = {"framework":"tensorflow","name":"name","runtime":"python2.7","config":{"handler":"handler","files":["files","files"]}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{namespace}/projects/{project}/deployments'.format(project='project_example', namespace='namespace_example'),
        headers=headers,
        json=deployment_data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_deployments_deploy(client):
    """Test case for projects_deployments_deploy

    Deploy an existing model
    """
    headers = { 
        'jwt': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{namespace}/projects/{project}/deployments/{deployment}/deploy'.format(project='project_example', namespace='namespace_example', deployment='deployment_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_deployments_list(client):
    """Test case for projects_deployments_list

    Retrieve deployments
    """
    params = [('limit', 'limit_example'),
                    ('offset', 'offset_example'),
                    ('name', 'name_example'),
                    ('ordering', 'ordering_example')]
    headers = { 
        'Accept': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{namespace}/projects/{project}/deployments'.format(project='project_example', namespace='namespace_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_deployments_read(client):
    """Test case for projects_deployments_read

    Retrieve a deployment
    """
    headers = { 
        'Accept': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{namespace}/projects/{project}/deployments/{deployment}'.format(project='project_example', namespace='namespace_example', deployment='deployment_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_deployments_replace(client):
    """Test case for projects_deployments_replace

    Replace a deployment
    """
    deployment_data = {"framework":"tensorflow","name":"name","runtime":"python2.7","config":{"handler":"handler","files":["files","files"]}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/{namespace}/projects/{project}/deployments/{deployment}'.format(project='project_example', namespace='namespace_example', deployment='deployment_example'),
        headers=headers,
        json=deployment_data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_deployments_update(client):
    """Test case for projects_deployments_update

    Update a deployment
    """
    deployment_data = {"framework":"tensorflow","name":"name","runtime":"python2.7","config":{"handler":"handler","files":["files","files"]}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/{namespace}/projects/{project}/deployments/{deployment}'.format(project='project_example', namespace='namespace_example', deployment='deployment_example'),
        headers=headers,
        json=deployment_data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_list(client):
    """Test case for projects_list

    Get available projects
    """
    params = [('limit', 'limit_example'),
                    ('offset', 'offset_example'),
                    ('private', 'private_example'),
                    ('name', 'name_example'),
                    ('ordering', 'ordering_example')]
    headers = { 
        'Accept': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{namespace}/projects'.format(namespace='namespace_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_projects_project_files_create(client):
    """Test case for projects_project_files_create

    Create project files
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'jwt': 'special-key',
    }
    data = FormData()
    data.add_field('file', '/path/to/file')
    data.add_field('base64_data', 'base64_data_example')
    data.add_field('name', 'name_example')
    data.add_field('path', 'path_example')
    response = await client.request(
        method='POST',
        path='/v1/{namespace}/projects/{project}/project_files'.format(project='project_example', namespace='namespace_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_project_files_delete(client):
    """Test case for projects_project_files_delete

    Delete a project file
    """
    headers = { 
        'Accept': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/{namespace}/projects/{project}/project_files/{id}'.format(project='project_example', namespace='namespace_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_project_files_list(client):
    """Test case for projects_project_files_list

    Get project files
    """
    params = [('limit', 'limit_example'),
                    ('offset', 'offset_example'),
                    ('ordering', 'ordering_example'),
                    ('filename', 'filename_example'),
                    ('content', 'content_example')]
    headers = { 
        'Accept': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{namespace}/projects/{project}/project_files'.format(project='project_example', namespace='namespace_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_project_files_read(client):
    """Test case for projects_project_files_read

    Get a project file
    """
    params = [('content', 'content_example')]
    headers = { 
        'Accept': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{namespace}/projects/{project}/project_files/{id}'.format(project='project_example', namespace='namespace_example', id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_projects_project_files_replace(client):
    """Test case for projects_project_files_replace

    Replace a project file
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'jwt': 'special-key',
    }
    data = FormData()
    data.add_field('file', '/path/to/file')
    data.add_field('base64_data', 'base64_data_example')
    data.add_field('name', 'name_example')
    data.add_field('path', 'path_example')
    response = await client.request(
        method='PUT',
        path='/v1/{namespace}/projects/{project}/project_files/{id}'.format(project='project_example', namespace='namespace_example', id='id_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_projects_project_files_update(client):
    """Test case for projects_project_files_update

    Update a project file
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'jwt': 'special-key',
    }
    data = FormData()
    data.add_field('file', '/path/to/file')
    data.add_field('base64_data', 'base64_data_example')
    data.add_field('name', 'name_example')
    data.add_field('path', 'path_example')
    response = await client.request(
        method='PATCH',
        path='/v1/{namespace}/projects/{project}/project_files/{id}'.format(project='project_example', namespace='namespace_example', id='id_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_read(client):
    """Test case for projects_read

    Get a project
    """
    headers = { 
        'Accept': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{namespace}/projects/{project}'.format(namespace='namespace_example', project='project_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_replace(client):
    """Test case for projects_replace

    Replace a project
    """
    project_data = {"private":True,"name":"name","description":"description"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/{namespace}/projects/{project}'.format(namespace='namespace_example', project='project_example'),
        headers=headers,
        json=project_data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_servers_api_key(client):
    """Test case for projects_servers_api_key

    Get server API key
    """
    headers = { 
        'Accept': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{namespace}/projects/{project}/servers/{server}/api-key'.format(project='project_example', namespace='namespace_example', server='server_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_servers_auth(client):
    """Test case for projects_servers_auth

    Server api key validation
    """
    headers = { 
        'jwt': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{namespace}/projects/{project}/servers/{server}/auth'.format(project='project_example', namespace='namespace_example', server='server_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_servers_create(client):
    """Test case for projects_servers_create

    Create a new server
    """
    server_data = {"connected":["connected","connected"],"image_name":"image_name","startup_script":"startup_script","server_size":"server_size","host":"host","name":"name","config":{"function":"function","type":"jupyter","command":"command","script":"script"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{namespace}/projects/{project}/servers'.format(project='project_example', namespace='namespace_example'),
        headers=headers,
        json=server_data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_servers_delete(client):
    """Test case for projects_servers_delete

    Delete a server
    """
    headers = { 
        'Accept': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/{namespace}/projects/{project}/servers/{server}'.format(project='project_example', namespace='namespace_example', server='server_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_servers_list(client):
    """Test case for projects_servers_list

    Retrieve servers
    """
    params = [('limit', 'limit_example'),
                    ('offset', 'offset_example'),
                    ('name', 'name_example'),
                    ('ordering', 'ordering_example')]
    headers = { 
        'Accept': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{namespace}/projects/{project}/servers'.format(project='project_example', namespace='namespace_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_servers_read(client):
    """Test case for projects_servers_read

    Retrieve a server
    """
    headers = { 
        'Accept': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{namespace}/projects/{project}/servers/{server}'.format(project='project_example', namespace='namespace_example', server='server_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_servers_replace(client):
    """Test case for projects_servers_replace

    Replace a server
    """
    server_data = {"connected":["connected","connected"],"image_name":"image_name","startup_script":"startup_script","server_size":"server_size","host":"host","name":"name","config":{"function":"function","type":"jupyter","command":"command","script":"script"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/{namespace}/projects/{project}/servers/{server}'.format(project='project_example', namespace='namespace_example', server='server_example'),
        headers=headers,
        json=server_data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_servers_run_stats_create(client):
    """Test case for projects_servers_run_stats_create

    Create a new server's run statistics
    """
    serverrunstats_data = {"size":6,"stacktrace":"stacktrace","stop":"stop","exit_code":0,"start":"start"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{namespace}/projects/{project}/servers/{server}/run-stats'.format(server='server_example', project='project_example', namespace='namespace_example'),
        headers=headers,
        json=serverrunstats_data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_servers_run_stats_delete(client):
    """Test case for projects_servers_run_stats_delete

    Delete a server's statistics
    """
    headers = { 
        'Accept': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/{namespace}/projects/{project}/servers/{server}/run-stats/{id}'.format(server='server_example', project='project_example', namespace='namespace_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_servers_run_stats_read(client):
    """Test case for projects_servers_run_stats_read

    Retrieve statistics for a server
    """
    headers = { 
        'Accept': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{namespace}/projects/{project}/servers/{server}/run-stats/{id}'.format(server='server_example', project='project_example', namespace='namespace_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_servers_run_stats_replace(client):
    """Test case for projects_servers_run_stats_replace

    Replace a server's statistics
    """
    serverrunstats_data = {"size":6,"stacktrace":"stacktrace","stop":"stop","exit_code":0,"start":"start"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/{namespace}/projects/{project}/servers/{server}/run-stats/{id}'.format(server='server_example', project='project_example', namespace='namespace_example', id='id_example'),
        headers=headers,
        json=serverrunstats_data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_servers_run_stats_update(client):
    """Test case for projects_servers_run_stats_update

    Update a server's statistics
    """
    serverrunstats_data = {"size":6,"stacktrace":"stacktrace","stop":"stop","exit_code":0,"start":"start"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/{namespace}/projects/{project}/servers/{server}/run-stats/{id}'.format(server='server_example', project='project_example', namespace='namespace_example', id='id_example'),
        headers=headers,
        json=serverrunstats_data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_servers_ssh_tunnels_create(client):
    """Test case for projects_servers_ssh_tunnels_create

    Create SSH Tunnel associated to a server
    """
    sshtunnel_data = {"endpoint":"endpoint","local_port":0,"host":"host","name":"name","remote_port":6,"username":"username"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{namespace}/projects/{project}/servers/{server}/ssh-tunnels'.format(server='server_example', project='project_example', namespace='namespace_example'),
        headers=headers,
        json=sshtunnel_data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_servers_ssh_tunnels_delete(client):
    """Test case for projects_servers_ssh_tunnels_delete

    Delete an SSH Tunnel associated to a server
    """
    headers = { 
        'Accept': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/{namespace}/projects/{project}/servers/{server}/ssh-tunnels/{tunnel}'.format(server='server_example', project='project_example', namespace='namespace_example', tunnel='tunnel_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_servers_ssh_tunnels_list(client):
    """Test case for projects_servers_ssh_tunnels_list

    Get SSH Tunnels associated to a server
    """
    params = [('limit', 'limit_example'),
                    ('offset', 'offset_example'),
                    ('ordering', 'ordering_example')]
    headers = { 
        'Accept': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{namespace}/projects/{project}/servers/{server}/ssh-tunnels'.format(server='server_example', project='project_example', namespace='namespace_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_servers_ssh_tunnels_read(client):
    """Test case for projects_servers_ssh_tunnels_read

    Get an SSH Tunnel associated to a server
    """
    headers = { 
        'Accept': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{namespace}/projects/{project}/servers/{server}/ssh-tunnels/{tunnel}'.format(server='server_example', project='project_example', namespace='namespace_example', tunnel='tunnel_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_servers_ssh_tunnels_replace(client):
    """Test case for projects_servers_ssh_tunnels_replace

    Replace SSH Tunnel associated to a server
    """
    sshtunnel_data = {"endpoint":"endpoint","local_port":0,"host":"host","name":"name","remote_port":6,"username":"username"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/{namespace}/projects/{project}/servers/{server}/ssh-tunnels/{tunnel}'.format(server='server_example', project='project_example', namespace='namespace_example', tunnel='tunnel_example'),
        headers=headers,
        json=sshtunnel_data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_servers_ssh_tunnels_update(client):
    """Test case for projects_servers_ssh_tunnels_update

    Update an SSH Tunnel associated to a server
    """
    sshtunnel_data = {"endpoint":"endpoint","local_port":0,"host":"host","name":"name","remote_port":6,"username":"username"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/{namespace}/projects/{project}/servers/{server}/ssh-tunnels/{tunnel}'.format(server='server_example', project='project_example', namespace='namespace_example', tunnel='tunnel_example'),
        headers=headers,
        json=sshtunnel_data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_servers_start(client):
    """Test case for projects_servers_start

    Start a server
    """
    headers = { 
        'jwt': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{namespace}/projects/{project}/servers/{server}/start'.format(project='project_example', namespace='namespace_example', server='server_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_servers_stats_delete(client):
    """Test case for projects_servers_stats_delete

    Delete a server's statistics
    """
    headers = { 
        'Accept': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/{namespace}/projects/{project}/servers/{server}/stats/{id}'.format(server='server_example', project='project_example', namespace='namespace_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_servers_stats_read(client):
    """Test case for projects_servers_stats_read

    Retrieve a server's statistics
    """
    headers = { 
        'Accept': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{namespace}/projects/{project}/servers/{server}/stats/{id}'.format(server='server_example', project='project_example', namespace='namespace_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_servers_stats_replace(client):
    """Test case for projects_servers_stats_replace

    Replace a server's statistics
    """
    serverstats_data = {"size":["size","size"],"stop":["stop","stop"],"non_field_errors":["non_field_errors","non_field_errors"],"start":["start","start"],"id":["id","id"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/{namespace}/projects/{project}/servers/{server}/stats/{id}'.format(server='server_example', project='project_example', namespace='namespace_example', id='id_example'),
        headers=headers,
        json=serverstats_data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_servers_stats_update(client):
    """Test case for projects_servers_stats_update

    Update a server's statistics
    """
    serverstats_data = {"size":["size","size"],"stop":["stop","stop"],"non_field_errors":["non_field_errors","non_field_errors"],"start":["start","start"],"id":["id","id"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/{namespace}/projects/{project}/servers/{server}/stats/{id}'.format(server='server_example', project='project_example', namespace='namespace_example', id='id_example'),
        headers=headers,
        json=serverstats_data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_servers_statuses(client):
    """Test case for projects_servers_statuses

    Retrieve server statuses
    """
    headers = { 
        'Accept': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{namespace}/projects/{project}/servers/statuses'.format(project='project_example', namespace='namespace_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_servers_stop(client):
    """Test case for projects_servers_stop

    Stop a server
    """
    headers = { 
        'jwt': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{namespace}/projects/{project}/servers/{server}/stop'.format(project='project_example', namespace='namespace_example', server='server_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_servers_update(client):
    """Test case for projects_servers_update

    Update a server
    """
    server_data = {"connected":["connected","connected"],"image_name":"image_name","startup_script":"startup_script","server_size":"server_size","host":"host","name":"name","config":{"function":"function","type":"jupyter","command":"command","script":"script"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/{namespace}/projects/{project}/servers/{server}'.format(project='project_example', namespace='namespace_example', server='server_example'),
        headers=headers,
        json=server_data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_update(client):
    """Test case for projects_update

    Update a project
    """
    project_data = {"private":True,"name":"name","description":"description"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/{namespace}/projects/{project}'.format(namespace='namespace_example', project='project_example'),
        headers=headers,
        json=project_data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_service_trigger_create(client):
    """Test case for service_trigger_create

    Create a new server trigger
    """
    server_action = {"webhook":{"payload":"{}","url":"url"},"name":"name","operation":"start"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{namespace}/projects/{project}/servers/{server}/triggers'.format(server='server_example', project='project_example', namespace='namespace_example'),
        headers=headers,
        json=server_action,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_service_trigger_delete(client):
    """Test case for service_trigger_delete

    Delete a server trigger
    """
    headers = { 
        'Accept': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/{namespace}/projects/{project}/servers/{server}/triggers/{trigger}'.format(server='server_example', project='project_example', namespace='namespace_example', trigger='trigger_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_service_trigger_list(client):
    """Test case for service_trigger_list

    Retrieve server triggers
    """
    params = [('name', 'name_example'),
                    ('limit', 'limit_example'),
                    ('offset', 'offset_example'),
                    ('ordering', 'ordering_example')]
    headers = { 
        'Accept': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{namespace}/projects/{project}/servers/{server}/triggers'.format(server='server_example', project='project_example', namespace='namespace_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_service_trigger_read(client):
    """Test case for service_trigger_read

    Get a server trigger
    """
    headers = { 
        'Accept': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{namespace}/projects/{project}/servers/{server}/triggers/{trigger}'.format(server='server_example', project='project_example', namespace='namespace_example', trigger='trigger_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_service_trigger_replace(client):
    """Test case for service_trigger_replace

    Replace a server trigger
    """
    server_action = {"webhook":{"payload":"{}","url":"url"},"name":"name","operation":"start"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/{namespace}/projects/{project}/servers/{server}/triggers/{trigger}'.format(server='server_example', project='project_example', namespace='namespace_example', trigger='trigger_example'),
        headers=headers,
        json=server_action,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_service_trigger_update(client):
    """Test case for service_trigger_update

    Update a server trigger
    """
    server_action = {"webhook":{"payload":"{}","url":"url"},"name":"name","operation":"start"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/{namespace}/projects/{project}/servers/{server}/triggers/{trigger}'.format(server='server_example', project='project_example', namespace='namespace_example', trigger='trigger_example'),
        headers=headers,
        json=server_action,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

