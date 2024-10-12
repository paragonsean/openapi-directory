# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.activity_list_public_events503_response import ActivityListPublicEvents503Response
from openapi_server.models.activity_mark_notifications_as_read202_response import ActivityMarkNotificationsAsRead202Response
from openapi_server.models.apps_get_installation415_response import AppsGetInstallation415Response
from openapi_server.models.basic_error import BasicError
from openapi_server.models.branch_protection import BranchProtection
from openapi_server.models.branch_restriction_policy import BranchRestrictionPolicy
from openapi_server.models.branch_short import BranchShort
from openapi_server.models.branch_with_protection import BranchWithProtection
from openapi_server.models.collaborator import Collaborator
from openapi_server.models.combined_commit_status import CombinedCommitStatus
from openapi_server.models.commit import Commit
from openapi_server.models.commit_activity import CommitActivity
from openapi_server.models.commit_comment import CommitComment
from openapi_server.models.commit_comparison import CommitComparison
from openapi_server.models.content_file import ContentFile
from openapi_server.models.content_tree import ContentTree
from openapi_server.models.contributor import Contributor
from openapi_server.models.contributor_activity import ContributorActivity
from openapi_server.models.deploy_key import DeployKey
from openapi_server.models.deployment import Deployment
from openapi_server.models.deployment_status import DeploymentStatus
from openapi_server.models.file_commit import FileCommit
from openapi_server.models.full_repository import FullRepository
from openapi_server.models.hook import Hook
from openapi_server.models.minimal_repository import MinimalRepository
from openapi_server.models.orgs_remove_outside_collaborator422_response import OrgsRemoveOutsideCollaborator422Response
from openapi_server.models.page import Page
from openapi_server.models.page_build import PageBuild
from openapi_server.models.page_build_status import PageBuildStatus
from openapi_server.models.participation_stats import ParticipationStats
from openapi_server.models.protected_branch import ProtectedBranch
from openapi_server.models.protected_branch_admin_enforced import ProtectedBranchAdminEnforced
from openapi_server.models.protected_branch_pull_request_review import ProtectedBranchPullRequestReview
from openapi_server.models.pull_request_simple import PullRequestSimple
from openapi_server.models.release import Release
from openapi_server.models.release_asset import ReleaseAsset
from openapi_server.models.repos_add_collaborator_request import ReposAddCollaboratorRequest
from openapi_server.models.repos_create_commit_comment_request import ReposCreateCommitCommentRequest
from openapi_server.models.repos_create_commit_status_request import ReposCreateCommitStatusRequest
from openapi_server.models.repos_create_deploy_key_request import ReposCreateDeployKeyRequest
from openapi_server.models.repos_create_deployment_request import ReposCreateDeploymentRequest
from openapi_server.models.repos_create_deployment_status_request import ReposCreateDeploymentStatusRequest
from openapi_server.models.repos_create_for_authenticated_user_request import ReposCreateForAuthenticatedUserRequest
from openapi_server.models.repos_create_fork_request import ReposCreateForkRequest
from openapi_server.models.repos_create_in_org_request import ReposCreateInOrgRequest
from openapi_server.models.repos_create_or_update_file_contents_request import ReposCreateOrUpdateFileContentsRequest
from openapi_server.models.repos_create_pages_site_request import ReposCreatePagesSiteRequest
from openapi_server.models.repos_create_release_request import ReposCreateReleaseRequest
from openapi_server.models.repos_create_using_template_request import ReposCreateUsingTemplateRequest
from openapi_server.models.repos_create_webhook_request import ReposCreateWebhookRequest
from openapi_server.models.repos_delete_file_request import ReposDeleteFileRequest
from openapi_server.models.repos_get_content200_response import ReposGetContent200Response
from openapi_server.models.repos_merge_request import ReposMergeRequest
from openapi_server.models.repos_replace_all_topics_request import ReposReplaceAllTopicsRequest
from openapi_server.models.repos_set_status_check_contexts_request import ReposSetStatusCheckContextsRequest
from openapi_server.models.repos_set_team_access_restrictions_request import ReposSetTeamAccessRestrictionsRequest
from openapi_server.models.repos_set_user_access_restrictions_request import ReposSetUserAccessRestrictionsRequest
from openapi_server.models.repos_transfer_request import ReposTransferRequest
from openapi_server.models.repos_update_branch_protection_request import ReposUpdateBranchProtectionRequest
from openapi_server.models.repos_update_commit_comment_request import ReposUpdateCommitCommentRequest
from openapi_server.models.repos_update_information_about_pages_site_request import ReposUpdateInformationAboutPagesSiteRequest
from openapi_server.models.repos_update_invitation_request import ReposUpdateInvitationRequest
from openapi_server.models.repos_update_pull_request_review_protection_request import ReposUpdatePullRequestReviewProtectionRequest
from openapi_server.models.repos_update_release_asset_request import ReposUpdateReleaseAssetRequest
from openapi_server.models.repos_update_release_request import ReposUpdateReleaseRequest
from openapi_server.models.repos_update_request import ReposUpdateRequest
from openapi_server.models.repos_update_status_check_protection_request import ReposUpdateStatusCheckProtectionRequest
from openapi_server.models.repos_update_webhook_request import ReposUpdateWebhookRequest
from openapi_server.models.repository import Repository
from openapi_server.models.repository_collaborator_permission import RepositoryCollaboratorPermission
from openapi_server.models.repository_invitation import RepositoryInvitation
from openapi_server.models.scim_error import ScimError
from openapi_server.models.short_branch import ShortBranch
from openapi_server.models.simple_user import SimpleUser
from openapi_server.models.status import Status
from openapi_server.models.status_check_policy import StatusCheckPolicy
from openapi_server.models.tag import Tag
from openapi_server.models.team import Team
from openapi_server.models.topic import Topic
from openapi_server.models.validation_error import ValidationError
from openapi_server.models.validation_error_simple import ValidationErrorSimple


