from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_error import APIError
from openapi_server.models.activity import Activity
from openapi_server.models.add_collaborator_option import AddCollaboratorOption
from openapi_server.models.annotated_tag import AnnotatedTag
from openapi_server.models.attachment import Attachment
from openapi_server.models.branch import Branch
from openapi_server.models.branch_protection import BranchProtection
from openapi_server.models.changed_file import ChangedFile
from openapi_server.models.combined_status import CombinedStatus
from openapi_server.models.commit import Commit
from openapi_server.models.commit_status import CommitStatus
from openapi_server.models.contents_response import ContentsResponse
from openapi_server.models.create_branch_protection_option import CreateBranchProtectionOption
from openapi_server.models.create_branch_repo_option import CreateBranchRepoOption
from openapi_server.models.create_file_options import CreateFileOptions
from openapi_server.models.create_fork_option import CreateForkOption
from openapi_server.models.create_hook_option import CreateHookOption
from openapi_server.models.create_key_option import CreateKeyOption
from openapi_server.models.create_pull_request_option import CreatePullRequestOption
from openapi_server.models.create_pull_review_options import CreatePullReviewOptions
from openapi_server.models.create_push_mirror_option import CreatePushMirrorOption
from openapi_server.models.create_release_option import CreateReleaseOption
from openapi_server.models.create_repo_option import CreateRepoOption
from openapi_server.models.create_status_option import CreateStatusOption
from openapi_server.models.create_tag_option import CreateTagOption
from openapi_server.models.create_wiki_page_options import CreateWikiPageOptions
from openapi_server.models.delete_file_options import DeleteFileOptions
from openapi_server.models.deploy_key import DeployKey
from openapi_server.models.dismiss_pull_review_options import DismissPullReviewOptions
from openapi_server.models.edit_attachment_options import EditAttachmentOptions
from openapi_server.models.edit_branch_protection_option import EditBranchProtectionOption
from openapi_server.models.edit_git_hook_option import EditGitHookOption
from openapi_server.models.edit_hook_option import EditHookOption
from openapi_server.models.edit_pull_request_option import EditPullRequestOption
from openapi_server.models.edit_release_option import EditReleaseOption
from openapi_server.models.edit_repo_option import EditRepoOption
from openapi_server.models.file_delete_response import FileDeleteResponse
from openapi_server.models.file_response import FileResponse
from openapi_server.models.generate_repo_option import GenerateRepoOption
from openapi_server.models.git_blob_response import GitBlobResponse
from openapi_server.models.git_hook import GitHook
from openapi_server.models.git_tree_response import GitTreeResponse
from openapi_server.models.hook import Hook
from openapi_server.models.issue_config import IssueConfig
from openapi_server.models.issue_config_validation import IssueConfigValidation
from openapi_server.models.issue_template import IssueTemplate
from openapi_server.models.merge_pull_request_option import MergePullRequestOption
from openapi_server.models.migrate_repo_options import MigrateRepoOptions
from openapi_server.models.note import Note
from openapi_server.models.pull_request import PullRequest
from openapi_server.models.pull_review import PullReview
from openapi_server.models.pull_review_comment import PullReviewComment
from openapi_server.models.pull_review_request_options import PullReviewRequestOptions
from openapi_server.models.push_mirror import PushMirror
from openapi_server.models.reference import Reference
from openapi_server.models.release import Release
from openapi_server.models.repo_collaborator_permission import RepoCollaboratorPermission
from openapi_server.models.repo_topic_options import RepoTopicOptions
from openapi_server.models.repository import Repository
from openapi_server.models.search_results import SearchResults
from openapi_server.models.submit_pull_review_options import SubmitPullReviewOptions
from openapi_server.models.tag import Tag
from openapi_server.models.team import Team
from openapi_server.models.topic_name import TopicName
from openapi_server.models.topic_response import TopicResponse
from openapi_server.models.tracked_time import TrackedTime
from openapi_server.models.transfer_repo_option import TransferRepoOption
from openapi_server.models.update_file_options import UpdateFileOptions
from openapi_server.models.user import User
from openapi_server.models.watch_info import WatchInfo
from openapi_server.models.wiki_commit_list import WikiCommitList
from openapi_server.models.wiki_page import WikiPage
from openapi_server.models.wiki_page_meta_data import WikiPageMetaData
from openapi_server import util


async def accept_repo_transfer(request: web.Request, owner, repo) -> web.Response:
    """Accept a repo transfer

    

    :param owner: owner of the repo to transfer
    :type owner: str
    :param repo: name of the repo to transfer
    :type repo: str

    """
    return web.Response(status=200)


async def create_current_user_repo(request: web.Request, body=None) -> web.Response:
    """Create a repository

    

    :param body: 
    :type body: dict | bytes

    """
    body = CreateRepoOption.from_dict(body)
    return web.Response(status=200)


