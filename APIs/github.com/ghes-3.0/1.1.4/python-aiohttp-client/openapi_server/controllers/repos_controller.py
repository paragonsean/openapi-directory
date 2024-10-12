from typing import List, Dict
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
from openapi_server.models.integration import Integration
from openapi_server.models.minimal_repository import MinimalRepository
from openapi_server.models.orgs_remove_outside_collaborator422_response import OrgsRemoveOutsideCollaborator422Response
from openapi_server.models.orgs_update_webhook_config_for_org_request import OrgsUpdateWebhookConfigForOrgRequest
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
from openapi_server.models.repos_create_dispatch_event_request import ReposCreateDispatchEventRequest
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
from openapi_server.models.repos_set_app_access_restrictions_request import ReposSetAppAccessRestrictionsRequest
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
from openapi_server.models.webhook_config import WebhookConfig
from openapi_server import util


async def repos_accept_invitation_for_authenticated_user(request: web.Request, invitation_id) -> web.Response:
    """Accept a repository invitation

    

    :param invitation_id: invitation_id parameter
    :type invitation_id: int

    """
    return web.Response(status=200)


async def repos_add_app_access_restrictions(request: web.Request, owner, repo, branch, body=None) -> web.Response:
    """Add app access restrictions

    Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub&#39;s products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  Grants the specified apps push access for this branch. Only installed GitHub Apps with &#x60;write&#x60; access to the &#x60;contents&#x60; permission can be added as authorized actors on a protected branch.  | Type    | Description                                                                                                                                                | | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | | &#x60;array&#x60; | The GitHub Apps that have push access to this branch. Use the app&#39;s &#x60;slug&#x60;. **Note**: The list of users, apps, and teams in total is limited to 100 items. |

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param branch: The name of the branch.
    :type branch: str
    :param body: 
    :type body: dict | bytes

    """
    body = ReposSetAppAccessRestrictionsRequest.from_dict(body)
    return web.Response(status=200)


async def repos_add_collaborator(request: web.Request, owner, repo, username, body=None) -> web.Response:
    """Add a repository collaborator

    This endpoint triggers [notifications](https://docs.github.com/en/github/managing-subscriptions-and-notifications-on-github/about-notifications). Creating content too quickly using this endpoint may result in secondary rate limiting. See \&quot;[Secondary rate limits](https://docs.github.com/enterprise-server@3.0/rest/overview/resources-in-the-rest-api#secondary-rate-limits)\&quot; and \&quot;[Dealing with secondary rate limits](https://docs.github.com/enterprise-server@3.0/rest/guides/best-practices-for-integrators#dealing-with-secondary-rate-limits)\&quot; for details.  For more information on permission levels, see \&quot;[Repository permission levels for an organization](https://docs.github.com/en/github/setting-up-and-managing-organizations-and-teams/repository-permission-levels-for-an-organization#permission-levels-for-repositories-owned-by-an-organization)\&quot;. There are restrictions on which permissions can be granted to organization members when an organization base role is in place. In this case, the permission being given must be equal to or higher than the org base permission. Otherwise, the request will fail with:  &#x60;&#x60;&#x60; Cannot assign {member} permission of {role name} &#x60;&#x60;&#x60;  Note that, if you choose not to pass any parameters, you&#39;ll need to set &#x60;Content-Length&#x60; to zero when calling out to this endpoint. For more information, see \&quot;[HTTP verbs](https://docs.github.com/enterprise-server@3.0/rest/overview/resources-in-the-rest-api#http-verbs).\&quot;  The invitee will receive a notification that they have been invited to the repository, which they must accept or decline. They may do this via the notifications page, the email they receive, or by using the [repository invitations API endpoints](https://docs.github.com/enterprise-server@3.0/rest/reference/repos#invitations).  **Rate limits**  You are limited to sending 50 invitations to a repository per 24 hour period. Note there is no limit if you are inviting organization members to an organization repository.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param username: 
    :type username: str
    :param body: 
    :type body: dict | bytes

    """
    body = ReposAddCollaboratorRequest.from_dict(body)
    return web.Response(status=200)


async def repos_add_status_check_contexts(request: web.Request, owner, repo, branch, body=None) -> web.Response:
    """Add status check contexts

    Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub&#39;s products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param branch: The name of the branch.
    :type branch: str
    :param body: 
    :type body: dict | bytes

    """
    body = ReposSetStatusCheckContextsRequest.from_dict(body)
    return web.Response(status=200)


async def repos_add_team_access_restrictions(request: web.Request, owner, repo, branch, body=None) -> web.Response:
    """Add team access restrictions

    Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub&#39;s products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  Grants the specified teams push access for this branch. You can also give push access to child teams.  | Type    | Description                                                                                                                                | | ------- | ------------------------------------------------------------------------------------------------------------------------------------------ | | &#x60;array&#x60; | The teams that can have push access. Use the team&#39;s &#x60;slug&#x60;. **Note**: The list of users, apps, and teams in total is limited to 100 items. |

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param branch: The name of the branch.
    :type branch: str
    :param body: 
    :type body: dict | bytes

    """
    body = ReposSetTeamAccessRestrictionsRequest.from_dict(body)
    return web.Response(status=200)


async def repos_add_user_access_restrictions(request: web.Request, owner, repo, branch, body=None) -> web.Response:
    """Add user access restrictions

    Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub&#39;s products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  Grants the specified people push access for this branch.  | Type    | Description                                                                                                                   | | ------- | ----------------------------------------------------------------------------------------------------------------------------- | | &#x60;array&#x60; | Usernames for people who can have push access. **Note**: The list of users, apps, and teams in total is limited to 100 items. |

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param branch: The name of the branch.
    :type branch: str
    :param body: 
    :type body: dict | bytes

    """
    body = ReposSetUserAccessRestrictionsRequest.from_dict(body)
    return web.Response(status=200)


async def repos_check_collaborator(request: web.Request, owner, repo, username) -> web.Response:
    """Check if a user is a repository collaborator

    For organization-owned repositories, the list of collaborators includes outside collaborators, organization members that are direct collaborators, organization members with access through team memberships, organization members with access through default organization permissions, and organization owners.  Team members will include the members of child teams.  You must authenticate using an access token with the &#x60;read:org&#x60; and &#x60;repo&#x60; scopes with push access to use this endpoint. GitHub Apps must have the &#x60;members&#x60; organization permission and &#x60;metadata&#x60; repository permission to use this endpoint.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param username: 
    :type username: str

    """
    return web.Response(status=200)


async def repos_compare_commits(request: web.Request, owner, repo, basehead) -> web.Response:
    """Compare two commits

    The &#x60;basehead&#x60; param is comprised of two parts: &#x60;base&#x60; and &#x60;head&#x60;. Both must be branch names in &#x60;repo&#x60;. To compare branches across other repositories in the same network as &#x60;repo&#x60;, use the format &#x60;&lt;USERNAME&gt;:branch&#x60;.  The response from the API is equivalent to running the &#x60;git log base..head&#x60; command; however, commits are returned in chronological order. Pass the appropriate [media type](https://docs.github.com/enterprise-server@3.0/rest/overview/media-types/#commits-commit-comparison-and-pull-requests) to fetch diff and patch formats.  The response also includes details on the files that were changed between the two commits. This includes the status of the change (for example, if a file was added, removed, modified, or renamed), and details of the change itself. For example, files with a &#x60;renamed&#x60; status have a &#x60;previous_filename&#x60; field showing the previous filename of the file, and files with a &#x60;modified&#x60; status have a &#x60;patch&#x60; field showing the changes made to the file.  **Working with large comparisons**  The response will include a comparison of up to 250 commits. If you are working with a larger commit range, you can use the [List commits](https://docs.github.com/enterprise-server@3.0/rest/reference/repos#list-commits) to enumerate all commits in the range.  For comparisons with extremely large diffs, you may receive an error response indicating that the diff took too long to generate. You can typically resolve this error by using a smaller commit range.  **Signature verification object**  The response will include a &#x60;verification&#x60; object that describes the result of verifying the commit&#39;s signature. The following fields are included in the &#x60;verification&#x60; object:  | Name | Type | Description | | ---- | ---- | ----------- | | &#x60;verified&#x60; | &#x60;boolean&#x60; | Indicates whether GitHub considers the signature in this commit to be verified. | | &#x60;reason&#x60; | &#x60;string&#x60; | The reason for verified value. Possible values and their meanings are enumerated in table below. | | &#x60;signature&#x60; | &#x60;string&#x60; | The signature that was extracted from the commit. | | &#x60;payload&#x60; | &#x60;string&#x60; | The value that was signed. |  These are the possible values for &#x60;reason&#x60; in the &#x60;verification&#x60; object:  | Value | Description | | ----- | ----------- | | &#x60;expired_key&#x60; | The key that made the signature is expired. | | &#x60;not_signing_key&#x60; | The \&quot;signing\&quot; flag is not among the usage flags in the GPG key that made the signature. | | &#x60;gpgverify_error&#x60; | There was an error communicating with the signature verification service. | | &#x60;gpgverify_unavailable&#x60; | The signature verification service is currently unavailable. | | &#x60;unsigned&#x60; | The object does not include a signature. | | &#x60;unknown_signature_type&#x60; | A non-PGP signature was found in the commit. | | &#x60;no_user&#x60; | No user was associated with the &#x60;committer&#x60; email address in the commit. | | &#x60;unverified_email&#x60; | The &#x60;committer&#x60; email address in the commit was associated with a user, but the email address is not verified on her/his account. | | &#x60;bad_email&#x60; | The &#x60;committer&#x60; email address in the commit is not included in the identities of the PGP key that made the signature. | | &#x60;unknown_key&#x60; | The key that made the signature has not been registered with any user&#39;s account. | | &#x60;malformed_signature&#x60; | There was an error parsing the signature. | | &#x60;invalid&#x60; | The signature could not be cryptographically verified using the key whose key-id was found in the signature. | | &#x60;valid&#x60; | None of the above errors applied, so the signature is considered to be verified. |

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param basehead: The base branch and head branch to compare. This parameter expects the format &#x60;{base}...{head}&#x60;.
    :type basehead: str

    """
    return web.Response(status=200)


