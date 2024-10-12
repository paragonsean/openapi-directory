# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.component_representation import ComponentRepresentation
from openapi_server.models.component_type_representation import ComponentTypeRepresentation


pytestmark = pytest.mark.asyncio

async def test_realm_components_get(client):
    """Test case for realm_components_get

    
    """
    params = [('name', 'name_example'),
                    ('parent', 'parent_example'),
                    ('type', 'type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/components'.format(realm='realm_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_components_id_delete(client):
    """Test case for realm_components_id_delete

    
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/{realm}/components/{id}'.format(realm='realm_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_components_id_get(client):
    """Test case for realm_components_id_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/components/{id}'.format(realm='realm_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_components_id_put(client):
    """Test case for realm_components_id_put

    
    """
    body = {"providerId":"providerId","name":"name","subType":"subType","id":"id","config":{"loadFactor":1.2315135,"threshold":1,"empty":True},"parentId":"parentId","providerType":"providerType"}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/{realm}/components/{id}'.format(realm='realm_example', id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_components_id_sub_component_types_get(client):
    """Test case for realm_components_id_sub_component_types_get

    List of subcomponent types that are available to configure for a particular parent component.
    """
    params = [('type', 'type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/components/{id}/sub-component-types'.format(realm='realm_example', id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_components_post(client):
    """Test case for realm_components_post

    
    """
    body = {"providerId":"providerId","name":"name","subType":"subType","id":"id","config":{"loadFactor":1.2315135,"threshold":1,"empty":True},"parentId":"parentId","providerType":"providerType"}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{realm}/components'.format(realm='realm_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

