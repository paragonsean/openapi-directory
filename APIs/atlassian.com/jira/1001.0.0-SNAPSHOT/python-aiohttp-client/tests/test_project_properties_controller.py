# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.entity_property import EntityProperty
from openapi_server.models.property_keys import PropertyKeys


pytestmark = pytest.mark.asyncio

async def test_delete_project_property(client):
    """Test case for delete_project_property

    Delete project property
    """
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/api/3/project/{project_id_or_key}/properties/{property_key}'.format(project_id_or_key='project_id_or_key_example', property_key='property_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_project_property(client):
    """Test case for get_project_property

    Get project property
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/project/{project_id_or_key}/properties/{property_key}'.format(project_id_or_key='project_id_or_key_example', property_key='property_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_project_property_keys(client):
    """Test case for get_project_property_keys

    Get project property keys
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/project/{project_id_or_key}/properties'.format(project_id_or_key='project_id_or_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_project_property(client):
    """Test case for set_project_property

    Set project property
    """
    body = {"number":5,"string":"string-value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/rest/api/3/project/{project_id_or_key}/properties/{property_key}'.format(project_id_or_key='project_id_or_key_example', property_key='property_key_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