async def repos_create_commit_comment(request: web.Request, owner, repo, commit_sha, body) -> web.Response:
    """Create a commit comment

    Create a comment for a commit using its &#x60;:commit_sha&#x60;.  This endpoint triggers [notifications](https://docs.github.com/en/github/managing-subscriptions-and-notifications-on-github/about-notifications). Creating content too quickly using this endpoint may result in secondary rate limiting. See \&quot;[Secondary rate limits](https://docs.github.com/enterprise-server@3.0/rest/overview/resources-in-the-rest-api#secondary-rate-limits)\&quot; and \&quot;[Dealing with secondary rate limits](https://docs.github.com/enterprise-server@3.0/rest/guides/best-practices-for-integrators#dealing-with-secondary-rate-limits)\&quot; for details.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param commit_sha: commit_sha parameter
    :type commit_sha: str
    :param body: 
    :type body: dict | bytes

    """
    body = ReposCreateCommitCommentRequest.from_dict(body)
    return web.Response(status=200)


async def repos_create_commit_signature_protection(request: web.Request, owner, repo, branch) -> web.Response:
    """Create commit signature protection

    Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub&#39;s products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  When authenticated with admin or owner permissions to the repository, you can use this endpoint to require signed commits on a branch. You must enable branch protection to require signed commits.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param branch: The name of the branch.
    :type branch: str

    """
    return web.Response(status=200)


async def repos_create_commit_status(request: web.Request, owner, repo, sha, body) -> web.Response:
    """Create a commit status

    Users with push access in a repository can create commit statuses for a given SHA.  Note: there is a limit of 1000 statuses per &#x60;sha&#x60; and &#x60;context&#x60; within a repository. Attempts to create more than 1000 statuses will result in a validation error.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param sha: 
    :type sha: str
    :param body: 
    :type body: dict | bytes

    """
    body = ReposCreateCommitStatusRequest.from_dict(body)
    return web.Response(status=200)


async def repos_create_deploy_key(request: web.Request, owner, repo, body) -> web.Response:
    """Create a deploy key

    You can create a read-only deploy key.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param body: 
    :type body: dict | bytes

    """
    body = ReposCreateDeployKeyRequest.from_dict(body)
    return web.Response(status=200)


async def repos_create_deployment(request: web.Request, owner, repo, body) -> web.Response:
    """Create a deployment

    Deployments offer a few configurable parameters with certain defaults.  The &#x60;ref&#x60; parameter can be any named branch, tag, or SHA. At GitHub Enterprise Server we often deploy branches and verify them before we merge a pull request.  The &#x60;environment&#x60; parameter allows deployments to be issued to different runtime environments. Teams often have multiple environments for verifying their applications, such as &#x60;production&#x60;, &#x60;staging&#x60;, and &#x60;qa&#x60;. This parameter makes it easier to track which environments have requested deployments. The default environment is &#x60;production&#x60;.  The &#x60;auto_merge&#x60; parameter is used to ensure that the requested ref is not behind the repository&#39;s default branch. If the ref _is_ behind the default branch for the repository, we will attempt to merge it for you. If the merge succeeds, the API will return a successful merge commit. If merge conflicts prevent the merge from succeeding, the API will return a failure response.  By default, [commit statuses](https://docs.github.com/enterprise-server@3.0/rest/reference/commits#commit-statuses) for every submitted context must be in a &#x60;success&#x60; state. The &#x60;required_contexts&#x60; parameter allows you to specify a subset of contexts that must be &#x60;success&#x60;, or to specify contexts that have not yet been submitted. You are not required to use commit statuses to deploy. If you do not require any contexts or create any commit statuses, the deployment will always succeed.  The &#x60;payload&#x60; parameter is available for any extra information that a deployment system might need. It is a JSON text field that will be passed on when a deployment event is dispatched.  The &#x60;task&#x60; parameter is used by the deployment system to allow different execution paths. In the web world this might be &#x60;deploy:migrations&#x60; to run schema changes on the system. In the compiled world this could be a flag to compile an application with debugging enabled.  Users with &#x60;repo&#x60; or &#x60;repo_deployment&#x60; scopes can create a deployment for a given ref.  #### Merged branch response You will see this response when GitHub automatically merges the base branch into the topic branch instead of creating a deployment. This auto-merge happens when: *   Auto-merge option is enabled in the repository *   Topic branch does not include the latest changes on the base branch, which is &#x60;master&#x60; in the response example *   There are no merge conflicts  If there are no new commits in the base branch, a new request to create a deployment should give a successful response.  #### Merge conflict response This error happens when the &#x60;auto_merge&#x60; option is enabled and when the default branch (in this case &#x60;master&#x60;), can&#39;t be merged into the branch that&#39;s being deployed (in this case &#x60;topic-branch&#x60;), due to merge conflicts.  #### Failed commit status checks This error happens when the &#x60;required_contexts&#x60; parameter indicates that one or more contexts need to have a &#x60;success&#x60; status for the commit to be deployed, but one or more of the required contexts do not have a state of &#x60;success&#x60;.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param body: 
    :type body: dict | bytes

    """
    body = ReposCreateDeploymentRequest.from_dict(body)
    return web.Response(status=200)


