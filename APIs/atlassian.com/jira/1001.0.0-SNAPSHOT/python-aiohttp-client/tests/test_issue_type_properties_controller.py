# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.entity_property import EntityProperty
from openapi_server.models.property_keys import PropertyKeys


pytestmark = pytest.mark.asyncio

async def test_delete_issue_type_property(client):
    """Test case for delete_issue_type_property

    Delete issue type property
    """
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/api/3/issuetype/{issue_type_id}/properties/{property_key}'.format(issue_type_id='issue_type_id_example', property_key='property_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_issue_type_property(client):
    """Test case for get_issue_type_property

    Get issue type property
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/issuetype/{issue_type_id}/properties/{property_key}'.format(issue_type_id='issue_type_id_example', property_key='property_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_issue_type_property_keys(client):
    """Test case for get_issue_type_property_keys

    Get issue type property keys
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/issuetype/{issue_type_id}/properties'.format(issue_type_id='issue_type_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_issue_type_property(client):
    """Test case for set_issue_type_property

    Set issue type property
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
        path='/rest/api/3/issuetype/{issue_type_id}/properties/{property_key}'.format(issue_type_id='issue_type_id_example', property_key='property_key_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

