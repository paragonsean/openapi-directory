# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.entity_property import EntityProperty
from openapi_server.models.operation_message import OperationMessage
from openapi_server.models.property_keys import PropertyKeys


pytestmark = pytest.mark.asyncio

async def test_addon_properties_resource_delete_addon_property_delete(client):
    """Test case for addon_properties_resource_delete_addon_property_delete

    Delete app property
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/atlassian-connect/1/addons/{addon_key}/properties/{property_key}'.format(addon_key='addon_key_example', property_key='property_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_addon_properties_resource_get_addon_properties_get(client):
    """Test case for addon_properties_resource_get_addon_properties_get

    Get app properties
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/atlassian-connect/1/addons/{addon_key}/properties'.format(addon_key='addon_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_addon_properties_resource_get_addon_property_get(client):
    """Test case for addon_properties_resource_get_addon_property_get

    Get app property
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/atlassian-connect/1/addons/{addon_key}/properties/{property_key}'.format(addon_key='addon_key_example', property_key='property_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_addon_properties_resource_put_addon_property_put(client):
    """Test case for addon_properties_resource_put_addon_property_put

    Set app property
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/rest/atlassian-connect/1/addons/{addon_key}/properties/{property_key}'.format(addon_key='addon_key_example', property_key='property_key_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