async def create_fork(request: web.Request, owner, repo, body=None) -> web.Response:
    """Fork a repository

    

    :param owner: owner of the repo to fork
    :type owner: str
    :param repo: name of the repo to fork
    :type repo: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateForkOption.from_dict(body)
    return web.Response(status=200)


async def generate_repo(request: web.Request, template_owner, template_repo, body=None) -> web.Response:
    """Create a repository using a template

    

    :param template_owner: name of the template repository owner
    :type template_owner: str
    :param template_repo: name of the template repository
    :type template_repo: str
    :param body: 
    :type body: dict | bytes

    """
    body = GenerateRepoOption.from_dict(body)
    return web.Response(status=200)


async def get_annotated_tag(request: web.Request, owner, repo, sha) -> web.Response:
    """Gets the tag object of an annotated tag (not lightweight tags)

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param sha: sha of the tag. The Git tags API only supports annotated tag objects, not lightweight tags.
    :type sha: str

    """
    return web.Response(status=200)


async def get_blob(request: web.Request, owner, repo, sha) -> web.Response:
    """Gets the blob of a repository.

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param sha: sha of the commit
    :type sha: str

    """
    return web.Response(status=200)


async def get_tree(request: web.Request, owner, repo, sha, recursive=None, page=None, per_page=None) -> web.Response:
    """Gets the tree of a repository.

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param sha: sha of the commit
    :type sha: str
    :param recursive: show all directories and files
    :type recursive: bool
    :param page: page number; the &#39;truncated&#39; field in the response will be true if there are still more items after this page, false if the last page
    :type page: int
    :param per_page: number of items per page
    :type per_page: int

    """
    return web.Response(status=200)


async def list_forks(request: web.Request, owner, repo, page=None, limit=None) -> web.Response:
    """List a repository&#39;s forks

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param page: page number of results to return (1-based)
    :type page: int
    :param limit: page size of results
    :type limit: int

    """
    return web.Response(status=200)


async def reject_repo_transfer(request: web.Request, owner, repo) -> web.Response:
    """Reject a repo transfer

    

    :param owner: owner of the repo to transfer
    :type owner: str
    :param repo: name of the repo to transfer
    :type repo: str

    """
    return web.Response(status=200)


async def repo_add_collaborator(request: web.Request, owner, repo, collaborator, body=None) -> web.Response:
    """Add a collaborator to a repository

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param collaborator: username of the collaborator to add
    :type collaborator: str
    :param body: 
    :type body: dict | bytes

    """
    body = AddCollaboratorOption.from_dict(body)
    return web.Response(status=200)


async def repo_add_push_mirror(request: web.Request, owner, repo, body=None) -> web.Response:
    """add a push mirror to the repository

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreatePushMirrorOption.from_dict(body)
    return web.Response(status=200)


async def repo_add_team(request: web.Request, owner, repo, team) -> web.Response:
    """Add a team to a repository

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param team: team name
    :type team: str

    """
    return web.Response(status=200)


async def repo_add_topic(request: web.Request, owner, repo, topic) -> web.Response:
    """Add a topic to a repository

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param topic: name of the topic to add
    :type topic: str

    """
    return web.Response(status=200)


async def repo_apply_diff_patch(request: web.Request, owner, repo, body) -> web.Response:
    """Apply diff patch to repository

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateFileOptions.from_dict(body)
    return web.Response(status=200)


async def repo_cancel_scheduled_auto_merge(request: web.Request, owner, repo, index) -> web.Response:
    """Cancel the scheduled auto merge for the given pull request

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param index: index of the pull request to merge
    :type index: int

    """
    return web.Response(status=200)


async def repo_check_collaborator(request: web.Request, owner, repo, collaborator) -> web.Response:
    """Check if a user is a collaborator of a repository

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param collaborator: username of the collaborator
    :type collaborator: str

    """
    return web.Response(status=200)


async def repo_check_team(request: web.Request, owner, repo, team) -> web.Response:
    """Check if a team is assigned to a repository

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param team: team name
    :type team: str

    """
    return web.Response(status=200)


async def repo_create_branch(request: web.Request, owner, repo, body=None) -> web.Response:
    """Create a branch

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateBranchRepoOption.from_dict(body)
    return web.Response(status=200)


async def repo_create_branch_protection(request: web.Request, owner, repo, body=None) -> web.Response:
    """Create a branch protections for a repository

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateBranchProtectionOption.from_dict(body)
    return web.Response(status=200)


async def repo_create_file(request: web.Request, owner, repo, filepath, body) -> web.Response:
    """Create a file in a repository

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param filepath: path of the file to create
    :type filepath: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateFileOptions.from_dict(body)
    return web.Response(status=200)


async def repo_create_hook(request: web.Request, owner, repo, body=None) -> web.Response:
    """Create a hook

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateHookOption.from_dict(body)
    return web.Response(status=200)


async def repo_create_key(request: web.Request, owner, repo, body=None) -> web.Response:
    """Add a key to a repository

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateKeyOption.from_dict(body)
    return web.Response(status=200)


async def repo_create_pull_request(request: web.Request, owner, repo, body=None) -> web.Response:
    """Create a pull request

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreatePullRequestOption.from_dict(body)
    return web.Response(status=200)


async def repo_create_pull_review(request: web.Request, owner, repo, index, body) -> web.Response:
    """Create a review to an pull request

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param index: index of the pull request
    :type index: int
    :param body: 
    :type body: dict | bytes

    """
    body = CreatePullReviewOptions.from_dict(body)
    return web.Response(status=200)


async def repo_create_pull_review_requests(request: web.Request, owner, repo, index, body) -> web.Response:
    """create review requests for a pull request

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param index: index of the pull request
    :type index: int
    :param body: 
    :type body: dict | bytes

    """
    body = PullReviewRequestOptions.from_dict(body)
    return web.Response(status=200)


async def repo_create_release(request: web.Request, owner, repo, body=None) -> web.Response:
    """Create a release

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateReleaseOption.from_dict(body)
    return web.Response(status=200)


