# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bulk_issue_is_watching import BulkIssueIsWatching
from openapi_server.models.issue_list import IssueList
from openapi_server.models.watchers import Watchers


pytestmark = pytest.mark.asyncio

async def test_add_watcher(client):
    """Test case for add_watcher

    Add watcher
    """
    body = 'body_example'
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/rest/api/3/issue/{issue_id_or_key}/watchers'.format(issue_id_or_key='issue_id_or_key_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_is_watching_issue_bulk(client):
    """Test case for get_is_watching_issue_bulk

    Get is watching issue bulk
    """
    body = {"issueIds":["issueIds","issueIds"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/rest/api/3/issue/watching',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_issue_watchers(client):
    """Test case for get_issue_watchers

    Get issue watchers
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/issue/{issue_id_or_key}/watchers'.format(issue_id_or_key='issue_id_or_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_watcher(client):
    """Test case for remove_watcher

    Delete watcher
    """
    params = [('username', 'username_example'),
                    ('accountId', '5b10ac8d82e05b22cc7d4ef5')]
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/api/3/issue/{issue_id_or_key}/watchers'.format(issue_id_or_key='issue_id_or_key_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

