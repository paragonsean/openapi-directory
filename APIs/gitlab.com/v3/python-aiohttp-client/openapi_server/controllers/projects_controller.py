from typing import List, Dict
from aiohttp import web

from openapi_server.models.access_requester import AccessRequester
from openapi_server.models.award_emoji import AwardEmoji
from openapi_server.models.basic_project_details import BasicProjectDetails
from openapi_server.models.board import Board
from openapi_server.models.build import Build
from openapi_server.models.commit_note import CommitNote
from openapi_server.models.commit_status import CommitStatus
from openapi_server.models.compare import Compare
from openapi_server.models.contributor import Contributor
from openapi_server.models.deployment import Deployment
from openapi_server.models.environment import Environment
from openapi_server.models.event import Event
from openapi_server.models.issue import Issue
from openapi_server.models.label import Label
from openapi_server.models.mr_note import MRNote
from openapi_server.models.member import Member
from openapi_server.models.merge_request import MergeRequest
from openapi_server.models.merge_request_changes import MergeRequestChanges
from openapi_server.models.merge_request_diff import MergeRequestDiff
from openapi_server.models.merge_request_diff_full import MergeRequestDiffFull
from openapi_server.models.milestone import Milestone
from openapi_server.models.note import Note
from openapi_server.models.notification_setting import NotificationSetting
from openapi_server.models.pipeline import Pipeline
from openapi_server.models.post_v3_groups_id_members_request import PostV3GroupsIdMembersRequest
from openapi_server.models.post_v3_projects_fork_id_request import PostV3ProjectsForkIdRequest
from openapi_server.models.post_v3_projects_id_boards_board_id_lists_request import PostV3ProjectsIdBoardsBoardIdListsRequest
from openapi_server.models.post_v3_projects_id_deploy_keys_request import PostV3ProjectsIdDeployKeysRequest
from openapi_server.models.post_v3_projects_id_environments_request import PostV3ProjectsIdEnvironmentsRequest
from openapi_server.models.post_v3_projects_id_hooks_request import PostV3ProjectsIdHooksRequest
from openapi_server.models.post_v3_projects_id_issues_issue_id_add_spent_time_request import PostV3ProjectsIdIssuesIssueIdAddSpentTimeRequest
from openapi_server.models.post_v3_projects_id_issues_issue_id_award_emoji_request import PostV3ProjectsIdIssuesIssueIdAwardEmojiRequest
from openapi_server.models.post_v3_projects_id_issues_issue_id_move_request import PostV3ProjectsIdIssuesIssueIdMoveRequest
from openapi_server.models.post_v3_projects_id_issues_noteable_id_notes_request import PostV3ProjectsIdIssuesNoteableIdNotesRequest
from openapi_server.models.post_v3_projects_id_issues_request import PostV3ProjectsIdIssuesRequest
from openapi_server.models.post_v3_projects_id_labels_request import PostV3ProjectsIdLabelsRequest
from openapi_server.models.post_v3_projects_id_merge_request_merge_request_id_comments_request import PostV3ProjectsIdMergeRequestMergeRequestIdCommentsRequest
from openapi_server.models.post_v3_projects_id_merge_requests_request import PostV3ProjectsIdMergeRequestsRequest
from openapi_server.models.post_v3_projects_id_milestones_request import PostV3ProjectsIdMilestonesRequest
from openapi_server.models.post_v3_projects_id_pipeline_request import PostV3ProjectsIdPipelineRequest
from openapi_server.models.post_v3_projects_id_ref_ref_trigger_builds_request import PostV3ProjectsIdRefRefTriggerBuildsRequest
from openapi_server.models.post_v3_projects_id_repository_branches_request import PostV3ProjectsIdRepositoryBranchesRequest
from openapi_server.models.post_v3_projects_id_repository_commits_request import PostV3ProjectsIdRepositoryCommitsRequest
from openapi_server.models.post_v3_projects_id_repository_commits_sha_cherry_pick_request import PostV3ProjectsIdRepositoryCommitsShaCherryPickRequest
from openapi_server.models.post_v3_projects_id_repository_commits_sha_comments_request import PostV3ProjectsIdRepositoryCommitsShaCommentsRequest
from openapi_server.models.post_v3_projects_id_repository_tags_request import PostV3ProjectsIdRepositoryTagsRequest
from openapi_server.models.post_v3_projects_id_runners_request import PostV3ProjectsIdRunnersRequest
from openapi_server.models.post_v3_projects_id_share_request import PostV3ProjectsIdShareRequest
from openapi_server.models.post_v3_projects_id_snippets_request import PostV3ProjectsIdSnippetsRequest
from openapi_server.models.post_v3_projects_id_statuses_sha_request import PostV3ProjectsIdStatusesShaRequest
from openapi_server.models.post_v3_projects_id_uploads_request import PostV3ProjectsIdUploadsRequest
from openapi_server.models.post_v3_projects_id_variables_request import PostV3ProjectsIdVariablesRequest
from openapi_server.models.post_v3_projects_request import PostV3ProjectsRequest
from openapi_server.models.post_v3_projects_user_user_id_request import PostV3ProjectsUserUserIdRequest
from openapi_server.models.project import Project
from openapi_server.models.project_group_link import ProjectGroupLink
from openapi_server.models.project_hook import ProjectHook
from openapi_server.models.project_service import ProjectService
from openapi_server.models.project_snippet import ProjectSnippet
from openapi_server.models.project_with_access import ProjectWithAccess
from openapi_server.models.put_v3_groups_id_access_requests_user_id_approve_request import PutV3GroupsIdAccessRequestsUserIdApproveRequest
from openapi_server.models.put_v3_groups_id_members_user_id_request import PutV3GroupsIdMembersUserIdRequest
from openapi_server.models.put_v3_projects_id_boards_board_id_lists_list_id_request import PutV3ProjectsIdBoardsBoardIdListsListIdRequest
from openapi_server.models.put_v3_projects_id_environments_environment_id_request import PutV3ProjectsIdEnvironmentsEnvironmentIdRequest
from openapi_server.models.put_v3_projects_id_issues_issue_id_request import PutV3ProjectsIdIssuesIssueIdRequest
from openapi_server.models.put_v3_projects_id_issues_noteable_id_notes_note_id_request import PutV3ProjectsIdIssuesNoteableIdNotesNoteIdRequest
from openapi_server.models.put_v3_projects_id_labels_request import PutV3ProjectsIdLabelsRequest
from openapi_server.models.put_v3_projects_id_merge_request_merge_request_id_merge_request import PutV3ProjectsIdMergeRequestMergeRequestIdMergeRequest
from openapi_server.models.put_v3_projects_id_merge_request_merge_request_id_request import PutV3ProjectsIdMergeRequestMergeRequestIdRequest
from openapi_server.models.put_v3_projects_id_milestones_milestone_id_request import PutV3ProjectsIdMilestonesMilestoneIdRequest
from openapi_server.models.put_v3_projects_id_notification_settings_request import PutV3ProjectsIdNotificationSettingsRequest
from openapi_server.models.put_v3_projects_id_repository_branches_branch_protect_request import PutV3ProjectsIdRepositoryBranchesBranchProtectRequest
from openapi_server.models.put_v3_projects_id_repository_files_request import PutV3ProjectsIdRepositoryFilesRequest
from openapi_server.models.put_v3_projects_id_repository_tags_tag_name_release_request import PutV3ProjectsIdRepositoryTagsTagNameReleaseRequest
from openapi_server.models.put_v3_projects_id_request import PutV3ProjectsIdRequest
from openapi_server.models.put_v3_projects_id_services_asana_request import PutV3ProjectsIdServicesAsanaRequest
from openapi_server.models.put_v3_projects_id_services_assembla_request import PutV3ProjectsIdServicesAssemblaRequest
from openapi_server.models.put_v3_projects_id_services_bamboo_request import PutV3ProjectsIdServicesBambooRequest
from openapi_server.models.put_v3_projects_id_services_bugzilla_request import PutV3ProjectsIdServicesBugzillaRequest
from openapi_server.models.put_v3_projects_id_services_buildkite_request import PutV3ProjectsIdServicesBuildkiteRequest
from openapi_server.models.put_v3_projects_id_services_builds_email_request import PutV3ProjectsIdServicesBuildsEmailRequest
from openapi_server.models.put_v3_projects_id_services_campfire_request import PutV3ProjectsIdServicesCampfireRequest
from openapi_server.models.put_v3_projects_id_services_drone_ci_request import PutV3ProjectsIdServicesDroneCiRequest
from openapi_server.models.put_v3_projects_id_services_emails_on_push_request import PutV3ProjectsIdServicesEmailsOnPushRequest
from openapi_server.models.put_v3_projects_id_services_external_wiki_request import PutV3ProjectsIdServicesExternalWikiRequest
from openapi_server.models.put_v3_projects_id_services_flowdock_request import PutV3ProjectsIdServicesFlowdockRequest
from openapi_server.models.put_v3_projects_id_services_gemnasium_request import PutV3ProjectsIdServicesGemnasiumRequest
from openapi_server.models.put_v3_projects_id_services_hipchat_request import PutV3ProjectsIdServicesHipchatRequest
from openapi_server.models.put_v3_projects_id_services_irker_request import PutV3ProjectsIdServicesIrkerRequest
from openapi_server.models.put_v3_projects_id_services_jira_request import PutV3ProjectsIdServicesJiraRequest
from openapi_server.models.put_v3_projects_id_services_kubernetes_request import PutV3ProjectsIdServicesKubernetesRequest
from openapi_server.models.put_v3_projects_id_services_mattermost_request import PutV3ProjectsIdServicesMattermostRequest
from openapi_server.models.put_v3_projects_id_services_mattermost_slash_commands_request import PutV3ProjectsIdServicesMattermostSlashCommandsRequest
from openapi_server.models.put_v3_projects_id_services_pipelines_email_request import PutV3ProjectsIdServicesPipelinesEmailRequest
from openapi_server.models.put_v3_projects_id_services_pivotaltracker_request import PutV3ProjectsIdServicesPivotaltrackerRequest
from openapi_server.models.put_v3_projects_id_services_pushover_request import PutV3ProjectsIdServicesPushoverRequest
from openapi_server.models.put_v3_projects_id_services_redmine_request import PutV3ProjectsIdServicesRedmineRequest
from openapi_server.models.put_v3_projects_id_services_slack_request import PutV3ProjectsIdServicesSlackRequest
from openapi_server.models.put_v3_projects_id_services_slack_slash_commands_request import PutV3ProjectsIdServicesSlackSlashCommandsRequest
from openapi_server.models.put_v3_projects_id_services_teamcity_request import PutV3ProjectsIdServicesTeamcityRequest
from openapi_server.models.put_v3_projects_id_snippets_snippet_id_request import PutV3ProjectsIdSnippetsSnippetIdRequest
from openapi_server.models.put_v3_projects_id_variables_key_request import PutV3ProjectsIdVariablesKeyRequest
from openapi_server.models.release import Release
from openapi_server.models.repo_branch import RepoBranch
from openapi_server.models.repo_commit import RepoCommit
from openapi_server.models.repo_commit_detail import RepoCommitDetail
from openapi_server.models.repo_tag import RepoTag
from openapi_server.models.repo_tree_object import RepoTreeObject
from openapi_server.models.runner import Runner
from openapi_server.models.ssh_key import SSHKey
from openapi_server.models.todo import Todo
from openapi_server.models.trigger import Trigger
from openapi_server.models.trigger_request import TriggerRequest
from openapi_server.models.user_basic import UserBasic
from openapi_server.models.variable import Variable
from openapi_server import util


async def delete_v3_projects_id(request: web.Request, id) -> web.Response:
    """Remove a project

    Remove a project

    :param id: The ID of a project
    :type id: str

    """
    return web.Response(status=200)


async def delete_v3_projects_id_access_requests_user_id(request: web.Request, id, user_id) -> web.Response:
    """Denies an access request for the given user.

    This feature was introduced in GitLab 8.11.

    :param id: The project ID
    :type id: str
    :param user_id: The user ID of the access requester
    :type user_id: int

    """
    return web.Response(status=200)


async def delete_v3_projects_id_boards_board_id_lists_list_id(request: web.Request, id, board_id, list_id) -> web.Response:
    """Delete a board list

    This feature was introduced in 8.13

    :param id: The ID of a project
    :type id: str
    :param board_id: The ID of a board
    :type board_id: int
    :param list_id: The ID of a board list
    :type list_id: int

    """
    return web.Response(status=200)


async def delete_v3_projects_id_deploy_keys_key_id(request: web.Request, id, key_id) -> web.Response:
    """Delete deploy key for a project

    Delete deploy key for a project

    :param id: The ID of the project
    :type id: str
    :param key_id: The ID of the deploy key
    :type key_id: int

    """
    return web.Response(status=200)


async def delete_v3_projects_id_deploy_keys_key_id_disable(request: web.Request, id, key_id) -> web.Response:
    """Disable a deploy key for a project

    This feature was added in GitLab 8.11

    :param id: The ID of the project
    :type id: str
    :param key_id: The ID of the deploy key
    :type key_id: int

    """
    return web.Response(status=200)


async def delete_v3_projects_id_environments_environment_id(request: web.Request, id, environment_id) -> web.Response:
    """Deletes an existing environment

    This feature was introduced in GitLab 8.11.

    :param id: The project ID
    :type id: str
    :param environment_id: The environment ID
    :type environment_id: int

    """
    return web.Response(status=200)


