# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.basic_error import BasicError
from openapi_server.models.reaction import Reaction
from openapi_server.models.reactions_create_for_commit_comment415_response import ReactionsCreateForCommitComment415Response
from openapi_server.models.reactions_create_for_commit_comment_request import ReactionsCreateForCommitCommentRequest
from openapi_server.models.reactions_create_for_issue_comment_request import ReactionsCreateForIssueCommentRequest
from openapi_server.models.reactions_create_for_issue_request import ReactionsCreateForIssueRequest
from openapi_server.models.reactions_create_for_pull_request_review_comment_request import ReactionsCreateForPullRequestReviewCommentRequest
from openapi_server.models.reactions_create_for_team_discussion_comment_in_org_request import ReactionsCreateForTeamDiscussionCommentInOrgRequest
from openapi_server.models.reactions_create_for_team_discussion_in_org_request import ReactionsCreateForTeamDiscussionInOrgRequest
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

async def test_reactions_create_for_team_discussion_comment_in_org(client):
    """Test case for reactions_create_for_team_discussion_comment_in_org

    Create reaction for a team discussion comment
    """
    body = {"content":"heart"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/comments/{comment_number}/reactions'.format(org='org_example', team_slug='team_slug_example', discussion_number=56, comment_number=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reactions_create_for_team_discussion_comment_legacy(client):
    """Test case for reactions_create_for_team_discussion_comment_legacy

    Create reaction for a team discussion comment (Legacy)
    """
    body = {"content":"heart"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/teams/{team_id}/discussions/{discussion_number}/comments/{comment_number}/reactions'.format(team_id=56, discussion_number=56, comment_number=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reactions_create_for_team_discussion_in_org(client):
    """Test case for reactions_create_for_team_discussion_in_org

    Create reaction for a team discussion
    """
    body = {"content":"heart"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/reactions'.format(org='org_example', team_slug='team_slug_example', discussion_number=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reactions_create_for_team_discussion_legacy(client):
    """Test case for reactions_create_for_team_discussion_legacy

    Create reaction for a team discussion (Legacy)
    """
    body = {"content":"heart"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/teams/{team_id}/discussions/{discussion_number}/reactions'.format(team_id=56, discussion_number=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reactions_delete_for_commit_comment(client):
    """Test case for reactions_delete_for_commit_comment

    Delete a commit comment reaction
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/repos/{owner}/{repo}/comments/{comment_id}/reactions/{reaction_id}'.format(owner='owner_example', repo='repo_example', comment_id=56, reaction_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reactions_delete_for_issue(client):
    """Test case for reactions_delete_for_issue

    Delete an issue reaction
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/repos/{owner}/{repo}/issues/{issue_number}/reactions/{reaction_id}'.format(owner='owner_example', repo='repo_example', issue_number=56, reaction_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reactions_delete_for_issue_comment(client):
    """Test case for reactions_delete_for_issue_comment

    Delete an issue comment reaction
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/repos/{owner}/{repo}/issues/comments/{comment_id}/reactions/{reaction_id}'.format(owner='owner_example', repo='repo_example', comment_id=56, reaction_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reactions_delete_for_pull_request_comment(client):
    """Test case for reactions_delete_for_pull_request_comment

    Delete a pull request comment reaction
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/repos/{owner}/{repo}/pulls/comments/{comment_id}/reactions/{reaction_id}'.format(owner='owner_example', repo='repo_example', comment_id=56, reaction_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reactions_delete_for_team_discussion(client):
    """Test case for reactions_delete_for_team_discussion

    Delete team discussion reaction
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/reactions/{reaction_id}'.format(org='org_example', team_slug='team_slug_example', discussion_number=56, reaction_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reactions_delete_for_team_discussion_comment(client):
    """Test case for reactions_delete_for_team_discussion_comment

    Delete team discussion comment reaction
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/comments/{comment_number}/reactions/{reaction_id}'.format(org='org_example', team_slug='team_slug_example', discussion_number=56, comment_number=56, reaction_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reactions_delete_legacy(client):
    """Test case for reactions_delete_legacy

    Delete a reaction (Legacy)
    """
    headers = { 
        'Accept': 'application/json',
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

async def test_reactions_list_for_team_discussion_comment_in_org(client):
    """Test case for reactions_list_for_team_discussion_comment_in_org

    List reactions for a team discussion comment
    """
    params = [('content', 'content_example'),
                    ('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/comments/{comment_number}/reactions'.format(org='org_example', team_slug='team_slug_example', discussion_number=56, comment_number=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reactions_list_for_team_discussion_comment_legacy(client):
    """Test case for reactions_list_for_team_discussion_comment_legacy

    List reactions for a team discussion comment (Legacy)
    """
    params = [('content', 'content_example'),
                    ('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/teams/{team_id}/discussions/{discussion_number}/comments/{comment_number}/reactions'.format(team_id=56, discussion_number=56, comment_number=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reactions_list_for_team_discussion_in_org(client):
    """Test case for reactions_list_for_team_discussion_in_org

    List reactions for a team discussion
    """
    params = [('content', 'content_example'),
                    ('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/reactions'.format(org='org_example', team_slug='team_slug_example', discussion_number=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reactions_list_for_team_discussion_legacy(client):
    """Test case for reactions_list_for_team_discussion_legacy

    List reactions for a team discussion (Legacy)
    """
    params = [('content', 'content_example'),
                    ('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/teams/{team_id}/discussions/{discussion_number}/reactions'.format(team_id=56, discussion_number=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

