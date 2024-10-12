# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.activity_list_public_events503_response import ActivityListPublicEvents503Response
from openapi_server.models.basic_error import BasicError
from openapi_server.models.issue import Issue
from openapi_server.models.issue_comment import IssueComment
from openapi_server.models.issue_event import IssueEvent
from openapi_server.models.issue_event_for_issue import IssueEventForIssue
from openapi_server.models.issues_add_assignees_request import IssuesAddAssigneesRequest
from openapi_server.models.issues_add_labels_request import IssuesAddLabelsRequest
from openapi_server.models.issues_create_label_request import IssuesCreateLabelRequest
from openapi_server.models.issues_create_milestone_request import IssuesCreateMilestoneRequest
from openapi_server.models.issues_create_request import IssuesCreateRequest
from openapi_server.models.issues_lock_request import IssuesLockRequest
from openapi_server.models.issues_remove_assignees_request import IssuesRemoveAssigneesRequest
from openapi_server.models.issues_set_labels_request import IssuesSetLabelsRequest
from openapi_server.models.issues_update_comment_request import IssuesUpdateCommentRequest
from openapi_server.models.issues_update_label_request import IssuesUpdateLabelRequest
from openapi_server.models.issues_update_milestone_request import IssuesUpdateMilestoneRequest
from openapi_server.models.issues_update_request import IssuesUpdateRequest
from openapi_server.models.label import Label
from openapi_server.models.milestone import Milestone
from openapi_server.models.simple_user import SimpleUser
from openapi_server.models.timeline_issue_events import TimelineIssueEvents
from openapi_server.models.validation_error import ValidationError


pytestmark = pytest.mark.asyncio

