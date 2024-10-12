# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.action_response import ActionResponse
from openapi_server.models.actions_response import ActionsResponse
from openapi_server.models.attach_volume_request import AttachVolumeRequest
from openapi_server.models.volumes_id_actions_change_protection_post_request import VolumesIdActionsChangeProtectionPostRequest
from openapi_server.models.volumes_id_actions_resize_post_request import VolumesIdActionsResizePostRequest


pytestmark = pytest.mark.asyncio

async def test_volumes_id_actions_action_id_get(client):
    """Test case for volumes_id_actions_action_id_get

    Get an Action for a Volume
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/volumes/{id}/actions/{action_id}'.format(id=56, action_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_volumes_id_actions_attach_post(client):
    """Test case for volumes_id_actions_attach_post

    Attach Volume to a Server
    """
    body = {"server":43,"automount":False}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/volumes/{id}/actions/attach'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_volumes_id_actions_change_protection_post(client):
    """Test case for volumes_id_actions_change_protection_post

    Change Volume Protection
    """
    body = openapi_server.VolumesIdActionsChangeProtectionPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/volumes/{id}/actions/change_protection'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_volumes_id_actions_detach_post(client):
    """Test case for volumes_id_actions_detach_post

    Detach Volume
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/volumes/{id}/actions/detach'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_volumes_id_actions_get(client):
    """Test case for volumes_id_actions_get

    Get all Actions for a Volume
    """
    params = [('sort', 'sort_example'),
                    ('status', 'status_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/volumes/{id}/actions'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_volumes_id_actions_resize_post(client):
    """Test case for volumes_id_actions_resize_post

    Resize Volume
    """
    body = openapi_server.VolumesIdActionsResizePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/volumes/{id}/actions/resize'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

