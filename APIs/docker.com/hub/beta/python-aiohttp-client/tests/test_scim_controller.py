# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.scim_resource_type import ScimResourceType
from openapi_server.models.scim_schema import ScimSchema
from openapi_server.models.scim_service_provider_config import ScimServiceProviderConfig
from openapi_server.models.scim_user import ScimUser
from openapi_server.models.v2_scim20_resource_types_get200_response import V2Scim20ResourceTypesGet200Response
from openapi_server.models.v2_scim20_resource_types_get401_response import V2Scim20ResourceTypesGet401Response
from openapi_server.models.v2_scim20_resource_types_get500_response import V2Scim20ResourceTypesGet500Response
from openapi_server.models.v2_scim20_resource_types_name_get404_response import V2Scim20ResourceTypesNameGet404Response
from openapi_server.models.v2_scim20_schemas_get200_response import V2Scim20SchemasGet200Response
from openapi_server.models.v2_scim20_users_get200_response import V2Scim20UsersGet200Response
from openapi_server.models.v2_scim20_users_get400_response import V2Scim20UsersGet400Response
from openapi_server.models.v2_scim20_users_get403_response import V2Scim20UsersGet403Response
from openapi_server.models.v2_scim20_users_id_put_request import V2Scim20UsersIdPutRequest
from openapi_server.models.v2_scim20_users_post409_response import V2Scim20UsersPost409Response
from openapi_server.models.v2_scim20_users_post_request import V2Scim20UsersPostRequest


pytestmark = pytest.mark.asyncio

async def test_v2_scim20_resource_types_get(client):
    """Test case for v2_scim20_resource_types_get

    List resource types
    """
    headers = { 
        'Accept': 'application/scim+json',
    }
    response = await client.request(
        method='GET',
        path='/v2/scim/2.0/ResourceTypes',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v2_scim20_resource_types_name_get(client):
    """Test case for v2_scim20_resource_types_name_get

    Get a resource type
    """
    headers = { 
        'Accept': 'application/scim+json',
    }
    response = await client.request(
        method='GET',
        path='/v2/scim/2.0/ResourceTypes/{name}'.format(name='User'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v2_scim20_schemas_get(client):
    """Test case for v2_scim20_schemas_get

    List schemas
    """
    headers = { 
        'Accept': 'application/scim+json',
    }
    response = await client.request(
        method='GET',
        path='/v2/scim/2.0/Schemas',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v2_scim20_schemas_id_get(client):
    """Test case for v2_scim20_schemas_id_get

    Get a schema
    """
    headers = { 
        'Accept': 'application/scim+json',
    }
    response = await client.request(
        method='GET',
        path='/v2/scim/2.0/Schemas/{id}'.format(id='urn:ietf:params:scim:schemas:core:2.0:User'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v2_scim20_service_provider_config_get(client):
    """Test case for v2_scim20_service_provider_config_get

    Get service provider config
    """
    headers = { 
        'Accept': 'application/scim+json',
    }
    response = await client.request(
        method='GET',
        path='/v2/scim/2.0/ServiceProviderConfig',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v2_scim20_users_get(client):
    """Test case for v2_scim20_users_get

    List users
    """
    params = [('startIndex', 1),
                    ('count', 10),
                    ('filter', 'userName eq \"jon.snow@docker.com\"'),
                    ('attributes', 'userName,displayName'),
                    ('sortOrder', 'sort_order_example'),
                    ('sortBy', 'userName')]
    headers = { 
        'Accept': 'application/scim+json',
    }
    response = await client.request(
        method='GET',
        path='/v2/scim/2.0/Users',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v2_scim20_users_id_get(client):
    """Test case for v2_scim20_users_id_get

    Get a user
    """
    headers = { 
        'Accept': 'application/scim+json',
    }
    response = await client.request(
        method='GET',
        path='/v2/scim/2.0/Users/{id}'.format(id='d80f7c79-7730-49d8-9a41-7c42fb622d9c'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v2_scim20_users_id_put(client):
    """Test case for v2_scim20_users_id_put

    Update a user
    """
    body = openapi_server.V2Scim20UsersIdPutRequest()
    headers = { 
        'Accept': 'application/scim+json',
        'Content-Type': 'application/scim+json',
    }
    response = await client.request(
        method='PUT',
        path='/v2/scim/2.0/Users/{id}'.format(id='d80f7c79-7730-49d8-9a41-7c42fb622d9c'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v2_scim20_users_post(client):
    """Test case for v2_scim20_users_post

    Create user
    """
    body = openapi_server.V2Scim20UsersPostRequest()
    headers = { 
        'Accept': 'application/scim+json',
        'Content-Type': 'application/scim+json',
    }
    response = await client.request(
        method='POST',
        path='/v2/scim/2.0/Users',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

