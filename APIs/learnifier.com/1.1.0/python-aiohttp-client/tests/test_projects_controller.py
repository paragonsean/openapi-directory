# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.activation_error import ActivationError
from openapi_server.models.add_participant import AddParticipant
from openapi_server.models.add_project import AddProject
from openapi_server.models.error import Error
from openapi_server.models.login_link import LoginLink
from openapi_server.models.participation import Participation
from openapi_server.models.project import Project
from openapi_server.models.project_team_member import ProjectTeamMember
from openapi_server.models.update_project import UpdateProject


pytestmark = pytest.mark.asyncio

async def test_extproject_get(client):
    """Test case for extproject_get

    Gets Organization Unit by external id
    """
    params = [('extid', 'extid_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/extproject',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_orgunits_orgid_projects_get(client):
    """Test case for orgunits_orgid_projects_get

    Organization Unit Projects
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/orgunits/{orgid}/projects'.format(orgid=3.4),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_orgunits_orgid_projects_post(client):
    """Test case for orgunits_orgid_projects_post

    Create project
    """
    body = openapi_server.AddProject()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/orgunits/{orgid}/projects'.format(orgid=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_orgunits_orgid_projects_projectid_delete(client):
    """Test case for orgunits_orgid_projects_projectid_delete

    Deletes the project
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/orgunits/{orgid}/projects/{projectid}'.format(orgid=56, projectid=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_orgunits_orgid_projects_projectid_get(client):
    """Test case for orgunits_orgid_projects_projectid_get

    Project information
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/orgunits/{orgid}/projects/{projectid}'.format(orgid=56, projectid=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_orgunits_orgid_projects_projectid_participants_get(client):
    """Test case for orgunits_orgid_projects_projectid_participants_get

    Project participants
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/orgunits/{orgid}/projects/{projectid}/participants'.format(orgid=56, projectid=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_orgunits_orgid_projects_projectid_participants_participant_id_activate_post(client):
    """Test case for orgunits_orgid_projects_projectid_participants_participant_id_activate_post

    Activate participant
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/orgunits/{orgid}/projects/{projectid}/participants/${participantId}/activate'.format(orgid=56, projectid=56, participant_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_orgunits_orgid_projects_projectid_participants_participant_id_delete(client):
    """Test case for orgunits_orgid_projects_projectid_participants_participant_id_delete

    Deletes a participant
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/orgunits/{orgid}/projects/{projectid}/participants/${participantId}'.format(orgid=56, projectid=56, participant_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_orgunits_orgid_projects_projectid_participants_participant_id_loginlink_post(client):
    """Test case for orgunits_orgid_projects_projectid_participants_participant_id_loginlink_post

    Participant login link
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/orgunits/{orgid}/projects/{projectid}/participants/${participantId}/loginlink'.format(orgid=56, projectid=56, participant_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_orgunits_orgid_projects_projectid_participants_post(client):
    """Test case for orgunits_orgid_projects_projectid_participants_post

    Add participant
    """
    body = openapi_server.AddParticipant()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/orgunits/{orgid}/projects/{projectid}/participants'.format(orgid=56, projectid=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_orgunits_orgid_projects_projectid_patch(client):
    """Test case for orgunits_orgid_projects_projectid_patch

    Update project information
    """
    body = openapi_server.UpdateProject()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/orgunits/{orgid}/projects/{projectid}'.format(orgid=56, projectid=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_orgunits_orgid_projects_projectid_teammembers_get(client):
    """Test case for orgunits_orgid_projects_projectid_teammembers_get

    Project team members
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/orgunits/{orgid}/projects/{projectid}/teammembers'.format(orgid=56, projectid=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