async def repo_create_release_attachment(request: web.Request, owner, repo, id, attachment, name=None) -> web.Response:
    """Create a release attachment

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param id: id of the release
    :type id: int
    :param attachment: attachment to upload
    :type attachment: str
    :param name: name of the attachment
    :type name: str

    """
    return web.Response(status=200)


async def repo_create_status(request: web.Request, owner, repo, sha, body=None) -> web.Response:
    """Create a commit status

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param sha: sha of the commit
    :type sha: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateStatusOption.from_dict(body)
    return web.Response(status=200)


async def repo_create_tag(request: web.Request, owner, repo, body=None) -> web.Response:
    """Create a new git tag in a repository

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateTagOption.from_dict(body)
    return web.Response(status=200)


async def repo_create_wiki_page(request: web.Request, owner, repo, body=None) -> web.Response:
    """Create a wiki page

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateWikiPageOptions.from_dict(body)
    return web.Response(status=200)


async def repo_delete(request: web.Request, owner, repo) -> web.Response:
    """Delete a repository

    

    :param owner: owner of the repo to delete
    :type owner: str
    :param repo: name of the repo to delete
    :type repo: str

    """
    return web.Response(status=200)


async def repo_delete_branch(request: web.Request, owner, repo, branch) -> web.Response:
    """Delete a specific branch from a repository

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param branch: branch to delete
    :type branch: str

    """
    return web.Response(status=200)


async def repo_delete_branch_protection(request: web.Request, owner, repo, name) -> web.Response:
    """Delete a specific branch protection for the repository

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param name: name of protected branch
    :type name: str

    """
    return web.Response(status=200)


async def repo_delete_collaborator(request: web.Request, owner, repo, collaborator) -> web.Response:
    """Delete a collaborator from a repository

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param collaborator: username of the collaborator to delete
    :type collaborator: str

    """
    return web.Response(status=200)


async def repo_delete_file(request: web.Request, owner, repo, filepath, body) -> web.Response:
    """Delete a file in a repository

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param filepath: path of the file to delete
    :type filepath: str
    :param body: 
    :type body: dict | bytes

    """
    body = DeleteFileOptions.from_dict(body)
    return web.Response(status=200)


async def repo_delete_git_hook(request: web.Request, owner, repo, id) -> web.Response:
    """Delete a Git hook in a repository

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param id: id of the hook to get
    :type id: str

    """
    return web.Response(status=200)


async def repo_delete_hook(request: web.Request, owner, repo, id) -> web.Response:
    """Delete a hook in a repository

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param id: id of the hook to delete
    :type id: int

    """
    return web.Response(status=200)


async def repo_delete_key(request: web.Request, owner, repo, id) -> web.Response:
    """Delete a key from a repository

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param id: id of the key to delete
    :type id: int

    """
    return web.Response(status=200)


async def repo_delete_pull_review(request: web.Request, owner, repo, index, id) -> web.Response:
    """Delete a specific review from a pull request

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param index: index of the pull request
    :type index: int
    :param id: id of the review
    :type id: int

    """
    return web.Response(status=200)


async def repo_delete_pull_review_requests(request: web.Request, owner, repo, index, body) -> web.Response:
    """cancel review requests for a pull request

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param index: index of the pull request
    :type index: int
    :param body: 
    :type body: dict | bytes

    """
    body = PullReviewRequestOptions.from_dict(body)
    return web.Response(status=200)


async def repo_delete_push_mirror(request: web.Request, owner, repo, name) -> web.Response:
    """deletes a push mirror from a repository by remoteName

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param name: remote name of the pushMirror
    :type name: str

    """
    return web.Response(status=200)


async def repo_delete_release(request: web.Request, owner, repo, id) -> web.Response:
    """Delete a release

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param id: id of the release to delete
    :type id: int

    """
    return web.Response(status=200)


async def repo_delete_release_attachment(request: web.Request, owner, repo, id, attachment_id) -> web.Response:
    """Delete a release attachment

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param id: id of the release
    :type id: int
    :param attachment_id: id of the attachment to delete
    :type attachment_id: int

    """
    return web.Response(status=200)


async def repo_delete_release_by_tag(request: web.Request, owner, repo, tag) -> web.Response:
    """Delete a release by tag name

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param tag: tag name of the release to delete
    :type tag: str

    """
    return web.Response(status=200)


async def repo_delete_tag(request: web.Request, owner, repo, tag) -> web.Response:
    """Delete a repository&#39;s tag by name

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param tag: name of tag to delete
    :type tag: str

    """
    return web.Response(status=200)


async def repo_delete_team(request: web.Request, owner, repo, team) -> web.Response:
    """Delete a team from a repository

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param team: team name
    :type team: str

    """
    return web.Response(status=200)


async def repo_delete_topic(request: web.Request, owner, repo, topic) -> web.Response:
    """Delete a topic from a repository

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param topic: name of the topic to delete
    :type topic: str

    """
    return web.Response(status=200)


async def repo_delete_wiki_page(request: web.Request, owner, repo, page_name) -> web.Response:
    """Delete a wiki page

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param page_name: name of the page
    :type page_name: str

    """
    return web.Response(status=200)


async def repo_dismiss_pull_review(request: web.Request, owner, repo, index, id, body) -> web.Response:
    """Dismiss a review for a pull request

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param index: index of the pull request
    :type index: int
    :param id: id of the review
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = DismissPullReviewOptions.from_dict(body)
    return web.Response(status=200)


