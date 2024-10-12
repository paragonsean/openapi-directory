# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.apps_get_installation415_response import AppsGetInstallation415Response
from openapi_server.models.basic_error import BasicError
from openapi_server.models.reaction import Reaction
from openapi_server.models.reactions_create_for_commit_comment_request import ReactionsCreateForCommitCommentRequest
from openapi_server.models.reactions_create_for_issue_comment_request import ReactionsCreateForIssueCommentRequest
from openapi_server.models.reactions_create_for_issue_request import ReactionsCreateForIssueRequest
from openapi_server.models.reactions_create_for_pull_request_review_comment_request import ReactionsCreateForPullRequestReviewCommentRequest
from openapi_server.models.reactions_create_for_team_discussion_comment_request import ReactionsCreateForTeamDiscussionCommentRequest
from openapi_server.models.reactions_create_for_team_discussion_request import ReactionsCreateForTeamDiscussionRequest
from openapi_server.models.validation_error import ValidationError


pytestmark = pytest.mark.asyncio

async def test_reactions_create_for_commit_comment(client):
    """Test case for reactions_create_for_commit_comment

    Create reaction for a commit comment
    """
    body = {"content":"heart"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/repos/{owner}/{repo}/comments/{comment_id}/reactions'.format(owner='owner_example', repo='repo_example', comment_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reactions_create_for_issue(client):
    """Test case for reactions_create_for_issue

    Create reaction for an issue
    """
    body = {"content":"heart"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/repos/{owner}/{repo}/issues/{issue_number}/reactions'.format(owner='owner_example', repo='repo_example', issue_number=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reactions_create_for_issue_comment(client):
    """Test case for reactions_create_for_issue_comment

    Create reaction for an issue comment
    """
    body = {"content":"heart"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/repos/{owner}/{repo}/issues/comments/{comment_id}/reactions'.format(owner='owner_example', repo='repo_example', comment_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reactions_create_for_pull_request_review_comment(client):
    """Test case for reactions_create_for_pull_request_review_comment

    Create reaction for a pull request review comment
    """
    body = {"content":"heart"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/repos/{owner}/{repo}/pulls/comments/{comment_id}/reactions'.format(owner='owner_example', repo='repo_example', comment_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reactions_create_for_team_discussion(client):
    """Test case for reactions_create_for_team_discussion

    Create reaction for a team discussion
    """
    body = {"content":"heart"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'accept': 'application/vnd.github.squirrel-girl-preview+json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/teams/{team_id}/discussions/{discussion_number}/reactions'.format(team_id=56, discussion_number=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reactions_create_for_team_discussion_comment(client):
    """Test case for reactions_create_for_team_discussion_comment

    Create reaction for a team discussion comment
    """
    body = {"content":"heart"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'accept': 'application/vnd.github.squirrel-girl-preview+json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/teams/{team_id}/discussions/{discussion_number}/comments/{comment_number}/reactions'.format(team_id=56, discussion_number=56, comment_number=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reactions_delete(client):
    """Test case for reactions_delete

    Delete a reaction
    """
    headers = { 
        'accept': 'application/vnd.github.squirrel-girl-preview+json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/reactions/{reaction_id}'.format(reaction_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reactions_list_for_commit_comment(client):
    """Test case for reactions_list_for_commit_comment

    List reactions for a commit comment
    """
    params = [('content', 'content_example'),
                    ('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/comments/{comment_id}/reactions'.format(owner='owner_example', repo='repo_example', comment_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reactions_list_for_issue(client):
    """Test case for reactions_list_for_issue

    List reactions for an issue
    """
    params = [('content', 'content_example'),
                    ('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/issues/{issue_number}/reactions'.format(owner='owner_example', repo='repo_example', issue_number=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reactions_list_for_issue_comment(client):
    """Test case for reactions_list_for_issue_comment

    List reactions for an issue comment
    """
    params = [('content', 'content_example'),
                    ('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/issues/comments/{comment_id}/reactions'.format(owner='owner_example', repo='repo_example', comment_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reactions_list_for_pull_request_review_comment(client):
    """Test case for reactions_list_for_pull_request_review_comment

    List reactions for a pull request review comment
    """
    params = [('content', 'content_example'),
                    ('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/pulls/comments/{comment_id}/reactions'.format(owner='owner_example', repo='repo_example', comment_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reactions_list_for_team_discussion(client):
    """Test case for reactions_list_for_team_discussion

    List reactions for a team discussion
    """
    params = [('content', 'content_example'),
                    ('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
        'accept': 'application/vnd.github.squirrel-girl-preview+json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/teams/{team_id}/discussions/{discussion_number}/reactions'.format(team_id=56, discussion_number=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reactions_list_for_team_discussion_comment(client):
    """Test case for reactions_list_for_team_discussion_comment

    List reactions for a team discussion comment
    """
    params = [('content', 'content_example'),
                    ('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
        'accept': 'application/vnd.github.squirrel-girl-preview+json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/teams/{team_id}/discussions/{discussion_number}/comments/{comment_number}/reactions'.format(team_id=56, discussion_number=56, comment_number=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