async def delete_v3_projects_id_fork(request: web.Request, id) -> web.Response:
    """Remove a forked_from relationship

    Remove a forked_from relationship

    :param id: The ID of a project
    :type id: str

    """
    return web.Response(status=200)


async def delete_v3_projects_id_hooks_hook_id(request: web.Request, id, hook_id) -> web.Response:
    """Deletes project hook

    Deletes project hook

    :param id: The ID of a project
    :type id: str
    :param hook_id: The ID of the hook to delete
    :type hook_id: int

    """
    return web.Response(status=200)


async def delete_v3_projects_id_issues_issue_id(request: web.Request, id, issue_id) -> web.Response:
    """Delete a project issue

    Delete a project issue

    :param id: The ID of a project
    :type id: str
    :param issue_id: The ID of a project issue
    :type issue_id: int

    """
    return web.Response(status=200)


async def delete_v3_projects_id_issues_issue_id_award_emoji_award_id(request: web.Request, award_id, id, issue_id) -> web.Response:
    """Delete a +awardables+ award emoji

    This feature was introduced in 8.9

    :param award_id: The ID of an award emoji
    :type award_id: int
    :param id: 
    :type id: int
    :param issue_id: 
    :type issue_id: int

    """
    return web.Response(status=200)


async def delete_v3_projects_id_issues_issue_id_notes_note_id_award_emoji_award_id(request: web.Request, award_id, id, issue_id, note_id) -> web.Response:
    """Delete a +awardables+ award emoji

    This feature was introduced in 8.9

    :param award_id: The ID of an award emoji
    :type award_id: int
    :param id: 
    :type id: int
    :param issue_id: 
    :type issue_id: int
    :param note_id: 
    :type note_id: int

    """
    return web.Response(status=200)


async def delete_v3_projects_id_issues_noteable_id_notes_note_id(request: web.Request, id, noteable_id, note_id) -> web.Response:
    """Delete a +noteable+ note

    Delete a +noteable+ note

    :param id: The ID of a project
    :type id: str
    :param noteable_id: The ID of the noteable
    :type noteable_id: int
    :param note_id: The ID of a note
    :type note_id: int

    """
    return web.Response(status=200)


async def delete_v3_projects_id_issues_subscribable_id_subscription(request: web.Request, id, subscribable_id) -> web.Response:
    """Unsubscribe from a resource

    Unsubscribe from a resource

    :param id: The ID of a project
    :type id: str
    :param subscribable_id: The ID of a resource
    :type subscribable_id: str

    """
    return web.Response(status=200)


async def delete_v3_projects_id_keys_key_id(request: web.Request, id, key_id) -> web.Response:
    """Delete deploy key for a project

    Delete deploy key for a project

    :param id: The ID of the project
    :type id: str
    :param key_id: The ID of the deploy key
    :type key_id: int

    """
    return web.Response(status=200)


async def delete_v3_projects_id_keys_key_id_disable(request: web.Request, id, key_id) -> web.Response:
    """Disable a deploy key for a project

    This feature was added in GitLab 8.11

    :param id: The ID of the project
    :type id: str
    :param key_id: The ID of the deploy key
    :type key_id: int

    """
    return web.Response(status=200)


async def delete_v3_projects_id_labels(request: web.Request, id, name) -> web.Response:
    """Delete an existing label

    Delete an existing label

    :param id: The ID of a project
    :type id: str
    :param name: The name of the label to be deleted
    :type name: str

    """
    return web.Response(status=200)


async def delete_v3_projects_id_labels_subscribable_id_subscription(request: web.Request, id, subscribable_id) -> web.Response:
    """Unsubscribe from a resource

    Unsubscribe from a resource

    :param id: The ID of a project
    :type id: str
    :param subscribable_id: The ID of a resource
    :type subscribable_id: str

    """
    return web.Response(status=200)


async def delete_v3_projects_id_members_user_id(request: web.Request, id, user_id) -> web.Response:
    """Removes a user from a group or project.

    Removes a user from a group or project.

    :param id: The project ID
    :type id: str
    :param user_id: The user ID of the member
    :type user_id: int

    """
    return web.Response(status=200)


async def delete_v3_projects_id_merge_request_subscribable_id_subscription(request: web.Request, id, subscribable_id) -> web.Response:
    """Unsubscribe from a resource

    Unsubscribe from a resource

    :param id: The ID of a project
    :type id: str
    :param subscribable_id: The ID of a resource
    :type subscribable_id: str

    """
    return web.Response(status=200)


async def delete_v3_projects_id_merge_requests_merge_request_id(request: web.Request, id, merge_request_id) -> web.Response:
    """Delete a merge request

    Delete a merge request

    :param id: The ID of a project
    :type id: str
    :param merge_request_id: The ID of a merge request
    :type merge_request_id: int

    """
    return web.Response(status=200)


async def delete_v3_projects_id_merge_requests_merge_request_id_award_emoji_award_id(request: web.Request, award_id, id, merge_request_id) -> web.Response:
    """Delete a +awardables+ award emoji

    This feature was introduced in 8.9

    :param award_id: The ID of an award emoji
    :type award_id: int
    :param id: 
    :type id: int
    :param merge_request_id: 
    :type merge_request_id: int

    """
    return web.Response(status=200)


async def delete_v3_projects_id_merge_requests_merge_request_id_notes_note_id_award_emoji_award_id(request: web.Request, award_id, id, merge_request_id, note_id) -> web.Response:
    """Delete a +awardables+ award emoji

    This feature was introduced in 8.9

    :param award_id: The ID of an award emoji
    :type award_id: int
    :param id: 
    :type id: int
    :param merge_request_id: 
    :type merge_request_id: int
    :param note_id: 
    :type note_id: int

    """
    return web.Response(status=200)


async def delete_v3_projects_id_merge_requests_noteable_id_notes_note_id(request: web.Request, id, noteable_id, note_id) -> web.Response:
    """Delete a +noteable+ note

    Delete a +noteable+ note

    :param id: The ID of a project
    :type id: str
    :param noteable_id: The ID of the noteable
    :type noteable_id: int
    :param note_id: The ID of a note
    :type note_id: int

    """
    return web.Response(status=200)


async def delete_v3_projects_id_merge_requests_subscribable_id_subscription(request: web.Request, id, subscribable_id) -> web.Response:
    """Unsubscribe from a resource

    Unsubscribe from a resource

    :param id: The ID of a project
    :type id: str
    :param subscribable_id: The ID of a resource
    :type subscribable_id: str

    """
    return web.Response(status=200)


async def delete_v3_projects_id_repository_branches_branch(request: web.Request, id, branch) -> web.Response:
    """Delete a branch

    Delete a branch

    :param id: The ID of a project
    :type id: str
    :param branch: The name of the branch
    :type branch: str

    """
    return web.Response(status=200)


async def delete_v3_projects_id_repository_files(request: web.Request, id, file_path, branch_name, commit_message, author_email=None, author_name=None) -> web.Response:
    """Delete an existing file in repository

    Delete an existing file in repository

    :param id: The project ID
    :type id: str
    :param file_path: The path to new file. Ex. lib/class.rb
    :type file_path: str
    :param branch_name: The name of branch
    :type branch_name: str
    :param commit_message: Commit Message
    :type commit_message: str
    :param author_email: The email of the author
    :type author_email: str
    :param author_name: The name of the author
    :type author_name: str

    """
    return web.Response(status=200)


async def delete_v3_projects_id_repository_merged_branches(request: web.Request, id) -> web.Response:
    """delete_v3_projects_id_repository_merged_branches

    

    :param id: The ID of a project
    :type id: str

    """
    return web.Response(status=200)


async def delete_v3_projects_id_repository_tags_tag_name(request: web.Request, id, tag_name) -> web.Response:
    """Delete a repository tag

    Delete a repository tag

    :param id: The ID of a project
    :type id: str
    :param tag_name: The name of the tag
    :type tag_name: str

    """
    return web.Response(status=200)


async def delete_v3_projects_id_runners_runner_id(request: web.Request, id, runner_id) -> web.Response:
    """Disable project&#39;s runner

    Disable project&#39;s runner

    :param id: The ID of a project
    :type id: str
    :param runner_id: The ID of the runner
    :type runner_id: int

    """
    return web.Response(status=200)


async def delete_v3_projects_id_services_service_slug(request: web.Request, service_slug, id) -> web.Response:
    """Delete a service for project

    Delete a service for project

    :param service_slug: The name of the service
    :type service_slug: str
    :param id: 
    :type id: int

    """
    return web.Response(status=200)


async def delete_v3_projects_id_share_group_id(request: web.Request, id, group_id) -> web.Response:
    """delete_v3_projects_id_share_group_id

    

    :param id: The ID of a project
    :type id: str
    :param group_id: The ID of the group
    :type group_id: int

    """
    return web.Response(status=200)


async def delete_v3_projects_id_snippets_noteable_id_notes_note_id(request: web.Request, id, noteable_id, note_id) -> web.Response:
    """Delete a +noteable+ note

    Delete a +noteable+ note

    :param id: The ID of a project
    :type id: str
    :param noteable_id: The ID of the noteable
    :type noteable_id: int
    :param note_id: The ID of a note
    :type note_id: int

    """
    return web.Response(status=200)


async def delete_v3_projects_id_snippets_snippet_id(request: web.Request, id, snippet_id) -> web.Response:
    """Delete a project snippet

    Delete a project snippet

    :param id: The ID of a project
    :type id: str
    :param snippet_id: The ID of a project snippet
    :type snippet_id: int

    """
    return web.Response(status=200)


async def delete_v3_projects_id_snippets_snippet_id_award_emoji_award_id(request: web.Request, award_id, id, snippet_id) -> web.Response:
    """Delete a +awardables+ award emoji

    This feature was introduced in 8.9

    :param award_id: The ID of an award emoji
    :type award_id: int
    :param id: 
    :type id: int
    :param snippet_id: 
    :type snippet_id: int

    """
    return web.Response(status=200)


async def delete_v3_projects_id_snippets_snippet_id_notes_note_id_award_emoji_award_id(request: web.Request, award_id, id, snippet_id, note_id) -> web.Response:
    """Delete a +awardables+ award emoji

    This feature was introduced in 8.9

    :param award_id: The ID of an award emoji
    :type award_id: int
    :param id: 
    :type id: int
    :param snippet_id: 
    :type snippet_id: int
    :param note_id: 
    :type note_id: int

    """
    return web.Response(status=200)


async def delete_v3_projects_id_star(request: web.Request, id) -> web.Response:
    """Unstar a project

    Unstar a project

    :param id: The ID of a project
    :type id: str

    """
    return web.Response(status=200)


async def delete_v3_projects_id_triggers_token(request: web.Request, id, token) -> web.Response:
    """Delete a trigger

    Delete a trigger

    :param id: The ID of a project
    :type id: str
    :param token: The unique token of trigger
    :type token: str

    """
    return web.Response(status=200)


async def delete_v3_projects_id_variables_key(request: web.Request, id, key) -> web.Response:
    """Delete an existing variable from a project

    Delete an existing variable from a project

    :param id: The ID of a project
    :type id: str
    :param key: The key of the variable
    :type key: str

    """
    return web.Response(status=200)


async def get_v3_projects(request: web.Request, order_by=None, sort=None, archived=None, visibility=None, search=None, page=None, per_page=None, simple=None) -> web.Response:
    """Get a projects list for authenticated user

    Get a projects list for authenticated user

    :param order_by: Return projects ordered by field
    :type order_by: str
    :param sort: Return projects sorted in ascending and descending order
    :type sort: str
    :param archived: Limit by archived status
    :type archived: bool
    :param visibility: Limit by visibility
    :type visibility: str
    :param search: Return list of authorized projects matching the search criteria
    :type search: str
    :param page: Current page number
    :type page: int
    :param per_page: Number of items per page
    :type per_page: int
    :param simple: Return only the ID, URL, name, and path of each project
    :type simple: bool

    """
    return web.Response(status=200)


async def get_v3_projects_all(request: web.Request, order_by=None, sort=None, archived=None, visibility=None, search=None, page=None, per_page=None, simple=None, statistics=None) -> web.Response:
    """Get all projects for admin user

    Get all projects for admin user

    :param order_by: Return projects ordered by field
    :type order_by: str
    :param sort: Return projects sorted in ascending and descending order
    :type sort: str
    :param archived: Limit by archived status
    :type archived: bool
    :param visibility: Limit by visibility
    :type visibility: str
    :param search: Return list of authorized projects matching the search criteria
    :type search: str
    :param page: Current page number
    :type page: int
    :param per_page: Number of items per page
    :type per_page: int
    :param simple: Return only the ID, URL, name, and path of each project
    :type simple: bool
    :param statistics: Include project statistics
    :type statistics: bool

    """
    return web.Response(status=200)


async def get_v3_projects_id(request: web.Request, id) -> web.Response:
    """Get a single project

    Get a single project

    :param id: The ID of a project
    :type id: str

    """
    return web.Response(status=200)


async def get_v3_projects_id_access_requests(request: web.Request, id, page=None, per_page=None) -> web.Response:
    """Gets a list of access requests for a project.

    This feature was introduced in GitLab 8.11.

    :param id: The project ID
    :type id: str
    :param page: Current page number
    :type page: int
    :param per_page: Number of items per page
    :type per_page: int

    """
    return web.Response(status=200)


