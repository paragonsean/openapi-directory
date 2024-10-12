# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.component_issues_count import ComponentIssuesCount
from openapi_server.models.page_bean_component_with_issue_count import PageBeanComponentWithIssueCount
from openapi_server.models.project_component import ProjectComponent


pytestmark = pytest.mark.asyncio

async def test_create_component(client):
    """Test case for create_component

    Create component
    """
    body = {"leadUserName":"leadUserName","description":"description","project":"project","leadAccountId":"leadAccountId","lead":"","isAssigneeTypeValid":True,"realAssigneeType":"PROJECT_DEFAULT","name":"name","self":"https://openapi-generator.tech","realAssignee":"","assignee":"","assigneeType":"PROJECT_DEFAULT","id":"id","projectId":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/rest/api/3/component',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_component(client):
    """Test case for delete_component

    Delete component
    """
    params = [('moveIssuesTo', 'move_issues_to_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/api/3/component/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_component(client):
    """Test case for get_component

    Get component
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/component/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_component_related_issues(client):
    """Test case for get_component_related_issues

    Get component issues count
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/component/{id}/relatedIssueCounts'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_project_components(client):
    """Test case for get_project_components

    Get project components
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/project/{project_id_or_key}/components'.format(project_id_or_key='project_id_or_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_project_components_paginated(client):
    """Test case for get_project_components_paginated

    Get project components paginated
    """
    params = [('startAt', 0),
                    ('maxResults', 50),
                    ('orderBy', 'order_by_example'),
                    ('query', 'query_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/project/{project_id_or_key}/component'.format(project_id_or_key='project_id_or_key_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_component(client):
    """Test case for update_component

    Update component
    """
    body = {"leadUserName":"leadUserName","description":"description","project":"project","leadAccountId":"leadAccountId","lead":"","isAssigneeTypeValid":True,"realAssigneeType":"PROJECT_DEFAULT","name":"name","self":"https://openapi-generator.tech","realAssignee":"","assignee":"","assigneeType":"PROJECT_DEFAULT","id":"id","projectId":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/rest/api/3/component/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

