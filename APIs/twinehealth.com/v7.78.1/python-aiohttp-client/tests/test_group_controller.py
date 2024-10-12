# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_group_request import CreateGroupRequest
from openapi_server.models.create_group_response import CreateGroupResponse
from openapi_server.models.create_or_update_error_response import CreateOrUpdateErrorResponse
from openapi_server.models.fetch_error_response import FetchErrorResponse
from openapi_server.models.fetch_group_response import FetchGroupResponse
from openapi_server.models.fetch_groups_response import FetchGroupsResponse


pytestmark = pytest.mark.asyncio

async def test_create_group(client):
    """Test case for create_group

    Create a group
    """
    body = openapi_server.CreateGroupRequest()
    headers = { 
        'Accept': 'application/vnd.api+json',
        'Content-Type': 'application/vnd.api+json',
    }
    response = await client.request(
        method='POST',
        path='/pub/group',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_group(client):
    """Test case for fetch_group

    Get a group
    """
    headers = { 
        'Accept': 'application/vnd.api+json',
    }
    response = await client.request(
        method='GET',
        path='/pub/group/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_groups(client):
    """Test case for fetch_groups

    List groups
    """
    params = [('filter[organization]', 'filter_organization_example'),
                    ('filter[name]', 'filter_name_example')]
    headers = { 
        'Accept': 'application/vnd.api+json',
    }
    response = await client.request(
        method='GET',
        path='/pub/group',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