async def get_v3_projects_id_boards(request: web.Request, id) -> web.Response:
    """Get all project boards

    This feature was introduced in 8.13

    :param id: The ID of a project
    :type id: str

    """
    return web.Response(status=200)


async def get_v3_projects_id_boards_board_id_lists(request: web.Request, id, board_id) -> web.Response:
    """Get the lists of a project board

    Does not include &#x60;backlog&#x60; and &#x60;done&#x60; lists. This feature was introduced in 8.13

    :param id: The ID of a project
    :type id: str
    :param board_id: The ID of a board
    :type board_id: int

    """
    return web.Response(status=200)


async def get_v3_projects_id_boards_board_id_lists_list_id(request: web.Request, id, board_id, list_id) -> web.Response:
    """Get a list of a project board

    This feature was introduced in 8.13

    :param id: The ID of a project
    :type id: str
    :param board_id: The ID of a board
    :type board_id: int
    :param list_id: The ID of a list
    :type list_id: int

    """
    return web.Response(status=200)


async def get_v3_projects_id_builds(request: web.Request, id, scope=None, page=None, per_page=None) -> web.Response:
    """Get a project builds

    Get a project builds

    :param id: The ID of a project
    :type id: str
    :param scope: The scope of builds to show
    :type scope: str
    :param page: Current page number
    :type page: int
    :param per_page: Number of items per page
    :type per_page: int

    """
    return web.Response(status=200)


async def get_v3_projects_id_builds_artifacts_ref_name_download(request: web.Request, id, ref_name, job) -> web.Response:
    """Download the artifacts file from build

    This feature was introduced in GitLab 8.10

    :param id: The ID of a project
    :type id: str
    :param ref_name: The ref from repository
    :type ref_name: str
    :param job: The name for the build
    :type job: str

    """
    return web.Response(status=200)


async def get_v3_projects_id_builds_build_id(request: web.Request, id, build_id) -> web.Response:
    """Get a specific build of a project

    Get a specific build of a project

    :param id: The ID of a project
    :type id: str
    :param build_id: The ID of a build
    :type build_id: int

    """
    return web.Response(status=200)


async def get_v3_projects_id_builds_build_id_artifacts(request: web.Request, id, build_id) -> web.Response:
    """Download the artifacts file from build

    This feature was introduced in GitLab 8.5

    :param id: The ID of a project
    :type id: str
    :param build_id: The ID of a build
    :type build_id: int

    """
    return web.Response(status=200)


async def get_v3_projects_id_builds_build_id_trace(request: web.Request, id, build_id) -> web.Response:
    """Get a trace of a specific build of a project

    Get a trace of a specific build of a project

    :param id: The ID of a project
    :type id: str
    :param build_id: The ID of a build
    :type build_id: int

    """
    return web.Response(status=200)


async def get_v3_projects_id_deploy_keys(request: web.Request, id) -> web.Response:
    """Get a specific project&#39;s deploy keys

    Get a specific project&#39;s deploy keys

    :param id: The ID of the project
    :type id: str

    """
    return web.Response(status=200)


async def get_v3_projects_id_deploy_keys_key_id(request: web.Request, id, key_id) -> web.Response:
    """Get single deploy key

    Get single deploy key

    :param id: The ID of the project
    :type id: str
    :param key_id: The ID of the deploy key
    :type key_id: int

    """
    return web.Response(status=200)


async def get_v3_projects_id_deployments(request: web.Request, id, page=None, per_page=None) -> web.Response:
    """Get all deployments of the project

    This feature was introduced in GitLab 8.11.

    :param id: The project ID
    :type id: str
    :param page: Current page number
    :type page: int
    :param per_page: Number of items per page
    :type per_page: int

    """
    return web.Response(status=200)


async def get_v3_projects_id_deployments_deployment_id(request: web.Request, id, deployment_id) -> web.Response:
    """Gets a specific deployment

    This feature was introduced in GitLab 8.11.

    :param id: The project ID
    :type id: str
    :param deployment_id: The deployment ID
    :type deployment_id: int

    """
    return web.Response(status=200)


async def get_v3_projects_id_environments(request: web.Request, id, page=None, per_page=None) -> web.Response:
    """Get all environments of the project

    This feature was introduced in GitLab 8.11.

    :param id: The project ID
    :type id: str
    :param page: Current page number
    :type page: int
    :param per_page: Number of items per page
    :type per_page: int

    """
    return web.Response(status=200)


async def get_v3_projects_id_events(request: web.Request, id, page=None, per_page=None) -> web.Response:
    """Get events for a single project

    Get events for a single project

    :param id: The ID of a project
    :type id: str
    :param page: Current page number
    :type page: int
    :param per_page: Number of items per page
    :type per_page: int

    """
    return web.Response(status=200)


async def get_v3_projects_id_hooks(request: web.Request, id, page=None, per_page=None) -> web.Response:
    """Get project hooks

    Get project hooks

    :param id: The ID of a project
    :type id: str
    :param page: Current page number
    :type page: int
    :param per_page: Number of items per page
    :type per_page: int

    """
    return web.Response(status=200)


async def get_v3_projects_id_hooks_hook_id(request: web.Request, id, hook_id) -> web.Response:
    """Get a project hook

    Get a project hook

    :param id: The ID of a project
    :type id: str
    :param hook_id: The ID of a project hook
    :type hook_id: int

    """
    return web.Response(status=200)


async def get_v3_projects_id_issues(request: web.Request, id, state=None, iid=None, labels=None, milestone=None, order_by=None, sort=None, page=None, per_page=None) -> web.Response:
    """Get a list of project issues

    Get a list of project issues

    :param id: The ID of a project
    :type id: str
    :param state: Return opened, closed, or all issues
    :type state: str
    :param iid: Return the issue having the given &#x60;iid&#x60;
    :type iid: int
    :param labels: Comma-separated list of label names
    :type labels: str
    :param milestone: Return issues for a specific milestone
    :type milestone: str
    :param order_by: Return issues ordered by &#x60;created_at&#x60; or &#x60;updated_at&#x60; fields.
    :type order_by: str
    :param sort: Return issues sorted in &#x60;asc&#x60; or &#x60;desc&#x60; order.
    :type sort: str
    :param page: Current page number
    :type page: int
    :param per_page: Number of items per page
    :type per_page: int

    """
    return web.Response(status=200)


async def get_v3_projects_id_issues_issue_id(request: web.Request, id, issue_id) -> web.Response:
    """Get a single project issue

    Get a single project issue

    :param id: The ID of a project
    :type id: str
    :param issue_id: The ID of a project issue
    :type issue_id: int

    """
    return web.Response(status=200)


async def get_v3_projects_id_issues_issue_id_award_emoji(request: web.Request, id, issue_id, page=None, per_page=None) -> web.Response:
    """Get a list of project +awardable+ award emoji

    This feature was introduced in 8.9

    :param id: The ID of a project
    :type id: str
    :param issue_id: The ID of an Issue, Merge Request or Snippet
    :type issue_id: int
    :param page: Current page number
    :type page: int
    :param per_page: Number of items per page
    :type per_page: int

    """
    return web.Response(status=200)


async def get_v3_projects_id_issues_issue_id_award_emoji_award_id(request: web.Request, award_id, id, issue_id) -> web.Response:
    """Get a specific award emoji

    This feature was introduced in 8.9

    :param award_id: The ID of the award
    :type award_id: int
    :param id: 
    :type id: int
    :param issue_id: 
    :type issue_id: int

    """
    return web.Response(status=200)


async def get_v3_projects_id_issues_issue_id_notes_note_id_award_emoji(request: web.Request, id, issue_id, note_id, page=None, per_page=None) -> web.Response:
    """Get a list of project +awardable+ award emoji

    This feature was introduced in 8.9

    :param id: 
    :type id: int
    :param issue_id: 
    :type issue_id: int
    :param note_id: 
    :type note_id: int
    :param page: Current page number
    :type page: int
    :param per_page: Number of items per page
    :type per_page: int

    """
    return web.Response(status=200)


async def get_v3_projects_id_issues_issue_id_notes_note_id_award_emoji_award_id(request: web.Request, award_id, id, issue_id, note_id) -> web.Response:
    """Get a specific award emoji

    This feature was introduced in 8.9

    :param award_id: The ID of the award
    :type award_id: int
    :param id: 
    :type id: int
    :param issue_id: 
    :type issue_id: int
    :param note_id: 
    :type note_id: int

    """
    return web.Response(status=200)


async def get_v3_projects_id_issues_issue_id_time_stats(request: web.Request, id, issue_id) -> web.Response:
    """Show time stats for a project issue

    Show time stats for a project issue

    :param id: The ID of a project
    :type id: str
    :param issue_id: The ID of a project issue
    :type issue_id: int

    """
    return web.Response(status=200)


async def get_v3_projects_id_issues_noteable_id_notes(request: web.Request, id, noteable_id, page=None, per_page=None) -> web.Response:
    """Get a list of project +noteable+ notes

    Get a list of project +noteable+ notes

    :param id: The ID of a project
    :type id: str
    :param noteable_id: The ID of the noteable
    :type noteable_id: int
    :param page: Current page number
    :type page: int
    :param per_page: Number of items per page
    :type per_page: int

    """
    return web.Response(status=200)


async def get_v3_projects_id_issues_noteable_id_notes_note_id(request: web.Request, id, note_id, noteable_id) -> web.Response:
    """Get a single +noteable+ note

    Get a single +noteable+ note

    :param id: The ID of a project
    :type id: str
    :param note_id: The ID of a note
    :type note_id: int
    :param noteable_id: The ID of the noteable
    :type noteable_id: int

    """
    return web.Response(status=200)


async def get_v3_projects_id_keys(request: web.Request, id) -> web.Response:
    """Get a specific project&#39;s deploy keys

    Get a specific project&#39;s deploy keys

    :param id: The ID of the project
    :type id: str

    """
    return web.Response(status=200)


async def get_v3_projects_id_keys_key_id(request: web.Request, id, key_id) -> web.Response:
    """Get single deploy key

    Get single deploy key

    :param id: The ID of the project
    :type id: str
    :param key_id: The ID of the deploy key
    :type key_id: int

    """
    return web.Response(status=200)


async def get_v3_projects_id_labels(request: web.Request, id) -> web.Response:
    """Get all labels of the project

    Get all labels of the project

    :param id: The ID of a project
    :type id: str

    """
    return web.Response(status=200)


async def get_v3_projects_id_members(request: web.Request, id, query=None, page=None, per_page=None) -> web.Response:
    """Gets a list of group or project members viewable by the authenticated user.

    Gets a list of group or project members viewable by the authenticated user.

    :param id: The project ID
    :type id: str
    :param query: A query string to search for members
    :type query: str
    :param page: Current page number
    :type page: int
    :param per_page: Number of items per page
    :type per_page: int

    """
    return web.Response(status=200)


async def get_v3_projects_id_members_user_id(request: web.Request, id, user_id) -> web.Response:
    """Gets a member of a group or project.

    Gets a member of a group or project.

    :param id: The project ID
    :type id: str
    :param user_id: The user ID of the member
    :type user_id: int

    """
    return web.Response(status=200)


async def get_v3_projects_id_merge_request_merge_request_id(request: web.Request, id, merge_request_id) -> web.Response:
    """Get a single merge request

    This endpoint is deprecated and will be removed in GitLab 9.0.

    :param id: The ID of a project
    :type id: str
    :param merge_request_id: The ID of a merge request
    :type merge_request_id: int

    """
    return web.Response(status=200)


async def get_v3_projects_id_merge_request_merge_request_id_changes(request: web.Request, id, merge_request_id) -> web.Response:
    """Show the merge request changes

    Show the merge request changes

    :param id: The ID of a project
    :type id: str
    :param merge_request_id: 
    :type merge_request_id: int

    """
    return web.Response(status=200)


async def get_v3_projects_id_merge_request_merge_request_id_closes_issues(request: web.Request, id, merge_request_id, page=None, per_page=None) -> web.Response:
    """List issues that will be closed on merge

    List issues that will be closed on merge

    :param id: The ID of a project
    :type id: str
    :param merge_request_id: 
    :type merge_request_id: int
    :param page: Current page number
    :type page: int
    :param per_page: Number of items per page
    :type per_page: int

    """
    return web.Response(status=200)


async def get_v3_projects_id_merge_request_merge_request_id_comments(request: web.Request, id, merge_request_id, page=None, per_page=None) -> web.Response:
    """Get the comments of a merge request

    Duplicate. DEPRECATED and WILL BE REMOVED in 9.0

    :param id: The ID of a project
    :type id: str
    :param merge_request_id: 
    :type merge_request_id: int
    :param page: Current page number
    :type page: int
    :param per_page: Number of items per page
    :type per_page: int

    """
    return web.Response(status=200)


async def get_v3_projects_id_merge_request_merge_request_id_commits(request: web.Request, id, merge_request_id) -> web.Response:
    """Get the commits of a merge request

    Get the commits of a merge request

    :param id: The ID of a project
    :type id: str
    :param merge_request_id: 
    :type merge_request_id: int

    """
    return web.Response(status=200)


