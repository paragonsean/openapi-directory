# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_new_collaborator_request import AddNewCollaboratorRequest
from openapi_server.models.modify_inactive_collaborator import ModifyInactiveCollaborator
from openapi_server.models.problem_detail import ProblemDetail
from openapi_server.models.story_collaborator import StoryCollaborator


pytestmark = pytest.mark.asyncio

async def test_story_id_collaborators_get(client):
    """Test case for story_id_collaborators_get

    Story Collaborators: List
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/story/{id}/collaborators'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_story_id_collaborators_inactive_post(client):
    """Test case for story_id_collaborators_inactive_post

    Story Collaborators: Edit Inactive User Permission
    """
    body = openapi_server.ModifyInactiveCollaborator()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/story/{id}/collaborators/inactive'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_story_id_collaborators_post(client):
    """Test case for story_id_collaborators_post

    Story Collaborators: Add New User
    """
    body = openapi_server.AddNewCollaboratorRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/story/{id}/collaborators'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_story_id_collaborators_userid_delete(client):
    """Test case for story_id_collaborators_userid_delete

    Story Collaborators: Remove User
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/story/{id}/collaborators/{story_collaborator_userid}'.format(id='id_example', story_collaborator_userid='story_collaborator_userid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_story_id_collaborators_userid_get(client):
    """Test case for story_id_collaborators_userid_get

    Story Collaborators: Access Permissions
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/story/{id}/collaborators/{story_collaborator_userid}'.format(id='id_example', story_collaborator_userid='story_collaborator_userid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_story_id_collaborators_userid_put(client):
    """Test case for story_id_collaborators_userid_put

    Story Collaborators: Edit Access Rights
    """
    body = openapi_server.StoryCollaborator()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/story/{id}/collaborators/{story_collaborator_userid}'.format(id='id_example', story_collaborator_userid='story_collaborator_userid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