async def repo_download_commit_diff_or_patch(request: web.Request, owner, repo, sha, diff_type) -> web.Response:
    """Get a commit&#39;s diff or patch

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param sha: SHA of the commit to get
    :type sha: str
    :param diff_type: whether the output is diff or patch
    :type diff_type: str

    """
    return web.Response(status=200)


async def repo_download_pull_diff_or_patch(request: web.Request, owner, repo, index, diff_type, binary=None) -> web.Response:
    """Get a pull request diff or patch

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param index: index of the pull request to get
    :type index: int
    :param diff_type: whether the output is diff or patch
    :type diff_type: str
    :param binary: whether to include binary file changes. if true, the diff is applicable with &#x60;git apply&#x60;
    :type binary: bool

    """
    return web.Response(status=200)


async def repo_edit(request: web.Request, owner, repo, body=None) -> web.Response:
    """Edit a repository&#39;s properties. Only fields that are set will be changed.

    

    :param owner: owner of the repo to edit
    :type owner: str
    :param repo: name of the repo to edit
    :type repo: str
    :param body: Properties of a repo that you can edit
    :type body: dict | bytes

    """
    body = EditRepoOption.from_dict(body)
    return web.Response(status=200)


async def repo_edit_branch_protection(request: web.Request, owner, repo, name, body=None) -> web.Response:
    """Edit a branch protections for a repository. Only fields that are set will be changed

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param name: name of protected branch
    :type name: str
    :param body: 
    :type body: dict | bytes

    """
    body = EditBranchProtectionOption.from_dict(body)
    return web.Response(status=200)


async def repo_edit_git_hook(request: web.Request, owner, repo, id, body=None) -> web.Response:
    """Edit a Git hook in a repository

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param id: id of the hook to get
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = EditGitHookOption.from_dict(body)
    return web.Response(status=200)


async def repo_edit_hook(request: web.Request, owner, repo, id, body=None) -> web.Response:
    """Edit a hook in a repository

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param id: index of the hook
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = EditHookOption.from_dict(body)
    return web.Response(status=200)


async def repo_edit_pull_request(request: web.Request, owner, repo, index, body=None) -> web.Response:
    """Update a pull request. If using deadline only the date will be taken into account, and time of day ignored.

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param index: index of the pull request to edit
    :type index: int
    :param body: 
    :type body: dict | bytes

    """
    body = EditPullRequestOption.from_dict(body)
    return web.Response(status=200)


async def repo_edit_release(request: web.Request, owner, repo, id, body=None) -> web.Response:
    """Update a release

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param id: id of the release to edit
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = EditReleaseOption.from_dict(body)
    return web.Response(status=200)


async def repo_edit_release_attachment(request: web.Request, owner, repo, id, attachment_id, body=None) -> web.Response:
    """Edit a release attachment

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param id: id of the release
    :type id: int
    :param attachment_id: id of the attachment to edit
    :type attachment_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = EditAttachmentOptions.from_dict(body)
    return web.Response(status=200)