async def get_v3_projects_id_merge_requests(request: web.Request, id, state=None, order_by=None, sort=None, page=None, per_page=None, iid=None) -> web.Response:
    """List merge requests

    List merge requests

    :param id: The ID of a project
    :type id: str
    :param state: Return opened, closed, merged, or all merge requests
    :type state: str
    :param order_by: Return merge requests ordered by &#x60;created_at&#x60; or &#x60;updated_at&#x60; fields.
    :type order_by: str
    :param sort: Return merge requests sorted in &#x60;asc&#x60; or &#x60;desc&#x60; order.
    :type sort: str
    :param page: Current page number
    :type page: int
    :param per_page: Number of items per page
    :type per_page: int
    :param iid: The IID of the merge requests
    :type iid: List[int]

    """
    return web.Response(status=200)


async def get_v3_projects_id_merge_requests_merge_request_id(request: web.Request, id, merge_request_id) -> web.Response:
    """Get a single merge request

    Get a single merge request

    :param id: The ID of a project
    :type id: str
    :param merge_request_id: 
    :type merge_request_id: int

    """
    return web.Response(status=200)


async def get_v3_projects_id_merge_requests_merge_request_id_award_emoji(request: web.Request, id, merge_request_id, page=None, per_page=None) -> web.Response:
    """Get a list of project +awardable+ award emoji

    This feature was introduced in 8.9

    :param id: The ID of a project
    :type id: str
    :param merge_request_id: The ID of an Issue, Merge Request or Snippet
    :type merge_request_id: int
    :param page: Current page number
    :type page: int
    :param per_page: Number of items per page
    :type per_page: int

    """
    return web.Response(status=200)


async def get_v3_projects_id_merge_requests_merge_request_id_award_emoji_award_id(request: web.Request, award_id, id, merge_request_id) -> web.Response:
    """Get a specific award emoji

    This feature was introduced in 8.9

    :param award_id: The ID of the award
    :type award_id: int
    :param id: 
    :type id: int
    :param merge_request_id: 
    :type merge_request_id: int

    """
    return web.Response(status=200)


async def get_v3_projects_id_merge_requests_merge_request_id_changes(request: web.Request, id, merge_request_id) -> web.Response:
    """Show the merge request changes

    Show the merge request changes

    :param id: The ID of a project
    :type id: str
    :param merge_request_id: 
    :type merge_request_id: int

    """
    return web.Response(status=200)


async def get_v3_projects_id_merge_requests_merge_request_id_closes_issues(request: web.Request, id, merge_request_id, page=None, per_page=None) -> web.Response:
    """List issues that will be closed on merge

    List issues that will be closed on merge

    :param id: The ID of a project
    :type id: str
    :param merge_request_id: 
    :type merge_request_id: int
    :param page: Current page number
    :type page: int
    :param per_page: Number of items per page
    :type per_page: int

    """
    return web.Response(status=200)


async def get_v3_projects_id_merge_requests_merge_request_id_comments(request: web.Request, id, merge_request_id, page=None, per_page=None) -> web.Response:
    """Get the comments of a merge request

    Duplicate. DEPRECATED and WILL BE REMOVED in 9.0

    :param id: The ID of a project
    :type id: str
    :param merge_request_id: 
    :type merge_request_id: int
    :param page: Current page number
    :type page: int
    :param per_page: Number of items per page
    :type per_page: int

    """
    return web.Response(status=200)


async def get_v3_projects_id_merge_requests_merge_request_id_commits(request: web.Request, id, merge_request_id) -> web.Response:
    """Get the commits of a merge request

    Get the commits of a merge request

    :param id: The ID of a project
    :type id: str
    :param merge_request_id: 
    :type merge_request_id: int

    """
    return web.Response(status=200)


async def get_v3_projects_id_merge_requests_merge_request_id_notes_note_id_award_emoji(request: web.Request, id, merge_request_id, note_id, page=None, per_page=None) -> web.Response:
    """Get a list of project +awardable+ award emoji

    This feature was introduced in 8.9

    :param id: 
    :type id: int
    :param merge_request_id: 
    :type merge_request_id: int
    :param note_id: 
    :type note_id: int
    :param page: Current page number
    :type page: int
    :param per_page: Number of items per page
    :type per_page: int

    """
    return web.Response(status=200)


async def get_v3_projects_id_merge_requests_merge_request_id_notes_note_id_award_emoji_award_id(request: web.Request, award_id, id, merge_request_id, note_id) -> web.Response:
    """Get a specific award emoji

    This feature was introduced in 8.9

    :param award_id: The ID of the award
    :type award_id: int
    :param id: 
    :type id: int
    :param merge_request_id: 
    :type merge_request_id: int
    :param note_id: 
    :type note_id: int

    """
    return web.Response(status=200)


async def get_v3_projects_id_merge_requests_merge_request_id_time_stats(request: web.Request, id, merge_request_id) -> web.Response:
    """Show time stats for a project merge_request

    Show time stats for a project merge_request

    :param id: The ID of a project
    :type id: str
    :param merge_request_id: The ID of a project merge_request
    :type merge_request_id: int

    """
    return web.Response(status=200)


async def get_v3_projects_id_merge_requests_merge_request_id_versions(request: web.Request, id, merge_request_id) -> web.Response:
    """Get a list of merge request diff versions

    This feature was introduced in GitLab 8.12.

    :param id: The ID of a project
    :type id: str
    :param merge_request_id: The ID of a merge request
    :type merge_request_id: int

    """
    return web.Response(status=200)


async def get_v3_projects_id_merge_requests_merge_request_id_versions_version_id(request: web.Request, id, merge_request_id, version_id) -> web.Response:
    """Get a single merge request diff version

    This feature was introduced in GitLab 8.12.

    :param id: The ID of a project
    :type id: str
    :param merge_request_id: The ID of a merge request
    :type merge_request_id: int
    :param version_id: The ID of a merge request diff version
    :type version_id: int

    """
    return web.Response(status=200)


async def get_v3_projects_id_merge_requests_noteable_id_notes(request: web.Request, id, noteable_id, page=None, per_page=None) -> web.Response:
    """Get a list of project +noteable+ notes

    Get a list of project +noteable+ notes

    :param id: The ID of a project
    :type id: str
    :param noteable_id: The ID of the noteable
    :type noteable_id: int
    :param page: Current page number
    :type page: int
    :param per_page: Number of items per page
    :type per_page: int

    """
    return web.Response(status=200)


async def get_v3_projects_id_merge_requests_noteable_id_notes_note_id(request: web.Request, id, note_id, noteable_id) -> web.Response:
    """Get a single +noteable+ note

    Get a single +noteable+ note

    :param id: The ID of a project
    :type id: str
    :param note_id: The ID of a note
    :type note_id: int
    :param noteable_id: The ID of the noteable
    :type noteable_id: int

    """
    return web.Response(status=200)


async def get_v3_projects_id_milestones(request: web.Request, id, state=None, page=None, per_page=None, iid=None) -> web.Response:
    """Get a list of project milestones

    Get a list of project milestones

    :param id: The ID of a project
    :type id: str
    :param state: Return \&quot;active\&quot;, \&quot;closed\&quot;, or \&quot;all\&quot; milestones
    :type state: str
    :param page: Current page number
    :type page: int
    :param per_page: Number of items per page
    :type per_page: int
    :param iid: The IID of the milestone
    :type iid: List[int]

    """
    return web.Response(status=200)


async def get_v3_projects_id_milestones_milestone_id(request: web.Request, id, milestone_id) -> web.Response:
    """Get a single project milestone

    Get a single project milestone

    :param id: The ID of a project
    :type id: str
    :param milestone_id: The ID of a project milestone
    :type milestone_id: int

    """
    return web.Response(status=200)


async def get_v3_projects_id_milestones_milestone_id_issues(request: web.Request, id, milestone_id, page=None, per_page=None) -> web.Response:
    """Get all issues for a single project milestone

    Get all issues for a single project milestone

    :param id: The ID of a project
    :type id: str
    :param milestone_id: The ID of a project milestone
    :type milestone_id: int
    :param page: Current page number
    :type page: int
    :param per_page: Number of items per page
    :type per_page: int

    """
    return web.Response(status=200)


async def get_v3_projects_id_notification_settings(request: web.Request, id) -> web.Response:
    """Get project level notification level settings, defaults to Global

    This feature was introduced in GitLab 8.12

    :param id: The group ID or project ID or project NAMESPACE/PROJECT_NAME
    :type id: str

    """
    return web.Response(status=200)


async def get_v3_projects_id_pipelines(request: web.Request, id, page=None, per_page=None, scope=None) -> web.Response:
    """Get all Pipelines of the project

    This feature was introduced in GitLab 8.11.

    :param id: The project ID
    :type id: str
    :param page: Current page number
    :type page: int
    :param per_page: Number of items per page
    :type per_page: int
    :param scope: Either running, branches, or tags
    :type scope: str

    """
    return web.Response(status=200)


async def get_v3_projects_id_pipelines_pipeline_id(request: web.Request, id, pipeline_id) -> web.Response:
    """Gets a specific pipeline for the project

    This feature was introduced in GitLab 8.11

    :param id: The project ID
    :type id: str
    :param pipeline_id: The pipeline ID
    :type pipeline_id: int

    """
    return web.Response(status=200)


async def get_v3_projects_id_repository_archive(request: web.Request, id, sha=None, format=None) -> web.Response:
    """Get an archive of the repository

    Get an archive of the repository

    :param id: The ID of a project
    :type id: str
    :param sha: The commit sha of the archive to be downloaded
    :type sha: str
    :param format: The archive format
    :type format: str

    """
    return web.Response(status=200)


async def get_v3_projects_id_repository_blobs_sha(request: web.Request, id, sha, filepath) -> web.Response:
    """Get a raw file contents

    Get a raw file contents

    :param id: The ID of a project
    :type id: str
    :param sha: The commit, branch name, or tag name
    :type sha: str
    :param filepath: The path to the file to display
    :type filepath: str

    """
    return web.Response(status=200)


async def get_v3_projects_id_repository_branches(request: web.Request, id) -> web.Response:
    """Get a project repository branches

    Get a project repository branches

    :param id: The ID of a project
    :type id: str

    """
    return web.Response(status=200)


async def get_v3_projects_id_repository_branches_branch(request: web.Request, id, branch) -> web.Response:
    """Get a single branch

    Get a single branch

    :param id: The ID of a project
    :type id: str
    :param branch: The name of the branch
    :type branch: str

    """
    return web.Response(status=200)


async def get_v3_projects_id_repository_commits(request: web.Request, id, ref_name=None, since=None, until=None, page=None, per_page=None, path=None) -> web.Response:
    """Get a project repository commits

    Get a project repository commits

    :param id: The ID of a project
    :type id: str
    :param ref_name: The name of a repository branch or tag, if not given the default branch is used
    :type ref_name: str
    :param since: Only commits after or in this date will be returned
    :type since: str
    :param until: Only commits before or in this date will be returned
    :type until: str
    :param page: The page for pagination
    :type page: int
    :param per_page: The number of results per page
    :type per_page: int
    :param path: The file path
    :type path: str

    """
    return web.Response(status=200)


async def get_v3_projects_id_repository_commits_sha(request: web.Request, id, sha) -> web.Response:
    """Get a specific commit of a project

    Get a specific commit of a project

    :param id: The ID of a project
    :type id: str
    :param sha: A commit sha, or the name of a branch or tag
    :type sha: str

    """
    return web.Response(status=200)


async def get_v3_projects_id_repository_commits_sha_blob(request: web.Request, id, sha, filepath) -> web.Response:
    """Get a raw file contents

    Get a raw file contents

    :param id: The ID of a project
    :type id: str
    :param sha: The commit, branch name, or tag name
    :type sha: str
    :param filepath: The path to the file to display
    :type filepath: str

    """
    return web.Response(status=200)


async def get_v3_projects_id_repository_commits_sha_builds(request: web.Request, id, sha, scope=None, page=None, per_page=None) -> web.Response:
    """Get builds for a specific commit of a project

    Get builds for a specific commit of a project

    :param id: The ID of a project
    :type id: str
    :param sha: The SHA id of a commit
    :type sha: str
    :param scope: The scope of builds to show
    :type scope: str
    :param page: Current page number
    :type page: int
    :param per_page: Number of items per page
    :type per_page: int

    """
    return web.Response(status=200)


async def get_v3_projects_id_repository_commits_sha_comments(request: web.Request, id, sha, page=None, per_page=None) -> web.Response:
    """Get a commit&#39;s comments

    Get a commit&#39;s comments

    :param id: The ID of a project
    :type id: str
    :param sha: A commit sha, or the name of a branch or tag
    :type sha: str
    :param page: Current page number
    :type page: int
    :param per_page: Number of items per page
    :type per_page: int

    """
    return web.Response(status=200)


async def get_v3_projects_id_repository_commits_sha_diff(request: web.Request, id, sha) -> web.Response:
    """Get the diff for a specific commit of a project

    Get the diff for a specific commit of a project

    :param id: The ID of a project
    :type id: str
    :param sha: A commit sha, or the name of a branch or tag
    :type sha: str

    """
    return web.Response(status=200)


async def get_v3_projects_id_repository_commits_sha_statuses(request: web.Request, id, sha, ref=None, stage=None, name=None, all=None, page=None, per_page=None) -> web.Response:
    """Get a commit&#39;s statuses

    Get a commit&#39;s statuses

    :param id: The ID of a project
    :type id: str
    :param sha: The commit hash
    :type sha: str
    :param ref: The ref
    :type ref: str
    :param stage: The stage
    :type stage: str
    :param name: The name
    :type name: str
    :param all: Show all statuses, default: false
    :type all: str
    :param page: Current page number
    :type page: int
    :param per_page: Number of items per page
    :type per_page: int

    """
    return web.Response(status=200)


