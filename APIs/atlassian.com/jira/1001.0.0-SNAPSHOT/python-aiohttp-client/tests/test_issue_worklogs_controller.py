# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.changed_worklogs import ChangedWorklogs
from openapi_server.models.page_of_worklogs import PageOfWorklogs
from openapi_server.models.worklog import Worklog
from openapi_server.models.worklog_ids_request_bean import WorklogIdsRequestBean


pytestmark = pytest.mark.asyncio

async def test_add_worklog(client):
    """Test case for add_worklog

    Add worklog
    """
    body = {"issueId":"issueId","visibility":"","timeSpent":"timeSpent","author":"","created":"2000-01-23T04:56:07.000+00:00","started":"2000-01-23T04:56:07.000+00:00","timeSpentSeconds":5,"updateAuthor":"","self":"https://openapi-generator.tech","comment":"","id":"id","updated":"2000-01-23T04:56:07.000+00:00","properties":[{"value":"","key":"key"},{"value":"","key":"key"}]}
    params = [('notifyUsers', True),
                    ('adjustEstimate', auto),
                    ('newEstimate', 'new_estimate_example'),
                    ('reduceBy', 'reduce_by_example'),
                    ('expand', ''),
                    ('overrideEditableFlag', False)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/rest/api/3/issue/{issue_id_or_key}/worklog'.format(issue_id_or_key='issue_id_or_key_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_worklog(client):
    """Test case for delete_worklog

    Delete worklog
    """
    params = [('notifyUsers', True),
                    ('adjustEstimate', auto),
                    ('newEstimate', 'new_estimate_example'),
                    ('increaseBy', 'increase_by_example'),
                    ('overrideEditableFlag', False)]
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/api/3/issue/{issue_id_or_key}/worklog/{id}'.format(issue_id_or_key='issue_id_or_key_example', id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_ids_of_worklogs_deleted_since(client):
    """Test case for get_ids_of_worklogs_deleted_since

    Get IDs of deleted worklogs
    """
    params = [('since', 0)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/worklog/deleted',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_ids_of_worklogs_modified_since(client):
    """Test case for get_ids_of_worklogs_modified_since

    Get IDs of updated worklogs
    """
    params = [('since', 0),
                    ('expand', '')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/worklog/updated',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_issue_worklog(client):
    """Test case for get_issue_worklog

    Get issue worklogs
    """
    params = [('startAt', 0),
                    ('maxResults', 5000),
                    ('startedAfter', 56),
                    ('startedBefore', 56),
                    ('expand', '')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/issue/{issue_id_or_key}/worklog'.format(issue_id_or_key='issue_id_or_key_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_worklog(client):
    """Test case for get_worklog

    Get worklog
    """
    params = [('expand', '')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/issue/{issue_id_or_key}/worklog/{id}'.format(issue_id_or_key='issue_id_or_key_example', id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_worklogs_for_ids(client):
    """Test case for get_worklogs_for_ids

    Get worklogs
    """
    body = {"ids":[0,0]}
    params = [('expand', '')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/rest/api/3/worklog/list',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_worklog(client):
    """Test case for update_worklog

    Update worklog
    """
    body = {"issueId":"issueId","visibility":"","timeSpent":"timeSpent","author":"","created":"2000-01-23T04:56:07.000+00:00","started":"2000-01-23T04:56:07.000+00:00","timeSpentSeconds":5,"updateAuthor":"","self":"https://openapi-generator.tech","comment":"","id":"id","updated":"2000-01-23T04:56:07.000+00:00","properties":[{"value":"","key":"key"},{"value":"","key":"key"}]}
    params = [('notifyUsers', True),
                    ('adjustEstimate', auto),
                    ('newEstimate', 'new_estimate_example'),
                    ('expand', ''),
                    ('overrideEditableFlag', False)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/rest/api/3/issue/{issue_id_or_key}/worklog/{id}'.format(issue_id_or_key='issue_id_or_key_example', id='id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