async def repos_create_deployment_status(request: web.Request, owner, repo, deployment_id, body) -> web.Response:
    """Create a deployment status

    Users with &#x60;push&#x60; access can create deployment statuses for a given deployment.  GitHub Apps require &#x60;read &amp; write&#x60; access to \&quot;Deployments\&quot; and &#x60;read-only&#x60; access to \&quot;Repo contents\&quot; (for private repos). OAuth Apps require the &#x60;repo_deployment&#x60; scope.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param deployment_id: deployment_id parameter
    :type deployment_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = ReposCreateDeploymentStatusRequest.from_dict(body)
    return web.Response(status=200)


async def repos_create_dispatch_event(request: web.Request, owner, repo, body) -> web.Response:
    """Create a repository dispatch event

    You can use this endpoint to trigger a webhook event called &#x60;repository_dispatch&#x60; when you want activity that happens outside of GitHub Enterprise Server to trigger a GitHub Actions workflow or GitHub App webhook. You must configure your GitHub Actions workflow or GitHub App to run when the &#x60;repository_dispatch&#x60; event occurs. For an example &#x60;repository_dispatch&#x60; webhook payload, see \&quot;[RepositoryDispatchEvent](https://docs.github.com/enterprise-server@3.0/webhooks/event-payloads/#repository_dispatch).\&quot;  The &#x60;client_payload&#x60; parameter is available for any extra information that your workflow might need. This parameter is a JSON payload that will be passed on when the webhook event is dispatched. For example, the &#x60;client_payload&#x60; can include a message that a user would like to send using a GitHub Actions workflow. Or the &#x60;client_payload&#x60; can be used as a test to debug your workflow.  This endpoint requires write access to the repository by providing either:    - Personal access tokens with &#x60;repo&#x60; scope. For more information, see \&quot;[Creating a personal access token for the command line](https://docs.github.com/articles/creating-a-personal-access-token-for-the-command-line)\&quot; in the GitHub Help documentation.   - GitHub Apps with both &#x60;metadata:read&#x60; and &#x60;contents:read&amp;write&#x60; permissions.  This input example shows how you can use the &#x60;client_payload&#x60; as a test to debug your workflow.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param body: 
    :type body: dict | bytes

    """
    body = ReposCreateDispatchEventRequest.from_dict(body)
    return web.Response(status=200)


async def repos_create_for_authenticated_user(request: web.Request, body) -> web.Response:
    """Create a repository for the authenticated user

    Creates a new repository for the authenticated user.  **OAuth scope requirements**  When using [OAuth](https://docs.github.com/enterprise-server@3.0/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/), authorizations must include:  *   &#x60;public_repo&#x60; scope or &#x60;repo&#x60; scope to create a public repository. Note: For GitHub AE, use &#x60;repo&#x60; scope to create an internal repository. *   &#x60;repo&#x60; scope to create a private repository.

    :param body: 
    :type body: dict | bytes

    """
    body = ReposCreateForAuthenticatedUserRequest.from_dict(body)
    return web.Response(status=200)


async def repos_create_fork(request: web.Request, owner, repo, body=None) -> web.Response:
    """Create a fork

    Create a fork for the authenticated user.  **Note**: Forking a Repository happens asynchronously. You may have to wait a short period of time before you can access the git objects. If this takes longer than 5 minutes, be sure to contact [GitHub Enterprise Server Support](https://support.github.com/contact?tags&#x3D;dotcom-rest-api).

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param body: 
    :type body: dict | bytes

    """
    body = ReposCreateForkRequest.from_dict(body)
    return web.Response(status=200)


async def repos_create_in_org(request: web.Request, org, body) -> web.Response:
    """Create an organization repository

    Creates a new repository in the specified organization. The authenticated user must be a member of the organization.  **OAuth scope requirements**  When using [OAuth](https://docs.github.com/enterprise-server@3.0/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/), authorizations must include:  *   &#x60;public_repo&#x60; scope or &#x60;repo&#x60; scope to create a public repository. Note: For GitHub AE, use &#x60;repo&#x60; scope to create an internal repository. *   &#x60;repo&#x60; scope to create a private repository

    :param org: 
    :type org: str
    :param body: 
    :type body: dict | bytes

    """
    body = ReposCreateInOrgRequest.from_dict(body)
    return web.Response(status=200)


async def repos_create_or_update_file_contents(request: web.Request, owner, repo, path, body) -> web.Response:
    """Create or update file contents

    Creates a new file or replaces an existing file in a repository.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param path: path parameter
    :type path: str
    :param body: 
    :type body: dict | bytes

    """
    body = ReposCreateOrUpdateFileContentsRequest.from_dict(body)
    return web.Response(status=200)


async def repos_create_pages_site(request: web.Request, owner, repo, body) -> web.Response:
    """Create a GitHub Enterprise Server Pages site

    Configures a GitHub Enterprise Server Pages site. For more information, see \&quot;[About GitHub Pages](/github/working-with-github-pages/about-github-pages).\&quot;

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param body: 
    :type body: dict | bytes

    """
    body = ReposCreatePagesSiteRequest.from_dict(body)
    return web.Response(status=200)


async def repos_create_release(request: web.Request, owner, repo, body) -> web.Response:
    """Create a release

    Users with push access to the repository can create a release.  This endpoint triggers [notifications](https://docs.github.com/en/github/managing-subscriptions-and-notifications-on-github/about-notifications). Creating content too quickly using this endpoint may result in secondary rate limiting. See \&quot;[Secondary rate limits](https://docs.github.com/enterprise-server@3.0/rest/overview/resources-in-the-rest-api#secondary-rate-limits)\&quot; and \&quot;[Dealing with secondary rate limits](https://docs.github.com/enterprise-server@3.0/rest/guides/best-practices-for-integrators#dealing-with-secondary-rate-limits)\&quot; for details.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param body: 
    :type body: dict | bytes

    """
    body = ReposCreateReleaseRequest.from_dict(body)
    return web.Response(status=200)


async def repos_create_using_template(request: web.Request, template_owner, template_repo, body) -> web.Response:
    """Create a repository using a template

    Creates a new repository using a repository template. Use the &#x60;template_owner&#x60; and &#x60;template_repo&#x60; route parameters to specify the repository to use as the template. The authenticated user must own or be a member of an organization that owns the repository. To check if a repository is available to use as a template, get the repository&#39;s information using the [Get a repository](https://docs.github.com/enterprise-server@3.0/rest/reference/repos#get-a-repository) endpoint and check that the &#x60;is_template&#x60; key is &#x60;true&#x60;.  **OAuth scope requirements**  When using [OAuth](https://docs.github.com/enterprise-server@3.0/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/), authorizations must include:  *   &#x60;public_repo&#x60; scope or &#x60;repo&#x60; scope to create a public repository. Note: For GitHub AE, use &#x60;repo&#x60; scope to create an internal repository. *   &#x60;repo&#x60; scope to create a private repository

    :param template_owner: 
    :type template_owner: str
    :param template_repo: 
    :type template_repo: str
    :param body: 
    :type body: dict | bytes

    """
    body = ReposCreateUsingTemplateRequest.from_dict(body)
    return web.Response(status=200)


async def repos_create_webhook(request: web.Request, owner, repo, body=None) -> web.Response:
    """Create a repository webhook

    Repositories can have multiple webhooks installed. Each webhook should have a unique &#x60;config&#x60;. Multiple webhooks can share the same &#x60;config&#x60; as long as those webhooks do not have any &#x60;events&#x60; that overlap.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param body: 
    :type body: dict | bytes

    """
    body = ReposCreateWebhookRequest.from_dict(body)
    return web.Response(status=200)


async def repos_decline_invitation_for_authenticated_user(request: web.Request, invitation_id) -> web.Response:
    """Decline a repository invitation

    

    :param invitation_id: invitation_id parameter
    :type invitation_id: int

    """
    return web.Response(status=200)


async def repos_delete(request: web.Request, owner, repo) -> web.Response:
    """Delete a repository

    Deleting a repository requires admin access. If OAuth is used, the &#x60;delete_repo&#x60; scope is required.  If an organization owner has configured the organization to prevent members from deleting organization-owned repositories, you will get a &#x60;403 Forbidden&#x60; response.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str

    """
    return web.Response(status=200)


async def repos_delete_access_restrictions(request: web.Request, owner, repo, branch) -> web.Response:
    """Delete access restrictions

    Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub&#39;s products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  Disables the ability to restrict who can push to this branch.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param branch: The name of the branch.
    :type branch: str

    """
    return web.Response(status=200)


async def repos_delete_admin_branch_protection(request: web.Request, owner, repo, branch) -> web.Response:
    """Delete admin branch protection

    Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub&#39;s products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  Removing admin enforcement requires admin or owner permissions to the repository and branch protection to be enabled.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param branch: The name of the branch.
    :type branch: str

    """
    return web.Response(status=200)


async def repos_delete_branch_protection(request: web.Request, owner, repo, branch) -> web.Response:
    """Delete branch protection

    Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub&#39;s products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param branch: The name of the branch.
    :type branch: str

    """
    return web.Response(status=200)


async def repos_delete_commit_comment(request: web.Request, owner, repo, comment_id) -> web.Response:
    """Delete a commit comment

    

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param comment_id: comment_id parameter
    :type comment_id: int

    """
    return web.Response(status=200)


async def repos_delete_commit_signature_protection(request: web.Request, owner, repo, branch) -> web.Response:
    """Delete commit signature protection

    Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub&#39;s products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  When authenticated with admin or owner permissions to the repository, you can use this endpoint to disable required signed commits on a branch. You must enable branch protection to require signed commits.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param branch: The name of the branch.
    :type branch: str

    """
    return web.Response(status=200)


async def repos_delete_deploy_key(request: web.Request, owner, repo, key_id) -> web.Response:
    """Delete a deploy key

    Deploy keys are immutable. If you need to update a key, remove the key and create a new one instead.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param key_id: key_id parameter
    :type key_id: int

    """
    return web.Response(status=200)


async def repos_delete_deployment(request: web.Request, owner, repo, deployment_id) -> web.Response:
    """Delete a deployment

    If the repository only has one deployment, you can delete the deployment regardless of its status. If the repository has more than one deployment, you can only delete inactive deployments. This ensures that repositories with multiple deployments will always have an active deployment. Anyone with &#x60;repo&#x60; or &#x60;repo_deployment&#x60; scopes can delete a deployment.  To set a deployment as inactive, you must:  *   Create a new deployment that is active so that the system has a record of the current state, then delete the previously active deployment. *   Mark the active deployment as inactive by adding any non-successful deployment status.  For more information, see \&quot;[Create a deployment](https://docs.github.com/enterprise-server@3.0/rest/reference/repos/#create-a-deployment)\&quot; and \&quot;[Create a deployment status](https://docs.github.com/enterprise-server@3.0/rest/reference/repos#create-a-deployment-status).\&quot;

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param deployment_id: deployment_id parameter
    :type deployment_id: int

    """
    return web.Response(status=200)


async def repos_delete_file(request: web.Request, owner, repo, path, body) -> web.Response:
    """Delete a file

    Deletes a file in a repository.  You can provide an additional &#x60;committer&#x60; parameter, which is an object containing information about the committer. Or, you can provide an &#x60;author&#x60; parameter, which is an object containing information about the author.  The &#x60;author&#x60; section is optional and is filled in with the &#x60;committer&#x60; information if omitted. If the &#x60;committer&#x60; information is omitted, the authenticated user&#39;s information is used.  You must provide values for both &#x60;name&#x60; and &#x60;email&#x60;, whether you choose to use &#x60;author&#x60; or &#x60;committer&#x60;. Otherwise, you&#39;ll receive a &#x60;422&#x60; status code.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param path: path parameter
    :type path: str
    :param body: 
    :type body: dict | bytes

    """
    body = ReposDeleteFileRequest.from_dict(body)
    return web.Response(status=200)


async def repos_delete_invitation(request: web.Request, owner, repo, invitation_id) -> web.Response:
    """Delete a repository invitation

    

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param invitation_id: invitation_id parameter
    :type invitation_id: int

    """
    return web.Response(status=200)


async def repos_delete_pages_site(request: web.Request, owner, repo) -> web.Response:
    """Delete a GitHub Enterprise Server Pages site

    

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str

    """
    return web.Response(status=200)


async def repos_delete_pull_request_review_protection(request: web.Request, owner, repo, branch) -> web.Response:
    """Delete pull request review protection

    Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub&#39;s products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param branch: The name of the branch.
    :type branch: str

    """
    return web.Response(status=200)


async def repos_delete_release(request: web.Request, owner, repo, release_id) -> web.Response:
    """Delete a release

    Users with push access to the repository can delete a release.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param release_id: release_id parameter
    :type release_id: int

    """
    return web.Response(status=200)


async def repos_delete_release_asset(request: web.Request, owner, repo, asset_id) -> web.Response:
    """Delete a release asset

    

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param asset_id: asset_id parameter
    :type asset_id: int

    """
    return web.Response(status=200)


async def repos_delete_webhook(request: web.Request, owner, repo, hook_id) -> web.Response:
    """Delete a repository webhook

    

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param hook_id: 
    :type hook_id: int

    """
    return web.Response(status=200)


async def repos_download_tarball_archive(request: web.Request, owner, repo, ref) -> web.Response:
    """Download a repository archive (tar)

    Gets a redirect URL to download a tar archive for a repository. If you omit &#x60;:ref&#x60;, the repository’s default branch (usually &#x60;master&#x60;) will be used. Please make sure your HTTP framework is configured to follow redirects or you will need to use the &#x60;Location&#x60; header to make a second &#x60;GET&#x60; request. **Note**: For private repositories, these links are temporary and expire after five minutes.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param ref: 
    :type ref: str

    """
    return web.Response(status=200)


async def repos_download_zipball_archive(request: web.Request, owner, repo, ref) -> web.Response:
    """Download a repository archive (zip)

    Gets a redirect URL to download a zip archive for a repository. If you omit &#x60;:ref&#x60;, the repository’s default branch (usually &#x60;master&#x60;) will be used. Please make sure your HTTP framework is configured to follow redirects or you will need to use the &#x60;Location&#x60; header to make a second &#x60;GET&#x60; request. **Note**: For private repositories, these links are temporary and expire after five minutes.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param ref: 
    :type ref: str

    """
    return web.Response(status=200)


async def repos_get(request: web.Request, owner, repo) -> web.Response:
    """Get a repository

    When you pass the &#x60;scarlet-witch-preview&#x60; media type, requests to get a repository will also return the repository&#39;s code of conduct if it can be detected from the repository&#39;s code of conduct file.  The &#x60;parent&#x60; and &#x60;source&#x60; objects are present when the repository is a fork. &#x60;parent&#x60; is the repository this repository was forked from, &#x60;source&#x60; is the ultimate source for the network.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str

    """
    return web.Response(status=200)


async def repos_get_access_restrictions(request: web.Request, owner, repo, branch) -> web.Response:
    """Get access restrictions

    Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub&#39;s products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  Lists who has access to this protected branch.  **Note**: Users, apps, and teams &#x60;restrictions&#x60; are only available for organization-owned repositories.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param branch: The name of the branch.
    :type branch: str

    """
    return web.Response(status=200)


async def repos_get_admin_branch_protection(request: web.Request, owner, repo, branch) -> web.Response:
    """Get admin branch protection

    Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub&#39;s products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param branch: The name of the branch.
    :type branch: str

    """
    return web.Response(status=200)


async def repos_get_all_status_check_contexts(request: web.Request, owner, repo, branch) -> web.Response:
    """Get all status check contexts

    Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub&#39;s products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param branch: The name of the branch.
    :type branch: str

    """
    return web.Response(status=200)


async def repos_get_all_topics(request: web.Request, owner, repo, page=None, per_page=None) -> web.Response:
    """Get all repository topics

    

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param page: Page number of the results to fetch.
    :type page: int
    :param per_page: Results per page (max 100)
    :type per_page: int

    """
    return web.Response(status=200)


async def repos_get_apps_with_access_to_protected_branch(request: web.Request, owner, repo, branch) -> web.Response:
    """Get apps with access to the protected branch

    Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub&#39;s products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  Lists the GitHub Apps that have push access to this branch. Only installed GitHub Apps with &#x60;write&#x60; access to the &#x60;contents&#x60; permission can be added as authorized actors on a protected branch.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param branch: The name of the branch.
    :type branch: str

    """
    return web.Response(status=200)


async def repos_get_branch(request: web.Request, owner, repo, branch) -> web.Response:
    """Get a branch

    

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param branch: The name of the branch.
    :type branch: str

    """
    return web.Response(status=200)


async def repos_get_branch_protection(request: web.Request, owner, repo, branch) -> web.Response:
    """Get branch protection

    Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub&#39;s products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param branch: The name of the branch.
    :type branch: str

    """
    return web.Response(status=200)


async def repos_get_code_frequency_stats(request: web.Request, owner, repo) -> web.Response:
    """Get the weekly commit activity

    Returns a weekly aggregate of the number of additions and deletions pushed to a repository.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str

    """
    return web.Response(status=200)


async def repos_get_collaborator_permission_level(request: web.Request, owner, repo, username) -> web.Response:
    """Get repository permissions for a user

    Checks the repository permission of a collaborator. The possible repository permissions are &#x60;admin&#x60;, &#x60;write&#x60;, &#x60;read&#x60;, and &#x60;none&#x60;.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param username: 
    :type username: str

    """
    return web.Response(status=200)


async def repos_get_combined_status_for_ref(request: web.Request, owner, repo, ref, per_page=None, page=None) -> web.Response:
    """Get the combined status for a specific reference

    Users with pull access in a repository can access a combined view of commit statuses for a given ref. The ref can be a SHA, a branch name, or a tag name.   Additionally, a combined &#x60;state&#x60; is returned. The &#x60;state&#x60; is one of:  *   **failure** if any of the contexts report as &#x60;error&#x60; or &#x60;failure&#x60; *   **pending** if there are no statuses or a context is &#x60;pending&#x60; *   **success** if the latest status for all contexts is &#x60;success&#x60;

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param ref: ref parameter
    :type ref: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def repos_get_commit(request: web.Request, owner, repo, ref, page=None, per_page=None) -> web.Response:
    """Get a commit

    Returns the contents of a single commit reference. You must have &#x60;read&#x60; access for the repository to use this endpoint.  **Note:** If there are more than 300 files in the commit diff, the response will include pagination link headers for the remaining files, up to a limit of 3000 files. Each page contains the static commit information, and the only changes are to the file listing.  You can pass the appropriate [media type](https://docs.github.com/enterprise-server@3.0/rest/overview/media-types/#commits-commit-comparison-and-pull-requests) to  fetch &#x60;diff&#x60; and &#x60;patch&#x60; formats. Diffs with binary data will have no &#x60;patch&#x60; property.  To return only the SHA-1 hash of the commit reference, you can provide the &#x60;sha&#x60; custom [media type](https://docs.github.com/enterprise-server@3.0/rest/overview/media-types/#commits-commit-comparison-and-pull-requests) in the &#x60;Accept&#x60; header. You can use this endpoint to check if a remote reference&#39;s SHA-1 hash is the same as your local reference&#39;s SHA-1 hash by providing the local SHA-1 reference as the ETag.  **Signature verification object**  The response will include a &#x60;verification&#x60; object that describes the result of verifying the commit&#39;s signature. The following fields are included in the &#x60;verification&#x60; object:  | Name | Type | Description | | ---- | ---- | ----------- | | &#x60;verified&#x60; | &#x60;boolean&#x60; | Indicates whether GitHub considers the signature in this commit to be verified. | | &#x60;reason&#x60; | &#x60;string&#x60; | The reason for verified value. Possible values and their meanings are enumerated in table below. | | &#x60;signature&#x60; | &#x60;string&#x60; | The signature that was extracted from the commit. | | &#x60;payload&#x60; | &#x60;string&#x60; | The value that was signed. |  These are the possible values for &#x60;reason&#x60; in the &#x60;verification&#x60; object:  | Value | Description | | ----- | ----------- | | &#x60;expired_key&#x60; | The key that made the signature is expired. | | &#x60;not_signing_key&#x60; | The \&quot;signing\&quot; flag is not among the usage flags in the GPG key that made the signature. | | &#x60;gpgverify_error&#x60; | There was an error communicating with the signature verification service. | | &#x60;gpgverify_unavailable&#x60; | The signature verification service is currently unavailable. | | &#x60;unsigned&#x60; | The object does not include a signature. | | &#x60;unknown_signature_type&#x60; | A non-PGP signature was found in the commit. | | &#x60;no_user&#x60; | No user was associated with the &#x60;committer&#x60; email address in the commit. | | &#x60;unverified_email&#x60; | The &#x60;committer&#x60; email address in the commit was associated with a user, but the email address is not verified on her/his account. | | &#x60;bad_email&#x60; | The &#x60;committer&#x60; email address in the commit is not included in the identities of the PGP key that made the signature. | | &#x60;unknown_key&#x60; | The key that made the signature has not been registered with any user&#39;s account. | | &#x60;malformed_signature&#x60; | There was an error parsing the signature. | | &#x60;invalid&#x60; | The signature could not be cryptographically verified using the key whose key-id was found in the signature. | | &#x60;valid&#x60; | None of the above errors applied, so the signature is considered to be verified. |

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param ref: ref parameter
    :type ref: str
    :param page: Page number of the results to fetch.
    :type page: int
    :param per_page: Results per page (max 100)
    :type per_page: int

    """
    return web.Response(status=200)


async def repos_get_commit_activity_stats(request: web.Request, owner, repo) -> web.Response:
    """Get the last year of commit activity

    Returns the last year of commit activity grouped by week. The &#x60;days&#x60; array is a group of commits per day, starting on &#x60;Sunday&#x60;.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str

    """
    return web.Response(status=200)


async def repos_get_commit_comment(request: web.Request, owner, repo, comment_id) -> web.Response:
    """Get a commit comment

    

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param comment_id: comment_id parameter
    :type comment_id: int

    """
    return web.Response(status=200)


async def repos_get_commit_signature_protection(request: web.Request, owner, repo, branch) -> web.Response:
    """Get commit signature protection

    Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub&#39;s products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  When authenticated with admin or owner permissions to the repository, you can use this endpoint to check whether a branch requires signed commits. An enabled status of &#x60;true&#x60; indicates you must sign commits on this branch. For more information, see [Signing commits with GPG](https://docs.github.com/articles/signing-commits-with-gpg) in GitHub Help.  **Note**: You must enable branch protection to require signed commits.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param branch: The name of the branch.
    :type branch: str

    """
    return web.Response(status=200)


async def repos_get_content(request: web.Request, owner, repo, path, ref=None) -> web.Response:
    """Get repository content

    Gets the contents of a file or directory in a repository. Specify the file path or directory in &#x60;:path&#x60;. If you omit &#x60;:path&#x60;, you will receive the contents of the repository&#39;s root directory. See the description below regarding what the API response includes for directories.   Files and symlinks support [a custom media type](https://docs.github.com/enterprise-server@3.0/rest/reference/repos#custom-media-types) for retrieving the raw content or rendered HTML (when supported). All content types support [a custom media type](https://docs.github.com/enterprise-server@3.0/rest/reference/repos#custom-media-types) to ensure the content is returned in a consistent object format.  **Note**: *   To get a repository&#39;s contents recursively, you can [recursively get the tree](https://docs.github.com/enterprise-server@3.0/rest/reference/git#trees). *   This API has an upper limit of 1,000 files for a directory. If you need to retrieve more files, use the [Git Trees API](https://docs.github.com/enterprise-server@3.0/rest/reference/git#get-a-tree). *   This API supports files up to 1 megabyte in size.  #### If the content is a directory The response will be an array of objects, one object for each item in the directory. When listing the contents of a directory, submodules have their \&quot;type\&quot; specified as \&quot;file\&quot;. Logically, the value _should_ be \&quot;submodule\&quot;. This behavior exists in API v3 [for backwards compatibility purposes](https://git.io/v1YCW). In the next major version of the API, the type will be returned as \&quot;submodule\&quot;.  #### If the content is a symlink  If the requested &#x60;:path&#x60; points to a symlink, and the symlink&#39;s target is a normal file in the repository, then the API responds with the content of the file (in the format shown in the example. Otherwise, the API responds with an object  describing the symlink itself.  #### If the content is a submodule The &#x60;submodule_git_url&#x60; identifies the location of the submodule repository, and the &#x60;sha&#x60; identifies a specific commit within the submodule repository. Git uses the given URL when cloning the submodule repository, and checks out the submodule at that specific commit.  If the submodule repository is not hosted on github.com, the Git URLs (&#x60;git_url&#x60; and &#x60;_links[\&quot;git\&quot;]&#x60;) and the github.com URLs (&#x60;html_url&#x60; and &#x60;_links[\&quot;html\&quot;]&#x60;) will have null values.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param path: path parameter
    :type path: str
    :param ref: The name of the commit/branch/tag. Default: the repository’s default branch (usually &#x60;master&#x60;)
    :type ref: str

    """
    return web.Response(status=200)


async def repos_get_contributors_stats(request: web.Request, owner, repo) -> web.Response:
    """Get all contributor commit activity

     Returns the &#x60;total&#x60; number of commits authored by the contributor. In addition, the response includes a Weekly Hash (&#x60;weeks&#x60; array) with the following information:  *   &#x60;w&#x60; - Start of the week, given as a [Unix timestamp](http://en.wikipedia.org/wiki/Unix_time). *   &#x60;a&#x60; - Number of additions *   &#x60;d&#x60; - Number of deletions *   &#x60;c&#x60; - Number of commits

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str

    """
    return web.Response(status=200)


async def repos_get_deploy_key(request: web.Request, owner, repo, key_id) -> web.Response:
    """Get a deploy key

    

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param key_id: key_id parameter
    :type key_id: int

    """
    return web.Response(status=200)


async def repos_get_deployment(request: web.Request, owner, repo, deployment_id) -> web.Response:
    """Get a deployment

    

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param deployment_id: deployment_id parameter
    :type deployment_id: int

    """
    return web.Response(status=200)


async def repos_get_deployment_status(request: web.Request, owner, repo, deployment_id, status_id) -> web.Response:
    """Get a deployment status

    Users with pull access can view a deployment status for a deployment:

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param deployment_id: deployment_id parameter
    :type deployment_id: int
    :param status_id: 
    :type status_id: int

    """
    return web.Response(status=200)


async def repos_get_latest_pages_build(request: web.Request, owner, repo) -> web.Response:
    """Get latest Pages build

    

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str

    """
    return web.Response(status=200)


async def repos_get_latest_release(request: web.Request, owner, repo) -> web.Response:
    """Get the latest release

    View the latest published full release for the repository.  The latest release is the most recent non-prerelease, non-draft release, sorted by the &#x60;created_at&#x60; attribute. The &#x60;created_at&#x60; attribute is the date of the commit used for the release, and not the date when the release was drafted or published.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str

    """
    return web.Response(status=200)


async def repos_get_pages(request: web.Request, owner, repo) -> web.Response:
    """Get a GitHub Enterprise Server Pages site

    

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str

    """
    return web.Response(status=200)


async def repos_get_pages_build(request: web.Request, owner, repo, build_id) -> web.Response:
    """Get GitHub Enterprise Server Pages build

    

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param build_id: 
    :type build_id: int

    """
    return web.Response(status=200)


async def repos_get_participation_stats(request: web.Request, owner, repo) -> web.Response:
    """Get the weekly commit count

    Returns the total commit counts for the &#x60;owner&#x60; and total commit counts in &#x60;all&#x60;. &#x60;all&#x60; is everyone combined, including the &#x60;owner&#x60; in the last 52 weeks. If you&#39;d like to get the commit counts for non-owners, you can subtract &#x60;owner&#x60; from &#x60;all&#x60;.  The array order is oldest week (index 0) to most recent week.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str

    """
    return web.Response(status=200)


async def repos_get_pull_request_review_protection(request: web.Request, owner, repo, branch) -> web.Response:
    """Get pull request review protection

    Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub&#39;s products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param branch: The name of the branch.
    :type branch: str

    """
    return web.Response(status=200)


async def repos_get_punch_card_stats(request: web.Request, owner, repo) -> web.Response:
    """Get the hourly commit count for each day

    Each array contains the day number, hour number, and number of commits:  *   &#x60;0-6&#x60;: Sunday - Saturday *   &#x60;0-23&#x60;: Hour of day *   Number of commits  For example, &#x60;[2, 14, 25]&#x60; indicates that there were 25 total commits, during the 2:00pm hour on Tuesdays. All times are based on the time zone of individual commits.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str

    """
    return web.Response(status=200)


async def repos_get_readme(request: web.Request, owner, repo, ref=None) -> web.Response:
    """Get a repository README

    Gets the preferred README for a repository.  READMEs support [custom media types](https://docs.github.com/enterprise-server@3.0/rest/reference/repos#custom-media-types) for retrieving the raw content or rendered HTML.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param ref: The name of the commit/branch/tag. Default: the repository’s default branch (usually &#x60;master&#x60;)
    :type ref: str

    """
    return web.Response(status=200)


async def repos_get_readme_in_directory(request: web.Request, owner, repo, dir, ref=None) -> web.Response:
    """Get a repository README for a directory

    Gets the README from a repository directory.  READMEs support [custom media types](https://docs.github.com/enterprise-server@3.0/rest/reference/repos#custom-media-types) for retrieving the raw content or rendered HTML.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param dir: The alternate path to look for a README file
    :type dir: str
    :param ref: The name of the commit/branch/tag. Default: the repository’s default branch (usually &#x60;master&#x60;)
    :type ref: str

    """
    return web.Response(status=200)


async def repos_get_release(request: web.Request, owner, repo, release_id) -> web.Response:
    """Get a release

    **Note:** This returns an &#x60;upload_url&#x60; key corresponding to the endpoint for uploading release assets. This key is a [hypermedia resource](https://docs.github.com/enterprise-server@3.0/rest/overview/resources-in-the-rest-api#hypermedia).

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param release_id: release_id parameter
    :type release_id: int

    """
    return web.Response(status=200)


async def repos_get_release_asset(request: web.Request, owner, repo, asset_id) -> web.Response:
    """Get a release asset

    To download the asset&#39;s binary content, set the &#x60;Accept&#x60; header of the request to [&#x60;application/octet-stream&#x60;](https://docs.github.com/enterprise-server@3.0/rest/overview/media-types). The API will either redirect the client to the location, or stream it directly if possible. API clients should handle both a &#x60;200&#x60; or &#x60;302&#x60; response.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param asset_id: asset_id parameter
    :type asset_id: int

    """
    return web.Response(status=200)


async def repos_get_release_by_tag(request: web.Request, owner, repo, tag) -> web.Response:
    """Get a release by tag name

    Get a published release with the specified tag.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param tag: tag parameter
    :type tag: str

    """
    return web.Response(status=200)


async def repos_get_status_checks_protection(request: web.Request, owner, repo, branch) -> web.Response:
    """Get status checks protection

    Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub&#39;s products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param branch: The name of the branch.
    :type branch: str

    """
    return web.Response(status=200)


async def repos_get_teams_with_access_to_protected_branch(request: web.Request, owner, repo, branch) -> web.Response:
    """Get teams with access to the protected branch

    Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub&#39;s products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  Lists the teams who have push access to this branch. The list includes child teams.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param branch: The name of the branch.
    :type branch: str

    """
    return web.Response(status=200)


async def repos_get_users_with_access_to_protected_branch(request: web.Request, owner, repo, branch) -> web.Response:
    """Get users with access to the protected branch

    Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub&#39;s products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  Lists the people who have push access to this branch.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param branch: The name of the branch.
    :type branch: str

    """
    return web.Response(status=200)


async def repos_get_webhook(request: web.Request, owner, repo, hook_id) -> web.Response:
    """Get a repository webhook

    Returns a webhook configured in a repository. To get only the webhook &#x60;config&#x60; properties, see \&quot;[Get a webhook configuration for a repository](/rest/reference/repos#get-a-webhook-configuration-for-a-repository).\&quot;

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param hook_id: 
    :type hook_id: int

    """
    return web.Response(status=200)


async def repos_get_webhook_config_for_repo(request: web.Request, owner, repo, hook_id) -> web.Response:
    """Get a webhook configuration for a repository

    Returns the webhook configuration for a repository. To get more information about the webhook, including the &#x60;active&#x60; state and &#x60;events&#x60;, use \&quot;[Get a repository webhook](/rest/reference/orgs#get-a-repository-webhook).\&quot;  Access tokens must have the &#x60;read:repo_hook&#x60; or &#x60;repo&#x60; scope, and GitHub Apps must have the &#x60;repository_hooks:read&#x60; permission.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param hook_id: 
    :type hook_id: int

    """
    return web.Response(status=200)


async def repos_list_branches(request: web.Request, owner, repo, protected=None, per_page=None, page=None) -> web.Response:
    """List branches

    

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param protected: Setting to &#x60;true&#x60; returns only protected branches. When set to &#x60;false&#x60;, only unprotected branches are returned. Omitting this parameter returns all branches.
    :type protected: bool
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def repos_list_branches_for_head_commit(request: web.Request, owner, repo, commit_sha) -> web.Response:
    """List branches for HEAD commit

    Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub&#39;s products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  Returns all branches where the given commit SHA is the HEAD, or latest commit for the branch.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param commit_sha: commit_sha parameter
    :type commit_sha: str

    """
    return web.Response(status=200)


async def repos_list_collaborators(request: web.Request, owner, repo, affiliation=None, per_page=None, page=None) -> web.Response:
    """List repository collaborators

    For organization-owned repositories, the list of collaborators includes outside collaborators, organization members that are direct collaborators, organization members with access through team memberships, organization members with access through default organization permissions, and organization owners.  Team members will include the members of child teams.  You must authenticate using an access token with the &#x60;read:org&#x60; and &#x60;repo&#x60; scopes with push access to use this endpoint. GitHub Apps must have the &#x60;members&#x60; organization permission and &#x60;metadata&#x60; repository permission to use this endpoint.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param affiliation: Filter collaborators returned by their affiliation. Can be one of:   \\* &#x60;outside&#x60;: All outside collaborators of an organization-owned repository.   \\* &#x60;direct&#x60;: All collaborators with permissions to an organization-owned repository, regardless of organization membership status.   \\* &#x60;all&#x60;: All collaborators the authenticated user can see.
    :type affiliation: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def repos_list_comments_for_commit(request: web.Request, owner, repo, commit_sha, per_page=None, page=None) -> web.Response:
    """List commit comments

    Use the &#x60;:commit_sha&#x60; to specify the commit that will have its comments listed.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param commit_sha: commit_sha parameter
    :type commit_sha: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def repos_list_commit_comments_for_repo(request: web.Request, owner, repo, per_page=None, page=None) -> web.Response:
    """List commit comments for a repository

    Commit Comments use [these custom media types](https://docs.github.com/enterprise-server@3.0/rest/reference/repos#custom-media-types). You can read more about the use of media types in the API [here](https://docs.github.com/enterprise-server@3.0/rest/overview/media-types/).  Comments are ordered by ascending ID.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def repos_list_commit_statuses_for_ref(request: web.Request, owner, repo, ref, per_page=None, page=None) -> web.Response:
    """List commit statuses for a reference

    Users with pull access in a repository can view commit statuses for a given ref. The ref can be a SHA, a branch name, or a tag name. Statuses are returned in reverse chronological order. The first status in the list will be the latest one.  This resource is also available via a legacy route: &#x60;GET /repos/:owner/:repo/statuses/:ref&#x60;.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param ref: ref parameter
    :type ref: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def repos_list_commits(request: web.Request, owner, repo, sha=None, path=None, author=None, since=None, until=None, per_page=None, page=None) -> web.Response:
    """List commits

    **Signature verification object**  The response will include a &#x60;verification&#x60; object that describes the result of verifying the commit&#39;s signature. The following fields are included in the &#x60;verification&#x60; object:  | Name | Type | Description | | ---- | ---- | ----------- | | &#x60;verified&#x60; | &#x60;boolean&#x60; | Indicates whether GitHub considers the signature in this commit to be verified. | | &#x60;reason&#x60; | &#x60;string&#x60; | The reason for verified value. Possible values and their meanings are enumerated in table below. | | &#x60;signature&#x60; | &#x60;string&#x60; | The signature that was extracted from the commit. | | &#x60;payload&#x60; | &#x60;string&#x60; | The value that was signed. |  These are the possible values for &#x60;reason&#x60; in the &#x60;verification&#x60; object:  | Value | Description | | ----- | ----------- | | &#x60;expired_key&#x60; | The key that made the signature is expired. | | &#x60;not_signing_key&#x60; | The \&quot;signing\&quot; flag is not among the usage flags in the GPG key that made the signature. | | &#x60;gpgverify_error&#x60; | There was an error communicating with the signature verification service. | | &#x60;gpgverify_unavailable&#x60; | The signature verification service is currently unavailable. | | &#x60;unsigned&#x60; | The object does not include a signature. | | &#x60;unknown_signature_type&#x60; | A non-PGP signature was found in the commit. | | &#x60;no_user&#x60; | No user was associated with the &#x60;committer&#x60; email address in the commit. | | &#x60;unverified_email&#x60; | The &#x60;committer&#x60; email address in the commit was associated with a user, but the email address is not verified on her/his account. | | &#x60;bad_email&#x60; | The &#x60;committer&#x60; email address in the commit is not included in the identities of the PGP key that made the signature. | | &#x60;unknown_key&#x60; | The key that made the signature has not been registered with any user&#39;s account. | | &#x60;malformed_signature&#x60; | There was an error parsing the signature. | | &#x60;invalid&#x60; | The signature could not be cryptographically verified using the key whose key-id was found in the signature. | | &#x60;valid&#x60; | None of the above errors applied, so the signature is considered to be verified. |

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param sha: SHA or branch to start listing commits from. Default: the repository’s default branch (usually &#x60;master&#x60;).
    :type sha: str
    :param path: Only commits containing this file path will be returned.
    :type path: str
    :param author: GitHub login or email address by which to filter by commit author.
    :type author: str
    :param since: Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;.
    :type since: str
    :param until: Only commits before this date will be returned. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;.
    :type until: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    since = util.deserialize_datetime(since)
    until = util.deserialize_datetime(until)
    return web.Response(status=200)


async def repos_list_contributors(request: web.Request, owner, repo, anon=None, per_page=None, page=None) -> web.Response:
    """List repository contributors

    Lists contributors to the specified repository and sorts them by the number of commits per contributor in descending order. This endpoint may return information that is a few hours old because the GitHub REST API v3 caches contributor data to improve performance.  GitHub identifies contributors by author email address. This endpoint groups contribution counts by GitHub user, which includes all associated email addresses. To improve performance, only the first 500 author email addresses in the repository link to GitHub users. The rest will appear as anonymous contributors without associated GitHub user information.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param anon: Set to &#x60;1&#x60; or &#x60;true&#x60; to include anonymous contributors in results.
    :type anon: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def repos_list_deploy_keys(request: web.Request, owner, repo, per_page=None, page=None) -> web.Response:
    """List deploy keys

    

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def repos_list_deployment_statuses(request: web.Request, owner, repo, deployment_id, per_page=None, page=None) -> web.Response:
    """List deployment statuses

    Users with pull access can view deployment statuses for a deployment:

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param deployment_id: deployment_id parameter
    :type deployment_id: int
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def repos_list_deployments(request: web.Request, owner, repo, sha=None, ref=None, task=None, environment=None, per_page=None, page=None) -> web.Response:
    """List deployments

    Simple filtering of deployments is available via query parameters:

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param sha: The SHA recorded at creation time.
    :type sha: str
    :param ref: The name of the ref. This can be a branch, tag, or SHA.
    :type ref: str
    :param task: The name of the task for the deployment (e.g., &#x60;deploy&#x60; or &#x60;deploy:migrations&#x60;).
    :type task: str
    :param environment: The name of the environment that was deployed to (e.g., &#x60;staging&#x60; or &#x60;production&#x60;).
    :type environment: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def repos_list_for_authenticated_user(request: web.Request, visibility=None, affiliation=None, type=None, sort=None, direction=None, per_page=None, page=None, since=None, before=None) -> web.Response:
    """List repositories for the authenticated user

    Lists repositories that the authenticated user has explicit permission (&#x60;:read&#x60;, &#x60;:write&#x60;, or &#x60;:admin&#x60;) to access.  The authenticated user has explicit permission to access repositories they own, repositories where they are a collaborator, and repositories that they can access through an organization membership.

    :param visibility: Can be one of &#x60;all&#x60;, &#x60;public&#x60;, or &#x60;private&#x60;. Note: For GitHub AE, can be one of &#x60;all&#x60;, &#x60;internal&#x60;, or &#x60;private&#x60;.
    :type visibility: str
    :param affiliation: Comma-separated list of values. Can include:   \\* &#x60;owner&#x60;: Repositories that are owned by the authenticated user.   \\* &#x60;collaborator&#x60;: Repositories that the user has been added to as a collaborator.   \\* &#x60;organization_member&#x60;: Repositories that the user has access to through being a member of an organization. This includes every repository on every team that the user is on.
    :type affiliation: str
    :param type: Can be one of &#x60;all&#x60;, &#x60;owner&#x60;, &#x60;public&#x60;, &#x60;private&#x60;, &#x60;member&#x60;. Note: For GitHub AE, can be one of &#x60;all&#x60;, &#x60;owner&#x60;, &#x60;internal&#x60;, &#x60;private&#x60;, &#x60;member&#x60;. Default: &#x60;all&#x60;      Will cause a &#x60;422&#x60; error if used in the same request as **visibility** or **affiliation**. Will cause a &#x60;422&#x60; error if used in the same request as **visibility** or **affiliation**.
    :type type: str
    :param sort: Can be one of &#x60;created&#x60;, &#x60;updated&#x60;, &#x60;pushed&#x60;, &#x60;full_name&#x60;.
    :type sort: str
    :param direction: Can be one of &#x60;asc&#x60; or &#x60;desc&#x60;. Default: &#x60;asc&#x60; when using &#x60;full_name&#x60;, otherwise &#x60;desc&#x60;
    :type direction: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int
    :param since: Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;.
    :type since: str
    :param before: Only show notifications updated before the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;.
    :type before: str

    """
    since = util.deserialize_datetime(since)
    before = util.deserialize_datetime(before)
    return web.Response(status=200)


async def repos_list_for_org(request: web.Request, org, type=None, sort=None, direction=None, per_page=None, page=None) -> web.Response:
    """List organization repositories

    Lists repositories for the specified organization.

    :param org: 
    :type org: str
    :param type: Specifies the types of repositories you want returned. Can be one of &#x60;all&#x60;, &#x60;public&#x60;, &#x60;private&#x60;, &#x60;forks&#x60;, &#x60;sources&#x60;, &#x60;member&#x60;, &#x60;internal&#x60;. Note: For GitHub AE, can be one of &#x60;all&#x60;, &#x60;private&#x60;, &#x60;forks&#x60;, &#x60;sources&#x60;, &#x60;member&#x60;, &#x60;internal&#x60;. Default: &#x60;all&#x60;. If your organization is associated with an enterprise account using GitHub Enterprise Cloud or GitHub Enterprise Server 2.20+, &#x60;type&#x60; can also be &#x60;internal&#x60;. However, the &#x60;internal&#x60; value is not yet supported when a GitHub App calls this API with an installation access token.
    :type type: str
    :param sort: Can be one of &#x60;created&#x60;, &#x60;updated&#x60;, &#x60;pushed&#x60;, &#x60;full_name&#x60;.
    :type sort: str
    :param direction: Can be one of &#x60;asc&#x60; or &#x60;desc&#x60;. Default: when using &#x60;full_name&#x60;: &#x60;asc&#x60;, otherwise &#x60;desc&#x60;
    :type direction: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def repos_list_for_user(request: web.Request, username, type=None, sort=None, direction=None, per_page=None, page=None) -> web.Response:
    """List repositories for a user

    Lists public repositories for the specified user. Note: For GitHub AE, this endpoint will list internal repositories for the specified user.

    :param username: 
    :type username: str
    :param type: Can be one of &#x60;all&#x60;, &#x60;owner&#x60;, &#x60;member&#x60;.
    :type type: str
    :param sort: Can be one of &#x60;created&#x60;, &#x60;updated&#x60;, &#x60;pushed&#x60;, &#x60;full_name&#x60;.
    :type sort: str
    :param direction: Can be one of &#x60;asc&#x60; or &#x60;desc&#x60;. Default: &#x60;asc&#x60; when using &#x60;full_name&#x60;, otherwise &#x60;desc&#x60;
    :type direction: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def repos_list_forks(request: web.Request, owner, repo, sort=None, per_page=None, page=None) -> web.Response:
    """List forks

    

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param sort: The sort order. Can be either &#x60;newest&#x60;, &#x60;oldest&#x60;, or &#x60;stargazers&#x60;.
    :type sort: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def repos_list_invitations(request: web.Request, owner, repo, per_page=None, page=None) -> web.Response:
    """List repository invitations

    When authenticating as a user with admin rights to a repository, this endpoint will list all currently open repository invitations.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def repos_list_invitations_for_authenticated_user(request: web.Request, per_page=None, page=None) -> web.Response:
    """List repository invitations for the authenticated user

    When authenticating as a user, this endpoint will list all currently open repository invitations for that user.

    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def repos_list_languages(request: web.Request, owner, repo) -> web.Response:
    """List repository languages

    Lists languages for the specified repository. The value shown for each language is the number of bytes of code written in that language.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str

    """
    return web.Response(status=200)


async def repos_list_pages_builds(request: web.Request, owner, repo, per_page=None, page=None) -> web.Response:
    """List GitHub Enterprise Server Pages builds

    

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def repos_list_public(request: web.Request, since=None, visibility=None) -> web.Response:
    """List public repositories

    Lists all public repositories in the order that they were created.  Note: - For GitHub Enterprise Server, this endpoint will only list repositories available to all users on the enterprise. - Pagination is powered exclusively by the &#x60;since&#x60; parameter. Use the [Link header](https://docs.github.com/enterprise-server@3.0/rest/overview/resources-in-the-rest-api#link-header) to get the URL for the next page of repositories.

    :param since: A repository ID. Only return repositories with an ID greater than this ID.
    :type since: int
    :param visibility: Specifies the types of repositories to return. Can be one of &#x60;all&#x60; or &#x60;public&#x60;. Default: &#x60;public&#x60;. Note: For GitHub Enterprise Server and GitHub AE, this endpoint will only list repositories available to all users on the enterprise.
    :type visibility: str

    """
    return web.Response(status=200)


async def repos_list_pull_requests_associated_with_commit(request: web.Request, owner, repo, commit_sha, per_page=None, page=None) -> web.Response:
    """List pull requests associated with a commit

    Lists the merged pull request that introduced the commit to the repository. If the commit is not present in the default branch, additionally returns open pull requests associated with the commit. The results may include open and closed pull requests. Additional preview headers may be required to see certain details for associated pull requests, such as whether a pull request is in a draft state. For more information about previews that might affect this endpoint, see the [List pull requests](https://docs.github.com/enterprise-server@3.0/rest/reference/pulls#list-pull-requests) endpoint.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param commit_sha: commit_sha parameter
    :type commit_sha: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def repos_list_release_assets(request: web.Request, owner, repo, release_id, per_page=None, page=None) -> web.Response:
    """List release assets

    

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param release_id: release_id parameter
    :type release_id: int
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def repos_list_releases(request: web.Request, owner, repo, per_page=None, page=None) -> web.Response:
    """List releases

    This returns a list of releases, which does not include regular Git tags that have not been associated with a release. To get a list of Git tags, use the [Repository Tags API](https://docs.github.com/enterprise-server@3.0/rest/reference/repos#list-repository-tags).  Information about published releases are available to everyone. Only users with push access will receive listings for draft releases.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def repos_list_tags(request: web.Request, owner, repo, per_page=None, page=None) -> web.Response:
    """List repository tags

    

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def repos_list_teams(request: web.Request, owner, repo, per_page=None, page=None) -> web.Response:
    """List repository teams

    

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def repos_list_webhooks(request: web.Request, owner, repo, per_page=None, page=None) -> web.Response:
    """List repository webhooks

    

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def repos_merge(request: web.Request, owner, repo, body) -> web.Response:
    """Merge a branch

    

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param body: 
    :type body: dict | bytes

    """
    body = ReposMergeRequest.from_dict(body)
    return web.Response(status=200)


async def repos_ping_webhook(request: web.Request, owner, repo, hook_id) -> web.Response:
    """Ping a repository webhook

    This will trigger a [ping event](https://docs.github.com/enterprise-server@3.0/webhooks/#ping-event) to be sent to the hook.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param hook_id: 
    :type hook_id: int

    """
    return web.Response(status=200)


async def repos_remove_app_access_restrictions(request: web.Request, owner, repo, branch, body=None) -> web.Response:
    """Remove app access restrictions

    Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub&#39;s products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  Removes the ability of an app to push to this branch. Only installed GitHub Apps with &#x60;write&#x60; access to the &#x60;contents&#x60; permission can be added as authorized actors on a protected branch.  | Type    | Description                                                                                                                                                | | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | | &#x60;array&#x60; | The GitHub Apps that have push access to this branch. Use the app&#39;s &#x60;slug&#x60;. **Note**: The list of users, apps, and teams in total is limited to 100 items. |

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param branch: The name of the branch.
    :type branch: str
    :param body: 
    :type body: dict | bytes

    """
    body = ReposSetAppAccessRestrictionsRequest.from_dict(body)
    return web.Response(status=200)


async def repos_remove_collaborator(request: web.Request, owner, repo, username) -> web.Response:
    """Remove a repository collaborator

    

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param username: 
    :type username: str

    """
    return web.Response(status=200)


async def repos_remove_status_check_contexts(request: web.Request, owner, repo, branch, body=None) -> web.Response:
    """Remove status check contexts

    Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub&#39;s products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param branch: The name of the branch.
    :type branch: str
    :param body: 
    :type body: dict | bytes

    """
    body = ReposSetStatusCheckContextsRequest.from_dict(body)
    return web.Response(status=200)


async def repos_remove_status_check_protection(request: web.Request, owner, repo, branch) -> web.Response:
    """Remove status check protection

    Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub&#39;s products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param branch: The name of the branch.
    :type branch: str

    """
    return web.Response(status=200)


async def repos_remove_team_access_restrictions(request: web.Request, owner, repo, branch, body=None) -> web.Response:
    """Remove team access restrictions

    Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub&#39;s products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  Removes the ability of a team to push to this branch. You can also remove push access for child teams.  | Type    | Description                                                                                                                                         | | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | | &#x60;array&#x60; | Teams that should no longer have push access. Use the team&#39;s &#x60;slug&#x60;. **Note**: The list of users, apps, and teams in total is limited to 100 items. |

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param branch: The name of the branch.
    :type branch: str
    :param body: 
    :type body: dict | bytes

    """
    body = ReposSetTeamAccessRestrictionsRequest.from_dict(body)
    return web.Response(status=200)


async def repos_remove_user_access_restrictions(request: web.Request, owner, repo, branch, body=None) -> web.Response:
    """Remove user access restrictions

    Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub&#39;s products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  Removes the ability of a user to push to this branch.  | Type    | Description                                                                                                                                   | | ------- | --------------------------------------------------------------------------------------------------------------------------------------------- | | &#x60;array&#x60; | Usernames of the people who should no longer have push access. **Note**: The list of users, apps, and teams in total is limited to 100 items. |

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param branch: The name of the branch.
    :type branch: str
    :param body: 
    :type body: dict | bytes

    """
    body = ReposSetUserAccessRestrictionsRequest.from_dict(body)
    return web.Response(status=200)


async def repos_replace_all_topics(request: web.Request, owner, repo, body) -> web.Response:
    """Replace all repository topics

    

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param body: 
    :type body: dict | bytes

    """
    body = ReposReplaceAllTopicsRequest.from_dict(body)
    return web.Response(status=200)


async def repos_request_pages_build(request: web.Request, owner, repo) -> web.Response:
    """Request a GitHub Enterprise Server Pages build

    You can request that your site be built from the latest revision on the default branch. This has the same effect as pushing a commit to your default branch, but does not require an additional commit. Manually triggering page builds can be helpful when diagnosing build warnings and failures.  Build requests are limited to one concurrent build per repository and one concurrent build per requester. If you request a build while another is still in progress, the second request will be queued until the first completes.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str

    """
    return web.Response(status=200)


async def repos_set_admin_branch_protection(request: web.Request, owner, repo, branch) -> web.Response:
    """Set admin branch protection

    Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub&#39;s products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  Adding admin enforcement requires admin or owner permissions to the repository and branch protection to be enabled.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param branch: The name of the branch.
    :type branch: str

    """
    return web.Response(status=200)


async def repos_set_app_access_restrictions(request: web.Request, owner, repo, branch, body=None) -> web.Response:
    """Set app access restrictions

    Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub&#39;s products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  Replaces the list of apps that have push access to this branch. This removes all apps that previously had push access and grants push access to the new list of apps. Only installed GitHub Apps with &#x60;write&#x60; access to the &#x60;contents&#x60; permission can be added as authorized actors on a protected branch.  | Type    | Description                                                                                                                                                | | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | | &#x60;array&#x60; | The GitHub Apps that have push access to this branch. Use the app&#39;s &#x60;slug&#x60;. **Note**: The list of users, apps, and teams in total is limited to 100 items. |

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param branch: The name of the branch.
    :type branch: str
    :param body: 
    :type body: dict | bytes

    """
    body = ReposSetAppAccessRestrictionsRequest.from_dict(body)
    return web.Response(status=200)


async def repos_set_status_check_contexts(request: web.Request, owner, repo, branch, body=None) -> web.Response:
    """Set status check contexts

    Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub&#39;s products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param branch: The name of the branch.
    :type branch: str
    :param body: 
    :type body: dict | bytes

    """
    body = ReposSetStatusCheckContextsRequest.from_dict(body)
    return web.Response(status=200)


async def repos_set_team_access_restrictions(request: web.Request, owner, repo, branch, body=None) -> web.Response:
    """Set team access restrictions

    Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub&#39;s products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  Replaces the list of teams that have push access to this branch. This removes all teams that previously had push access and grants push access to the new list of teams. Team restrictions include child teams.  | Type    | Description                                                                                                                                | | ------- | ------------------------------------------------------------------------------------------------------------------------------------------ | | &#x60;array&#x60; | The teams that can have push access. Use the team&#39;s &#x60;slug&#x60;. **Note**: The list of users, apps, and teams in total is limited to 100 items. |

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param branch: The name of the branch.
    :type branch: str
    :param body: 
    :type body: dict | bytes

    """
    body = ReposSetTeamAccessRestrictionsRequest.from_dict(body)
    return web.Response(status=200)


async def repos_set_user_access_restrictions(request: web.Request, owner, repo, branch, body=None) -> web.Response:
    """Set user access restrictions

    Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub&#39;s products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  Replaces the list of people that have push access to this branch. This removes all people that previously had push access and grants push access to the new list of people.  | Type    | Description                                                                                                                   | | ------- | ----------------------------------------------------------------------------------------------------------------------------- | | &#x60;array&#x60; | Usernames for people who can have push access. **Note**: The list of users, apps, and teams in total is limited to 100 items. |

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param branch: The name of the branch.
    :type branch: str
    :param body: 
    :type body: dict | bytes

    """
    body = ReposSetUserAccessRestrictionsRequest.from_dict(body)
    return web.Response(status=200)


async def repos_test_push_webhook(request: web.Request, owner, repo, hook_id) -> web.Response:
    """Test the push repository webhook

    This will trigger the hook with the latest push to the current repository if the hook is subscribed to &#x60;push&#x60; events. If the hook is not subscribed to &#x60;push&#x60; events, the server will respond with 204 but no test POST will be generated.  **Note**: Previously &#x60;/repos/:owner/:repo/hooks/:hook_id/test&#x60;

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param hook_id: 
    :type hook_id: int

    """
    return web.Response(status=200)


async def repos_transfer(request: web.Request, owner, repo, body) -> web.Response:
    """Transfer a repository

    A transfer request will need to be accepted by the new owner when transferring a personal repository to another user. The response will contain the original &#x60;owner&#x60;, and the transfer will continue asynchronously. For more details on the requirements to transfer personal and organization-owned repositories, see [about repository transfers](https://docs.github.com/articles/about-repository-transfers/).

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param body: 
    :type body: dict | bytes

    """
    body = ReposTransferRequest.from_dict(body)
    return web.Response(status=200)


async def repos_update(request: web.Request, owner, repo, body=None) -> web.Response:
    """Update a repository

    **Note**: To edit a repository&#39;s topics, use the [Replace all repository topics](https://docs.github.com/enterprise-server@3.0/rest/reference/repos#replace-all-repository-topics) endpoint.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param body: 
    :type body: dict | bytes

    """
    body = ReposUpdateRequest.from_dict(body)
    return web.Response(status=200)


async def repos_update_branch_protection(request: web.Request, owner, repo, branch, body) -> web.Response:
    """Update branch protection

    Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub&#39;s products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  Protecting a branch requires admin or owner permissions to the repository.  **Note**: Passing new arrays of &#x60;users&#x60; and &#x60;teams&#x60; replaces their previous values.  **Note**: The list of users, apps, and teams in total is limited to 100 items.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param branch: The name of the branch.
    :type branch: str
    :param body: 
    :type body: dict | bytes

    """
    body = ReposUpdateBranchProtectionRequest.from_dict(body)
    return web.Response(status=200)


async def repos_update_commit_comment(request: web.Request, owner, repo, comment_id, body) -> web.Response:
    """Update a commit comment

    

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param comment_id: comment_id parameter
    :type comment_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = ReposUpdateCommitCommentRequest.from_dict(body)
    return web.Response(status=200)


async def repos_update_information_about_pages_site(request: web.Request, owner, repo, body) -> web.Response:
    """Update information about a GitHub Enterprise Server Pages site

    Updates information for a GitHub Enterprise Server Pages site. For more information, see \&quot;[About GitHub Pages](/github/working-with-github-pages/about-github-pages).

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param body: 
    :type body: dict | bytes

    """
    body = ReposUpdateInformationAboutPagesSiteRequest.from_dict(body)
    return web.Response(status=200)


async def repos_update_invitation(request: web.Request, owner, repo, invitation_id, body=None) -> web.Response:
    """Update a repository invitation

    

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param invitation_id: invitation_id parameter
    :type invitation_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = ReposUpdateInvitationRequest.from_dict(body)
    return web.Response(status=200)


async def repos_update_pull_request_review_protection(request: web.Request, owner, repo, branch, body=None) -> web.Response:
    """Update pull request review protection

    Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub&#39;s products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  Updating pull request review enforcement requires admin or owner permissions to the repository and branch protection to be enabled.  **Note**: Passing new arrays of &#x60;users&#x60; and &#x60;teams&#x60; replaces their previous values.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param branch: The name of the branch.
    :type branch: str
    :param body: 
    :type body: dict | bytes

    """
    body = ReposUpdatePullRequestReviewProtectionRequest.from_dict(body)
    return web.Response(status=200)


async def repos_update_release(request: web.Request, owner, repo, release_id, body=None) -> web.Response:
    """Update a release

    Users with push access to the repository can edit a release.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param release_id: release_id parameter
    :type release_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = ReposUpdateReleaseRequest.from_dict(body)
    return web.Response(status=200)


async def repos_update_release_asset(request: web.Request, owner, repo, asset_id, body=None) -> web.Response:
    """Update a release asset

    Users with push access to the repository can edit a release asset.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param asset_id: asset_id parameter
    :type asset_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = ReposUpdateReleaseAssetRequest.from_dict(body)
    return web.Response(status=200)


async def repos_update_status_check_protection(request: web.Request, owner, repo, branch, body=None) -> web.Response:
    """Update status check protection

    Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub&#39;s products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  Updating required status checks requires admin or owner permissions to the repository and branch protection to be enabled.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param branch: The name of the branch.
    :type branch: str
    :param body: 
    :type body: dict | bytes

    """
    body = ReposUpdateStatusCheckProtectionRequest.from_dict(body)
    return web.Response(status=200)


async def repos_update_webhook(request: web.Request, owner, repo, hook_id, body) -> web.Response:
    """Update a repository webhook

    Updates a webhook configured in a repository. If you previously had a &#x60;secret&#x60; set, you must provide the same &#x60;secret&#x60; or set a new &#x60;secret&#x60; or the secret will be removed. If you are only updating individual webhook &#x60;config&#x60; properties, use \&quot;[Update a webhook configuration for a repository](/rest/reference/repos#update-a-webhook-configuration-for-a-repository).\&quot;

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param hook_id: 
    :type hook_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = ReposUpdateWebhookRequest.from_dict(body)
    return web.Response(status=200)


async def repos_update_webhook_config_for_repo(request: web.Request, owner, repo, hook_id, body=None) -> web.Response:
    """Update a webhook configuration for a repository

    Updates the webhook configuration for a repository. To update more information about the webhook, including the &#x60;active&#x60; state and &#x60;events&#x60;, use \&quot;[Update a repository webhook](/rest/reference/orgs#update-a-repository-webhook).\&quot;  Access tokens must have the &#x60;write:repo_hook&#x60; or &#x60;repo&#x60; scope, and GitHub Apps must have the &#x60;repository_hooks:write&#x60; permission.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param hook_id: 
    :type hook_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = OrgsUpdateWebhookConfigForOrgRequest.from_dict(body)
    return web.Response(status=200)


async def repos_upload_release_asset(request: web.Request, owner, repo, release_id, name, label=None, body=None) -> web.Response:
    """Upload a release asset

    This endpoint makes use of [a Hypermedia relation](https://docs.github.com/enterprise-server@3.0/rest/overview/resources-in-the-rest-api#hypermedia) to determine which URL to access. The endpoint you call to upload release assets is specific to your release. Use the &#x60;upload_url&#x60; returned in the response of the [Create a release endpoint](https://docs.github.com/enterprise-server@3.0/rest/reference/repos#create-a-release) to upload a release asset.  You need to use an HTTP client which supports [SNI](http://en.wikipedia.org/wiki/Server_Name_Indication) to make calls to this endpoint.  Most libraries will set the required &#x60;Content-Length&#x60; header automatically. Use the required &#x60;Content-Type&#x60; header to provide the media type of the asset. For a list of media types, see [Media Types](https://www.iana.org/assignments/media-types/media-types.xhtml). For example:   &#x60;application/zip&#x60;  GitHub Enterprise Server expects the asset data in its raw binary form, rather than JSON. You will send the raw binary content of the asset as the request body. Everything else about the endpoint is the same as the rest of the API. For example, you&#39;ll still need to pass your authentication to be able to upload an asset.  When an upstream failure occurs, you will receive a &#x60;502 Bad Gateway&#x60; status. This may leave an empty asset with a state of &#x60;starter&#x60;. It can be safely deleted.  **Notes:** *   GitHub Enterprise Server renames asset filenames that have special characters, non-alphanumeric characters, and leading or trailing periods. The \&quot;[List assets for a release](https://docs.github.com/enterprise-server@3.0/rest/reference/repos#list-assets-for-a-release)\&quot; endpoint lists the renamed filenames. For more information and help, contact [GitHub Enterprise Server Support](https://support.github.com/contact?tags&#x3D;dotcom-rest-api). *   If you upload an asset with the same filename as another uploaded asset, you&#39;ll receive an error and must delete the old file before you can re-upload the new asset.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param release_id: release_id parameter
    :type release_id: int
    :param name: 
    :type name: str
    :param label: 
    :type label: str
    :param body: 
    :type body: str

    """
    return web.Response(status=200)