async def get_v3_projects_id_repository_compare(request: web.Request, id, _from, to) -> web.Response:
    """Compare two branches, tags, or commits

    Compare two branches, tags, or commits

    :param id: The ID of a project
    :type id: str
    :param _from: The commit, branch name, or tag name to start comparison
    :type _from: str
    :param to: The commit, branch name, or tag name to stop comparison
    :type to: str

    """
    return web.Response(status=200)


async def get_v3_projects_id_repository_contributors(request: web.Request, id) -> web.Response:
    """Get repository contributors

    Get repository contributors

    :param id: The ID of a project
    :type id: str

    """
    return web.Response(status=200)


async def get_v3_projects_id_repository_files(request: web.Request, id, file_path, ref) -> web.Response:
    """Get a file from repository

    Get a file from repository

    :param id: The project ID
    :type id: str
    :param file_path: The path to the file. Ex. lib/class.rb
    :type file_path: str
    :param ref: The name of branch, tag, or commit
    :type ref: str

    """
    return web.Response(status=200)


async def get_v3_projects_id_repository_raw_blobs_sha(request: web.Request, id, sha) -> web.Response:
    """Get a raw blob contents by blob sha

    Get a raw blob contents by blob sha

    :param id: The ID of a project
    :type id: str
    :param sha: The commit, branch name, or tag name
    :type sha: str

    """
    return web.Response(status=200)


async def get_v3_projects_id_repository_tags(request: web.Request, id) -> web.Response:
    """Get a project repository tags

    Get a project repository tags

    :param id: The ID of a project
    :type id: str

    """
    return web.Response(status=200)


async def get_v3_projects_id_repository_tags_tag_name(request: web.Request, id, tag_name) -> web.Response:
    """Get a single repository tag

    Get a single repository tag

    :param id: The ID of a project
    :type id: str
    :param tag_name: The name of the tag
    :type tag_name: str

    """
    return web.Response(status=200)


async def get_v3_projects_id_repository_tree(request: web.Request, id, ref_name=None, path=None, recursive=None) -> web.Response:
    """Get a project repository tree

    Get a project repository tree

    :param id: The ID of a project
    :type id: str
    :param ref_name: The name of a repository branch or tag, if not given the default branch is used
    :type ref_name: str
    :param path: The path of the tree
    :type path: str
    :param recursive: Used to get a recursive tree
    :type recursive: bool

    """
    return web.Response(status=200)


async def get_v3_projects_id_runners(request: web.Request, id, scope=None, page=None, per_page=None) -> web.Response:
    """Get runners available for project

    Get runners available for project

    :param id: The ID of a project
    :type id: str
    :param scope: The scope of specific runners to show
    :type scope: str
    :param page: Current page number
    :type page: int
    :param per_page: Number of items per page
    :type per_page: int

    """
    return web.Response(status=200)


async def get_v3_projects_id_services_service_slug(request: web.Request, service_slug, id) -> web.Response:
    """Get the service settings for project

    Get the service settings for project

    :param service_slug: The name of the service
    :type service_slug: str
    :param id: 
    :type id: int

    """
    return web.Response(status=200)


async def get_v3_projects_id_snippets(request: web.Request, id, page=None, per_page=None) -> web.Response:
    """Get all project snippets

    Get all project snippets

    :param id: The ID of a project
    :type id: str
    :param page: Current page number
    :type page: int
    :param per_page: Number of items per page
    :type per_page: int

    """
    return web.Response(status=200)


async def get_v3_projects_id_snippets_noteable_id_notes(request: web.Request, id, noteable_id, page=None, per_page=None) -> web.Response:
    """Get a list of project +noteable+ notes

    Get a list of project +noteable+ notes

    :param id: The ID of a project
    :type id: str
    :param noteable_id: The ID of the noteable
    :type noteable_id: int
    :param page: Current page number
    :type page: int
    :param per_page: Number of items per page
    :type per_page: int

    """
    return web.Response(status=200)


async def get_v3_projects_id_snippets_noteable_id_notes_note_id(request: web.Request, id, note_id, noteable_id) -> web.Response:
    """Get a single +noteable+ note

    Get a single +noteable+ note

    :param id: The ID of a project
    :type id: str
    :param note_id: The ID of a note
    :type note_id: int
    :param noteable_id: The ID of the noteable
    :type noteable_id: int

    """
    return web.Response(status=200)


async def get_v3_projects_id_snippets_snippet_id(request: web.Request, id, snippet_id) -> web.Response:
    """Get a single project snippet

    Get a single project snippet

    :param id: The ID of a project
    :type id: str
    :param snippet_id: The ID of a project snippet
    :type snippet_id: int

    """
    return web.Response(status=200)


async def get_v3_projects_id_snippets_snippet_id_award_emoji(request: web.Request, id, snippet_id, page=None, per_page=None) -> web.Response:
    """Get a list of project +awardable+ award emoji

    This feature was introduced in 8.9

    :param id: The ID of a project
    :type id: str
    :param snippet_id: The ID of an Issue, Merge Request or Snippet
    :type snippet_id: int
    :param page: Current page number
    :type page: int
    :param per_page: Number of items per page
    :type per_page: int

    """
    return web.Response(status=200)


async def get_v3_projects_id_snippets_snippet_id_award_emoji_award_id(request: web.Request, award_id, id, snippet_id) -> web.Response:
    """Get a specific award emoji

    This feature was introduced in 8.9

    :param award_id: The ID of the award
    :type award_id: int
    :param id: 
    :type id: int
    :param snippet_id: 
    :type snippet_id: int

    """
    return web.Response(status=200)


async def get_v3_projects_id_snippets_snippet_id_notes_note_id_award_emoji(request: web.Request, id, snippet_id, note_id, page=None, per_page=None) -> web.Response:
    """Get a list of project +awardable+ award emoji

    This feature was introduced in 8.9

    :param id: 
    :type id: int
    :param snippet_id: 
    :type snippet_id: int
    :param note_id: 
    :type note_id: int
    :param page: Current page number
    :type page: int
    :param per_page: Number of items per page
    :type per_page: int

    """
    return web.Response(status=200)


async def get_v3_projects_id_snippets_snippet_id_notes_note_id_award_emoji_award_id(request: web.Request, award_id, id, snippet_id, note_id) -> web.Response:
    """Get a specific award emoji

    This feature was introduced in 8.9

    :param award_id: The ID of the award
    :type award_id: int
    :param id: 
    :type id: int
    :param snippet_id: 
    :type snippet_id: int
    :param note_id: 
    :type note_id: int

    """
    return web.Response(status=200)


async def get_v3_projects_id_snippets_snippet_id_raw(request: web.Request, id, snippet_id) -> web.Response:
    """Get a raw project snippet

    Get a raw project snippet

    :param id: The ID of a project
    :type id: str
    :param snippet_id: The ID of a project snippet
    :type snippet_id: int

    """
    return web.Response(status=200)


async def get_v3_projects_id_triggers(request: web.Request, id, page=None, per_page=None) -> web.Response:
    """Get triggers list

    Get triggers list

    :param id: The ID of a project
    :type id: str
    :param page: Current page number
    :type page: int
    :param per_page: Number of items per page
    :type per_page: int

    """
    return web.Response(status=200)


async def get_v3_projects_id_triggers_token(request: web.Request, id, token) -> web.Response:
    """Get specific trigger of a project

    Get specific trigger of a project

    :param id: The ID of a project
    :type id: str
    :param token: The unique token of trigger
    :type token: str

    """
    return web.Response(status=200)


async def get_v3_projects_id_users(request: web.Request, id, search=None, page=None, per_page=None) -> web.Response:
    """Get the users list of a project

    Get the users list of a project

    :param id: The ID of a project
    :type id: str
    :param search: Return list of users matching the search criteria
    :type search: str
    :param page: Current page number
    :type page: int
    :param per_page: Number of items per page
    :type per_page: int

    """
    return web.Response(status=200)


async def get_v3_projects_id_variables(request: web.Request, id, page=None, per_page=None) -> web.Response:
    """Get project variables

    Get project variables

    :param id: The ID of a project
    :type id: str
    :param page: Current page number
    :type page: int
    :param per_page: Number of items per page
    :type per_page: int

    """
    return web.Response(status=200)


async def get_v3_projects_id_variables_key(request: web.Request, id, key) -> web.Response:
    """Get a specific variable from a project

    Get a specific variable from a project

    :param id: The ID of a project
    :type id: str
    :param key: The key of the variable
    :type key: str

    """
    return web.Response(status=200)


async def get_v3_projects_owned(request: web.Request, order_by=None, sort=None, archived=None, visibility=None, search=None, page=None, per_page=None, simple=None, statistics=None) -> web.Response:
    """Get an owned projects list for authenticated user

    Get an owned projects list for authenticated user

    :param order_by: Return projects ordered by field
    :type order_by: str
    :param sort: Return projects sorted in ascending and descending order
    :type sort: str
    :param archived: Limit by archived status
    :type archived: bool
    :param visibility: Limit by visibility
    :type visibility: str
    :param search: Return list of authorized projects matching the search criteria
    :type search: str
    :param page: Current page number
    :type page: int
    :param per_page: Number of items per page
    :type per_page: int
    :param simple: Return only the ID, URL, name, and path of each project
    :type simple: bool
    :param statistics: Include project statistics
    :type statistics: bool

    """
    return web.Response(status=200)


async def get_v3_projects_search_query(request: web.Request, query, order_by=None, sort=None, page=None, per_page=None) -> web.Response:
    """Search for projects the current user has access to

    Search for projects the current user has access to

    :param query: The project name to be searched
    :type query: str
    :param order_by: Return projects ordered by field
    :type order_by: str
    :param sort: Return projects sorted in ascending and descending order
    :type sort: str
    :param page: Current page number
    :type page: int
    :param per_page: Number of items per page
    :type per_page: int

    """
    return web.Response(status=200)


async def get_v3_projects_starred(request: web.Request, order_by=None, sort=None, archived=None, visibility=None, search=None, page=None, per_page=None, simple=None) -> web.Response:
    """Gets starred project for the authenticated user

    Gets starred project for the authenticated user

    :param order_by: Return projects ordered by field
    :type order_by: str
    :param sort: Return projects sorted in ascending and descending order
    :type sort: str
    :param archived: Limit by archived status
    :type archived: bool
    :param visibility: Limit by visibility
    :type visibility: str
    :param search: Return list of authorized projects matching the search criteria
    :type search: str
    :param page: Current page number
    :type page: int
    :param per_page: Number of items per page
    :type per_page: int
    :param simple: Return only the ID, URL, name, and path of each project
    :type simple: bool

    """
    return web.Response(status=200)


async def get_v3_projects_visible(request: web.Request, order_by=None, sort=None, archived=None, visibility=None, search=None, page=None, per_page=None, simple=None) -> web.Response:
    """Get a list of visible projects for authenticated user

    Get a list of visible projects for authenticated user

    :param order_by: Return projects ordered by field
    :type order_by: str
    :param sort: Return projects sorted in ascending and descending order
    :type sort: str
    :param archived: Limit by archived status
    :type archived: bool
    :param visibility: Limit by visibility
    :type visibility: str
    :param search: Return list of authorized projects matching the search criteria
    :type search: str
    :param page: Current page number
    :type page: int
    :param per_page: Number of items per page
    :type per_page: int
    :param simple: Return only the ID, URL, name, and path of each project
    :type simple: bool

    """
    return web.Response(status=200)


async def post_v3_projects(request: web.Request, body) -> web.Response:
    """Create new project

    Create new project

    :param body: 
    :type body: dict | bytes

    """
    body = PostV3ProjectsRequest.from_dict(body)
    return web.Response(status=200)


async def post_v3_projects_fork_id(request: web.Request, id, body=None) -> web.Response:
    """Fork new project for the current user or provided namespace.

    Fork new project for the current user or provided namespace.

    :param id: The ID of a project
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PostV3ProjectsForkIdRequest.from_dict(body)
    return web.Response(status=200)


async def post_v3_projects_id_access_requests(request: web.Request, id) -> web.Response:
    """Requests access for the authenticated user to a project.

    This feature was introduced in GitLab 8.11.

    :param id: The project ID
    :type id: str

    """
    return web.Response(status=200)


async def post_v3_projects_id_archive(request: web.Request, id) -> web.Response:
    """Archive a project

    Archive a project

    :param id: The ID of a project
    :type id: str

    """
    return web.Response(status=200)


async def post_v3_projects_id_boards_board_id_lists(request: web.Request, id, board_id, body) -> web.Response:
    """Create a new board list

    This feature was introduced in 8.13

    :param id: The ID of a project
    :type id: str
    :param board_id: The ID of a board
    :type board_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PostV3ProjectsIdBoardsBoardIdListsRequest.from_dict(body)
    return web.Response(status=200)


async def post_v3_projects_id_builds_build_id_artifacts_keep(request: web.Request, id, build_id) -> web.Response:
    """Keep the artifacts to prevent them from being deleted

    Keep the artifacts to prevent them from being deleted

    :param id: The ID of a project
    :type id: str
    :param build_id: The ID of a build
    :type build_id: int

    """
    return web.Response(status=200)


