# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_models_api_error import APIModelsApiError
from openapi_server.models.api_paged_response_update_system_models_bundle import APIPagedResponseUpdateSystemModelsBundle
from openapi_server.models.api_paged_response_update_system_models_update_group import APIPagedResponseUpdateSystemModelsUpdateGroup
from openapi_server.models.update_system_models_update_group import UpdateSystemModelsUpdateGroup


pytestmark = pytest.mark.asyncio

async def test_api_v2_update_groups_idget(client):
    """Test case for api_v2_update_groups_idget

    Get a specific Update Group by ID.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/UpdateGroups/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_groups_add_update_group_user(client):
    """Test case for update_groups_add_update_group_user

    Add an updateGroup that a user can see.
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/UpdateGroups/{id}/Users/{user_id}'.format(id='id_example', user_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_groups_delete(client):
    """Test case for update_groups_delete

    Delete an Update Group.
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/UpdateGroups/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_groups_get(client):
    """Test case for update_groups_get

    Get a list of Update Groups.  Update Groups are used by the client to register for a specific type of update.
    """
    params = [('limit', 56),
                    ('offset', 56),
                    ('userID', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/UpdateGroups',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_groups_get_update_group_bundles(client):
    """Test case for update_groups_get_update_group_bundles

    Get a list of bundles for UpdateGroup.
    """
    params = [('IncludeInactive', True),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/UpdateGroups/{id}/Bundles'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_update_groups_post(client):
    """Test case for update_groups_post

    Add a new Update Group.  The report field is a string that has a dot based request for a specific piece of submitted data.
    """
    body = openapi_server.UpdateSystemModelsUpdateGroup()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/UpdateGroups',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_update_groups_put(client):
    """Test case for update_groups_put

    Modify an Update Group.
    """
    body = openapi_server.UpdateSystemModelsUpdateGroup()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v2/UpdateGroups/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_groups_remove_update_group_user(client):
    """Test case for update_groups_remove_update_group_user

    Deletes an update group a user could see.
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/UpdateGroups/{id}/Users/{user_id}'.format(id='id_example', user_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

