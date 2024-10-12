# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.created_issue import CreatedIssue
from openapi_server.models.created_issues import CreatedIssues
from openapi_server.models.error_collection import ErrorCollection
from openapi_server.models.issue_bean import IssueBean
from openapi_server.models.issue_changelog_ids import IssueChangelogIds
from openapi_server.models.issue_create_metadata import IssueCreateMetadata
from openapi_server.models.issue_event import IssueEvent
from openapi_server.models.issue_update_details import IssueUpdateDetails
from openapi_server.models.issue_update_metadata import IssueUpdateMetadata
from openapi_server.models.issues_update_bean import IssuesUpdateBean
from openapi_server.models.notification import Notification
from openapi_server.models.page_bean_changelog import PageBeanChangelog
from openapi_server.models.page_of_changelogs import PageOfChangelogs
from openapi_server.models.transitions import Transitions
from openapi_server.models.user import User


pytestmark = pytest.mark.asyncio

async def test_assign_issue(client):
    """Test case for assign_issue

    Assign issue
    """
    body = {"avatarUrls":"","displayName":"displayName","accountType":"atlassian","active":True,"groups":"","timeZone":"timeZone","locale":"locale","accountId":"accountId","emailAddress":"emailAddress","expand":"expand","name":"name","self":"https://openapi-generator.tech","key":"key","applicationRoles":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/rest/api/3/issue/{issue_id_or_key}/assignee'.format(issue_id_or_key='issue_id_or_key_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_issue(client):
    """Test case for create_issue

    Create issue
    """
    body = {"historyMetadata":"","update":{"key":[{"add":"triaged","set":"A new summary","edit":{"originalEstimate":"1w 1d","remainingEstimate":"4d"},"copy":{"issuelinks":{"sourceIssues":[{"key":"FP-5"}]}},"remove":"blocker"},{"add":"triaged","set":"A new summary","edit":{"originalEstimate":"1w 1d","remainingEstimate":"4d"},"copy":{"issuelinks":{"sourceIssues":[{"key":"FP-5"}]}},"remove":"blocker"}]},"fields":{"key":""},"properties":[{"value":"","key":"key"},{"value":"","key":"key"}],"transition":""}
    params = [('updateHistory', False)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/rest/api/3/issue',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_issues(client):
    """Test case for create_issues

    Bulk create issue
    """
    body = {"issueUpdates":[{"historyMetadata":"","update":{"key":[{"add":"triaged","set":"A new summary","edit":{"originalEstimate":"1w 1d","remainingEstimate":"4d"},"copy":{"issuelinks":{"sourceIssues":[{"key":"FP-5"}]}},"remove":"blocker"},{"add":"triaged","set":"A new summary","edit":{"originalEstimate":"1w 1d","remainingEstimate":"4d"},"copy":{"issuelinks":{"sourceIssues":[{"key":"FP-5"}]}},"remove":"blocker"}]},"fields":{"key":""},"properties":[{"value":"","key":"key"},{"value":"","key":"key"}],"transition":""},{"historyMetadata":"","update":{"key":[{"add":"triaged","set":"A new summary","edit":{"originalEstimate":"1w 1d","remainingEstimate":"4d"},"copy":{"issuelinks":{"sourceIssues":[{"key":"FP-5"}]}},"remove":"blocker"},{"add":"triaged","set":"A new summary","edit":{"originalEstimate":"1w 1d","remainingEstimate":"4d"},"copy":{"issuelinks":{"sourceIssues":[{"key":"FP-5"}]}},"remove":"blocker"}]},"fields":{"key":""},"properties":[{"value":"","key":"key"},{"value":"","key":"key"}],"transition":""}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/rest/api/3/issue/bulk',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_issue(client):
    """Test case for delete_issue

    Delete issue
    """
    params = [('deleteSubtasks', false)]
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/api/3/issue/{issue_id_or_key}'.format(issue_id_or_key='issue_id_or_key_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_do_transition(client):
    """Test case for do_transition

    Transition issue
    """
    body = {"historyMetadata":"","update":{"key":[{"add":"triaged","set":"A new summary","edit":{"originalEstimate":"1w 1d","remainingEstimate":"4d"},"copy":{"issuelinks":{"sourceIssues":[{"key":"FP-5"}]}},"remove":"blocker"},{"add":"triaged","set":"A new summary","edit":{"originalEstimate":"1w 1d","remainingEstimate":"4d"},"copy":{"issuelinks":{"sourceIssues":[{"key":"FP-5"}]}},"remove":"blocker"}]},"fields":{"key":""},"properties":[{"value":"","key":"key"},{"value":"","key":"key"}],"transition":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/rest/api/3/issue/{issue_id_or_key}/transitions'.format(issue_id_or_key='issue_id_or_key_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_edit_issue(client):
    """Test case for edit_issue

    Edit issue
    """
    body = {"historyMetadata":"","update":{"key":[{"add":"triaged","set":"A new summary","edit":{"originalEstimate":"1w 1d","remainingEstimate":"4d"},"copy":{"issuelinks":{"sourceIssues":[{"key":"FP-5"}]}},"remove":"blocker"},{"add":"triaged","set":"A new summary","edit":{"originalEstimate":"1w 1d","remainingEstimate":"4d"},"copy":{"issuelinks":{"sourceIssues":[{"key":"FP-5"}]}},"remove":"blocker"}]},"fields":{"key":""},"properties":[{"value":"","key":"key"},{"value":"","key":"key"}],"transition":""}
    params = [('notifyUsers', True),
                    ('overrideScreenSecurity', False),
                    ('overrideEditableFlag', False)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/rest/api/3/issue/{issue_id_or_key}'.format(issue_id_or_key='issue_id_or_key_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_change_logs(client):
    """Test case for get_change_logs

    Get changelogs
    """
    params = [('startAt', 0),
                    ('maxResults', 100)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/issue/{issue_id_or_key}/changelog'.format(issue_id_or_key='issue_id_or_key_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_change_logs_by_ids(client):
    """Test case for get_change_logs_by_ids

    Get changelogs by IDs
    """
    body = {"changelogIds":[0,0]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/rest/api/3/issue/{issue_id_or_key}/changelog/list'.format(issue_id_or_key='issue_id_or_key_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_create_issue_meta(client):
    """Test case for get_create_issue_meta

    Get create issue metadata
    """
    params = [('projectIds', ['project_ids_example']),
                    ('projectKeys', ['project_keys_example']),
                    ('issuetypeIds', ['issuetype_ids_example']),
                    ('issuetypeNames', ['issuetype_names_example']),
                    ('expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/issue/createmeta',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_edit_issue_meta(client):
    """Test case for get_edit_issue_meta

    Get edit issue metadata
    """
    params = [('overrideScreenSecurity', False),
                    ('overrideEditableFlag', False)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/issue/{issue_id_or_key}/editmeta'.format(issue_id_or_key='issue_id_or_key_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_events(client):
    """Test case for get_events

    Get events
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/events',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_issue(client):
    """Test case for get_issue

    Get issue
    """
    params = [('fields', ['fields_example']),
                    ('fieldsByKeys', False),
                    ('expand', 'expand_example'),
                    ('properties', ['properties_example']),
                    ('updateHistory', False)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/issue/{issue_id_or_key}'.format(issue_id_or_key='issue_id_or_key_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_transitions(client):
    """Test case for get_transitions

    Get transitions
    """
    params = [('expand', 'expand_example'),
                    ('transitionId', 'transition_id_example'),
                    ('skipRemoteOnlyCondition', False),
                    ('includeUnavailableTransitions', False),
                    ('sortByOpsBarAndStatus', False)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/issue/{issue_id_or_key}/transitions'.format(issue_id_or_key='issue_id_or_key_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notify(client):
    """Test case for notify

    Send notification for issue
    """
    body = {"htmlBody":"htmlBody","subject":"subject","textBody":"textBody","to":"","restrict":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/rest/api/3/issue/{issue_id_or_key}/notify'.format(issue_id_or_key='issue_id_or_key_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