async def post_v3_projects_id_builds_build_id_cancel(request: web.Request, id, build_id) -> web.Response:
    """Cancel a specific build of a project

    Cancel a specific build of a project

    :param id: The ID of a project
    :type id: str
    :param build_id: The ID of a build
    :type build_id: int

    """
    return web.Response(status=200)


async def post_v3_projects_id_builds_build_id_erase(request: web.Request, id, build_id) -> web.Response:
    """Erase build (remove artifacts and build trace)

    Erase build (remove artifacts and build trace)

    :param id: The ID of a project
    :type id: str
    :param build_id: The ID of a build
    :type build_id: int

    """
    return web.Response(status=200)


async def post_v3_projects_id_builds_build_id_play(request: web.Request, id, build_id) -> web.Response:
    """Trigger a manual build

    This feature was added in GitLab 8.11

    :param id: The ID of a project
    :type id: str
    :param build_id: The ID of a Build
    :type build_id: int

    """
    return web.Response(status=200)


async def post_v3_projects_id_builds_build_id_retry(request: web.Request, id, build_id) -> web.Response:
    """Retry a specific build of a project

    Retry a specific build of a project

    :param id: The ID of a project
    :type id: str
    :param build_id: The ID of a build
    :type build_id: int

    """
    return web.Response(status=200)


async def post_v3_projects_id_deploy_keys(request: web.Request, id, body) -> web.Response:
    """Add new deploy key to currently authenticated user

    Add new deploy key to currently authenticated user

    :param id: The ID of the project
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PostV3ProjectsIdDeployKeysRequest.from_dict(body)
    return web.Response(status=200)


async def post_v3_projects_id_deploy_keys_key_id_enable(request: web.Request, id, key_id) -> web.Response:
    """Enable a deploy key for a project

    This feature was added in GitLab 8.11

    :param id: The ID of the project
    :type id: str
    :param key_id: The ID of the deploy key
    :type key_id: int

    """
    return web.Response(status=200)


async def post_v3_projects_id_environments(request: web.Request, id, body) -> web.Response:
    """Creates a new environment

    This feature was introduced in GitLab 8.11.

    :param id: The project ID
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PostV3ProjectsIdEnvironmentsRequest.from_dict(body)
    return web.Response(status=200)


async def post_v3_projects_id_fork_forked_from_id(request: web.Request, id, forked_from_id) -> web.Response:
    """Mark this project as forked from another

    Mark this project as forked from another

    :param id: The ID of a project
    :type id: str
    :param forked_from_id: The ID of the project it was forked from
    :type forked_from_id: str

    """
    return web.Response(status=200)


async def post_v3_projects_id_hooks(request: web.Request, id, body) -> web.Response:
    """Add hook to project

    Add hook to project

    :param id: The ID of a project
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PostV3ProjectsIdHooksRequest.from_dict(body)
    return web.Response(status=200)


async def post_v3_projects_id_issues(request: web.Request, id, body) -> web.Response:
    """Create a new project issue

    Create a new project issue

    :param id: The ID of a project
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PostV3ProjectsIdIssuesRequest.from_dict(body)
    return web.Response(status=200)


async def post_v3_projects_id_issues_issue_id_add_spent_time(request: web.Request, id, issue_id, body) -> web.Response:
    """Add spent time for a project issue

    Add spent time for a project issue

    :param id: The ID of a project
    :type id: str
    :param issue_id: The ID of a project issue
    :type issue_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PostV3ProjectsIdIssuesIssueIdAddSpentTimeRequest.from_dict(body)
    return web.Response(status=200)


async def post_v3_projects_id_issues_issue_id_award_emoji(request: web.Request, id, issue_id, body) -> web.Response:
    """Award a new Emoji

    This feature was introduced in 8.9

    :param id: 
    :type id: int
    :param issue_id: 
    :type issue_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PostV3ProjectsIdIssuesIssueIdAwardEmojiRequest.from_dict(body)
    return web.Response(status=200)


async def post_v3_projects_id_issues_issue_id_move(request: web.Request, id, issue_id, body) -> web.Response:
    """Move an existing issue

    Move an existing issue

    :param id: The ID of a project
    :type id: str
    :param issue_id: The ID of a project issue
    :type issue_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PostV3ProjectsIdIssuesIssueIdMoveRequest.from_dict(body)
    return web.Response(status=200)


async def post_v3_projects_id_issues_issue_id_notes_note_id_award_emoji(request: web.Request, id, issue_id, note_id, body) -> web.Response:
    """Award a new Emoji

    This feature was introduced in 8.9

    :param id: 
    :type id: int
    :param issue_id: 
    :type issue_id: int
    :param note_id: 
    :type note_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PostV3ProjectsIdIssuesIssueIdAwardEmojiRequest.from_dict(body)
    return web.Response(status=200)


async def post_v3_projects_id_issues_issue_id_reset_spent_time(request: web.Request, id, issue_id) -> web.Response:
    """Reset spent time for a project issue

    Reset spent time for a project issue

    :param id: The ID of a project
    :type id: str
    :param issue_id: The ID of a project issue
    :type issue_id: int

    """
    return web.Response(status=200)


async def post_v3_projects_id_issues_issue_id_reset_time_estimate(request: web.Request, id, issue_id) -> web.Response:
    """Reset the time estimate for a project issue

    Reset the time estimate for a project issue

    :param id: The ID of a project
    :type id: str
    :param issue_id: The ID of a project issue
    :type issue_id: int

    """
    return web.Response(status=200)


async def post_v3_projects_id_issues_issue_id_time_estimate(request: web.Request, id, issue_id, body) -> web.Response:
    """Set a time estimate for a project issue

    Set a time estimate for a project issue

    :param id: The ID of a project
    :type id: str
    :param issue_id: The ID of a project issue
    :type issue_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PostV3ProjectsIdIssuesIssueIdAddSpentTimeRequest.from_dict(body)
    return web.Response(status=200)


async def post_v3_projects_id_issues_issue_id_todo(request: web.Request, id, issue_id) -> web.Response:
    """Create a todo on an issuable

    Create a todo on an issuable

    :param id: The ID of a project
    :type id: str
    :param issue_id: The ID of an issuable
    :type issue_id: int

    """
    return web.Response(status=200)


async def post_v3_projects_id_issues_noteable_id_notes(request: web.Request, id, noteable_id, body) -> web.Response:
    """Create a new +noteable+ note

    Create a new +noteable+ note

    :param id: The ID of a project
    :type id: str
    :param noteable_id: The ID of the noteable
    :type noteable_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PostV3ProjectsIdIssuesNoteableIdNotesRequest.from_dict(body)
    return web.Response(status=200)


async def post_v3_projects_id_issues_subscribable_id_subscription(request: web.Request, id, subscribable_id) -> web.Response:
    """Subscribe to a resource

    Subscribe to a resource

    :param id: The ID of a project
    :type id: str
    :param subscribable_id: The ID of a resource
    :type subscribable_id: str

    """
    return web.Response(status=200)


async def post_v3_projects_id_keys(request: web.Request, id, body) -> web.Response:
    """Add new deploy key to currently authenticated user

    Add new deploy key to currently authenticated user

    :param id: The ID of the project
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PostV3ProjectsIdDeployKeysRequest.from_dict(body)
    return web.Response(status=200)


async def post_v3_projects_id_keys_key_id_enable(request: web.Request, id, key_id) -> web.Response:
    """Enable a deploy key for a project

    This feature was added in GitLab 8.11

    :param id: The ID of the project
    :type id: str
    :param key_id: The ID of the deploy key
    :type key_id: int

    """
    return web.Response(status=200)


async def post_v3_projects_id_labels(request: web.Request, id, body) -> web.Response:
    """Create a new label

    Create a new label

    :param id: The ID of a project
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PostV3ProjectsIdLabelsRequest.from_dict(body)
    return web.Response(status=200)


async def post_v3_projects_id_labels_subscribable_id_subscription(request: web.Request, id, subscribable_id) -> web.Response:
    """Subscribe to a resource

    Subscribe to a resource

    :param id: The ID of a project
    :type id: str
    :param subscribable_id: The ID of a resource
    :type subscribable_id: str

    """
    return web.Response(status=200)


async def post_v3_projects_id_members(request: web.Request, id, body) -> web.Response:
    """Adds a member to a group or project.

    Adds a member to a group or project.

    :param id: The project ID
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PostV3GroupsIdMembersRequest.from_dict(body)
    return web.Response(status=200)


async def post_v3_projects_id_merge_request_merge_request_id_cancel_merge_when_build_succeeds(request: web.Request, id, merge_request_id) -> web.Response:
    """Cancel merge if \&quot;Merge When Pipeline Succeeds\&quot; is enabled

    Cancel merge if \&quot;Merge When Pipeline Succeeds\&quot; is enabled

    :param id: The ID of a project
    :type id: str
    :param merge_request_id: 
    :type merge_request_id: int

    """
    return web.Response(status=200)


async def post_v3_projects_id_merge_request_merge_request_id_comments(request: web.Request, id, merge_request_id, body) -> web.Response:
    """Post a comment to a merge request

    Duplicate. DEPRECATED and WILL BE REMOVED in 9.0

    :param id: The ID of a project
    :type id: str
    :param merge_request_id: 
    :type merge_request_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PostV3ProjectsIdMergeRequestMergeRequestIdCommentsRequest.from_dict(body)
    return web.Response(status=200)


async def post_v3_projects_id_merge_request_subscribable_id_subscription(request: web.Request, id, subscribable_id) -> web.Response:
    """Subscribe to a resource

    Subscribe to a resource

    :param id: The ID of a project
    :type id: str
    :param subscribable_id: The ID of a resource
    :type subscribable_id: str

    """
    return web.Response(status=200)


async def post_v3_projects_id_merge_requests(request: web.Request, id, body) -> web.Response:
    """Create a merge request

    Create a merge request

    :param id: The ID of a project
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PostV3ProjectsIdMergeRequestsRequest.from_dict(body)
    return web.Response(status=200)


async def post_v3_projects_id_merge_requests_merge_request_id_add_spent_time(request: web.Request, id, merge_request_id, body) -> web.Response:
    """Add spent time for a project merge_request

    Add spent time for a project merge_request

    :param id: The ID of a project
    :type id: str
    :param merge_request_id: The ID of a project merge_request
    :type merge_request_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PostV3ProjectsIdIssuesIssueIdAddSpentTimeRequest.from_dict(body)
    return web.Response(status=200)


async def post_v3_projects_id_merge_requests_merge_request_id_award_emoji(request: web.Request, id, merge_request_id, body) -> web.Response:
    """Award a new Emoji

    This feature was introduced in 8.9

    :param id: 
    :type id: int
    :param merge_request_id: 
    :type merge_request_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PostV3ProjectsIdIssuesIssueIdAwardEmojiRequest.from_dict(body)
    return web.Response(status=200)


async def post_v3_projects_id_merge_requests_merge_request_id_cancel_merge_when_build_succeeds(request: web.Request, id, merge_request_id) -> web.Response:
    """Cancel merge if \&quot;Merge When Pipeline Succeeds\&quot; is enabled

    Cancel merge if \&quot;Merge When Pipeline Succeeds\&quot; is enabled

    :param id: The ID of a project
    :type id: str
    :param merge_request_id: 
    :type merge_request_id: int

    """
    return web.Response(status=200)


async def post_v3_projects_id_merge_requests_merge_request_id_comments(request: web.Request, id, merge_request_id, body) -> web.Response:
    """Post a comment to a merge request

    Duplicate. DEPRECATED and WILL BE REMOVED in 9.0

    :param id: The ID of a project
    :type id: str
    :param merge_request_id: 
    :type merge_request_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PostV3ProjectsIdMergeRequestMergeRequestIdCommentsRequest.from_dict(body)
    return web.Response(status=200)


async def post_v3_projects_id_merge_requests_merge_request_id_notes_note_id_award_emoji(request: web.Request, id, merge_request_id, note_id, body) -> web.Response:
    """Award a new Emoji

    This feature was introduced in 8.9

    :param id: 
    :type id: int
    :param merge_request_id: 
    :type merge_request_id: int
    :param note_id: 
    :type note_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PostV3ProjectsIdIssuesIssueIdAwardEmojiRequest.from_dict(body)
    return web.Response(status=200)


async def post_v3_projects_id_merge_requests_merge_request_id_reset_spent_time(request: web.Request, id, merge_request_id) -> web.Response:
    """Reset spent time for a project merge_request

    Reset spent time for a project merge_request

    :param id: The ID of a project
    :type id: str
    :param merge_request_id: The ID of a project merge_request
    :type merge_request_id: int

    """
    return web.Response(status=200)


async def post_v3_projects_id_merge_requests_merge_request_id_reset_time_estimate(request: web.Request, id, merge_request_id) -> web.Response:
    """Reset the time estimate for a project merge_request

    Reset the time estimate for a project merge_request

    :param id: The ID of a project
    :type id: str
    :param merge_request_id: The ID of a project merge_request
    :type merge_request_id: int

    """
    return web.Response(status=200)


async def post_v3_projects_id_merge_requests_merge_request_id_time_estimate(request: web.Request, id, merge_request_id, body) -> web.Response:
    """Set a time estimate for a project merge_request

    Set a time estimate for a project merge_request

    :param id: The ID of a project
    :type id: str
    :param merge_request_id: The ID of a project merge_request
    :type merge_request_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PostV3ProjectsIdIssuesIssueIdAddSpentTimeRequest.from_dict(body)
    return web.Response(status=200)


