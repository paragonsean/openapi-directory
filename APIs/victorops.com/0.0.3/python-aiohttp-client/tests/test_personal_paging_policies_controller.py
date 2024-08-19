# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_group_payload import AddGroupPayload
from openapi_server.models.add_step_payload import AddStepPayload
from openapi_server.models.api_public_v1_profile_username_policies_get200_response import ApiPublicV1ProfileUsernamePoliciesGet200Response
from openapi_server.models.api_public_v1_profile_username_policies_post200_response import ApiPublicV1ProfileUsernamePoliciesPost200Response
from openapi_server.models.api_public_v1_profile_username_policies_step_post200_response import ApiPublicV1ProfileUsernamePoliciesStepPost200Response


pytestmark = pytest.mark.asyncio

async def test_api_public_v1_profile_username_policies_get(client):
    """Test case for api_public_v1_profile_username_policies_get

    Get the user's paging policy
    """
    headers = { 
        'Accept': 'application/json',
        'x_vo_api_id': 'x_vo_api_id_example',
        'x_vo_api_key': 'x_vo_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api-public/v1/profile/{username}/policies'.format(username='username_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_api_public_v1_profile_username_policies_post(client):
    """Test case for api_public_v1_profile_username_policies_post

    Create a paging policy step
    """
    body = openapi_server.AddGroupPayload()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_vo_api_id': 'x_vo_api_id_example',
        'x_vo_api_key': 'x_vo_api_key_example',
    }
    response = await client.request(
        method='POST',
        path='/api-public/v1/profile/{username}/policies'.format(username='username_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_public_v1_profile_username_policies_step_get(client):
    """Test case for api_public_v1_profile_username_policies_step_get

    Get a paging policy step
    """
    headers = { 
        'Accept': 'application/json',
        'x_vo_api_id': 'x_vo_api_id_example',
        'x_vo_api_key': 'x_vo_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api-public/v1/profile/{username}/policies/{step}'.format(username='username_example', step=3.4),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_api_public_v1_profile_username_policies_step_post(client):
    """Test case for api_public_v1_profile_username_policies_step_post

    Create a rule for a paging policy step
    """
    body = openapi_server.AddStepPayload()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_vo_api_id': 'x_vo_api_id_example',
        'x_vo_api_key': 'x_vo_api_key_example',
    }
    response = await client.request(
        method='POST',
        path='/api-public/v1/profile/{username}/policies/{step}'.format(username='username_example', step=3.4),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_api_public_v1_profile_username_policies_step_put(client):
    """Test case for api_public_v1_profile_username_policies_step_put

    Update a paging policy step
    """
    body = openapi_server.AddGroupPayload()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_vo_api_id': 'x_vo_api_id_example',
        'x_vo_api_key': 'x_vo_api_key_example',
    }
    response = await client.request(
        method='PUT',
        path='/api-public/v1/profile/{username}/policies/{step}'.format(username='username_example', step=3.4),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_public_v1_profile_username_policies_step_rule_delete(client):
    """Test case for api_public_v1_profile_username_policies_step_rule_delete

    Delete a rule from a paging policy step
    """
    headers = { 
        'Accept': 'application/json',
        'x_vo_api_id': 'x_vo_api_id_example',
        'x_vo_api_key': 'x_vo_api_key_example',
    }
    response = await client.request(
        method='DELETE',
        path='/api-public/v1/profile/{username}/policies/{step}/{rule}'.format(username='username_example', step=3.4, rule=3.4),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_public_v1_profile_username_policies_step_rule_get(client):
    """Test case for api_public_v1_profile_username_policies_step_rule_get

    Get a rule from a paging policy step
    """
    headers = { 
        'Accept': 'application/json',
        'x_vo_api_id': 'x_vo_api_id_example',
        'x_vo_api_key': 'x_vo_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api-public/v1/profile/{username}/policies/{step}/{rule}'.format(username='username_example', step=3.4, rule=3.4),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_api_public_v1_profile_username_policies_step_rule_put(client):
    """Test case for api_public_v1_profile_username_policies_step_rule_put

    Update a rule for a paging policy step
    """
    body = openapi_server.AddStepPayload()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_vo_api_id': 'x_vo_api_id_example',
        'x_vo_api_key': 'x_vo_api_key_example',
    }
    response = await client.request(
        method='PUT',
        path='/api-public/v1/profile/{username}/policies/{step}/{rule}'.format(username='username_example', step=3.4, rule=3.4),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

