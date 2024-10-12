# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.remote_issue_link import RemoteIssueLink
from openapi_server.models.remote_issue_link_identifies import RemoteIssueLinkIdentifies
from openapi_server.models.remote_issue_link_request import RemoteIssueLinkRequest


pytestmark = pytest.mark.asyncio

async def test_create_or_update_remote_issue_link(client):
    """Test case for create_or_update_remote_issue_link

    Create or update remote issue link
    """
    body = {"application":"","globalId":"globalId","relationship":"relationship","object":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/rest/api/3/issue/{issue_id_or_key}/remotelink'.format(issue_id_or_key='issue_id_or_key_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_remote_issue_link_by_global_id(client):
    """Test case for delete_remote_issue_link_by_global_id

    Delete remote issue link by global ID
    """
    params = [('globalId', 'system=http://www.mycompany.com/support&id=1')]
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/api/3/issue/{issue_id_or_key}/remotelink'.format(issue_id_or_key='10000'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_remote_issue_link_by_id(client):
    """Test case for delete_remote_issue_link_by_id

    Delete remote issue link by ID
    """
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/api/3/issue/{issue_id_or_key}/remotelink/{link_id}'.format(issue_id_or_key='10000', link_id='10000'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_remote_issue_link_by_id(client):
    """Test case for get_remote_issue_link_by_id

    Get remote issue link by ID
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/issue/{issue_id_or_key}/remotelink/{link_id}'.format(issue_id_or_key='issue_id_or_key_example', link_id='link_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_remote_issue_links(client):
    """Test case for get_remote_issue_links

    Get remote issue links
    """
    params = [('globalId', 'global_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/issue/{issue_id_or_key}/remotelink'.format(issue_id_or_key='10000'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_remote_issue_link(client):
    """Test case for update_remote_issue_link

    Update remote issue link by ID
    """
    body = {"application":"","globalId":"globalId","relationship":"relationship","object":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/rest/api/3/issue/{issue_id_or_key}/remotelink/{link_id}'.format(issue_id_or_key='10000', link_id='10000'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

