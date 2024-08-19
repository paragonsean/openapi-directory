# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.apps_get_installation415_response import AppsGetInstallation415Response
from openapi_server.models.basic_error import BasicError
from openapi_server.models.commit import Commit
from openapi_server.models.diff_entry import DiffEntry
from openapi_server.models.enterprise_admin_update_org_name202_response import EnterpriseAdminUpdateOrgName202Response
from openapi_server.models.orgs_remove_outside_collaborator422_response import OrgsRemoveOutsideCollaborator422Response
from openapi_server.models.pull_request import PullRequest
from openapi_server.models.pull_request_merge_result import PullRequestMergeResult
from openapi_server.models.pull_request_review import PullRequestReview
from openapi_server.models.pull_request_review_comment import PullRequestReviewComment
from openapi_server.models.pull_request_review_request import PullRequestReviewRequest
from openapi_server.models.pull_request_simple import PullRequestSimple
from openapi_server.models.pulls_create_reply_for_review_comment_request import PullsCreateReplyForReviewCommentRequest
from openapi_server.models.pulls_create_request import PullsCreateRequest
from openapi_server.models.pulls_create_review_comment_request import PullsCreateReviewCommentRequest
from openapi_server.models.pulls_create_review_request import PullsCreateReviewRequest
from openapi_server.models.pulls_dismiss_review_request import PullsDismissReviewRequest
from openapi_server.models.pulls_merge_request import PullsMergeRequest
from openapi_server.models.pulls_remove_requested_reviewers_request import PullsRemoveRequestedReviewersRequest
from openapi_server.models.pulls_request_reviewers_request import PullsRequestReviewersRequest
from openapi_server.models.pulls_submit_review_request import PullsSubmitReviewRequest
from openapi_server.models.pulls_update_branch_request import PullsUpdateBranchRequest
from openapi_server.models.pulls_update_request import PullsUpdateRequest
from openapi_server.models.pulls_update_review_comment_request import PullsUpdateReviewCommentRequest
from openapi_server.models.pulls_update_review_request import PullsUpdateReviewRequest
from openapi_server.models.review_comment import ReviewComment
from openapi_server.models.validation_error import ValidationError
from openapi_server.models.validation_error_simple import ValidationErrorSimple


pytestmark = pytest.mark.asyncio

