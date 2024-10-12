# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_public_v1_overrides_get200_response import ApiPublicV1OverridesGet200Response
from openapi_server.models.api_public_v1_overrides_post200_response import ApiPublicV1OverridesPost200Response
from openapi_server.models.api_public_v1_overrides_public_id_get200_response import ApiPublicV1OverridesPublicIdGet200Response
from openapi_server.models.assignment import Assignment
from openapi_server.models.scheduled_override_payload import ScheduledOverridePayload
from openapi_server.models.update_assignment import UpdateAssignment


pytestmark = pytest.mark.asyncio

async def test_api_public_v1_overrides_get(client):
    """Test case for api_public_v1_overrides_get

    List the scheduled overrides
    """
    headers = { 
        'Accept': 'application/json',
        'x_vo_api_id': 'x_vo_api_id_example',
        'x_vo_api_key': 'x_vo_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api-public/v1/overrides',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_api_public_v1_overrides_post(client):
    """Test case for api_public_v1_overrides_post

    Creates a new scheduled override
    """
    body = openapi_server.ScheduledOverridePayload()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_vo_api_id': 'x_vo_api_id_example',
        'x_vo_api_key': 'x_vo_api_key_example',
    }
    response = await client.request(
        method='POST',
        path='/api-public/v1/overrides',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_public_v1_overrides_public_id_assignments_get(client):
    """Test case for api_public_v1_overrides_public_id_assignments_get

    Get the specified scheduled override
    """
    headers = { 
        'Accept': 'application/json',
        'x_vo_api_id': 'x_vo_api_id_example',
        'x_vo_api_key': 'x_vo_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api-public/v1/overrides/{public_id}/assignments'.format(public_id='public_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_public_v1_overrides_public_id_assignments_policy_slug_delete(client):
    """Test case for api_public_v1_overrides_public_id_assignments_policy_slug_delete

    Delete the scheduled override assignment
    """
    headers = { 
        'Accept': 'application/json',
        'x_vo_api_id': 'x_vo_api_id_example',
        'x_vo_api_key': 'x_vo_api_key_example',
    }
    response = await client.request(
        method='DELETE',
        path='/api-public/v1/overrides/{public_id}/assignments/{policy_slug}'.format(public_id='public_id_example', policy_slug='policy_slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_public_v1_overrides_public_id_assignments_policy_slug_get(client):
    """Test case for api_public_v1_overrides_public_id_assignments_policy_slug_get

    Get the specified scheduled override assignment
    """
    headers = { 
        'Accept': 'application/json',
        'x_vo_api_id': 'x_vo_api_id_example',
        'x_vo_api_key': 'x_vo_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api-public/v1/overrides/{public_id}/assignments/{policy_slug}'.format(public_id='public_id_example', policy_slug='policy_slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_api_public_v1_overrides_public_id_assignments_policy_slug_put(client):
    """Test case for api_public_v1_overrides_public_id_assignments_policy_slug_put

    Update the scheduled override assignment
    """
    body = openapi_server.UpdateAssignment()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_vo_api_id': 'x_vo_api_id_example',
        'x_vo_api_key': 'x_vo_api_key_example',
    }
    response = await client.request(
        method='PUT',
        path='/api-public/v1/overrides/{public_id}/assignments/{policy_slug}'.format(public_id='public_id_example', policy_slug='policy_slug_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_public_v1_overrides_public_id_delete(client):
    """Test case for api_public_v1_overrides_public_id_delete

    Deletes a scheduled override
    """
    headers = { 
        'x_vo_api_id': 'x_vo_api_id_example',
        'x_vo_api_key': 'x_vo_api_key_example',
    }
    response = await client.request(
        method='DELETE',
        path='/api-public/v1/overrides/{public_id}'.format(public_id='public_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_public_v1_overrides_public_id_get(client):
    """Test case for api_public_v1_overrides_public_id_get

    Get the specified scheduled override
    """
    headers = { 
        'Accept': 'application/json',
        'x_vo_api_id': 'x_vo_api_id_example',
        'x_vo_api_key': 'x_vo_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api-public/v1/overrides/{public_id}'.format(public_id='public_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