async def repo_edit_wiki_page(request: web.Request, owner, repo, page_name, body=None) -> web.Response:
    """Edit a wiki page

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param page_name: name of the page
    :type page_name: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateWikiPageOptions.from_dict(body)
    return web.Response(status=200)


async def repo_get(request: web.Request, owner, repo) -> web.Response:
    """Get a repository

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str

    """
    return web.Response(status=200)


async def repo_get_all_commits(request: web.Request, owner, repo, sha=None, path=None, stat=None, page=None, limit=None) -> web.Response:
    """Get a list of all commits from a repository

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param sha: SHA or branch to start listing commits from (usually &#39;master&#39;)
    :type sha: str
    :param path: filepath of a file/dir
    :type path: str
    :param stat: include diff stats for every commit (disable for speedup, default &#39;true&#39;)
    :type stat: bool
    :param page: page number of results to return (1-based)
    :type page: int
    :param limit: page size of results (ignored if used with &#39;path&#39;)
    :type limit: int

    """
    return web.Response(status=200)


async def repo_get_archive(request: web.Request, owner, repo, archive) -> web.Response:
    """Get an archive of a repository

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param archive: the git reference for download with attached archive format (e.g. master.zip)
    :type archive: str

    """
    return web.Response(status=200)


async def repo_get_assignees(request: web.Request, owner, repo) -> web.Response:
    """Return all users that have write access and can be assigned to issues

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str

    """
    return web.Response(status=200)


async def repo_get_branch(request: web.Request, owner, repo, branch) -> web.Response:
    """Retrieve a specific branch from a repository, including its effective branch protection

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param branch: branch to get
    :type branch: str

    """
    return web.Response(status=200)


async def repo_get_branch_protection(request: web.Request, owner, repo, name) -> web.Response:
    """Get a specific branch protection for the repository

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param name: name of protected branch
    :type name: str

    """
    return web.Response(status=200)


async def repo_get_by_id(request: web.Request, id) -> web.Response:
    """Get a repository by id

    

    :param id: id of the repo to get
    :type id: int

    """
    return web.Response(status=200)


async def repo_get_combined_status_by_ref(request: web.Request, owner, repo, ref, page=None, limit=None) -> web.Response:
    """Get a commit&#39;s combined status, by branch/tag/commit reference

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param ref: name of branch/tag/commit
    :type ref: str
    :param page: page number of results to return (1-based)
    :type page: int
    :param limit: page size of results
    :type limit: int

    """
    return web.Response(status=200)


async def repo_get_contents(request: web.Request, owner, repo, filepath, ref=None) -> web.Response:
    """Gets the metadata and contents (if a file) of an entry in a repository, or a list of entries if a dir

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param filepath: path of the dir, file, symlink or submodule in the repo
    :type filepath: str
    :param ref: The name of the commit/branch/tag. Default the repository’s default branch (usually master)
    :type ref: str

    """
    return web.Response(status=200)


async def repo_get_contents_list(request: web.Request, owner, repo, ref=None) -> web.Response:
    """Gets the metadata of all the entries of the root dir

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param ref: The name of the commit/branch/tag. Default the repository’s default branch (usually master)
    :type ref: str

    """
    return web.Response(status=200)


async def repo_get_editor_config(request: web.Request, owner, repo, filepath, ref=None) -> web.Response:
    """Get the EditorConfig definitions of a file in a repository

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param filepath: filepath of file to get
    :type filepath: str
    :param ref: The name of the commit/branch/tag. Default the repository’s default branch (usually master)
    :type ref: str

    """
    return web.Response(status=200)


async def repo_get_git_hook(request: web.Request, owner, repo, id) -> web.Response:
    """Get a Git hook

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param id: id of the hook to get
    :type id: str

    """
    return web.Response(status=200)


async def repo_get_hook(request: web.Request, owner, repo, id) -> web.Response:
    """Get a hook

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param id: id of the hook to get
    :type id: int

    """
    return web.Response(status=200)


async def repo_get_issue_config(request: web.Request, owner, repo) -> web.Response:
    """Returns the issue config for a repo

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str

    """
    return web.Response(status=200)


async def repo_get_issue_templates(request: web.Request, owner, repo) -> web.Response:
    """Get available issue templates for a repository

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str

    """
    return web.Response(status=200)


async def repo_get_key(request: web.Request, owner, repo, id) -> web.Response:
    """Get a repository&#39;s key by id

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param id: id of the key to get
    :type id: int

    """
    return web.Response(status=200)


async def repo_get_languages(request: web.Request, owner, repo) -> web.Response:
    """Get languages and number of bytes of code written

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str

    """
    return web.Response(status=200)


async def repo_get_latest_release(request: web.Request, owner, repo) -> web.Response:
    """Gets the most recent non-prerelease, non-draft release of a repository, sorted by created_at

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str

    """
    return web.Response(status=200)


async def repo_get_note(request: web.Request, owner, repo, sha) -> web.Response:
    """Get a note corresponding to a single commit from a repository

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param sha: a git ref or commit sha
    :type sha: str

    """
    return web.Response(status=200)


async def repo_get_pull_request(request: web.Request, owner, repo, index) -> web.Response:
    """Get a pull request

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param index: index of the pull request to get
    :type index: int

    """
    return web.Response(status=200)


async def repo_get_pull_request_commits(request: web.Request, owner, repo, index, page=None, limit=None) -> web.Response:
    """Get commits for a pull request

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param index: index of the pull request to get
    :type index: int
    :param page: page number of results to return (1-based)
    :type page: int
    :param limit: page size of results
    :type limit: int

    """
    return web.Response(status=200)


async def repo_get_pull_request_files(request: web.Request, owner, repo, index, skip_to=None, whitespace=None, page=None, limit=None) -> web.Response:
    """Get changed files for a pull request

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param index: index of the pull request to get
    :type index: int
    :param skip_to: skip to given file
    :type skip_to: str
    :param whitespace: whitespace behavior
    :type whitespace: str
    :param page: page number of results to return (1-based)
    :type page: int
    :param limit: page size of results
    :type limit: int

    """
    return web.Response(status=200)


async def repo_get_pull_review(request: web.Request, owner, repo, index, id) -> web.Response:
    """Get a specific review for a pull request

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param index: index of the pull request
    :type index: int
    :param id: id of the review
    :type id: int

    """
    return web.Response(status=200)


async def repo_get_pull_review_comments(request: web.Request, owner, repo, index, id) -> web.Response:
    """Get a specific review for a pull request

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param index: index of the pull request
    :type index: int
    :param id: id of the review
    :type id: int

    """
    return web.Response(status=200)


async def repo_get_push_mirror_by_remote_name(request: web.Request, owner, repo, name) -> web.Response:
    """Get push mirror of the repository by remoteName

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param name: remote name of push mirror
    :type name: str

    """
    return web.Response(status=200)


async def repo_get_raw_file(request: web.Request, owner, repo, filepath, ref=None) -> web.Response:
    """Get a file from a repository

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param filepath: filepath of the file to get
    :type filepath: str
    :param ref: The name of the commit/branch/tag. Default the repository’s default branch (usually master)
    :type ref: str

    """
    return web.Response(status=200)


async def repo_get_raw_file_or_lfs(request: web.Request, owner, repo, filepath, ref=None) -> web.Response:
    """Get a file or it&#39;s LFS object from a repository

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param filepath: filepath of the file to get
    :type filepath: str
    :param ref: The name of the commit/branch/tag. Default the repository’s default branch (usually master)
    :type ref: str

    """
    return web.Response(status=200)


async def repo_get_release(request: web.Request, owner, repo, id) -> web.Response:
    """Get a release

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param id: id of the release to get
    :type id: int

    """
    return web.Response(status=200)


async def repo_get_release_attachment(request: web.Request, owner, repo, id, attachment_id) -> web.Response:
    """Get a release attachment

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param id: id of the release
    :type id: int
    :param attachment_id: id of the attachment to get
    :type attachment_id: int

    """
    return web.Response(status=200)


async def repo_get_release_by_tag(request: web.Request, owner, repo, tag) -> web.Response:
    """Get a release by tag name

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param tag: tag name of the release to get
    :type tag: str

    """
    return web.Response(status=200)


async def repo_get_repo_permissions(request: web.Request, owner, repo, collaborator) -> web.Response:
    """Get repository permissions for a user

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param collaborator: username of the collaborator
    :type collaborator: str

    """
    return web.Response(status=200)


async def repo_get_reviewers(request: web.Request, owner, repo) -> web.Response:
    """Return all users that can be requested to review in this repo

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str

    """
    return web.Response(status=200)


async def repo_get_single_commit(request: web.Request, owner, repo, sha) -> web.Response:
    """Get a single commit from a repository

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param sha: a git ref or commit sha
    :type sha: str

    """
    return web.Response(status=200)


async def repo_get_tag(request: web.Request, owner, repo, tag) -> web.Response:
    """Get the tag of a repository by tag name

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param tag: name of tag
    :type tag: str

    """
    return web.Response(status=200)


async def repo_get_wiki_page(request: web.Request, owner, repo, page_name) -> web.Response:
    """Get a wiki page

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param page_name: name of the page
    :type page_name: str

    """
    return web.Response(status=200)


async def repo_get_wiki_page_revisions(request: web.Request, owner, repo, page_name, page=None) -> web.Response:
    """Get revisions of a wiki page

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param page_name: name of the page
    :type page_name: str
    :param page: page number of results to return (1-based)
    :type page: int

    """
    return web.Response(status=200)


async def repo_get_wiki_pages(request: web.Request, owner, repo, page=None, limit=None) -> web.Response:
    """Get all wiki pages

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param page: page number of results to return (1-based)
    :type page: int
    :param limit: page size of results
    :type limit: int

    """
    return web.Response(status=200)


async def repo_list_activity_feeds(request: web.Request, owner, repo, _date=None, page=None, limit=None) -> web.Response:
    """List a repository&#39;s activity feeds

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param _date: the date of the activities to be found
    :type _date: str
    :param page: page number of results to return (1-based)
    :type page: int
    :param limit: page size of results
    :type limit: int

    """
    _date = util.deserialize_date(_date)
    return web.Response(status=200)


async def repo_list_all_git_refs(request: web.Request, owner, repo) -> web.Response:
    """Get specified ref or filtered repository&#39;s refs

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str

    """
    return web.Response(status=200)


async def repo_list_branch_protection(request: web.Request, owner, repo) -> web.Response:
    """List branch protections for a repository

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str

    """
    return web.Response(status=200)


async def repo_list_branches(request: web.Request, owner, repo, page=None, limit=None) -> web.Response:
    """List a repository&#39;s branches

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param page: page number of results to return (1-based)
    :type page: int
    :param limit: page size of results
    :type limit: int

    """
    return web.Response(status=200)


async def repo_list_collaborators(request: web.Request, owner, repo, page=None, limit=None) -> web.Response:
    """List a repository&#39;s collaborators

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param page: page number of results to return (1-based)
    :type page: int
    :param limit: page size of results
    :type limit: int

    """
    return web.Response(status=200)


async def repo_list_git_hooks(request: web.Request, owner, repo) -> web.Response:
    """List the Git hooks in a repository

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str

    """
    return web.Response(status=200)


async def repo_list_git_refs(request: web.Request, owner, repo, ref) -> web.Response:
    """Get specified ref or filtered repository&#39;s refs

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param ref: part or full name of the ref
    :type ref: str

    """
    return web.Response(status=200)


async def repo_list_hooks(request: web.Request, owner, repo, page=None, limit=None) -> web.Response:
    """List the hooks in a repository

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param page: page number of results to return (1-based)
    :type page: int
    :param limit: page size of results
    :type limit: int

    """
    return web.Response(status=200)


async def repo_list_keys(request: web.Request, owner, repo, key_id=None, fingerprint=None, page=None, limit=None) -> web.Response:
    """List a repository&#39;s keys

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param key_id: the key_id to search for
    :type key_id: int
    :param fingerprint: fingerprint of the key
    :type fingerprint: str
    :param page: page number of results to return (1-based)
    :type page: int
    :param limit: page size of results
    :type limit: int

    """
    return web.Response(status=200)


async def repo_list_pull_requests(request: web.Request, owner, repo, state=None, sort=None, milestone=None, labels=None, page=None, limit=None) -> web.Response:
    """List a repo&#39;s pull requests

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param state: State of pull request: open or closed (optional)
    :type state: str
    :param sort: Type of sort
    :type sort: str
    :param milestone: ID of the milestone
    :type milestone: int
    :param labels: Label IDs
    :type labels: List[int]
    :param page: page number of results to return (1-based)
    :type page: int
    :param limit: page size of results
    :type limit: int

    """
    return web.Response(status=200)


async def repo_list_pull_reviews(request: web.Request, owner, repo, index, page=None, limit=None) -> web.Response:
    """List all reviews for a pull request

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param index: index of the pull request
    :type index: int
    :param page: page number of results to return (1-based)
    :type page: int
    :param limit: page size of results
    :type limit: int

    """
    return web.Response(status=200)


async def repo_list_push_mirrors(request: web.Request, owner, repo, page=None, limit=None) -> web.Response:
    """Get all push mirrors of the repository

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param page: page number of results to return (1-based)
    :type page: int
    :param limit: page size of results
    :type limit: int

    """
    return web.Response(status=200)


async def repo_list_release_attachments(request: web.Request, owner, repo, id) -> web.Response:
    """List release&#39;s attachments

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param id: id of the release
    :type id: int

    """
    return web.Response(status=200)


async def repo_list_releases(request: web.Request, owner, repo, draft=None, pre_release=None, per_page=None, page=None, limit=None) -> web.Response:
    """List a repo&#39;s releases

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param draft: filter (exclude / include) drafts, if you dont have repo write access none will show
    :type draft: bool
    :param pre_release: filter (exclude / include) pre-releases
    :type pre_release: bool
    :param per_page: page size of results, deprecated - use limit
    :type per_page: int
    :param page: page number of results to return (1-based)
    :type page: int
    :param limit: page size of results
    :type limit: int

    """
    return web.Response(status=200)


async def repo_list_stargazers(request: web.Request, owner, repo, page=None, limit=None) -> web.Response:
    """List a repo&#39;s stargazers

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param page: page number of results to return (1-based)
    :type page: int
    :param limit: page size of results
    :type limit: int

    """
    return web.Response(status=200)


async def repo_list_statuses(request: web.Request, owner, repo, sha, sort=None, state=None, page=None, limit=None) -> web.Response:
    """Get a commit&#39;s statuses

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param sha: sha of the commit
    :type sha: str
    :param sort: type of sort
    :type sort: str
    :param state: type of state
    :type state: str
    :param page: page number of results to return (1-based)
    :type page: int
    :param limit: page size of results
    :type limit: int

    """
    return web.Response(status=200)


async def repo_list_statuses_by_ref(request: web.Request, owner, repo, ref, sort=None, state=None, page=None, limit=None) -> web.Response:
    """Get a commit&#39;s statuses, by branch/tag/commit reference

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param ref: name of branch/tag/commit
    :type ref: str
    :param sort: type of sort
    :type sort: str
    :param state: type of state
    :type state: str
    :param page: page number of results to return (1-based)
    :type page: int
    :param limit: page size of results
    :type limit: int

    """
    return web.Response(status=200)


async def repo_list_subscribers(request: web.Request, owner, repo, page=None, limit=None) -> web.Response:
    """List a repo&#39;s watchers

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param page: page number of results to return (1-based)
    :type page: int
    :param limit: page size of results
    :type limit: int

    """
    return web.Response(status=200)


async def repo_list_tags(request: web.Request, owner, repo, page=None, limit=None) -> web.Response:
    """List a repository&#39;s tags

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param page: page number of results to return (1-based)
    :type page: int
    :param limit: page size of results, default maximum page size is 50
    :type limit: int

    """
    return web.Response(status=200)


async def repo_list_teams(request: web.Request, owner, repo) -> web.Response:
    """List a repository&#39;s teams

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str

    """
    return web.Response(status=200)


async def repo_list_topics(request: web.Request, owner, repo, page=None, limit=None) -> web.Response:
    """Get list of topics that a repository has

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param page: page number of results to return (1-based)
    :type page: int
    :param limit: page size of results
    :type limit: int

    """
    return web.Response(status=200)


async def repo_merge_pull_request(request: web.Request, owner, repo, index, body=None) -> web.Response:
    """Merge a pull request

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param index: index of the pull request to merge
    :type index: int
    :param body: 
    :type body: dict | bytes

    """
    body = MergePullRequestOption.from_dict(body)
    return web.Response(status=200)


async def repo_migrate(request: web.Request, body=None) -> web.Response:
    """Migrate a remote git repository

    

    :param body: 
    :type body: dict | bytes

    """
    body = MigrateRepoOptions.from_dict(body)
    return web.Response(status=200)


async def repo_mirror_sync(request: web.Request, owner, repo) -> web.Response:
    """Sync a mirrored repository

    

    :param owner: owner of the repo to sync
    :type owner: str
    :param repo: name of the repo to sync
    :type repo: str

    """
    return web.Response(status=200)


async def repo_pull_request_is_merged(request: web.Request, owner, repo, index) -> web.Response:
    """Check if a pull request has been merged

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param index: index of the pull request
    :type index: int

    """
    return web.Response(status=200)


async def repo_push_mirror_sync(request: web.Request, owner, repo) -> web.Response:
    """Sync all push mirrored repository

    

    :param owner: owner of the repo to sync
    :type owner: str
    :param repo: name of the repo to sync
    :type repo: str

    """
    return web.Response(status=200)


async def repo_search(request: web.Request, q=None, topic=None, include_desc=None, uid=None, priority_owner_id=None, team_id=None, starred_by=None, private=None, is_private=None, template=None, archived=None, mode=None, exclusive=None, sort=None, order=None, page=None, limit=None) -> web.Response:
    """Search for repositories

    

    :param q: keyword
    :type q: str
    :param topic: Limit search to repositories with keyword as topic
    :type topic: bool
    :param include_desc: include search of keyword within repository description
    :type include_desc: bool
    :param uid: search only for repos that the user with the given id owns or contributes to
    :type uid: int
    :param priority_owner_id: repo owner to prioritize in the results
    :type priority_owner_id: int
    :param team_id: search only for repos that belong to the given team id
    :type team_id: int
    :param starred_by: search only for repos that the user with the given id has starred
    :type starred_by: int
    :param private: include private repositories this user has access to (defaults to true)
    :type private: bool
    :param is_private: show only pubic, private or all repositories (defaults to all)
    :type is_private: bool
    :param template: include template repositories this user has access to (defaults to true)
    :type template: bool
    :param archived: show only archived, non-archived or all repositories (defaults to all)
    :type archived: bool
    :param mode: type of repository to search for. Supported values are \&quot;fork\&quot;, \&quot;source\&quot;, \&quot;mirror\&quot; and \&quot;collaborative\&quot;
    :type mode: str
    :param exclusive: if &#x60;uid&#x60; is given, search only for repos that the user owns
    :type exclusive: bool
    :param sort: sort repos by attribute. Supported values are \&quot;alpha\&quot;, \&quot;created\&quot;, \&quot;updated\&quot;, \&quot;size\&quot;, and \&quot;id\&quot;. Default is \&quot;alpha\&quot;
    :type sort: str
    :param order: sort order, either \&quot;asc\&quot; (ascending) or \&quot;desc\&quot; (descending). Default is \&quot;asc\&quot;, ignored if \&quot;sort\&quot; is not specified.
    :type order: str
    :param page: page number of results to return (1-based)
    :type page: int
    :param limit: page size of results
    :type limit: int

    """
    return web.Response(status=200)


async def repo_signing_key(request: web.Request, owner, repo) -> web.Response:
    """Get signing-key.gpg for given repository

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str

    """
    return web.Response(status=200)


async def repo_submit_pull_review(request: web.Request, owner, repo, index, id, body) -> web.Response:
    """Submit a pending review to an pull request

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param index: index of the pull request
    :type index: int
    :param id: id of the review
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = SubmitPullReviewOptions.from_dict(body)
    return web.Response(status=200)


async def repo_test_hook(request: web.Request, owner, repo, id, ref=None) -> web.Response:
    """Test a push webhook

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param id: id of the hook to test
    :type id: int
    :param ref: The name of the commit/branch/tag, indicates which commit will be loaded to the webhook payload.
    :type ref: str

    """
    return web.Response(status=200)


async def repo_tracked_times(request: web.Request, owner, repo, user=None, since=None, before=None, page=None, limit=None) -> web.Response:
    """List a repo&#39;s tracked times

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param user: optional filter by user (available for issue managers)
    :type user: str
    :param since: Only show times updated after the given time. This is a timestamp in RFC 3339 format
    :type since: str
    :param before: Only show times updated before the given time. This is a timestamp in RFC 3339 format
    :type before: str
    :param page: page number of results to return (1-based)
    :type page: int
    :param limit: page size of results
    :type limit: int

    """
    since = util.deserialize_datetime(since)
    before = util.deserialize_datetime(before)
    return web.Response(status=200)


async def repo_transfer(request: web.Request, owner, repo, body) -> web.Response:
    """Transfer a repo ownership

    

    :param owner: owner of the repo to transfer
    :type owner: str
    :param repo: name of the repo to transfer
    :type repo: str
    :param body: Transfer Options
    :type body: dict | bytes

    """
    body = TransferRepoOption.from_dict(body)
    return web.Response(status=200)


async def repo_un_dismiss_pull_review(request: web.Request, owner, repo, index, id) -> web.Response:
    """Cancel to dismiss a review for a pull request

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param index: index of the pull request
    :type index: int
    :param id: id of the review
    :type id: int

    """
    return web.Response(status=200)


async def repo_update_file(request: web.Request, owner, repo, filepath, body) -> web.Response:
    """Update a file in a repository

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param filepath: path of the file to update
    :type filepath: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateFileOptions.from_dict(body)
    return web.Response(status=200)


async def repo_update_pull_request(request: web.Request, owner, repo, index, style=None) -> web.Response:
    """Merge PR&#39;s baseBranch into headBranch

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param index: index of the pull request to get
    :type index: int
    :param style: how to update pull request
    :type style: str

    """
    return web.Response(status=200)


async def repo_update_topics(request: web.Request, owner, repo, body=None) -> web.Response:
    """Replace list of topics for a repository

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param body: 
    :type body: dict | bytes

    """
    body = RepoTopicOptions.from_dict(body)
    return web.Response(status=200)


async def repo_validate_issue_config(request: web.Request, owner, repo) -> web.Response:
    """Returns the validation information for a issue config

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str

    """
    return web.Response(status=200)


async def topic_search(request: web.Request, q, page=None, limit=None) -> web.Response:
    """search topics via keyword

    

    :param q: keywords to search
    :type q: str
    :param page: page number of results to return (1-based)
    :type page: int
    :param limit: page size of results
    :type limit: int

    """
    return web.Response(status=200)


async def user_current_check_subscription(request: web.Request, owner, repo) -> web.Response:
    """Check if the current user is watching a repo

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str

    """
    return web.Response(status=200)


async def user_current_delete_subscription(request: web.Request, owner, repo) -> web.Response:
    """Unwatch a repo

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str

    """
    return web.Response(status=200)


async def user_current_put_subscription(request: web.Request, owner, repo) -> web.Response:
    """Watch a repo

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str

    """
    return web.Response(status=200)


async def user_tracked_times(request: web.Request, owner, repo, user) -> web.Response:
    """List a user&#39;s tracked times in a repo

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param user: username of user
    :type user: str

    """
    return web.Response(status=200)