pytestmark = pytest.mark.asyncio

async def test_repos_accept_invitation(client):
    """Test case for repos_accept_invitation

    Accept a repository invitation
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/user/repository_invitations/{invitation_id}'.format(invitation_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_add_collaborator(client):
    """Test case for repos_add_collaborator

    Add a repository collaborator
    """
    body = openapi_server.ReposAddCollaboratorRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/repos/{owner}/{repo}/collaborators/{username}'.format(owner='owner_example', repo='repo_example', username='username_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_add_status_check_contexts(client):
    """Test case for repos_add_status_check_contexts

    Add status check contexts
    """
    body = openapi_server.ReposSetStatusCheckContextsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks/contexts'.format(owner='owner_example', repo='repo_example', branch='branch_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_add_team_access_restrictions(client):
    """Test case for repos_add_team_access_restrictions

    Add team access restrictions
    """
    body = openapi_server.ReposSetTeamAccessRestrictionsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/teams'.format(owner='owner_example', repo='repo_example', branch='branch_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_add_user_access_restrictions(client):
    """Test case for repos_add_user_access_restrictions

    Add user access restrictions
    """
    body = openapi_server.ReposSetUserAccessRestrictionsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/users'.format(owner='owner_example', repo='repo_example', branch='branch_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_check_collaborator(client):
    """Test case for repos_check_collaborator

    Check if a user is a repository collaborator
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/collaborators/{username}'.format(owner='owner_example', repo='repo_example', username='username_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_compare_commits(client):
    """Test case for repos_compare_commits

    Compare two commits
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/compare/{basehead}'.format(owner='owner_example', repo='repo_example', basehead='basehead_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_create_commit_comment(client):
    """Test case for repos_create_commit_comment

    Create a commit comment
    """
    body = {"body":"Great stuff","line":1,"path":"file1.txt","position":4}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/repos/{owner}/{repo}/commits/{commit_sha}/comments'.format(owner='owner_example', repo='repo_example', commit_sha='commit_sha_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_create_commit_signature_protection(client):
    """Test case for repos_create_commit_signature_protection

    Create commit signature protection
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/repos/{owner}/{repo}/branches/{branch}/protection/required_signatures'.format(owner='owner_example', repo='repo_example', branch='branch_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_create_commit_status(client):
    """Test case for repos_create_commit_status

    Create a commit status
    """
    body = {"context":"continuous-integration/jenkins","description":"The build succeeded!","state":"success","target_url":"https://example.com/build/status"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/repos/{owner}/{repo}/statuses/{sha}'.format(owner='owner_example', repo='repo_example', sha='sha_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_create_deploy_key(client):
    """Test case for repos_create_deploy_key

    Create a deploy key
    """
    body = {"key":"ssh-rsa AAA...","read_only":true,"title":"octocat@octomac"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/repos/{owner}/{repo}/keys'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_create_deployment(client):
    """Test case for repos_create_deployment

    Create a deployment
    """
    body = {"auto_merge":false,"description":"Deploy request from hubot","payload":"{ \"deploy\": \"migrate\" }","ref":"topic-branch","required_contexts":["ci/janky","security/brakeman"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/repos/{owner}/{repo}/deployments'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_create_deployment_status(client):
    """Test case for repos_create_deployment_status

    Create a deployment status
    """
    body = {"description":"Deployment finished successfully.","environment":"production","log_url":"https://example.com/deployment/42/output","state":"success"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/repos/{owner}/{repo}/deployments/{deployment_id}/statuses'.format(owner='owner_example', repo='repo_example', deployment_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_create_for_authenticated_user(client):
    """Test case for repos_create_for_authenticated_user

    Create a repository for the authenticated user
    """
    body = openapi_server.ReposCreateForAuthenticatedUserRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/user/repos',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_create_fork(client):
    """Test case for repos_create_fork

    Create a fork
    """
    body = openapi_server.ReposCreateForkRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/repos/{owner}/{repo}/forks'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_create_in_org(client):
    """Test case for repos_create_in_org

    Create an organization repository
    """
    body = {"description":"This is your first repository","has_issues":true,"has_projects":true,"has_wiki":true,"homepage":"https://github.com","name":"Hello-World","private":false}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/orgs/{org}/repos'.format(org='org_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_create_or_update_file_contents(client):
    """Test case for repos_create_or_update_file_contents

    Create or update file contents
    """
    body = {"committer":{"email":"octocat@github.com","name":"Monalisa Octocat"},"content":"bXkgbmV3IGZpbGUgY29udGVudHM=","message":"my commit message"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/repos/{owner}/{repo}/contents/{path}'.format(owner='owner_example', repo='repo_example', path='path_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_create_pages_site(client):
    """Test case for repos_create_pages_site

    Create a GitHub Pages site
    """
    body = {"source":{"branch":"master","path":"/docs"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/repos/{owner}/{repo}/pages'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_create_release(client):
    """Test case for repos_create_release

    Create a release
    """
    body = {"body":"Description of the release","draft":false,"name":"v1.0.0","prerelease":false,"tag_name":"v1.0.0","target_commitish":"master"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/repos/{owner}/{repo}/releases'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_create_using_template(client):
    """Test case for repos_create_using_template

    Create a repository using a template
    """
    body = {"description":"This is your first repository","include_all_branches":false,"name":"Hello-World","owner":"octocat","private":false}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/repos/{template_owner}/{template_repo}/generate'.format(template_owner='template_owner_example', template_repo='template_repo_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_create_webhook(client):
    """Test case for repos_create_webhook

    Create a repository webhook
    """
    body = {"active":true,"config":{"content_type":"json","insecure_ssl":"0","url":"https://example.com/webhook"},"events":["push","pull_request"],"name":"web"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/repos/{owner}/{repo}/hooks'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_decline_invitation(client):
    """Test case for repos_decline_invitation

    Decline a repository invitation
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/user/repository_invitations/{invitation_id}'.format(invitation_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_delete(client):
    """Test case for repos_delete

    Delete a repository
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/repos/{owner}/{repo}'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_delete_access_restrictions(client):
    """Test case for repos_delete_access_restrictions

    Delete access restrictions
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/repos/{owner}/{repo}/branches/{branch}/protection/restrictions'.format(owner='owner_example', repo='repo_example', branch='branch_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_delete_admin_branch_protection(client):
    """Test case for repos_delete_admin_branch_protection

    Delete admin branch protection
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/repos/{owner}/{repo}/branches/{branch}/protection/enforce_admins'.format(owner='owner_example', repo='repo_example', branch='branch_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_delete_branch_protection(client):
    """Test case for repos_delete_branch_protection

    Delete branch protection
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/repos/{owner}/{repo}/branches/{branch}/protection'.format(owner='owner_example', repo='repo_example', branch='branch_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_delete_commit_comment(client):
    """Test case for repos_delete_commit_comment

    Delete a commit comment
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/repos/{owner}/{repo}/comments/{comment_id}'.format(owner='owner_example', repo='repo_example', comment_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_delete_commit_signature_protection(client):
    """Test case for repos_delete_commit_signature_protection

    Delete commit signature protection
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/repos/{owner}/{repo}/branches/{branch}/protection/required_signatures'.format(owner='owner_example', repo='repo_example', branch='branch_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_delete_deploy_key(client):
    """Test case for repos_delete_deploy_key

    Delete a deploy key
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/repos/{owner}/{repo}/keys/{key_id}'.format(owner='owner_example', repo='repo_example', key_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_delete_file(client):
    """Test case for repos_delete_file

    Delete a file
    """
    body = {"committer":{"email":"octocat@github.com","name":"Monalisa Octocat"},"message":"my commit message","sha":"329688480d39049927147c162b9d2deaf885005f"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/repos/{owner}/{repo}/contents/{path}'.format(owner='owner_example', repo='repo_example', path='path_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_delete_invitation(client):
    """Test case for repos_delete_invitation

    Delete a repository invitation
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/repos/{owner}/{repo}/invitations/{invitation_id}'.format(owner='owner_example', repo='repo_example', invitation_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_delete_pages_site(client):
    """Test case for repos_delete_pages_site

    Delete a GitHub Enterprise Server Pages site
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/repos/{owner}/{repo}/pages'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_delete_pull_request_review_protection(client):
    """Test case for repos_delete_pull_request_review_protection

    Delete pull request review protection
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/repos/{owner}/{repo}/branches/{branch}/protection/required_pull_request_reviews'.format(owner='owner_example', repo='repo_example', branch='branch_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_delete_release(client):
    """Test case for repos_delete_release

    Delete a release
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/repos/{owner}/{repo}/releases/{release_id}'.format(owner='owner_example', repo='repo_example', release_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_delete_release_asset(client):
    """Test case for repos_delete_release_asset

    Delete a release asset
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/repos/{owner}/{repo}/releases/assets/{asset_id}'.format(owner='owner_example', repo='repo_example', asset_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_delete_webhook(client):
    """Test case for repos_delete_webhook

    Delete a repository webhook
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/repos/{owner}/{repo}/hooks/{hook_id}'.format(owner='owner_example', repo='repo_example', hook_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_download_tarball_archive(client):
    """Test case for repos_download_tarball_archive

    Download a repository archive (tar)
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/tarball/{ref}'.format(owner='owner_example', repo='repo_example', ref='ref_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_download_zipball_archive(client):
    """Test case for repos_download_zipball_archive

    Download a repository archive (zip)
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/zipball/{ref}'.format(owner='owner_example', repo='repo_example', ref='ref_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_get(client):
    """Test case for repos_get

    Get a repository
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_get_access_restrictions(client):
    """Test case for repos_get_access_restrictions

    Get access restrictions
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/branches/{branch}/protection/restrictions'.format(owner='owner_example', repo='repo_example', branch='branch_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_get_admin_branch_protection(client):
    """Test case for repos_get_admin_branch_protection

    Get admin branch protection
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/branches/{branch}/protection/enforce_admins'.format(owner='owner_example', repo='repo_example', branch='branch_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_get_all_status_check_contexts(client):
    """Test case for repos_get_all_status_check_contexts

    Get all status check contexts
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks/contexts'.format(owner='owner_example', repo='repo_example', branch='branch_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_get_all_topics(client):
    """Test case for repos_get_all_topics

    Get all repository topics
    """
    params = [('page', 1),
                    ('per_page', 30)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/topics'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_get_branch(client):
    """Test case for repos_get_branch

    Get a branch
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/branches/{branch}'.format(owner='owner_example', repo='repo_example', branch='branch_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_get_branch_protection(client):
    """Test case for repos_get_branch_protection

    Get branch protection
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/branches/{branch}/protection'.format(owner='owner_example', repo='repo_example', branch='branch_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_get_code_frequency_stats(client):
    """Test case for repos_get_code_frequency_stats

    Get the weekly commit activity
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/stats/code_frequency'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_get_collaborator_permission_level(client):
    """Test case for repos_get_collaborator_permission_level

    Get repository permissions for a user
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/collaborators/{username}/permission'.format(owner='owner_example', repo='repo_example', username='username_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_get_combined_status_for_ref(client):
    """Test case for repos_get_combined_status_for_ref

    Get the combined status for a specific reference
    """
    params = [('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/commits/{ref}/status'.format(owner='owner_example', repo='repo_example', ref='ref_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_get_commit(client):
    """Test case for repos_get_commit

    Get a commit
    """
    params = [('page', 1),
                    ('per_page', 30)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/commits/{ref}'.format(owner='owner_example', repo='repo_example', ref='ref_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_get_commit_activity_stats(client):
    """Test case for repos_get_commit_activity_stats

    Get the last year of commit activity
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/stats/commit_activity'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_get_commit_comment(client):
    """Test case for repos_get_commit_comment

    Get a commit comment
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/comments/{comment_id}'.format(owner='owner_example', repo='repo_example', comment_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_get_commit_signature_protection(client):
    """Test case for repos_get_commit_signature_protection

    Get commit signature protection
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/branches/{branch}/protection/required_signatures'.format(owner='owner_example', repo='repo_example', branch='branch_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_get_content(client):
    """Test case for repos_get_content

    Get repository content
    """
    params = [('ref', 'ref_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/contents/{path}'.format(owner='owner_example', repo='repo_example', path='path_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_get_contributors_stats(client):
    """Test case for repos_get_contributors_stats

    Get all contributor commit activity
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/stats/contributors'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_get_deploy_key(client):
    """Test case for repos_get_deploy_key

    Get a deploy key
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/keys/{key_id}'.format(owner='owner_example', repo='repo_example', key_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_get_deployment(client):
    """Test case for repos_get_deployment

    Get a deployment
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/deployments/{deployment_id}'.format(owner='owner_example', repo='repo_example', deployment_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_get_deployment_status(client):
    """Test case for repos_get_deployment_status

    Get a deployment status
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/deployments/{deployment_id}/statuses/{status_id}'.format(owner='owner_example', repo='repo_example', deployment_id=56, status_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_get_latest_pages_build(client):
    """Test case for repos_get_latest_pages_build

    Get latest Pages build
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/pages/builds/latest'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_get_latest_release(client):
    """Test case for repos_get_latest_release

    Get the latest release
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/releases/latest'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_get_pages(client):
    """Test case for repos_get_pages

    Get a GitHub Enterprise Server Pages site
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/pages'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_get_pages_build(client):
    """Test case for repos_get_pages_build

    Get GitHub Enterprise Server Pages build
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/pages/builds/{build_id}'.format(owner='owner_example', repo='repo_example', build_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_get_participation_stats(client):
    """Test case for repos_get_participation_stats

    Get the weekly commit count
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/stats/participation'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_get_pull_request_review_protection(client):
    """Test case for repos_get_pull_request_review_protection

    Get pull request review protection
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/branches/{branch}/protection/required_pull_request_reviews'.format(owner='owner_example', repo='repo_example', branch='branch_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_get_punch_card_stats(client):
    """Test case for repos_get_punch_card_stats

    Get the hourly commit count for each day
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/stats/punch_card'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_get_readme(client):
    """Test case for repos_get_readme

    Get a repository README
    """
    params = [('ref', 'ref_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/readme'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_get_readme_in_directory(client):
    """Test case for repos_get_readme_in_directory

    Get a repository README for a directory
    """
    params = [('ref', 'ref_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/readme/{dir}'.format(owner='owner_example', repo='repo_example', dir='dir_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_get_release(client):
    """Test case for repos_get_release

    Get a release
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/releases/{release_id}'.format(owner='owner_example', repo='repo_example', release_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_get_release_asset(client):
    """Test case for repos_get_release_asset

    Get a release asset
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/releases/assets/{asset_id}'.format(owner='owner_example', repo='repo_example', asset_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_get_release_by_tag(client):
    """Test case for repos_get_release_by_tag

    Get a release by tag name
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/releases/tags/{tag}'.format(owner='owner_example', repo='repo_example', tag='tag_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_get_status_checks_protection(client):
    """Test case for repos_get_status_checks_protection

    Get status checks protection
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks'.format(owner='owner_example', repo='repo_example', branch='branch_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_get_teams_with_access_to_protected_branch(client):
    """Test case for repos_get_teams_with_access_to_protected_branch

    Get teams with access to the protected branch
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/teams'.format(owner='owner_example', repo='repo_example', branch='branch_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_get_users_with_access_to_protected_branch(client):
    """Test case for repos_get_users_with_access_to_protected_branch

    Get users with access to the protected branch
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/users'.format(owner='owner_example', repo='repo_example', branch='branch_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_get_webhook(client):
    """Test case for repos_get_webhook

    Get a repository webhook
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/hooks/{hook_id}'.format(owner='owner_example', repo='repo_example', hook_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_list_branches(client):
    """Test case for repos_list_branches

    List branches
    """
    params = [('protected', True),
                    ('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/branches'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_list_branches_for_head_commit(client):
    """Test case for repos_list_branches_for_head_commit

    List branches for HEAD commit
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/commits/{commit_sha}/branches-where-head'.format(owner='owner_example', repo='repo_example', commit_sha='commit_sha_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_list_collaborators(client):
    """Test case for repos_list_collaborators

    List repository collaborators
    """
    params = [('affiliation', all),
                    ('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/collaborators'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_list_comments_for_commit(client):
    """Test case for repos_list_comments_for_commit

    List commit comments
    """
    params = [('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/commits/{commit_sha}/comments'.format(owner='owner_example', repo='repo_example', commit_sha='commit_sha_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_list_commit_comments_for_repo(client):
    """Test case for repos_list_commit_comments_for_repo

    List commit comments for a repository
    """
    params = [('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/comments'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_list_commit_statuses_for_ref(client):
    """Test case for repos_list_commit_statuses_for_ref

    List commit statuses for a reference
    """
    params = [('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/commits/{ref}/statuses'.format(owner='owner_example', repo='repo_example', ref='ref_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_list_commits(client):
    """Test case for repos_list_commits

    List commits
    """
    params = [('sha', 'sha_example'),
                    ('path', 'path_example'),
                    ('author', 'author_example'),
                    ('since', '2013-10-20T19:20:30+01:00'),
                    ('until', '2013-10-20T19:20:30+01:00'),
                    ('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/commits'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_list_contributors(client):
    """Test case for repos_list_contributors

    List repository contributors
    """
    params = [('anon', 'anon_example'),
                    ('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/contributors'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_list_deploy_keys(client):
    """Test case for repos_list_deploy_keys

    List deploy keys
    """
    params = [('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/keys'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_list_deployment_statuses(client):
    """Test case for repos_list_deployment_statuses

    List deployment statuses
    """
    params = [('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/deployments/{deployment_id}/statuses'.format(owner='owner_example', repo='repo_example', deployment_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_list_deployments(client):
    """Test case for repos_list_deployments

    List deployments
    """
    params = [('sha', 'none'),
                    ('ref', 'none'),
                    ('task', 'none'),
                    ('environment', 'none'),
                    ('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/deployments'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_list_for_authenticated_user(client):
    """Test case for repos_list_for_authenticated_user

    List repositories for the authenticated user
    """
    params = [('visibility', all),
                    ('affiliation', 'owner,collaborator,organization_member'),
                    ('type', all),
                    ('sort', full_name),
                    ('direction', 'direction_example'),
                    ('per_page', 30),
                    ('page', 1),
                    ('since', '2013-10-20T19:20:30+01:00'),
                    ('before', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/user/repos',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_list_for_org(client):
    """Test case for repos_list_for_org

    List organization repositories
    """
    params = [('type', 'type_example'),
                    ('sort', created),
                    ('direction', 'direction_example'),
                    ('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/orgs/{org}/repos'.format(org='org_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_list_for_user(client):
    """Test case for repos_list_for_user

    List repositories for a user
    """
    params = [('type', owner),
                    ('sort', full_name),
                    ('direction', 'direction_example'),
                    ('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/users/{username}/repos'.format(username='username_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_list_forks(client):
    """Test case for repos_list_forks

    List forks
    """
    params = [('sort', newest),
                    ('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/forks'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_list_invitations(client):
    """Test case for repos_list_invitations

    List repository invitations
    """
    params = [('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/invitations'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_list_invitations_for_authenticated_user(client):
    """Test case for repos_list_invitations_for_authenticated_user

    List repository invitations for the authenticated user
    """
    params = [('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/user/repository_invitations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_list_languages(client):
    """Test case for repos_list_languages

    List repository languages
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/languages'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_list_pages_builds(client):
    """Test case for repos_list_pages_builds

    List GitHub Enterprise Server Pages builds
    """
    params = [('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/pages/builds'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_list_public(client):
    """Test case for repos_list_public

    List public repositories
    """
    params = [('since', 56),
                    ('visibility', public)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repositories',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_list_pull_requests_associated_with_commit(client):
    """Test case for repos_list_pull_requests_associated_with_commit

    List pull requests associated with a commit
    """
    params = [('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/commits/{commit_sha}/pulls'.format(owner='owner_example', repo='repo_example', commit_sha='commit_sha_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_list_release_assets(client):
    """Test case for repos_list_release_assets

    List release assets
    """
    params = [('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/releases/{release_id}/assets'.format(owner='owner_example', repo='repo_example', release_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_list_releases(client):
    """Test case for repos_list_releases

    List releases
    """
    params = [('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/releases'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_list_tags(client):
    """Test case for repos_list_tags

    List repository tags
    """
    params = [('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/tags'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_list_teams(client):
    """Test case for repos_list_teams

    List repository teams
    """
    params = [('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/teams'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_list_webhooks(client):
    """Test case for repos_list_webhooks

    List repository webhooks
    """
    params = [('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/hooks'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_merge(client):
    """Test case for repos_merge

    Merge a branch
    """
    body = {"base":"master","commit_message":"Shipped cool_feature!","head":"cool_feature"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/repos/{owner}/{repo}/merges'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_ping_webhook(client):
    """Test case for repos_ping_webhook

    Ping a repository webhook
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/repos/{owner}/{repo}/hooks/{hook_id}/pings'.format(owner='owner_example', repo='repo_example', hook_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_remove_collaborator(client):
    """Test case for repos_remove_collaborator

    Remove a repository collaborator
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/repos/{owner}/{repo}/collaborators/{username}'.format(owner='owner_example', repo='repo_example', username='username_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_remove_status_check_contexts(client):
    """Test case for repos_remove_status_check_contexts

    Remove status check contexts
    """
    body = openapi_server.ReposSetStatusCheckContextsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks/contexts'.format(owner='owner_example', repo='repo_example', branch='branch_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_remove_status_check_protection(client):
    """Test case for repos_remove_status_check_protection

    Remove status check protection
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks'.format(owner='owner_example', repo='repo_example', branch='branch_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_remove_team_access_restrictions(client):
    """Test case for repos_remove_team_access_restrictions

    Remove team access restrictions
    """
    body = openapi_server.ReposSetTeamAccessRestrictionsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/teams'.format(owner='owner_example', repo='repo_example', branch='branch_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_remove_user_access_restrictions(client):
    """Test case for repos_remove_user_access_restrictions

    Remove user access restrictions
    """
    body = openapi_server.ReposSetUserAccessRestrictionsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/users'.format(owner='owner_example', repo='repo_example', branch='branch_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_replace_all_topics(client):
    """Test case for repos_replace_all_topics

    Replace all repository topics
    """
    body = {"names":["octocat","atom","electron","api"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/repos/{owner}/{repo}/topics'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_request_pages_build(client):
    """Test case for repos_request_pages_build

    Request a GitHub Enterprise Server Pages build
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/repos/{owner}/{repo}/pages/builds'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_set_admin_branch_protection(client):
    """Test case for repos_set_admin_branch_protection

    Set admin branch protection
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/repos/{owner}/{repo}/branches/{branch}/protection/enforce_admins'.format(owner='owner_example', repo='repo_example', branch='branch_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_set_status_check_contexts(client):
    """Test case for repos_set_status_check_contexts

    Set status check contexts
    """
    body = openapi_server.ReposSetStatusCheckContextsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks/contexts'.format(owner='owner_example', repo='repo_example', branch='branch_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_set_team_access_restrictions(client):
    """Test case for repos_set_team_access_restrictions

    Set team access restrictions
    """
    body = openapi_server.ReposSetTeamAccessRestrictionsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/teams'.format(owner='owner_example', repo='repo_example', branch='branch_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_set_user_access_restrictions(client):
    """Test case for repos_set_user_access_restrictions

    Set user access restrictions
    """
    body = openapi_server.ReposSetUserAccessRestrictionsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/users'.format(owner='owner_example', repo='repo_example', branch='branch_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_test_push_webhook(client):
    """Test case for repos_test_push_webhook

    Test the push repository webhook
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/repos/{owner}/{repo}/hooks/{hook_id}/tests'.format(owner='owner_example', repo='repo_example', hook_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_transfer(client):
    """Test case for repos_transfer

    Transfer a repository
    """
    body = {"new_owner":"github","team_ids":[12,345]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/repos/{owner}/{repo}/transfer'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_update(client):
    """Test case for repos_update

    Update a repository
    """
    body = {"description":"This is your first repository","has_issues":true,"has_projects":true,"has_wiki":true,"homepage":"https://github.com","name":"Hello-World","private":true}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/repos/{owner}/{repo}'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_update_branch_protection(client):
    """Test case for repos_update_branch_protection

    Update branch protection
    """
    body = {"allow_deletions":true,"allow_force_pushes":true,"enforce_admins":true,"required_conversation_resolution":true,"required_linear_history":true,"required_pull_request_reviews":{"dismiss_stale_reviews":true,"dismissal_restrictions":{"teams":["justice-league"],"users":["octocat"]},"require_code_owner_reviews":true,"required_approving_review_count":2},"required_status_checks":{"contexts":["continuous-integration/travis-ci"],"strict":true},"restrictions":{"apps":["super-ci"],"teams":["justice-league"],"users":["octocat"]}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/repos/{owner}/{repo}/branches/{branch}/protection'.format(owner='owner_example', repo='repo_example', branch='branch_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_update_commit_comment(client):
    """Test case for repos_update_commit_comment

    Update a commit comment
    """
    body = {"body":"Nice change"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/repos/{owner}/{repo}/comments/{comment_id}'.format(owner='owner_example', repo='repo_example', comment_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_update_information_about_pages_site(client):
    """Test case for repos_update_information_about_pages_site

    Update information about a GitHub Pages site
    """
    body = {"source":"master /docs"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/repos/{owner}/{repo}/pages'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_update_invitation(client):
    """Test case for repos_update_invitation

    Update a repository invitation
    """
    body = openapi_server.ReposUpdateInvitationRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/repos/{owner}/{repo}/invitations/{invitation_id}'.format(owner='owner_example', repo='repo_example', invitation_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_update_pull_request_review_protection(client):
    """Test case for repos_update_pull_request_review_protection

    Update pull request review protection
    """
    body = {"dismiss_stale_reviews":true,"dismissal_restrictions":{"teams":["justice-league"],"users":["octocat"]},"require_code_owner_reviews":true,"required_approving_review_count":2}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/repos/{owner}/{repo}/branches/{branch}/protection/required_pull_request_reviews'.format(owner='owner_example', repo='repo_example', branch='branch_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_update_release(client):
    """Test case for repos_update_release

    Update a release
    """
    body = {"body":"Description of the release","draft":false,"name":"v1.0.0","prerelease":false,"tag_name":"v1.0.0","target_commitish":"master"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/repos/{owner}/{repo}/releases/{release_id}'.format(owner='owner_example', repo='repo_example', release_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_update_release_asset(client):
    """Test case for repos_update_release_asset

    Update a release asset
    """
    body = {"label":"Mac binary","name":"foo-1.0.0-osx.zip"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/repos/{owner}/{repo}/releases/assets/{asset_id}'.format(owner='owner_example', repo='repo_example', asset_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_update_status_check_protection(client):
    """Test case for repos_update_status_check_protection

    Update status check protection
    """
    body = {"contexts":["continuous-integration/travis-ci"],"strict":true}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks'.format(owner='owner_example', repo='repo_example', branch='branch_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repos_update_webhook(client):
    """Test case for repos_update_webhook

    Update a repository webhook
    """
    body = {"active":true,"add_events":["pull_request"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/repos/{owner}/{repo}/hooks/{hook_id}'.format(owner='owner_example', repo='repo_example', hook_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_repos_upload_release_asset(client):
    """Test case for repos_upload_release_asset

    Upload a release asset
    """
    body = 'body_example'
    params = [('name', 'name_example'),
                    ('label', 'label_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/repos/{owner}/{repo}/releases/{release_id}/assets'.format(owner='owner_example', repo='repo_example', release_id=56),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