async def post_v3_projects_id_merge_requests_merge_request_id_todo(request: web.Request, id, merge_request_id) -> web.Response:
    """Create a todo on an issuable

    Create a todo on an issuable

    :param id: The ID of a project
    :type id: str
    :param merge_request_id: The ID of an issuable
    :type merge_request_id: int

    """
    return web.Response(status=200)


async def post_v3_projects_id_merge_requests_noteable_id_notes(request: web.Request, id, noteable_id, body) -> web.Response:
    """Create a new +noteable+ note

    Create a new +noteable+ note

    :param id: The ID of a project
    :type id: str
    :param noteable_id: The ID of the noteable
    :type noteable_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PostV3ProjectsIdIssuesNoteableIdNotesRequest.from_dict(body)
    return web.Response(status=200)


async def post_v3_projects_id_merge_requests_subscribable_id_subscription(request: web.Request, id, subscribable_id) -> web.Response:
    """Subscribe to a resource

    Subscribe to a resource

    :param id: The ID of a project
    :type id: str
    :param subscribable_id: The ID of a resource
    :type subscribable_id: str

    """
    return web.Response(status=200)


async def post_v3_projects_id_milestones(request: web.Request, id, body) -> web.Response:
    """Create a new project milestone

    Create a new project milestone

    :param id: The ID of a project
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PostV3ProjectsIdMilestonesRequest.from_dict(body)
    return web.Response(status=200)


async def post_v3_projects_id_pipeline(request: web.Request, id, body) -> web.Response:
    """Create a new pipeline

    This feature was introduced in GitLab 8.14

    :param id: The project ID
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PostV3ProjectsIdPipelineRequest.from_dict(body)
    return web.Response(status=200)


async def post_v3_projects_id_pipelines_pipeline_id_cancel(request: web.Request, id, pipeline_id) -> web.Response:
    """Cancel all builds in the pipeline

    This feature was introduced in GitLab 8.11.

    :param id: The project ID
    :type id: str
    :param pipeline_id: The pipeline ID
    :type pipeline_id: int

    """
    return web.Response(status=200)


async def post_v3_projects_id_pipelines_pipeline_id_retry(request: web.Request, id, pipeline_id) -> web.Response:
    """Retry failed builds in the pipeline

    This feature was introduced in GitLab 8.11.

    :param id: The project ID
    :type id: str
    :param pipeline_id: The pipeline ID
    :type pipeline_id: int

    """
    return web.Response(status=200)


async def post_v3_projects_id_ref_reftrigger_builds(request: web.Request, id, ref, body) -> web.Response:
    """Trigger a GitLab project build

    Trigger a GitLab project build

    :param id: The ID of a project
    :type id: str
    :param ref: The commit sha or name of a branch or tag
    :type ref: str
    :param body: 
    :type body: dict | bytes

    """
    body = PostV3ProjectsIdRefRefTriggerBuildsRequest.from_dict(body)
    return web.Response(status=200)


async def post_v3_projects_id_repository_branches(request: web.Request, id, body) -> web.Response:
    """Create branch

    Create branch

    :param id: The ID of a project
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PostV3ProjectsIdRepositoryBranchesRequest.from_dict(body)
    return web.Response(status=200)


async def post_v3_projects_id_repository_commits(request: web.Request, id, body) -> web.Response:
    """Commit multiple file changes as one commit

    This feature was introduced in GitLab 8.13

    :param id: The ID of a project
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PostV3ProjectsIdRepositoryCommitsRequest.from_dict(body)
    return web.Response(status=200)


async def post_v3_projects_id_repository_commits_sha_cherry_pick(request: web.Request, id, sha, body) -> web.Response:
    """Cherry pick commit into a branch

    This feature was introduced in GitLab 8.15

    :param id: The ID of a project
    :type id: str
    :param sha: A commit sha to be cherry picked
    :type sha: str
    :param body: 
    :type body: dict | bytes

    """
    body = PostV3ProjectsIdRepositoryCommitsShaCherryPickRequest.from_dict(body)
    return web.Response(status=200)


async def post_v3_projects_id_repository_commits_sha_comments(request: web.Request, id, sha, body) -> web.Response:
    """Post comment to commit

    Post comment to commit

    :param id: The ID of a project
    :type id: str
    :param sha: The commit&#39;s SHA
    :type sha: str
    :param body: 
    :type body: dict | bytes

    """
    body = PostV3ProjectsIdRepositoryCommitsShaCommentsRequest.from_dict(body)
    return web.Response(status=200)


async def post_v3_projects_id_repository_files(request: web.Request, id, body) -> web.Response:
    """Create new file in repository

    Create new file in repository

    :param id: The project ID
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PutV3ProjectsIdRepositoryFilesRequest.from_dict(body)
    return web.Response(status=200)


async def post_v3_projects_id_repository_tags(request: web.Request, id, body) -> web.Response:
    """Create a new repository tag

    Create a new repository tag

    :param id: The ID of a project
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PostV3ProjectsIdRepositoryTagsRequest.from_dict(body)
    return web.Response(status=200)


async def post_v3_projects_id_repository_tags_tag_name_release(request: web.Request, id, tag_name, body) -> web.Response:
    """Add a release note to a tag

    Add a release note to a tag

    :param id: The ID of a project
    :type id: str
    :param tag_name: The name of the tag
    :type tag_name: str
    :param body: 
    :type body: dict | bytes

    """
    body = PutV3ProjectsIdRepositoryTagsTagNameReleaseRequest.from_dict(body)
    return web.Response(status=200)


async def post_v3_projects_id_runners(request: web.Request, id, body) -> web.Response:
    """Enable a runner for a project

    Enable a runner for a project

    :param id: The ID of a project
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PostV3ProjectsIdRunnersRequest.from_dict(body)
    return web.Response(status=200)


async def post_v3_projects_id_services_mattermost_slash_commands_trigger(request: web.Request, id, body) -> web.Response:
    """Trigger a slash command for mattermost-slash-commands

    Added in GitLab 8.13

    :param id: The ID of a project
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PutV3ProjectsIdServicesMattermostSlashCommandsRequest.from_dict(body)
    return web.Response(status=200)


async def post_v3_projects_id_services_slack_slash_commands_trigger(request: web.Request, id, body) -> web.Response:
    """Trigger a slash command for slack-slash-commands

    Added in GitLab 8.13

    :param id: The ID of a project
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PutV3ProjectsIdServicesSlackSlashCommandsRequest.from_dict(body)
    return web.Response(status=200)


async def post_v3_projects_id_share(request: web.Request, id, body) -> web.Response:
    """Share the project with a group

    Share the project with a group

    :param id: The ID of a project
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PostV3ProjectsIdShareRequest.from_dict(body)
    return web.Response(status=200)


async def post_v3_projects_id_snippets(request: web.Request, id, body) -> web.Response:
    """Create a new project snippet

    Create a new project snippet

    :param id: The ID of a project
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PostV3ProjectsIdSnippetsRequest.from_dict(body)
    return web.Response(status=200)


async def post_v3_projects_id_snippets_noteable_id_notes(request: web.Request, id, noteable_id, body) -> web.Response:
    """Create a new +noteable+ note

    Create a new +noteable+ note

    :param id: The ID of a project
    :type id: str
    :param noteable_id: The ID of the noteable
    :type noteable_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PostV3ProjectsIdIssuesNoteableIdNotesRequest.from_dict(body)
    return web.Response(status=200)


async def post_v3_projects_id_snippets_snippet_id_award_emoji(request: web.Request, id, snippet_id, body) -> web.Response:
    """Award a new Emoji

    This feature was introduced in 8.9

    :param id: 
    :type id: int
    :param snippet_id: 
    :type snippet_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PostV3ProjectsIdIssuesIssueIdAwardEmojiRequest.from_dict(body)
    return web.Response(status=200)


async def post_v3_projects_id_snippets_snippet_id_notes_note_id_award_emoji(request: web.Request, id, snippet_id, note_id, body) -> web.Response:
    """Award a new Emoji

    This feature was introduced in 8.9

    :param id: 
    :type id: int
    :param snippet_id: 
    :type snippet_id: int
    :param note_id: 
    :type note_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PostV3ProjectsIdIssuesIssueIdAwardEmojiRequest.from_dict(body)
    return web.Response(status=200)


async def post_v3_projects_id_star(request: web.Request, id) -> web.Response:
    """Star a project

    Star a project

    :param id: The ID of a project
    :type id: str

    """
    return web.Response(status=200)


async def post_v3_projects_id_statuses_sha(request: web.Request, id, sha, body) -> web.Response:
    """Post status to a commit

    Post status to a commit

    :param id: The ID of a project
    :type id: str
    :param sha: The commit hash
    :type sha: str
    :param body: 
    :type body: dict | bytes

    """
    body = PostV3ProjectsIdStatusesShaRequest.from_dict(body)
    return web.Response(status=200)


async def post_v3_projects_id_triggers(request: web.Request, id) -> web.Response:
    """Create a trigger

    Create a trigger

    :param id: The ID of a project
    :type id: str

    """
    return web.Response(status=200)


async def post_v3_projects_id_unarchive(request: web.Request, id) -> web.Response:
    """Unarchive a project

    Unarchive a project

    :param id: The ID of a project
    :type id: str

    """
    return web.Response(status=200)


async def post_v3_projects_id_uploads(request: web.Request, id, body) -> web.Response:
    """Upload a file

    Upload a file

    :param id: The ID of a project
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PostV3ProjectsIdUploadsRequest.from_dict(body)
    return web.Response(status=200)


async def post_v3_projects_id_variables(request: web.Request, id, body) -> web.Response:
    """Create a new variable in a project

    Create a new variable in a project

    :param id: The ID of a project
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PostV3ProjectsIdVariablesRequest.from_dict(body)
    return web.Response(status=200)


async def post_v3_projects_user_user_id(request: web.Request, user_id, body) -> web.Response:
    """Create new project for a specified user. Only available to admin users.

    Create new project for a specified user. Only available to admin users.

    :param user_id: The ID of a user
    :type user_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PostV3ProjectsUserUserIdRequest.from_dict(body)
    return web.Response(status=200)


async def put_v3_projects_id(request: web.Request, id, body=None) -> web.Response:
    """Update an existing project

    Update an existing project

    :param id: The ID of a project
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PutV3ProjectsIdRequest.from_dict(body)
    return web.Response(status=200)


async def put_v3_projects_id_access_requests_user_id_approve(request: web.Request, id, user_id, body=None) -> web.Response:
    """Approves an access request for the given user.

    This feature was introduced in GitLab 8.11.

    :param id: The project ID
    :type id: str
    :param user_id: The user ID of the access requester
    :type user_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PutV3GroupsIdAccessRequestsUserIdApproveRequest.from_dict(body)
    return web.Response(status=200)


async def put_v3_projects_id_boards_board_id_lists_list_id(request: web.Request, id, board_id, list_id, body) -> web.Response:
    """Moves a board list to a new position

    This feature was introduced in 8.13

    :param id: The ID of a project
    :type id: str
    :param board_id: The ID of a board
    :type board_id: int
    :param list_id: The ID of a list
    :type list_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PutV3ProjectsIdBoardsBoardIdListsListIdRequest.from_dict(body)
    return web.Response(status=200)


async def put_v3_projects_id_environments_environment_id(request: web.Request, id, environment_id, body=None) -> web.Response:
    """Updates an existing environment

    This feature was introduced in GitLab 8.11.

    :param id: The project ID
    :type id: str
    :param environment_id: The environment ID
    :type environment_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PutV3ProjectsIdEnvironmentsEnvironmentIdRequest.from_dict(body)
    return web.Response(status=200)


async def put_v3_projects_id_hooks_hook_id(request: web.Request, id, hook_id, body) -> web.Response:
    """Update an existing project hook

    Update an existing project hook

    :param id: The ID of a project
    :type id: str
    :param hook_id: The ID of the hook to update
    :type hook_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PostV3ProjectsIdHooksRequest.from_dict(body)
    return web.Response(status=200)


async def put_v3_projects_id_issues_issue_id(request: web.Request, id, issue_id, body=None) -> web.Response:
    """Update an existing issue

    Update an existing issue

    :param id: The ID of a project
    :type id: str
    :param issue_id: The ID of a project issue
    :type issue_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PutV3ProjectsIdIssuesIssueIdRequest.from_dict(body)
    return web.Response(status=200)


async def put_v3_projects_id_issues_noteable_id_notes_note_id(request: web.Request, id, noteable_id, note_id, body) -> web.Response:
    """Update an existing +noteable+ note

    Update an existing +noteable+ note

    :param id: The ID of a project
    :type id: str
    :param noteable_id: The ID of the noteable
    :type noteable_id: int
    :param note_id: The ID of a note
    :type note_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PutV3ProjectsIdIssuesNoteableIdNotesNoteIdRequest.from_dict(body)
    return web.Response(status=200)


async def put_v3_projects_id_labels(request: web.Request, id, body) -> web.Response:
    """Update an existing label. At least one optional parameter is required.

    Update an existing label. At least one optional parameter is required.

    :param id: The ID of a project
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PutV3ProjectsIdLabelsRequest.from_dict(body)
    return web.Response(status=200)


