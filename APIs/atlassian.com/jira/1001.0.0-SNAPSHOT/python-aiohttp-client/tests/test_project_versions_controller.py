# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.delete_and_replace_version_bean import DeleteAndReplaceVersionBean
from openapi_server.models.page_bean_version import PageBeanVersion
from openapi_server.models.version import Version
from openapi_server.models.version_issue_counts import VersionIssueCounts
from openapi_server.models.version_move_bean import VersionMoveBean
from openapi_server.models.version_unresolved_issues_count import VersionUnresolvedIssuesCount


pytestmark = pytest.mark.asyncio

async def test_create_version(client):
    """Test case for create_version

    Create version
    """
    body = {"releaseDate":"2000-01-23","description":"description","project":"project","archived":True,"expand":"expand","operations":[{"weight":0,"href":"href","id":"id","label":"label","styleClass":"styleClass","title":"title","iconClass":"iconClass"},{"weight":0,"href":"href","id":"id","label":"label","styleClass":"styleClass","title":"title","iconClass":"iconClass"}],"overdue":True,"name":"name","moveUnfixedIssuesTo":"https://openapi-generator.tech","self":"https://openapi-generator.tech","userReleaseDate":"userReleaseDate","id":"id","userStartDate":"userStartDate","projectId":6,"released":True,"startDate":"2000-01-23","issuesStatusForFixVersion":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/rest/api/3/version',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_and_replace_version(client):
    """Test case for delete_and_replace_version

    Delete and replace version
    """
    body = {"moveAffectedIssuesTo":1,"moveFixIssuesTo":5,"customFieldReplacementList":[{"customFieldId":0,"moveTo":6},{"customFieldId":0,"moveTo":6}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/rest/api/3/version/{id}/removeAndSwap'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_version(client):
    """Test case for delete_version

    Delete version
    """
    params = [('moveFixIssuesTo', 'move_fix_issues_to_example'),
                    ('moveAffectedIssuesTo', 'move_affected_issues_to_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/api/3/version/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_project_versions(client):
    """Test case for get_project_versions

    Get project versions
    """
    params = [('expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/project/{project_id_or_key}/versions'.format(project_id_or_key='project_id_or_key_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_project_versions_paginated(client):
    """Test case for get_project_versions_paginated

    Get project versions paginated
    """
    params = [('startAt', 0),
                    ('maxResults', 50),
                    ('orderBy', 'order_by_example'),
                    ('query', 'query_example'),
                    ('status', 'status_example'),
                    ('expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/project/{project_id_or_key}/version'.format(project_id_or_key='project_id_or_key_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_version(client):
    """Test case for get_version

    Get version
    """
    params = [('expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/version/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_version_related_issues(client):
    """Test case for get_version_related_issues

    Get version's related issues count
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/version/{id}/relatedIssueCounts'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_version_unresolved_issues(client):
    """Test case for get_version_unresolved_issues

    Get version's unresolved issues count
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/version/{id}/unresolvedIssueCount'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_merge_versions(client):
    """Test case for merge_versions

    Merge versions
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/rest/api/3/version/{id}/mergeto/{move_issues_to}'.format(id='id_example', move_issues_to='move_issues_to_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_move_version(client):
    """Test case for move_version

    Move version
    """
    body = {"after":"https://openapi-generator.tech","position":"Earlier"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/rest/api/3/version/{id}/move'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_version(client):
    """Test case for update_version

    Update version
    """
    body = {"releaseDate":"2000-01-23","description":"description","project":"project","archived":True,"expand":"expand","operations":[{"weight":0,"href":"href","id":"id","label":"label","styleClass":"styleClass","title":"title","iconClass":"iconClass"},{"weight":0,"href":"href","id":"id","label":"label","styleClass":"styleClass","title":"title","iconClass":"iconClass"}],"overdue":True,"name":"name","moveUnfixedIssuesTo":"https://openapi-generator.tech","self":"https://openapi-generator.tech","userReleaseDate":"userReleaseDate","id":"id","userStartDate":"userStartDate","projectId":6,"released":True,"startDate":"2000-01-23","issuesStatusForFixVersion":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/rest/api/3/version/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

