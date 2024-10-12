# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.issue_field_option import IssueFieldOption
from openapi_server.models.issue_field_option_create_bean import IssueFieldOptionCreateBean
from openapi_server.models.page_bean_issue_field_option import PageBeanIssueFieldOption
from openapi_server.models.task_progress_bean_remove_option_from_issues_result import TaskProgressBeanRemoveOptionFromIssuesResult


pytestmark = pytest.mark.asyncio

async def test_create_issue_field_option(client):
    """Test case for create_issue_field_option

    Create issue field option
    """
    body = {"config":{"scope":"","attributes":["notSelectable","notSelectable"]},"value":"value","properties":{"key":""}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/rest/api/3/field/{field_key}/option'.format(field_key='field_key_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_issue_field_option(client):
    """Test case for delete_issue_field_option

    Delete issue field option
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/api/3/field/{field_key}/option/{option_id}'.format(field_key='field_key_example', option_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_issue_field_options(client):
    """Test case for get_all_issue_field_options

    Get all issue field options
    """
    params = [('startAt', 0),
                    ('maxResults', 50)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/field/{field_key}/option'.format(field_key='field_key_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_issue_field_option(client):
    """Test case for get_issue_field_option

    Get issue field option
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/field/{field_key}/option/{option_id}'.format(field_key='field_key_example', option_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_selectable_issue_field_options(client):
    """Test case for get_selectable_issue_field_options

    Get selectable issue field options
    """
    params = [('startAt', 0),
                    ('maxResults', 50),
                    ('projectId', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/field/{field_key}/option/suggestions/edit'.format(field_key='field_key_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_visible_issue_field_options(client):
    """Test case for get_visible_issue_field_options

    Get visible issue field options
    """
    params = [('startAt', 0),
                    ('maxResults', 56),
                    ('projectId', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/field/{field_key}/option/suggestions/search'.format(field_key='field_key_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_replace_issue_field_option(client):
    """Test case for replace_issue_field_option

    Replace issue field option
    """
    params = [('replaceWith', 56),
                    ('jql', 'jql_example'),
                    ('overrideScreenSecurity', False),
                    ('overrideEditableFlag', False)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/api/3/field/{field_key}/option/{option_id}/issue'.format(field_key='field_key_example', option_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_issue_field_option(client):
    """Test case for update_issue_field_option

    Update issue field option
    """
    body = {"id":5,"config":{"scope":"","attributes":["notSelectable","notSelectable"]},"value":"value","properties":{"key":""}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/rest/api/3/field/{field_key}/option/{option_id}'.format(field_key='field_key_example', option_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