async def put_v3_projects_id_members_user_id(request: web.Request, id, user_id, body) -> web.Response:
    """Updates a member of a group or project.

    Updates a member of a group or project.

    :param id: The project ID
    :type id: str
    :param user_id: The user ID of the new member
    :type user_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PutV3GroupsIdMembersUserIdRequest.from_dict(body)
    return web.Response(status=200)


async def put_v3_projects_id_merge_request_merge_request_id(request: web.Request, id, merge_request_id, body=None) -> web.Response:
    """Update a merge request

    Update a merge request

    :param id: The ID of a project
    :type id: str
    :param merge_request_id: 
    :type merge_request_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PutV3ProjectsIdMergeRequestMergeRequestIdRequest.from_dict(body)
    return web.Response(status=200)


async def put_v3_projects_id_merge_request_merge_request_id_merge(request: web.Request, id, merge_request_id, body=None) -> web.Response:
    """Merge a merge request

    Merge a merge request

    :param id: The ID of a project
    :type id: str
    :param merge_request_id: 
    :type merge_request_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PutV3ProjectsIdMergeRequestMergeRequestIdMergeRequest.from_dict(body)
    return web.Response(status=200)


async def put_v3_projects_id_merge_requests_merge_request_id(request: web.Request, id, merge_request_id, body=None) -> web.Response:
    """Update a merge request

    Update a merge request

    :param id: The ID of a project
    :type id: str
    :param merge_request_id: 
    :type merge_request_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PutV3ProjectsIdMergeRequestMergeRequestIdRequest.from_dict(body)
    return web.Response(status=200)


async def put_v3_projects_id_merge_requests_merge_request_id_merge(request: web.Request, id, merge_request_id, body=None) -> web.Response:
    """Merge a merge request

    Merge a merge request

    :param id: The ID of a project
    :type id: str
    :param merge_request_id: 
    :type merge_request_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PutV3ProjectsIdMergeRequestMergeRequestIdMergeRequest.from_dict(body)
    return web.Response(status=200)


async def put_v3_projects_id_merge_requests_noteable_id_notes_note_id(request: web.Request, id, noteable_id, note_id, body) -> web.Response:
    """Update an existing +noteable+ note

    Update an existing +noteable+ note

    :param id: The ID of a project
    :type id: str
    :param noteable_id: The ID of the noteable
    :type noteable_id: int
    :param note_id: The ID of a note
    :type note_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PutV3ProjectsIdIssuesNoteableIdNotesNoteIdRequest.from_dict(body)
    return web.Response(status=200)


async def put_v3_projects_id_milestones_milestone_id(request: web.Request, id, milestone_id, body=None) -> web.Response:
    """Update an existing project milestone

    Update an existing project milestone

    :param id: The ID of a project
    :type id: str
    :param milestone_id: The ID of a project milestone
    :type milestone_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PutV3ProjectsIdMilestonesMilestoneIdRequest.from_dict(body)
    return web.Response(status=200)


async def put_v3_projects_id_notification_settings(request: web.Request, id, body=None) -> web.Response:
    """Update project level notification level settings, defaults to Global

    This feature was introduced in GitLab 8.12

    :param id: The group ID or project ID or project NAMESPACE/PROJECT_NAME
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PutV3ProjectsIdNotificationSettingsRequest.from_dict(body)
    return web.Response(status=200)


async def put_v3_projects_id_repository_branches_branch_protect(request: web.Request, id, branch, body=None) -> web.Response:
    """Protect a single branch

    Protect a single branch

    :param id: The ID of a project
    :type id: str
    :param branch: The name of the branch
    :type branch: str
    :param body: 
    :type body: dict | bytes

    """
    body = PutV3ProjectsIdRepositoryBranchesBranchProtectRequest.from_dict(body)
    return web.Response(status=200)


async def put_v3_projects_id_repository_branches_branch_unprotect(request: web.Request, id, branch) -> web.Response:
    """Unprotect a single branch

    Unprotect a single branch

    :param id: The ID of a project
    :type id: str
    :param branch: The name of the branch
    :type branch: str

    """
    return web.Response(status=200)


async def put_v3_projects_id_repository_files(request: web.Request, id, body) -> web.Response:
    """Update existing file in repository

    Update existing file in repository

    :param id: The project ID
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PutV3ProjectsIdRepositoryFilesRequest.from_dict(body)
    return web.Response(status=200)


async def put_v3_projects_id_repository_tags_tag_name_release(request: web.Request, id, tag_name, body) -> web.Response:
    """Update a tag&#39;s release note

    Update a tag&#39;s release note

    :param id: The ID of a project
    :type id: str
    :param tag_name: The name of the tag
    :type tag_name: str
    :param body: 
    :type body: dict | bytes

    """
    body = PutV3ProjectsIdRepositoryTagsTagNameReleaseRequest.from_dict(body)
    return web.Response(status=200)


async def put_v3_projects_id_services_asana(request: web.Request, id, body) -> web.Response:
    """Set asana service for project

    Set asana service for project

    :param id: 
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PutV3ProjectsIdServicesAsanaRequest.from_dict(body)
    return web.Response(status=200)


async def put_v3_projects_id_services_assembla(request: web.Request, id, body) -> web.Response:
    """Set assembla service for project

    Set assembla service for project

    :param id: 
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PutV3ProjectsIdServicesAssemblaRequest.from_dict(body)
    return web.Response(status=200)


async def put_v3_projects_id_services_bamboo(request: web.Request, id, body) -> web.Response:
    """Set bamboo service for project

    Set bamboo service for project

    :param id: 
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PutV3ProjectsIdServicesBambooRequest.from_dict(body)
    return web.Response(status=200)


async def put_v3_projects_id_services_bugzilla(request: web.Request, id, body) -> web.Response:
    """Set bugzilla service for project

    Set bugzilla service for project

    :param id: 
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PutV3ProjectsIdServicesBugzillaRequest.from_dict(body)
    return web.Response(status=200)


async def put_v3_projects_id_services_buildkite(request: web.Request, id, body) -> web.Response:
    """Set buildkite service for project

    Set buildkite service for project

    :param id: 
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PutV3ProjectsIdServicesBuildkiteRequest.from_dict(body)
    return web.Response(status=200)


async def put_v3_projects_id_services_builds_email(request: web.Request, id, body) -> web.Response:
    """Set builds-email service for project

    Set builds-email service for project

    :param id: 
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PutV3ProjectsIdServicesBuildsEmailRequest.from_dict(body)
    return web.Response(status=200)


async def put_v3_projects_id_services_campfire(request: web.Request, id, body) -> web.Response:
    """Set campfire service for project

    Set campfire service for project

    :param id: 
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PutV3ProjectsIdServicesCampfireRequest.from_dict(body)
    return web.Response(status=200)


async def put_v3_projects_id_services_custom_issue_tracker(request: web.Request, id, body) -> web.Response:
    """Set custom-issue-tracker service for project

    Set custom-issue-tracker service for project

    :param id: 
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PutV3ProjectsIdServicesBugzillaRequest.from_dict(body)
    return web.Response(status=200)


async def put_v3_projects_id_services_drone_ci(request: web.Request, id, body) -> web.Response:
    """Set drone-ci service for project

    Set drone-ci service for project

    :param id: 
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PutV3ProjectsIdServicesDroneCiRequest.from_dict(body)
    return web.Response(status=200)


async def put_v3_projects_id_services_emails_on_push(request: web.Request, id, body) -> web.Response:
    """Set emails-on-push service for project

    Set emails-on-push service for project

    :param id: 
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PutV3ProjectsIdServicesEmailsOnPushRequest.from_dict(body)
    return web.Response(status=200)


async def put_v3_projects_id_services_external_wiki(request: web.Request, id, body) -> web.Response:
    """Set external-wiki service for project

    Set external-wiki service for project

    :param id: 
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PutV3ProjectsIdServicesExternalWikiRequest.from_dict(body)
    return web.Response(status=200)


async def put_v3_projects_id_services_flowdock(request: web.Request, id, body) -> web.Response:
    """Set flowdock service for project

    Set flowdock service for project

    :param id: 
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PutV3ProjectsIdServicesFlowdockRequest.from_dict(body)
    return web.Response(status=200)


async def put_v3_projects_id_services_gemnasium(request: web.Request, id, body) -> web.Response:
    """Set gemnasium service for project

    Set gemnasium service for project

    :param id: 
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PutV3ProjectsIdServicesGemnasiumRequest.from_dict(body)
    return web.Response(status=200)


async def put_v3_projects_id_services_hipchat(request: web.Request, id, body) -> web.Response:
    """Set hipchat service for project

    Set hipchat service for project

    :param id: 
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PutV3ProjectsIdServicesHipchatRequest.from_dict(body)
    return web.Response(status=200)


async def put_v3_projects_id_services_irker(request: web.Request, id, body) -> web.Response:
    """Set irker service for project

    Set irker service for project

    :param id: 
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PutV3ProjectsIdServicesIrkerRequest.from_dict(body)
    return web.Response(status=200)


async def put_v3_projects_id_services_jira(request: web.Request, id, body) -> web.Response:
    """Set jira service for project

    Set jira service for project

    :param id: 
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PutV3ProjectsIdServicesJiraRequest.from_dict(body)
    return web.Response(status=200)


async def put_v3_projects_id_services_kubernetes(request: web.Request, id, body) -> web.Response:
    """Set kubernetes service for project

    Set kubernetes service for project

    :param id: 
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PutV3ProjectsIdServicesKubernetesRequest.from_dict(body)
    return web.Response(status=200)


async def put_v3_projects_id_services_mattermost(request: web.Request, id, body) -> web.Response:
    """Set mattermost service for project

    Set mattermost service for project

    :param id: 
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PutV3ProjectsIdServicesMattermostRequest.from_dict(body)
    return web.Response(status=200)


async def put_v3_projects_id_services_mattermost_slash_commands(request: web.Request, id, body) -> web.Response:
    """Set mattermost-slash-commands service for project

    Set mattermost-slash-commands service for project

    :param id: 
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PutV3ProjectsIdServicesMattermostSlashCommandsRequest.from_dict(body)
    return web.Response(status=200)


async def put_v3_projects_id_services_pipelines_email(request: web.Request, id, body) -> web.Response:
    """Set pipelines-email service for project

    Set pipelines-email service for project

    :param id: 
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PutV3ProjectsIdServicesPipelinesEmailRequest.from_dict(body)
    return web.Response(status=200)


async def put_v3_projects_id_services_pivotaltracker(request: web.Request, id, body) -> web.Response:
    """Set pivotaltracker service for project

    Set pivotaltracker service for project

    :param id: 
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PutV3ProjectsIdServicesPivotaltrackerRequest.from_dict(body)
    return web.Response(status=200)


async def put_v3_projects_id_services_pushover(request: web.Request, id, body) -> web.Response:
    """Set pushover service for project

    Set pushover service for project

    :param id: 
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PutV3ProjectsIdServicesPushoverRequest.from_dict(body)
    return web.Response(status=200)


async def put_v3_projects_id_services_redmine(request: web.Request, id, body) -> web.Response:
    """Set redmine service for project

    Set redmine service for project

    :param id: 
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PutV3ProjectsIdServicesRedmineRequest.from_dict(body)
    return web.Response(status=200)


async def put_v3_projects_id_services_slack(request: web.Request, id, body) -> web.Response:
    """Set slack service for project

    Set slack service for project

    :param id: 
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PutV3ProjectsIdServicesSlackRequest.from_dict(body)
    return web.Response(status=200)


async def put_v3_projects_id_services_slack_slash_commands(request: web.Request, id, body) -> web.Response:
    """Set slack-slash-commands service for project

    Set slack-slash-commands service for project

    :param id: 
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PutV3ProjectsIdServicesSlackSlashCommandsRequest.from_dict(body)
    return web.Response(status=200)


async def put_v3_projects_id_services_teamcity(request: web.Request, id, body) -> web.Response:
    """Set teamcity service for project

    Set teamcity service for project

    :param id: 
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PutV3ProjectsIdServicesTeamcityRequest.from_dict(body)
    return web.Response(status=200)


async def put_v3_projects_id_snippets_noteable_id_notes_note_id(request: web.Request, id, noteable_id, note_id, body) -> web.Response:
    """Update an existing +noteable+ note

    Update an existing +noteable+ note

    :param id: The ID of a project
    :type id: str
    :param noteable_id: The ID of the noteable
    :type noteable_id: int
    :param note_id: The ID of a note
    :type note_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PutV3ProjectsIdIssuesNoteableIdNotesNoteIdRequest.from_dict(body)
    return web.Response(status=200)


async def put_v3_projects_id_snippets_snippet_id(request: web.Request, id, snippet_id, body=None) -> web.Response:
    """Update an existing project snippet

    Update an existing project snippet

    :param id: The ID of a project
    :type id: str
    :param snippet_id: The ID of a project snippet
    :type snippet_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PutV3ProjectsIdSnippetsSnippetIdRequest.from_dict(body)
    return web.Response(status=200)


async def put_v3_projects_id_variables_key(request: web.Request, id, key, body=None) -> web.Response:
    """Update an existing variable from a project

    Update an existing variable from a project

    :param id: The ID of a project
    :type id: str
    :param key: The key of the variable
    :type key: str
    :param body: 
    :type body: dict | bytes

    """
    body = PutV3ProjectsIdVariablesKeyRequest.from_dict(body)
    return web.Response(status=200)
