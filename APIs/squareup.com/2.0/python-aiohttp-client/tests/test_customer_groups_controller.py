# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_customer_group_request import CreateCustomerGroupRequest
from openapi_server.models.create_customer_group_response import CreateCustomerGroupResponse
from openapi_server.models.delete_customer_group_response import DeleteCustomerGroupResponse
from openapi_server.models.list_customer_groups_response import ListCustomerGroupsResponse
from openapi_server.models.retrieve_customer_group_response import RetrieveCustomerGroupResponse
from openapi_server.models.update_customer_group_request import UpdateCustomerGroupRequest
from openapi_server.models.update_customer_group_response import UpdateCustomerGroupResponse


pytestmark = pytest.mark.asyncio

async def test_create_customer_group(client):
    """Test case for create_customer_group

    CreateCustomerGroup
    """
    body = {"request_body":{"group":{"name":"Loyal Customers"}}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/customers/groups',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_customer_group(client):
    """Test case for delete_customer_group

    DeleteCustomerGroup
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/customers/groups/{group_id}'.format(group_id='group_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_customer_groups(client):
    """Test case for list_customer_groups

    ListCustomerGroups
    """
    params = [('cursor', 'cursor_example'),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/customers/groups',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_customer_group(client):
    """Test case for retrieve_customer_group

    RetrieveCustomerGroup
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/customers/groups/{group_id}'.format(group_id='group_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_customer_group(client):
    """Test case for update_customer_group

    UpdateCustomerGroup
    """
    body = {"request_body":{"group":{"name":"Loyal Customers"}}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v2/customers/groups/{group_id}'.format(group_id='group_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

