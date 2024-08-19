# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData
from aiohttp import FormData

from openapi_server.models.add_time_option import AddTimeOption
from openapi_server.models.attachment import Attachment
from openapi_server.models.comment import Comment
from openapi_server.models.create_issue_comment_option import CreateIssueCommentOption
from openapi_server.models.create_issue_option import CreateIssueOption
from openapi_server.models.create_label_option import CreateLabelOption
from openapi_server.models.create_milestone_option import CreateMilestoneOption
from openapi_server.models.edit_attachment_options import EditAttachmentOptions
from openapi_server.models.edit_deadline_option import EditDeadlineOption
from openapi_server.models.edit_issue_comment_option import EditIssueCommentOption
from openapi_server.models.edit_issue_option import EditIssueOption
from openapi_server.models.edit_label_option import EditLabelOption
from openapi_server.models.edit_milestone_option import EditMilestoneOption
from openapi_server.models.edit_reaction_option import EditReactionOption
from openapi_server.models.issue import Issue
from openapi_server.models.issue_deadline import IssueDeadline
from openapi_server.models.issue_labels_option import IssueLabelsOption
from openapi_server.models.issue_meta import IssueMeta
from openapi_server.models.label import Label
from openapi_server.models.milestone import Milestone
from openapi_server.models.reaction import Reaction
from openapi_server.models.timeline_comment import TimelineComment
from openapi_server.models.tracked_time import TrackedTime
from openapi_server.models.user import User
from openapi_server.models.watch_info import WatchInfo


pytestmark = pytest.mark.asyncio

