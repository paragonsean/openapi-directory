# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.entity_property import EntityProperty
from openapi_server.models.property_keys import PropertyKeys


pytestmark = pytest.mark.asyncio

async def test_delete_worklog_property(client):
    """Test case for delete_worklog_property

    Delete worklog property
    """
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/api/3/issue/{issue_id_or_key}/worklog/{worklog_id}/properties/{property_key}'.format(issue_id_or_key='issue_id_or_key_example', worklog_id='worklog_id_example', property_key='property_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_worklog_property(client):
    """Test case for get_worklog_property

    Get worklog property
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/issue/{issue_id_or_key}/worklog/{worklog_id}/properties/{property_key}'.format(issue_id_or_key='issue_id_or_key_example', worklog_id='worklog_id_example', property_key='property_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_worklog_property_keys(client):
    """Test case for get_worklog_property_keys

    Get worklog property keys
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/issue/{issue_id_or_key}/worklog/{worklog_id}/properties'.format(issue_id_or_key='issue_id_or_key_example', worklog_id='worklog_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_worklog_property(client):
    """Test case for set_worklog_property

    Set worklog property
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/rest/api/3/issue/{issue_id_or_key}/worklog/{worklog_id}/properties/{property_key}'.format(issue_id_or_key='issue_id_or_key_example', worklog_id='worklog_id_example', property_key='property_key_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