async def test_issues_add_assignees(client):
    """Test case for issues_add_assignees

    Add assignees to an issue
    """
    body = {"assignees":["hubot","other_user"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/repos/{owner}/{repo}/issues/{issue_number}/assignees'.format(owner='owner_example', repo='repo_example', issue_number=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issues_add_labels(client):
    """Test case for issues_add_labels

    Add labels to an issue
    """
    body = {"labels":["bug","enhancement"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/repos/{owner}/{repo}/issues/{issue_number}/labels'.format(owner='owner_example', repo='repo_example', issue_number=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issues_check_user_can_be_assigned(client):
    """Test case for issues_check_user_can_be_assigned

    Check if a user can be assigned
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/assignees/{assignee}'.format(owner='owner_example', repo='repo_example', assignee='assignee_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issues_create(client):
    """Test case for issues_create

    Create an issue
    """
    body = {"assignees":["octocat"],"body":"I'm having a problem with this.","labels":["bug"],"milestone":1,"title":"Found a bug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/repos/{owner}/{repo}/issues'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issues_create_comment(client):
    """Test case for issues_create_comment

    Create an issue comment
    """
    body = {"body":"Me too"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/repos/{owner}/{repo}/issues/{issue_number}/comments'.format(owner='owner_example', repo='repo_example', issue_number=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issues_create_label(client):
    """Test case for issues_create_label

    Create a label
    """
    body = {"color":"f29513","description":"Something isn't working","name":"bug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/repos/{owner}/{repo}/labels'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issues_create_milestone(client):
    """Test case for issues_create_milestone

    Create a milestone
    """
    body = {"description":"Tracking milestone for version 1.0","due_on":"2012-10-09T23:39:01Z","state":"open","title":"v1.0"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/repos/{owner}/{repo}/milestones'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issues_delete_comment(client):
    """Test case for issues_delete_comment

    Delete an issue comment
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/repos/{owner}/{repo}/issues/comments/{comment_id}'.format(owner='owner_example', repo='repo_example', comment_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issues_delete_label(client):
    """Test case for issues_delete_label

    Delete a label
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/repos/{owner}/{repo}/labels/{name}'.format(owner='owner_example', repo='repo_example', name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issues_delete_milestone(client):
    """Test case for issues_delete_milestone

    Delete a milestone
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/repos/{owner}/{repo}/milestones/{milestone_number}'.format(owner='owner_example', repo='repo_example', milestone_number=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issues_get(client):
    """Test case for issues_get

    Get an issue
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/issues/{issue_number}'.format(owner='owner_example', repo='repo_example', issue_number=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issues_get_comment(client):
    """Test case for issues_get_comment

    Get an issue comment
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/issues/comments/{comment_id}'.format(owner='owner_example', repo='repo_example', comment_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issues_get_event(client):
    """Test case for issues_get_event

    Get an issue event
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/issues/events/{event_id}'.format(owner='owner_example', repo='repo_example', event_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issues_get_label(client):
    """Test case for issues_get_label

    Get a label
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/labels/{name}'.format(owner='owner_example', repo='repo_example', name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issues_get_milestone(client):
    """Test case for issues_get_milestone

    Get a milestone
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/milestones/{milestone_number}'.format(owner='owner_example', repo='repo_example', milestone_number=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issues_list(client):
    """Test case for issues_list

    List issues assigned to the authenticated user
    """
    params = [('filter', assigned),
                    ('state', open),
                    ('labels', 'labels_example'),
                    ('sort', created),
                    ('direction', desc),
                    ('since', '2013-10-20T19:20:30+01:00'),
                    ('collab', True),
                    ('orgs', True),
                    ('owned', True),
                    ('pulls', True),
                    ('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/issues',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issues_list_assignees(client):
    """Test case for issues_list_assignees

    List assignees
    """
    params = [('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/assignees'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issues_list_comments(client):
    """Test case for issues_list_comments

    List issue comments
    """
    params = [('since', '2013-10-20T19:20:30+01:00'),
                    ('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/issues/{issue_number}/comments'.format(owner='owner_example', repo='repo_example', issue_number=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issues_list_comments_for_repo(client):
    """Test case for issues_list_comments_for_repo

    List issue comments for a repository
    """
    params = [('sort', created),
                    ('direction', 'direction_example'),
                    ('since', '2013-10-20T19:20:30+01:00'),
                    ('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/issues/comments'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issues_list_events(client):
    """Test case for issues_list_events

    List issue events
    """
    params = [('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/issues/{issue_number}/events'.format(owner='owner_example', repo='repo_example', issue_number=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issues_list_events_for_repo(client):
    """Test case for issues_list_events_for_repo

    List issue events for a repository
    """
    params = [('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/issues/events'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issues_list_events_for_timeline(client):
    """Test case for issues_list_events_for_timeline

    List timeline events for an issue
    """
    params = [('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/issues/{issue_number}/timeline'.format(owner='owner_example', repo='repo_example', issue_number=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issues_list_for_authenticated_user(client):
    """Test case for issues_list_for_authenticated_user

    List user account issues assigned to the authenticated user
    """
    params = [('filter', assigned),
                    ('state', open),
                    ('labels', 'labels_example'),
                    ('sort', created),
                    ('direction', desc),
                    ('since', '2013-10-20T19:20:30+01:00'),
                    ('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/user/issues',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issues_list_for_org(client):
    """Test case for issues_list_for_org

    List organization issues assigned to the authenticated user
    """
    params = [('filter', assigned),
                    ('state', open),
                    ('labels', 'labels_example'),
                    ('sort', created),
                    ('direction', desc),
                    ('since', '2013-10-20T19:20:30+01:00'),
                    ('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/orgs/{org}/issues'.format(org='org_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issues_list_for_repo(client):
    """Test case for issues_list_for_repo

    List repository issues
    """
    params = [('milestone', 'milestone_example'),
                    ('state', open),
                    ('assignee', 'assignee_example'),
                    ('creator', 'creator_example'),
                    ('mentioned', 'mentioned_example'),
                    ('labels', 'labels_example'),
                    ('sort', created),
                    ('direction', desc),
                    ('since', '2013-10-20T19:20:30+01:00'),
                    ('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/issues'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issues_list_labels_for_milestone(client):
    """Test case for issues_list_labels_for_milestone

    List labels for issues in a milestone
    """
    params = [('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/milestones/{milestone_number}/labels'.format(owner='owner_example', repo='repo_example', milestone_number=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issues_list_labels_for_repo(client):
    """Test case for issues_list_labels_for_repo

    List labels for a repository
    """
    params = [('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/labels'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issues_list_labels_on_issue(client):
    """Test case for issues_list_labels_on_issue

    List labels for an issue
    """
    params = [('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/issues/{issue_number}/labels'.format(owner='owner_example', repo='repo_example', issue_number=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issues_list_milestones(client):
    """Test case for issues_list_milestones

    List milestones
    """
    params = [('state', open),
                    ('sort', due_on),
                    ('direction', asc),
                    ('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/milestones'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issues_lock(client):
    """Test case for issues_lock

    Lock an issue
    """
    body = openapi_server.IssuesLockRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/repos/{owner}/{repo}/issues/{issue_number}/lock'.format(owner='owner_example', repo='repo_example', issue_number=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issues_remove_all_labels(client):
    """Test case for issues_remove_all_labels

    Remove all labels from an issue
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/repos/{owner}/{repo}/issues/{issue_number}/labels'.format(owner='owner_example', repo='repo_example', issue_number=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issues_remove_assignees(client):
    """Test case for issues_remove_assignees

    Remove assignees from an issue
    """
    body = {"assignees":["hubot","other_user"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/repos/{owner}/{repo}/issues/{issue_number}/assignees'.format(owner='owner_example', repo='repo_example', issue_number=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issues_remove_label(client):
    """Test case for issues_remove_label

    Remove a label from an issue
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/repos/{owner}/{repo}/issues/{issue_number}/labels/{name}'.format(owner='owner_example', repo='repo_example', issue_number=56, name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issues_set_labels(client):
    """Test case for issues_set_labels

    Set labels for an issue
    """
    body = {"labels":["bug","enhancement"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/repos/{owner}/{repo}/issues/{issue_number}/labels'.format(owner='owner_example', repo='repo_example', issue_number=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issues_unlock(client):
    """Test case for issues_unlock

    Unlock an issue
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/repos/{owner}/{repo}/issues/{issue_number}/lock'.format(owner='owner_example', repo='repo_example', issue_number=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issues_update(client):
    """Test case for issues_update

    Update an issue
    """
    body = {"assignees":["octocat"],"body":"I'm having a problem with this.","labels":["bug"],"milestone":1,"state":"open","title":"Found a bug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/repos/{owner}/{repo}/issues/{issue_number}'.format(owner='owner_example', repo='repo_example', issue_number=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issues_update_comment(client):
    """Test case for issues_update_comment

    Update an issue comment
    """
    body = {"body":"Me too"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/repos/{owner}/{repo}/issues/comments/{comment_id}'.format(owner='owner_example', repo='repo_example', comment_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issues_update_label(client):
    """Test case for issues_update_label

    Update a label
    """
    body = {"color":"b01f26","description":"Small bug fix required","new_name":"bug :bug:"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/repos/{owner}/{repo}/labels/{name}'.format(owner='owner_example', repo='repo_example', name='name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issues_update_milestone(client):
    """Test case for issues_update_milestone

    Update a milestone
    """
    body = {"description":"Tracking milestone for version 1.0","due_on":"2012-10-09T23:39:01Z","state":"open","title":"v1.0"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/repos/{owner}/{repo}/milestones/{milestone_number}'.format(owner='owner_example', repo='repo_example', milestone_number=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

