# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.avatar import Avatar
from openapi_server.models.project_avatars import ProjectAvatars


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_create_project_avatar(client):
    """Test case for create_project_avatar

    Load project avatar
    """
    body = None
    params = [('x', 0),
                    ('y', 0),
                    ('size', 56)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/rest/api/3/project/{project_id_or_key}/avatar2'.format(project_id_or_key='project_id_or_key_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_project_avatar(client):
    """Test case for delete_project_avatar

    Delete project avatar
    """
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/api/3/project/{project_id_or_key}/avatar/{id}'.format(project_id_or_key='project_id_or_key_example', id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_project_avatars(client):
    """Test case for get_all_project_avatars

    Get all project avatars
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/project/{project_id_or_key}/avatars'.format(project_id_or_key='project_id_or_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_project_avatar(client):
    """Test case for update_project_avatar

    Set project avatar
    """
    body = {"isDeletable":True,"owner":"owner","fileName":"fileName","urls":{"key":"https://openapi-generator.tech"},"isSelected":True,"isSystemAvatar":True,"id":"id"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/rest/api/3/project/{project_id_or_key}/avatar'.format(project_id_or_key='project_id_or_key_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