async def test_pulls_check_if_merged(client):
    """Test case for pulls_check_if_merged

    Check if a pull request has been merged
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/pulls/{pull_number}/merge'.format(owner='owner_example', repo='repo_example', pull_number=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pulls_create(client):
    """Test case for pulls_create

    Create a pull request
    """
    body = {"base":"master","body":"Please pull these awesome changes in!","head":"octocat:new-feature","title":"Amazing new feature"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/repos/{owner}/{repo}/pulls'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pulls_create_reply_for_review_comment(client):
    """Test case for pulls_create_reply_for_review_comment

    Create a reply for a review comment
    """
    body = {"body":"Great stuff!"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/repos/{owner}/{repo}/pulls/{pull_number}/comments/{comment_id}/replies'.format(owner='owner_example', repo='repo_example', pull_number=56, comment_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pulls_create_review(client):
    """Test case for pulls_create_review

    Create a review for a pull request
    """
    body = {"body":"This is close to perfect! Please address the suggested inline change.","comments":[{"body":"Please add more information here, and fix this typo.","path":"file.md","position":6}],"commit_id":"ecdd80bb57125d7ba9641ffaa4d7d2c19d3f3091","event":"REQUEST_CHANGES"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/repos/{owner}/{repo}/pulls/{pull_number}/reviews'.format(owner='owner_example', repo='repo_example', pull_number=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pulls_create_review_comment(client):
    """Test case for pulls_create_review_comment

    Create a review comment for a pull request
    """
    body = {"body":"Great stuff!","commit_id":"6dcb09b5b57875f334f61aebed695e2e4193db5e","line":2,"path":"file1.txt","side":"RIGHT","start_line":1,"start_side":"RIGHT"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/repos/{owner}/{repo}/pulls/{pull_number}/comments'.format(owner='owner_example', repo='repo_example', pull_number=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pulls_delete_pending_review(client):
    """Test case for pulls_delete_pending_review

    Delete a pending review for a pull request
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}'.format(owner='owner_example', repo='repo_example', pull_number=56, review_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pulls_delete_review_comment(client):
    """Test case for pulls_delete_review_comment

    Delete a review comment for a pull request
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/repos/{owner}/{repo}/pulls/comments/{comment_id}'.format(owner='owner_example', repo='repo_example', comment_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pulls_dismiss_review(client):
    """Test case for pulls_dismiss_review

    Dismiss a review for a pull request
    """
    body = openapi_server.PullsDismissReviewRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}/dismissals'.format(owner='owner_example', repo='repo_example', pull_number=56, review_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pulls_get(client):
    """Test case for pulls_get

    Get a pull request
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/pulls/{pull_number}'.format(owner='owner_example', repo='repo_example', pull_number=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pulls_get_review(client):
    """Test case for pulls_get_review

    Get a review for a pull request
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}'.format(owner='owner_example', repo='repo_example', pull_number=56, review_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pulls_get_review_comment(client):
    """Test case for pulls_get_review_comment

    Get a review comment for a pull request
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/pulls/comments/{comment_id}'.format(owner='owner_example', repo='repo_example', comment_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pulls_list(client):
    """Test case for pulls_list

    List pull requests
    """
    params = [('state', open),
                    ('head', 'head_example'),
                    ('base', 'base_example'),
                    ('sort', created),
                    ('direction', 'direction_example'),
                    ('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/pulls'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pulls_list_comments_for_review(client):
    """Test case for pulls_list_comments_for_review

    List comments for a pull request review
    """
    params = [('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}/comments'.format(owner='owner_example', repo='repo_example', pull_number=56, review_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pulls_list_commits(client):
    """Test case for pulls_list_commits

    List commits on a pull request
    """
    params = [('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/pulls/{pull_number}/commits'.format(owner='owner_example', repo='repo_example', pull_number=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pulls_list_files(client):
    """Test case for pulls_list_files

    List pull requests files
    """
    params = [('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/pulls/{pull_number}/files'.format(owner='owner_example', repo='repo_example', pull_number=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pulls_list_requested_reviewers(client):
    """Test case for pulls_list_requested_reviewers

    List requested reviewers for a pull request
    """
    params = [('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewers'.format(owner='owner_example', repo='repo_example', pull_number=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pulls_list_review_comments(client):
    """Test case for pulls_list_review_comments

    List review comments on a pull request
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
        path='/api/v3/repos/{owner}/{repo}/pulls/{pull_number}/comments'.format(owner='owner_example', repo='repo_example', pull_number=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pulls_list_review_comments_for_repo(client):
    """Test case for pulls_list_review_comments_for_repo

    List review comments in a repository
    """
    params = [('sort', 'sort_example'),
                    ('direction', 'direction_example'),
                    ('since', '2013-10-20T19:20:30+01:00'),
                    ('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/pulls/comments'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pulls_list_reviews(client):
    """Test case for pulls_list_reviews

    List reviews for a pull request
    """
    params = [('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/pulls/{pull_number}/reviews'.format(owner='owner_example', repo='repo_example', pull_number=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pulls_merge(client):
    """Test case for pulls_merge

    Merge a pull request
    """
    body = openapi_server.PullsMergeRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/repos/{owner}/{repo}/pulls/{pull_number}/merge'.format(owner='owner_example', repo='repo_example', pull_number=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pulls_remove_requested_reviewers(client):
    """Test case for pulls_remove_requested_reviewers

    Remove requested reviewers from a pull request
    """
    body = {"reviewers":["octocat","hubot","other_user"],"team_reviewers":["justice-league"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewers'.format(owner='owner_example', repo='repo_example', pull_number=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pulls_request_reviewers(client):
    """Test case for pulls_request_reviewers

    Request reviewers for a pull request
    """
    body = {"reviewers":["octocat","hubot","other_user"],"team_reviewers":["justice-league"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewers'.format(owner='owner_example', repo='repo_example', pull_number=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pulls_submit_review(client):
    """Test case for pulls_submit_review

    Submit a review for a pull request
    """
    body = openapi_server.PullsSubmitReviewRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}/events'.format(owner='owner_example', repo='repo_example', pull_number=56, review_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pulls_update(client):
    """Test case for pulls_update

    Update a pull request
    """
    body = {"base":"master","body":"updated body","state":"open","title":"new title"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/repos/{owner}/{repo}/pulls/{pull_number}'.format(owner='owner_example', repo='repo_example', pull_number=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pulls_update_branch(client):
    """Test case for pulls_update_branch

    Update a pull request branch
    """
    body = {"expected_head_sha":"6dcb09b5b57875f334f61aebed695e2e4193db5e"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/repos/{owner}/{repo}/pulls/{pull_number}/update-branch'.format(owner='owner_example', repo='repo_example', pull_number=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pulls_update_review(client):
    """Test case for pulls_update_review

    Update a review for a pull request
    """
    body = {"body":"This is close to perfect! Please address the suggested inline change. And add more about this."}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}'.format(owner='owner_example', repo='repo_example', pull_number=56, review_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pulls_update_review_comment(client):
    """Test case for pulls_update_review_comment

    Update a review comment for a pull request
    """
    body = {"body":"I like this too!"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/repos/{owner}/{repo}/pulls/comments/{comment_id}'.format(owner='owner_example', repo='repo_example', comment_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

