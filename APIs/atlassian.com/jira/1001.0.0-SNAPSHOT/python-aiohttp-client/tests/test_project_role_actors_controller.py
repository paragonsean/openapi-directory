# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.actor_input_bean import ActorInputBean
from openapi_server.models.actors_map import ActorsMap
from openapi_server.models.project_role import ProjectRole
from openapi_server.models.project_role_actors_update_bean import ProjectRoleActorsUpdateBean


pytestmark = pytest.mark.asyncio

async def test_add_actor_users(client):
    """Test case for add_actor_users

    Add actors to project role
    """
    body = {"groupId":["groupId","groupId"],"user":["user","user"],"group":["group","group"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/rest/api/3/project/{project_id_or_key}/role/{id}'.format(project_id_or_key='project_id_or_key_example', id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_project_role_actors_to_role(client):
    """Test case for add_project_role_actors_to_role

    Add default actors to project role
    """
    body = {"groupId":["groupId","groupId"],"user":["user","user"],"group":["group","group"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/rest/api/3/role/{id}/actors'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_actor(client):
    """Test case for delete_actor

    Delete actors from project role
    """
    params = [('user', '5b10ac8d82e05b22cc7d4ef5'),
                    ('group', 'group_example'),
                    ('groupId', 'group_id_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/api/3/project/{project_id_or_key}/role/{id}'.format(project_id_or_key='project_id_or_key_example', id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_project_role_actors_from_role(client):
    """Test case for delete_project_role_actors_from_role

    Delete default actors from project role
    """
    params = [('user', '5b10ac8d82e05b22cc7d4ef5'),
                    ('groupId', 'group_id_example'),
                    ('group', 'group_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/api/3/role/{id}/actors'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_project_role_actors_for_role(client):
    """Test case for get_project_role_actors_for_role

    Get default actors for project role
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/role/{id}/actors'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_actors(client):
    """Test case for set_actors

    Set actors for project role
    """
    body = {"categorisedActors":{"key":["categorisedActors","categorisedActors"]},"id":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/rest/api/3/project/{project_id_or_key}/role/{id}'.format(project_id_or_key='project_id_or_key_example', id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

