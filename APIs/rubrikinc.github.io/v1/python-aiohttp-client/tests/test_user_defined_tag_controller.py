# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.resource_tag_definition import ResourceTagDefinition
from openapi_server.models.resource_tag_delete_response import ResourceTagDeleteResponse
from openapi_server.models.resource_tag_detail import ResourceTagDetail
from openapi_server.models.resource_tag_get_response import ResourceTagGetResponse
from openapi_server.models.resource_tag_update import ResourceTagUpdate


pytestmark = pytest.mark.asyncio

async def test_create_user_defined_tag(client):
    """Test case for create_user_defined_tag

    Create a user-defined resource tag for tagging cloud compute resources
    """
    body = {"scopeRefId":"scopeRefId","value":"value","key":"key"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/user_defined_tag',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_user_defined_tag(client):
    """Test case for delete_user_defined_tag

    Delete a user-defined resource tag
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/user_defined_tag/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_user_defined_tag_bulk(client):
    """Test case for delete_user_defined_tag_bulk

    Delete a list of user-defined resource tags
    """
    params = [('ids', ['ids_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/user_defined_tag',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_user_defined_tag(client):
    """Test case for get_user_defined_tag

    Get user-defined tag
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/user_defined_tag/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_user_defined_tag(client):
    """Test case for query_user_defined_tag

    Get user-defined resource tags
    """
    params = [('key', 'key_example'),
                    ('scope_ref_id', 'scope_ref_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/user_defined_tag',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_user_defined_tag(client):
    """Test case for update_user_defined_tag

    Update the value of a user-defined resource tag
    """
    body = {"value":"value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/user_defined_tag/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

