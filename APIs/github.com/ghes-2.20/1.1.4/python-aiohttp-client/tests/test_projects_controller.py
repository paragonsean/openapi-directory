# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.apps_get_installation415_response import AppsGetInstallation415Response
from openapi_server.models.basic_error import BasicError
from openapi_server.models.orgs_update422_response import OrgsUpdate422Response
from openapi_server.models.project import Project
from openapi_server.models.project_card import ProjectCard
from openapi_server.models.project_column import ProjectColumn
from openapi_server.models.projects_add_collaborator_request import ProjectsAddCollaboratorRequest
from openapi_server.models.projects_create_card_request import ProjectsCreateCardRequest
from openapi_server.models.projects_create_for_authenticated_user_request import ProjectsCreateForAuthenticatedUserRequest
from openapi_server.models.projects_create_for_org_request import ProjectsCreateForOrgRequest
from openapi_server.models.projects_delete_card403_response import ProjectsDeleteCard403Response
from openapi_server.models.projects_move_card403_response import ProjectsMoveCard403Response
from openapi_server.models.projects_move_card503_response import ProjectsMoveCard503Response
from openapi_server.models.projects_move_card_request import ProjectsMoveCardRequest
from openapi_server.models.projects_move_column_request import ProjectsMoveColumnRequest
from openapi_server.models.projects_update_card_request import ProjectsUpdateCardRequest
from openapi_server.models.projects_update_column_request import ProjectsUpdateColumnRequest
from openapi_server.models.projects_update_request import ProjectsUpdateRequest
from openapi_server.models.repository_collaborator_permission import RepositoryCollaboratorPermission
from openapi_server.models.simple_user import SimpleUser
from openapi_server.models.validation_error import ValidationError
from openapi_server.models.validation_error_simple import ValidationErrorSimple


pytestmark = pytest.mark.asyncio

async def test_projects_add_collaborator(client):
    """Test case for projects_add_collaborator

    Add project collaborator
    """
    body = openapi_server.ProjectsAddCollaboratorRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/projects/{project_id}/collaborators/{username}'.format(project_id=56, username='username_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_create_card(client):
    """Test case for projects_create_card

    Create a project card
    """
    body = openapi_server.ProjectsCreateCardRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/projects/columns/{column_id}/cards'.format(column_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_create_column(client):
    """Test case for projects_create_column

    Create a project column
    """
    body = openapi_server.ProjectsUpdateColumnRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/projects/{project_id}/columns'.format(project_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_create_for_authenticated_user(client):
    """Test case for projects_create_for_authenticated_user

    Create a user project
    """
    body = openapi_server.ProjectsCreateForAuthenticatedUserRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/user/projects',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_create_for_org(client):
    """Test case for projects_create_for_org

    Create an organization project
    """
    body = {"body":"High-level roadmap for the upcoming year.","name":"Organization Roadmap"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/orgs/{org}/projects'.format(org='org_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_create_for_repo(client):
    """Test case for projects_create_for_repo

    Create a repository project
    """
    body = {"body":"Developer documentation project for the developer site.","name":"Projects Documentation"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/repos/{owner}/{repo}/projects'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_delete(client):
    """Test case for projects_delete

    Delete a project
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/projects/{project_id}'.format(project_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_delete_card(client):
    """Test case for projects_delete_card

    Delete a project card
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/projects/columns/cards/{card_id}'.format(card_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_delete_column(client):
    """Test case for projects_delete_column

    Delete a project column
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/projects/columns/{column_id}'.format(column_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_get(client):
    """Test case for projects_get

    Get a project
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{project_id}'.format(project_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_get_card(client):
    """Test case for projects_get_card

    Get a project card
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/columns/cards/{card_id}'.format(card_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_get_column(client):
    """Test case for projects_get_column

    Get a project column
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/columns/{column_id}'.format(column_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_get_permission_for_user(client):
    """Test case for projects_get_permission_for_user

    Get project permission for a user
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{project_id}/collaborators/{username}/permission'.format(project_id=56, username='username_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_list_cards(client):
    """Test case for projects_list_cards

    List project cards
    """
    params = [('archived_state', not_archived),
                    ('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/columns/{column_id}/cards'.format(column_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_list_collaborators(client):
    """Test case for projects_list_collaborators

    List project collaborators
    """
    params = [('affiliation', all),
                    ('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{project_id}/collaborators'.format(project_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_list_columns(client):
    """Test case for projects_list_columns

    List project columns
    """
    params = [('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{project_id}/columns'.format(project_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_list_for_org(client):
    """Test case for projects_list_for_org

    List organization projects
    """
    params = [('state', open),
                    ('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/orgs/{org}/projects'.format(org='org_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_list_for_repo(client):
    """Test case for projects_list_for_repo

    List repository projects
    """
    params = [('state', open),
                    ('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/projects'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_list_for_user(client):
    """Test case for projects_list_for_user

    List user projects
    """
    params = [('state', open),
                    ('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/users/{username}/projects'.format(username='username_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_move_card(client):
    """Test case for projects_move_card

    Move a project card
    """
    body = openapi_server.ProjectsMoveCardRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/projects/columns/cards/{card_id}/moves'.format(card_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_move_column(client):
    """Test case for projects_move_column

    Move a project column
    """
    body = openapi_server.ProjectsMoveColumnRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/projects/columns/{column_id}/moves'.format(column_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_remove_collaborator(client):
    """Test case for projects_remove_collaborator

    Remove user as a collaborator
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/projects/{project_id}/collaborators/{username}'.format(project_id=56, username='username_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_update(client):
    """Test case for projects_update

    Update a project
    """
    body = openapi_server.ProjectsUpdateRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/projects/{project_id}'.format(project_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_update_card(client):
    """Test case for projects_update_card

    Update an existing project card
    """
    body = openapi_server.ProjectsUpdateCardRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/projects/columns/cards/{card_id}'.format(card_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_update_column(client):
    """Test case for projects_update_column

    Update an existing project column
    """
    body = openapi_server.ProjectsUpdateColumnRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/projects/columns/{column_id}'.format(column_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

