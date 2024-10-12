# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_group200_response import CreateGroup200Response
from openapi_server.models.create_group_category200_response import CreateGroupCategory200Response
from openapi_server.models.delete_group200_response import DeleteGroup200Response
from openapi_server.models.delete_group_category200_response import DeleteGroupCategory200Response
from openapi_server.models.get_group_category_details200_response import GetGroupCategoryDetails200Response
from openapi_server.models.get_group_tree200_response import GetGroupTree200Response
from openapi_server.models.group_category import GroupCategory
from openapi_server.models.group_category_update import GroupCategoryUpdate
from openapi_server.models.group_details200_response import GroupDetails200Response
from openapi_server.models.group_new import GroupNew
from openapi_server.models.group_update import GroupUpdate
from openapi_server.models.list_groups200_response import ListGroups200Response
from openapi_server.models.reload_group200_response import ReloadGroup200Response
from openapi_server.models.update_group200_response import UpdateGroup200Response
from openapi_server.models.update_group_category200_response import UpdateGroupCategory200Response


pytestmark = pytest.mark.asyncio

async def test_create_group(client):
    """Test case for create_group

    Create a group
    """
    body = openapi_server.GroupNew()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/rudder/api/latest/groups',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_group_category(client):
    """Test case for create_group_category

    Create a group category
    """
    body = openapi_server.GroupCategory()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/rudder/api/latest/groups/categories',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_group(client):
    """Test case for delete_group

    Delete a group
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/rudder/api/latest/groups/{group_id}'.format(group_id='9a1773c9-0889-40b6-be89-f6504443ac1b'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_group_category(client):
    """Test case for delete_group_category

    Delete group category
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/rudder/api/latest/groups/categories/{group_category_id}'.format(group_category_id='e0a311fa-f7b2-4f9e-89a9-db517b9c6b90'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_group_category_details(client):
    """Test case for get_group_category_details

    Get group category details
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/rudder/api/latest/groups/categories/{group_category_id}'.format(group_category_id='e0a311fa-f7b2-4f9e-89a9-db517b9c6b90'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_group_tree(client):
    """Test case for get_group_tree

    Get groups tree
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/rudder/api/latest/groups/tree',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_group_details(client):
    """Test case for group_details

    Get group details
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/rudder/api/latest/groups/{group_id}'.format(group_id='9a1773c9-0889-40b6-be89-f6504443ac1b'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_groups(client):
    """Test case for list_groups

    List all groups
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/rudder/api/latest/groups',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reload_group(client):
    """Test case for reload_group

    Reload a group
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/rudder/api/latest/groups/{group_id}/reload'.format(group_id='9a1773c9-0889-40b6-be89-f6504443ac1b'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_group(client):
    """Test case for update_group

    Update group details
    """
    body = openapi_server.GroupUpdate()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/rudder/api/latest/groups/{group_id}'.format(group_id='9a1773c9-0889-40b6-be89-f6504443ac1b'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_group_category(client):
    """Test case for update_group_category

    Update group category details
    """
    body = openapi_server.GroupCategoryUpdate()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/rudder/api/latest/groups/categories/{group_category_id}'.format(group_category_id='e0a311fa-f7b2-4f9e-89a9-db517b9c6b90'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

