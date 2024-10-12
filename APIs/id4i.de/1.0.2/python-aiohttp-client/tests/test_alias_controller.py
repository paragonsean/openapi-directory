# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_error import ApiError
from openapi_server.models.guid_alias import GuidAlias
from openapi_server.models.paginated_response_of_guid import PaginatedResponseOfGuid


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_add_guid_alias(client):
    """Test case for add_guid_alias

    Add alias for GUID or Collection
    """
    body = {"alias":"alias"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/id4ns/{id4n}/alias/{alias_type}'.format(id4n='id4n_example', alias_type='alias_type_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_guid_alias_types(client):
    """Test case for get_guid_alias_types

    List all supported alias types
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/search/guids/aliases/types',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_guid_aliases(client):
    """Test case for get_guid_aliases

    Get all aliases for the given GUID or Collection.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/id4ns/{id4n}/alias'.format(id4n='id4n_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_guid_alias(client):
    """Test case for remove_guid_alias

    Remove aliases from GUID or Collection
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/id4ns/{id4n}/alias/{alias_type}'.format(id4n='id4n_example', alias_type='alias_type_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_by_alias(client):
    """Test case for search_by_alias

    Search for GUIDs by alias
    """
    params = [('alias', 'alias_example'),
                    ('aliasType', 'alias_type_example'),
                    ('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/search/guids',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

