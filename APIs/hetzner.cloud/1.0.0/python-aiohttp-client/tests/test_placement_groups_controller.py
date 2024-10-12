# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_placement_group_request import CreatePlacementGroupRequest
from openapi_server.models.create_placement_group_response import CreatePlacementGroupResponse
from openapi_server.models.placement_group_response import PlacementGroupResponse
from openapi_server.models.placement_groups_response import PlacementGroupsResponse
from openapi_server.models.update_placement_group_request import UpdatePlacementGroupRequest


pytestmark = pytest.mark.asyncio

async def test_placement_groups_get(client):
    """Test case for placement_groups_get

    Get all PlacementGroups
    """
    params = [('sort', 'sort_example'),
                    ('name', 'name_example'),
                    ('label_selector', 'label_selector_example'),
                    ('type', 'type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/placement_groups',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_placement_groups_id_delete(client):
    """Test case for placement_groups_id_delete

    Delete a PlacementGroup
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v1/placement_groups/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_placement_groups_id_get(client):
    """Test case for placement_groups_id_get

    Get a PlacementGroup
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/placement_groups/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_placement_groups_id_put(client):
    """Test case for placement_groups_id_put

    Update a PlacementGroup
    """
    body = {"name":"my Placement Group","labels":{"labelkey":"value"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v1/placement_groups/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_placement_groups_post(client):
    """Test case for placement_groups_post

    Create a PlacementGroup
    """
    body = {"name":"my Placement Group","type":"spread","labels":"{}"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/placement_groups',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