async def test_issue_add_label(client):
    """Test case for issue_add_label

    Add a label to an issue
    """
    body = {"labels":[0,0]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/repos/{owner}/{repo}/issues/{index}/labels'.format(owner='owner_example', repo='repo_example', index=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issue_add_subscription(client):
    """Test case for issue_add_subscription

    Subscribe user to issue
    """
    headers = { 
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/repos/{owner}/{repo}/issues/{index}/subscriptions/{user}'.format(owner='owner_example', repo='repo_example', index=56, user='user_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issue_add_time(client):
    """Test case for issue_add_time

    Add tracked time to a issue
    """
    body = {"created":"2000-01-23T04:56:07.000+00:00","user_name":"user_name","time":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/repos/{owner}/{repo}/issues/{index}/times'.format(owner='owner_example', repo='repo_example', index=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issue_check_subscription(client):
    """Test case for issue_check_subscription

    Check if user is subscribed to an issue
    """
    headers = { 
        'Accept': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/repos/{owner}/{repo}/issues/{index}/subscriptions/check'.format(owner='owner_example', repo='repo_example', index=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issue_clear_labels(client):
    """Test case for issue_clear_labels

    Remove all labels from an issue
    """
    headers = { 
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/repos/{owner}/{repo}/issues/{index}/labels'.format(owner='owner_example', repo='repo_example', index=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issue_create_comment(client):
    """Test case for issue_create_comment

    Add a comment to an issue
    """
    body = {"body":"body"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/repos/{owner}/{repo}/issues/{index}/comments'.format(owner='owner_example', repo='repo_example', index=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issue_create_issue(client):
    """Test case for issue_create_issue

    Create an issue. If using deadline only the date will be taken into account, and time of day ignored.
    """
    body = {"ref":"ref","milestone":6,"due_date":"2000-01-23T04:56:07.000+00:00","assignees":["assignees","assignees"],"closed":True,"assignee":"assignee","body":"body","title":"title","labels":[0,0]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/repos/{owner}/{repo}/issues'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_issue_create_issue_attachment(client):
    """Test case for issue_create_issue_attachment

    Create an issue attachment
    """
    params = [('name', 'name_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    data = FormData()
    data.add_field('attachment', '/path/to/file')
    response = await client.request(
        method='POST',
        path='/api/v1/repos/{owner}/{repo}/issues/{index}/assets'.format(owner='owner_example', repo='repo_example', index=56),
        headers=headers,
        data=data,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_issue_create_issue_blocking(client):
    """Test case for issue_create_issue_blocking

    Block the issue given in the body by the issue in path
    """
    body = {"owner":"owner","repo":"repo","index":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/repos/{owner}/{repo}/issues/{index}/blocks'.format(owner='owner_example', repo='repo_example', index='index_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_issue_create_issue_comment_attachment(client):
    """Test case for issue_create_issue_comment_attachment

    Create a comment attachment
    """
    params = [('name', 'name_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    data = FormData()
    data.add_field('attachment', '/path/to/file')
    response = await client.request(
        method='POST',
        path='/api/v1/repos/{owner}/{repo}/issues/comments/{id}/assets'.format(owner='owner_example', repo='repo_example', id=56),
        headers=headers,
        data=data,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_issue_create_issue_dependencies(client):
    """Test case for issue_create_issue_dependencies

    Make the issue in the url depend on the issue in the form.
    """
    body = {"owner":"owner","repo":"repo","index":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/repos/{owner}/{repo}/issues/{index}/dependencies'.format(owner='owner_example', repo='repo_example', index='index_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issue_create_label(client):
    """Test case for issue_create_label

    Create a label
    """
    body = {"color":"#00aabb","name":"name","description":"description","exclusive":False}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/repos/{owner}/{repo}/labels'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issue_create_milestone(client):
    """Test case for issue_create_milestone

    Create a milestone
    """
    body = {"description":"description","state":"open","title":"title","due_on":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/repos/{owner}/{repo}/milestones'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issue_delete(client):
    """Test case for issue_delete

    Delete an issue
    """
    headers = { 
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/repos/{owner}/{repo}/issues/{index}'.format(owner='owner_example', repo='repo_example', index=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issue_delete_comment(client):
    """Test case for issue_delete_comment

    Delete a comment
    """
    headers = { 
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/repos/{owner}/{repo}/issues/comments/{id}'.format(owner='owner_example', repo='repo_example', id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issue_delete_comment_deprecated(client):
    """Test case for issue_delete_comment_deprecated

    Delete a comment
    """
    headers = { 
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/repos/{owner}/{repo}/issues/{index}/comments/{id}'.format(owner='owner_example', repo='repo_example', index=56, id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issue_delete_comment_reaction(client):
    """Test case for issue_delete_comment_reaction

    Remove a reaction from a comment of an issue
    """
    body = {"content":"content"}
    headers = { 
        'Content-Type': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/repos/{owner}/{repo}/issues/comments/{id}/reactions'.format(owner='owner_example', repo='repo_example', id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issue_delete_issue_attachment(client):
    """Test case for issue_delete_issue_attachment

    Delete an issue attachment
    """
    headers = { 
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/repos/{owner}/{repo}/issues/{index}/assets/{attachment_id}'.format(owner='owner_example', repo='repo_example', index=56, attachment_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issue_delete_issue_comment_attachment(client):
    """Test case for issue_delete_issue_comment_attachment

    Delete a comment attachment
    """
    headers = { 
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/repos/{owner}/{repo}/issues/comments/{id}/assets/{attachment_id}'.format(owner='owner_example', repo='repo_example', id=56, attachment_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issue_delete_issue_reaction(client):
    """Test case for issue_delete_issue_reaction

    Remove a reaction from an issue
    """
    body = {"content":"content"}
    headers = { 
        'Content-Type': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/repos/{owner}/{repo}/issues/{index}/reactions'.format(owner='owner_example', repo='repo_example', index=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issue_delete_label(client):
    """Test case for issue_delete_label

    Delete a label
    """
    headers = { 
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/repos/{owner}/{repo}/labels/{id}'.format(owner='owner_example', repo='repo_example', id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issue_delete_milestone(client):
    """Test case for issue_delete_milestone

    Delete a milestone
    """
    headers = { 
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/repos/{owner}/{repo}/milestones/{id}'.format(owner='owner_example', repo='repo_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issue_delete_stop_watch(client):
    """Test case for issue_delete_stop_watch

    Delete an issue's existing stopwatch.
    """
    headers = { 
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/repos/{owner}/{repo}/issues/{index}/stopwatch/delete'.format(owner='owner_example', repo='repo_example', index=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issue_delete_subscription(client):
    """Test case for issue_delete_subscription

    Unsubscribe user from issue
    """
    headers = { 
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/repos/{owner}/{repo}/issues/{index}/subscriptions/{user}'.format(owner='owner_example', repo='repo_example', index=56, user='user_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issue_delete_time(client):
    """Test case for issue_delete_time

    Delete specific tracked time
    """
    headers = { 
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/repos/{owner}/{repo}/issues/{index}/times/{id}'.format(owner='owner_example', repo='repo_example', index=56, id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issue_edit_comment(client):
    """Test case for issue_edit_comment

    Edit a comment
    """
    body = {"body":"body"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/repos/{owner}/{repo}/issues/comments/{id}'.format(owner='owner_example', repo='repo_example', id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issue_edit_comment_deprecated(client):
    """Test case for issue_edit_comment_deprecated

    Edit a comment
    """
    body = {"body":"body"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/repos/{owner}/{repo}/issues/{index}/comments/{id}'.format(owner='owner_example', repo='repo_example', index=56, id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issue_edit_issue(client):
    """Test case for issue_edit_issue

    Edit an issue. If using deadline only the date will be taken into account, and time of day ignored.
    """
    body = {"unset_due_date":True,"ref":"ref","milestone":0,"due_date":"2000-01-23T04:56:07.000+00:00","assignees":["assignees","assignees"],"assignee":"assignee","state":"state","body":"body","title":"title"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/repos/{owner}/{repo}/issues/{index}'.format(owner='owner_example', repo='repo_example', index=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issue_edit_issue_attachment(client):
    """Test case for issue_edit_issue_attachment

    Edit an issue attachment
    """
    body = {"name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/repos/{owner}/{repo}/issues/{index}/assets/{attachment_id}'.format(owner='owner_example', repo='repo_example', index=56, attachment_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issue_edit_issue_comment_attachment(client):
    """Test case for issue_edit_issue_comment_attachment

    Edit a comment attachment
    """
    body = {"name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/repos/{owner}/{repo}/issues/comments/{id}/assets/{attachment_id}'.format(owner='owner_example', repo='repo_example', id=56, attachment_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issue_edit_issue_deadline(client):
    """Test case for issue_edit_issue_deadline

    Set an issue deadline. If set to null, the deadline is deleted. If using deadline only the date will be taken into account, and time of day ignored.
    """
    body = {"due_date":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/repos/{owner}/{repo}/issues/{index}/deadline'.format(owner='owner_example', repo='repo_example', index=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issue_edit_label(client):
    """Test case for issue_edit_label

    Update a label
    """
    body = {"color":"#00aabb","name":"name","description":"description","exclusive":False}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/repos/{owner}/{repo}/labels/{id}'.format(owner='owner_example', repo='repo_example', id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issue_edit_milestone(client):
    """Test case for issue_edit_milestone

    Update a milestone
    """
    body = {"description":"description","state":"state","title":"title","due_on":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/repos/{owner}/{repo}/milestones/{id}'.format(owner='owner_example', repo='repo_example', id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issue_get_comment(client):
    """Test case for issue_get_comment

    Get a comment
    """
    headers = { 
        'Accept': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/repos/{owner}/{repo}/issues/comments/{id}'.format(owner='owner_example', repo='repo_example', id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issue_get_comment_reactions(client):
    """Test case for issue_get_comment_reactions

    Get a list of reactions from a comment of an issue
    """
    headers = { 
        'Accept': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/repos/{owner}/{repo}/issues/comments/{id}/reactions'.format(owner='owner_example', repo='repo_example', id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issue_get_comments(client):
    """Test case for issue_get_comments

    List all comments on an issue
    """
    params = [('since', '2013-10-20T19:20:30+01:00'),
                    ('before', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/repos/{owner}/{repo}/issues/{index}/comments'.format(owner='owner_example', repo='repo_example', index=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issue_get_comments_and_timeline(client):
    """Test case for issue_get_comments_and_timeline

    List all comments and events on an issue
    """
    params = [('since', '2013-10-20T19:20:30+01:00'),
                    ('page', 56),
                    ('limit', 56),
                    ('before', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/repos/{owner}/{repo}/issues/{index}/timeline'.format(owner='owner_example', repo='repo_example', index=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issue_get_issue(client):
    """Test case for issue_get_issue

    Get an issue
    """
    headers = { 
        'Accept': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/repos/{owner}/{repo}/issues/{index}'.format(owner='owner_example', repo='repo_example', index=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issue_get_issue_attachment(client):
    """Test case for issue_get_issue_attachment

    Get an issue attachment
    """
    headers = { 
        'Accept': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/repos/{owner}/{repo}/issues/{index}/assets/{attachment_id}'.format(owner='owner_example', repo='repo_example', index=56, attachment_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issue_get_issue_comment_attachment(client):
    """Test case for issue_get_issue_comment_attachment

    Get a comment attachment
    """
    headers = { 
        'Accept': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/repos/{owner}/{repo}/issues/comments/{id}/assets/{attachment_id}'.format(owner='owner_example', repo='repo_example', id=56, attachment_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issue_get_issue_reactions(client):
    """Test case for issue_get_issue_reactions

    Get a list reactions of an issue
    """
    params = [('page', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/repos/{owner}/{repo}/issues/{index}/reactions'.format(owner='owner_example', repo='repo_example', index=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issue_get_label(client):
    """Test case for issue_get_label

    Get a single label
    """
    headers = { 
        'Accept': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/repos/{owner}/{repo}/labels/{id}'.format(owner='owner_example', repo='repo_example', id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issue_get_labels(client):
    """Test case for issue_get_labels

    Get an issue's labels
    """
    headers = { 
        'Accept': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/repos/{owner}/{repo}/issues/{index}/labels'.format(owner='owner_example', repo='repo_example', index=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issue_get_milestone(client):
    """Test case for issue_get_milestone

    Get a milestone
    """
    headers = { 
        'Accept': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/repos/{owner}/{repo}/milestones/{id}'.format(owner='owner_example', repo='repo_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issue_get_milestones_list(client):
    """Test case for issue_get_milestones_list

    Get all of a repository's opened milestones
    """
    params = [('state', 'state_example'),
                    ('name', 'name_example'),
                    ('page', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/repos/{owner}/{repo}/milestones'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issue_get_repo_comments(client):
    """Test case for issue_get_repo_comments

    List all comments in a repository
    """
    params = [('since', '2013-10-20T19:20:30+01:00'),
                    ('before', '2013-10-20T19:20:30+01:00'),
                    ('page', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/repos/{owner}/{repo}/issues/comments'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issue_list_blocks(client):
    """Test case for issue_list_blocks

    List issues that are blocked by this issue
    """
    params = [('page', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/repos/{owner}/{repo}/issues/{index}/blocks'.format(owner='owner_example', repo='repo_example', index='index_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issue_list_issue_attachments(client):
    """Test case for issue_list_issue_attachments

    List issue's attachments
    """
    headers = { 
        'Accept': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/repos/{owner}/{repo}/issues/{index}/assets'.format(owner='owner_example', repo='repo_example', index=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issue_list_issue_comment_attachments(client):
    """Test case for issue_list_issue_comment_attachments

    List comment's attachments
    """
    headers = { 
        'Accept': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/repos/{owner}/{repo}/issues/comments/{id}/assets'.format(owner='owner_example', repo='repo_example', id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issue_list_issue_dependencies(client):
    """Test case for issue_list_issue_dependencies

    List an issue's dependencies, i.e all issues that block this issue.
    """
    params = [('page', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/repos/{owner}/{repo}/issues/{index}/dependencies'.format(owner='owner_example', repo='repo_example', index='index_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issue_list_issues(client):
    """Test case for issue_list_issues

    List a repository's issues
    """
    params = [('state', 'state_example'),
                    ('labels', 'labels_example'),
                    ('q', 'q_example'),
                    ('type', 'type_example'),
                    ('milestones', 'milestones_example'),
                    ('since', '2013-10-20T19:20:30+01:00'),
                    ('before', '2013-10-20T19:20:30+01:00'),
                    ('created_by', 'created_by_example'),
                    ('assigned_by', 'assigned_by_example'),
                    ('mentioned_by', 'mentioned_by_example'),
                    ('page', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/repos/{owner}/{repo}/issues'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issue_list_labels(client):
    """Test case for issue_list_labels

    Get all of a repository's labels
    """
    params = [('page', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/repos/{owner}/{repo}/labels'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issue_post_comment_reaction(client):
    """Test case for issue_post_comment_reaction

    Add a reaction to a comment of an issue
    """
    body = {"content":"content"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/repos/{owner}/{repo}/issues/comments/{id}/reactions'.format(owner='owner_example', repo='repo_example', id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issue_post_issue_reaction(client):
    """Test case for issue_post_issue_reaction

    Add a reaction to an issue
    """
    body = {"content":"content"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/repos/{owner}/{repo}/issues/{index}/reactions'.format(owner='owner_example', repo='repo_example', index=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_issue_remove_issue_blocking(client):
    """Test case for issue_remove_issue_blocking

    Unblock the issue given in the body by the issue in path
    """
    body = {"owner":"owner","repo":"repo","index":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/repos/{owner}/{repo}/issues/{index}/blocks'.format(owner='owner_example', repo='repo_example', index='index_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_issue_remove_issue_dependencies(client):
    """Test case for issue_remove_issue_dependencies

    Remove an issue dependency
    """
    body = {"owner":"owner","repo":"repo","index":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/repos/{owner}/{repo}/issues/{index}/dependencies'.format(owner='owner_example', repo='repo_example', index='index_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issue_remove_label(client):
    """Test case for issue_remove_label

    Remove a label from an issue
    """
    headers = { 
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/repos/{owner}/{repo}/issues/{index}/labels/{id}'.format(owner='owner_example', repo='repo_example', index=56, id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issue_replace_labels(client):
    """Test case for issue_replace_labels

    Replace an issue's labels
    """
    body = {"labels":[0,0]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/repos/{owner}/{repo}/issues/{index}/labels'.format(owner='owner_example', repo='repo_example', index=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issue_reset_time(client):
    """Test case for issue_reset_time

    Reset a tracked time of an issue
    """
    headers = { 
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/repos/{owner}/{repo}/issues/{index}/times'.format(owner='owner_example', repo='repo_example', index=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issue_search_issues(client):
    """Test case for issue_search_issues

    Search for issues across the repositories that the user has access to
    """
    params = [('state', 'state_example'),
                    ('labels', 'labels_example'),
                    ('milestones', 'milestones_example'),
                    ('q', 'q_example'),
                    ('priority_repo_id', 56),
                    ('type', 'type_example'),
                    ('since', '2013-10-20T19:20:30+01:00'),
                    ('before', '2013-10-20T19:20:30+01:00'),
                    ('assigned', True),
                    ('created', True),
                    ('mentioned', True),
                    ('review_requested', True),
                    ('reviewed', True),
                    ('owner', 'owner_example'),
                    ('team', 'team_example'),
                    ('page', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/repos/issues/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issue_start_stop_watch(client):
    """Test case for issue_start_stop_watch

    Start stopwatch on an issue.
    """
    headers = { 
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/repos/{owner}/{repo}/issues/{index}/stopwatch/start'.format(owner='owner_example', repo='repo_example', index=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issue_stop_stop_watch(client):
    """Test case for issue_stop_stop_watch

    Stop an issue's existing stopwatch.
    """
    headers = { 
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/repos/{owner}/{repo}/issues/{index}/stopwatch/stop'.format(owner='owner_example', repo='repo_example', index=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issue_subscriptions(client):
    """Test case for issue_subscriptions

    Get users who subscribed on an issue.
    """
    params = [('page', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/repos/{owner}/{repo}/issues/{index}/subscriptions'.format(owner='owner_example', repo='repo_example', index=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issue_tracked_times(client):
    """Test case for issue_tracked_times

    List an issue's tracked times
    """
    params = [('user', 'user_example'),
                    ('since', '2013-10-20T19:20:30+01:00'),
                    ('before', '2013-10-20T19:20:30+01:00'),
                    ('page', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/repos/{owner}/{repo}/issues/{index}/times'.format(owner='owner_example', repo='repo_example', index=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

