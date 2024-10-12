# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.issue_link_type import IssueLinkType
from openapi_server.models.issue_link_types import IssueLinkTypes


pytestmark = pytest.mark.asyncio

async def test_create_issue_link_type(client):
    """Test case for create_issue_link_type

    Create issue link type
    """
    body = {"inward":"inward","name":"name","self":"https://openapi-generator.tech","id":"id","outward":"outward"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/rest/api/3/issueLinkType',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_issue_link_type(client):
    """Test case for delete_issue_link_type

    Delete issue link type
    """
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/api/3/issueLinkType/{issue_link_type_id}'.format(issue_link_type_id='issue_link_type_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_issue_link_type(client):
    """Test case for get_issue_link_type

    Get issue link type
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/issueLinkType/{issue_link_type_id}'.format(issue_link_type_id='issue_link_type_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_issue_link_types(client):
    """Test case for get_issue_link_types

    Get issue link types
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/issueLinkType',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_issue_link_type(client):
    """Test case for update_issue_link_type

    Update issue link type
    """
    body = {"inward":"inward","name":"name","self":"https://openapi-generator.tech","id":"id","outward":"outward"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/rest/api/3/issueLinkType/{issue_link_type_id}'.format(issue_link_type_id='issue_link_type_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

