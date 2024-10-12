# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData
from aiohttp import FormData

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


pytestmark = pytest.mark.asyncio

async def test_delete_v3_projects_id(client):
    """Test case for delete_v3_projects_id

    Remove a project
    """
    headers = { 
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/projects/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_v3_projects_id_access_requests_user_id(client):
    """Test case for delete_v3_projects_id_access_requests_user_id

    Denies an access request for the given user.
    """
    headers = { 
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/projects/{id}/access_requests/{user_id}'.format(id='id_example', user_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_v3_projects_id_boards_board_id_lists_list_id(client):
    """Test case for delete_v3_projects_id_boards_board_id_lists_list_id

    Delete a board list
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/projects/{id}/boards/{board_id}/lists/{list_id}'.format(id='id_example', board_id=56, list_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_v3_projects_id_deploy_keys_key_id(client):
    """Test case for delete_v3_projects_id_deploy_keys_key_id

    Delete deploy key for a project
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/projects/{id}/deploy_keys/{key_id}'.format(id='id_example', key_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_v3_projects_id_deploy_keys_key_id_disable(client):
    """Test case for delete_v3_projects_id_deploy_keys_key_id_disable

    Disable a deploy key for a project
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/projects/{id}/deploy_keys/{key_id}/disable'.format(id='id_example', key_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_v3_projects_id_environments_environment_id(client):
    """Test case for delete_v3_projects_id_environments_environment_id

    Deletes an existing environment
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/projects/{id}/environments/{environment_id}'.format(id='id_example', environment_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_v3_projects_id_fork(client):
    """Test case for delete_v3_projects_id_fork

    Remove a forked_from relationship
    """
    headers = { 
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/projects/{id}/fork'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_v3_projects_id_hooks_hook_id(client):
    """Test case for delete_v3_projects_id_hooks_hook_id

    Deletes project hook
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/projects/{id}/hooks/{hook_id}'.format(id='id_example', hook_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_v3_projects_id_issues_issue_id(client):
    """Test case for delete_v3_projects_id_issues_issue_id

    Delete a project issue
    """
    headers = { 
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/projects/{id}/issues/{issue_id}'.format(id='id_example', issue_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_v3_projects_id_issues_issue_id_award_emoji_award_id(client):
    """Test case for delete_v3_projects_id_issues_issue_id_award_emoji_award_id

    Delete a +awardables+ award emoji
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/projects/{id}/issues/{issue_id}/award_emoji/{award_id}'.format(award_id=56, id=56, issue_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_v3_projects_id_issues_issue_id_notes_note_id_award_emoji_award_id(client):
    """Test case for delete_v3_projects_id_issues_issue_id_notes_note_id_award_emoji_award_id

    Delete a +awardables+ award emoji
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/projects/{id}/issues/{issue_id}/notes/{note_id}/award_emoji/{award_id}'.format(award_id=56, id=56, issue_id=56, note_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_v3_projects_id_issues_noteable_id_notes_note_id(client):
    """Test case for delete_v3_projects_id_issues_noteable_id_notes_note_id

    Delete a +noteable+ note
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/projects/{id}/issues/{noteable_id}/notes/{note_id}'.format(id='id_example', noteable_id=56, note_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_v3_projects_id_issues_subscribable_id_subscription(client):
    """Test case for delete_v3_projects_id_issues_subscribable_id_subscription

    Unsubscribe from a resource
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/projects/{id}/issues/{subscribable_id}/subscription'.format(id='id_example', subscribable_id='subscribable_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_v3_projects_id_keys_key_id(client):
    """Test case for delete_v3_projects_id_keys_key_id

    Delete deploy key for a project
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/projects/{id}/keys/{key_id}'.format(id='id_example', key_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_v3_projects_id_keys_key_id_disable(client):
    """Test case for delete_v3_projects_id_keys_key_id_disable

    Disable a deploy key for a project
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/projects/{id}/keys/{key_id}/disable'.format(id='id_example', key_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_v3_projects_id_labels(client):
    """Test case for delete_v3_projects_id_labels

    Delete an existing label
    """
    params = [('name', 'name_example')]
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/projects/{id}/labels'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_v3_projects_id_labels_subscribable_id_subscription(client):
    """Test case for delete_v3_projects_id_labels_subscribable_id_subscription

    Unsubscribe from a resource
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/projects/{id}/labels/{subscribable_id}/subscription'.format(id='id_example', subscribable_id='subscribable_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_v3_projects_id_members_user_id(client):
    """Test case for delete_v3_projects_id_members_user_id

    Removes a user from a group or project.
    """
    headers = { 
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/projects/{id}/members/{user_id}'.format(id='id_example', user_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_v3_projects_id_merge_request_subscribable_id_subscription(client):
    """Test case for delete_v3_projects_id_merge_request_subscribable_id_subscription

    Unsubscribe from a resource
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/projects/{id}/merge_request/{subscribable_id}/subscription'.format(id='id_example', subscribable_id='subscribable_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_v3_projects_id_merge_requests_merge_request_id(client):
    """Test case for delete_v3_projects_id_merge_requests_merge_request_id

    Delete a merge request
    """
    headers = { 
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/projects/{id}/merge_requests/{merge_request_id}'.format(id='id_example', merge_request_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_v3_projects_id_merge_requests_merge_request_id_award_emoji_award_id(client):
    """Test case for delete_v3_projects_id_merge_requests_merge_request_id_award_emoji_award_id

    Delete a +awardables+ award emoji
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/projects/{id}/merge_requests/{merge_request_id}/award_emoji/{award_id}'.format(award_id=56, id=56, merge_request_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_v3_projects_id_merge_requests_merge_request_id_notes_note_id_award_emoji_award_id(client):
    """Test case for delete_v3_projects_id_merge_requests_merge_request_id_notes_note_id_award_emoji_award_id

    Delete a +awardables+ award emoji
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/projects/{id}/merge_requests/{merge_request_id}/notes/{note_id}/award_emoji/{award_id}'.format(award_id=56, id=56, merge_request_id=56, note_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_v3_projects_id_merge_requests_noteable_id_notes_note_id(client):
    """Test case for delete_v3_projects_id_merge_requests_noteable_id_notes_note_id

    Delete a +noteable+ note
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/projects/{id}/merge_requests/{noteable_id}/notes/{note_id}'.format(id='id_example', noteable_id=56, note_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_v3_projects_id_merge_requests_subscribable_id_subscription(client):
    """Test case for delete_v3_projects_id_merge_requests_subscribable_id_subscription

    Unsubscribe from a resource
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/projects/{id}/merge_requests/{subscribable_id}/subscription'.format(id='id_example', subscribable_id='subscribable_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_v3_projects_id_repository_branches_branch(client):
    """Test case for delete_v3_projects_id_repository_branches_branch

    Delete a branch
    """
    headers = { 
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/projects/{id}/repository/branches/{branch}'.format(id='id_example', branch='branch_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_v3_projects_id_repository_files(client):
    """Test case for delete_v3_projects_id_repository_files

    Delete an existing file in repository
    """
    params = [('file_path', 'file_path_example'),
                    ('branch_name', 'branch_name_example'),
                    ('commit_message', 'commit_message_example'),
                    ('author_email', 'author_email_example'),
                    ('author_name', 'author_name_example')]
    headers = { 
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/projects/{id}/repository/files'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_v3_projects_id_repository_merged_branches(client):
    """Test case for delete_v3_projects_id_repository_merged_branches

    
    """
    headers = { 
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/projects/{id}/repository/merged_branches'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_v3_projects_id_repository_tags_tag_name(client):
    """Test case for delete_v3_projects_id_repository_tags_tag_name

    Delete a repository tag
    """
    headers = { 
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/projects/{id}/repository/tags/{tag_name}'.format(id='id_example', tag_name='tag_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_v3_projects_id_runners_runner_id(client):
    """Test case for delete_v3_projects_id_runners_runner_id

    Disable project's runner
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/projects/{id}/runners/{runner_id}'.format(id='id_example', runner_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_v3_projects_id_services_service_slug(client):
    """Test case for delete_v3_projects_id_services_service_slug

    Delete a service for project
    """
    headers = { 
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/projects/{id}/services/{service_slug}'.format(service_slug='service_slug_example', id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_v3_projects_id_share_group_id(client):
    """Test case for delete_v3_projects_id_share_group_id

    
    """
    headers = { 
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/projects/{id}/share/{group_id}'.format(id='id_example', group_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_v3_projects_id_snippets_noteable_id_notes_note_id(client):
    """Test case for delete_v3_projects_id_snippets_noteable_id_notes_note_id

    Delete a +noteable+ note
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/projects/{id}/snippets/{noteable_id}/notes/{note_id}'.format(id='id_example', noteable_id=56, note_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_v3_projects_id_snippets_snippet_id(client):
    """Test case for delete_v3_projects_id_snippets_snippet_id

    Delete a project snippet
    """
    headers = { 
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/projects/{id}/snippets/{snippet_id}'.format(id='id_example', snippet_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_v3_projects_id_snippets_snippet_id_award_emoji_award_id(client):
    """Test case for delete_v3_projects_id_snippets_snippet_id_award_emoji_award_id

    Delete a +awardables+ award emoji
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/projects/{id}/snippets/{snippet_id}/award_emoji/{award_id}'.format(award_id=56, id=56, snippet_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_v3_projects_id_snippets_snippet_id_notes_note_id_award_emoji_award_id(client):
    """Test case for delete_v3_projects_id_snippets_snippet_id_notes_note_id_award_emoji_award_id

    Delete a +awardables+ award emoji
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/projects/{id}/snippets/{snippet_id}/notes/{note_id}/award_emoji/{award_id}'.format(award_id=56, id=56, snippet_id=56, note_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_v3_projects_id_star(client):
    """Test case for delete_v3_projects_id_star

    Unstar a project
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/projects/{id}/star'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_v3_projects_id_triggers_token(client):
    """Test case for delete_v3_projects_id_triggers_token

    Delete a trigger
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/projects/{id}/triggers/{token}'.format(id='id_example', token='token_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_v3_projects_id_variables_key(client):
    """Test case for delete_v3_projects_id_variables_key

    Delete an existing variable from a project
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/projects/{id}/variables/{key}'.format(id='id_example', key='key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects(client):
    """Test case for get_v3_projects

    Get a projects list for authenticated user
    """
    params = [('order_by', created_at),
                    ('sort', desc),
                    ('archived', True),
                    ('visibility', 'visibility_example'),
                    ('search', 'search_example'),
                    ('page', 56),
                    ('per_page', 56),
                    ('simple', True)]
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_all(client):
    """Test case for get_v3_projects_all

    Get all projects for admin user
    """
    params = [('order_by', created_at),
                    ('sort', desc),
                    ('archived', True),
                    ('visibility', 'visibility_example'),
                    ('search', 'search_example'),
                    ('page', 56),
                    ('per_page', 56),
                    ('simple', True),
                    ('statistics', True)]
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/all',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_id(client):
    """Test case for get_v3_projects_id

    Get a single project
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_id_access_requests(client):
    """Test case for get_v3_projects_id_access_requests

    Gets a list of access requests for a project.
    """
    params = [('page', 56),
                    ('per_page', 56)]
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}/access_requests'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_id_boards(client):
    """Test case for get_v3_projects_id_boards

    Get all project boards
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}/boards'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_id_boards_board_id_lists(client):
    """Test case for get_v3_projects_id_boards_board_id_lists

    Get the lists of a project board
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}/boards/{board_id}/lists'.format(id='id_example', board_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_id_boards_board_id_lists_list_id(client):
    """Test case for get_v3_projects_id_boards_board_id_lists_list_id

    Get a list of a project board
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}/boards/{board_id}/lists/{list_id}'.format(id='id_example', board_id=56, list_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_id_builds(client):
    """Test case for get_v3_projects_id_builds

    Get a project builds
    """
    params = [('scope', 'scope_example'),
                    ('page', 56),
                    ('per_page', 56)]
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}/builds'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_id_builds_artifacts_ref_name_download(client):
    """Test case for get_v3_projects_id_builds_artifacts_ref_name_download

    Download the artifacts file from build
    """
    params = [('job', 'job_example')]
    headers = { 
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}/builds/artifacts/{ref_name}/download'.format(id='id_example', ref_name='ref_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_id_builds_build_id(client):
    """Test case for get_v3_projects_id_builds_build_id

    Get a specific build of a project
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}/builds/{build_id}'.format(id='id_example', build_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_id_builds_build_id_artifacts(client):
    """Test case for get_v3_projects_id_builds_build_id_artifacts

    Download the artifacts file from build
    """
    headers = { 
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}/builds/{build_id}/artifacts'.format(id='id_example', build_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_id_builds_build_id_trace(client):
    """Test case for get_v3_projects_id_builds_build_id_trace

    Get a trace of a specific build of a project
    """
    headers = { 
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}/builds/{build_id}/trace'.format(id='id_example', build_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_id_deploy_keys(client):
    """Test case for get_v3_projects_id_deploy_keys

    Get a specific project's deploy keys
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}/deploy_keys'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_id_deploy_keys_key_id(client):
    """Test case for get_v3_projects_id_deploy_keys_key_id

    Get single deploy key
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}/deploy_keys/{key_id}'.format(id='id_example', key_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_id_deployments(client):
    """Test case for get_v3_projects_id_deployments

    Get all deployments of the project
    """
    params = [('page', 56),
                    ('per_page', 56)]
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}/deployments'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_id_deployments_deployment_id(client):
    """Test case for get_v3_projects_id_deployments_deployment_id

    Gets a specific deployment
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}/deployments/{deployment_id}'.format(id='id_example', deployment_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_id_environments(client):
    """Test case for get_v3_projects_id_environments

    Get all environments of the project
    """
    params = [('page', 56),
                    ('per_page', 56)]
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}/environments'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_id_events(client):
    """Test case for get_v3_projects_id_events

    Get events for a single project
    """
    params = [('page', 56),
                    ('per_page', 56)]
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}/events'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_id_hooks(client):
    """Test case for get_v3_projects_id_hooks

    Get project hooks
    """
    params = [('page', 56),
                    ('per_page', 56)]
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}/hooks'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_id_hooks_hook_id(client):
    """Test case for get_v3_projects_id_hooks_hook_id

    Get a project hook
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}/hooks/{hook_id}'.format(id='id_example', hook_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_id_issues(client):
    """Test case for get_v3_projects_id_issues

    Get a list of project issues
    """
    params = [('state', all),
                    ('iid', 56),
                    ('labels', 'labels_example'),
                    ('milestone', 'milestone_example'),
                    ('order_by', created_at),
                    ('sort', desc),
                    ('page', 56),
                    ('per_page', 56)]
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}/issues'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_id_issues_issue_id(client):
    """Test case for get_v3_projects_id_issues_issue_id

    Get a single project issue
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}/issues/{issue_id}'.format(id='id_example', issue_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_id_issues_issue_id_award_emoji(client):
    """Test case for get_v3_projects_id_issues_issue_id_award_emoji

    Get a list of project +awardable+ award emoji
    """
    params = [('page', 56),
                    ('per_page', 56)]
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}/issues/{issue_id}/award_emoji'.format(id='id_example', issue_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_id_issues_issue_id_award_emoji_award_id(client):
    """Test case for get_v3_projects_id_issues_issue_id_award_emoji_award_id

    Get a specific award emoji
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}/issues/{issue_id}/award_emoji/{award_id}'.format(award_id=56, id=56, issue_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_id_issues_issue_id_notes_note_id_award_emoji(client):
    """Test case for get_v3_projects_id_issues_issue_id_notes_note_id_award_emoji

    Get a list of project +awardable+ award emoji
    """
    params = [('page', 56),
                    ('per_page', 56)]
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}/issues/{issue_id}/notes/{note_id}/award_emoji'.format(id=56, issue_id=56, note_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_id_issues_issue_id_notes_note_id_award_emoji_award_id(client):
    """Test case for get_v3_projects_id_issues_issue_id_notes_note_id_award_emoji_award_id

    Get a specific award emoji
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}/issues/{issue_id}/notes/{note_id}/award_emoji/{award_id}'.format(award_id=56, id=56, issue_id=56, note_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_id_issues_issue_id_time_stats(client):
    """Test case for get_v3_projects_id_issues_issue_id_time_stats

    Show time stats for a project issue
    """
    headers = { 
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}/issues/{issue_id}/time_stats'.format(id='id_example', issue_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_id_issues_noteable_id_notes(client):
    """Test case for get_v3_projects_id_issues_noteable_id_notes

    Get a list of project +noteable+ notes
    """
    params = [('page', 56),
                    ('per_page', 56)]
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}/issues/{noteable_id}/notes'.format(id='id_example', noteable_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_id_issues_noteable_id_notes_note_id(client):
    """Test case for get_v3_projects_id_issues_noteable_id_notes_note_id

    Get a single +noteable+ note
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}/issues/{noteable_id}/notes/{note_id}'.format(id='id_example', note_id=56, noteable_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_id_keys(client):
    """Test case for get_v3_projects_id_keys

    Get a specific project's deploy keys
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}/keys'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_id_keys_key_id(client):
    """Test case for get_v3_projects_id_keys_key_id

    Get single deploy key
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}/keys/{key_id}'.format(id='id_example', key_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_id_labels(client):
    """Test case for get_v3_projects_id_labels

    Get all labels of the project
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}/labels'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_id_members(client):
    """Test case for get_v3_projects_id_members

    Gets a list of group or project members viewable by the authenticated user.
    """
    params = [('query', 'query_example'),
                    ('page', 56),
                    ('per_page', 56)]
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}/members'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_id_members_user_id(client):
    """Test case for get_v3_projects_id_members_user_id

    Gets a member of a group or project.
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}/members/{user_id}'.format(id='id_example', user_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_id_merge_request_merge_request_id(client):
    """Test case for get_v3_projects_id_merge_request_merge_request_id

    Get a single merge request
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}/merge_request/{merge_request_id}'.format(id='id_example', merge_request_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_id_merge_request_merge_request_id_changes(client):
    """Test case for get_v3_projects_id_merge_request_merge_request_id_changes

    Show the merge request changes
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}/merge_request/{merge_request_id}/changes'.format(id='id_example', merge_request_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_id_merge_request_merge_request_id_closes_issues(client):
    """Test case for get_v3_projects_id_merge_request_merge_request_id_closes_issues

    List issues that will be closed on merge
    """
    params = [('page', 56),
                    ('per_page', 56)]
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}/merge_request/{merge_request_id}/closes_issues'.format(id='id_example', merge_request_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_id_merge_request_merge_request_id_comments(client):
    """Test case for get_v3_projects_id_merge_request_merge_request_id_comments

    Get the comments of a merge request
    """
    params = [('page', 56),
                    ('per_page', 56)]
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}/merge_request/{merge_request_id}/comments'.format(id='id_example', merge_request_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_id_merge_request_merge_request_id_commits(client):
    """Test case for get_v3_projects_id_merge_request_merge_request_id_commits

    Get the commits of a merge request
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}/merge_request/{merge_request_id}/commits'.format(id='id_example', merge_request_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_get_v3_projects_id_merge_requests(client):
    """Test case for get_v3_projects_id_merge_requests

    List merge requests
    """
    params = [('state', all),
                    ('order_by', created_at),
                    ('sort', desc),
                    ('page', 56),
                    ('per_page', 56)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    data = FormData()
    data.add_field('iid', [56])
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}/merge_requests'.format(id='id_example'),
        headers=headers,
        data=data,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_id_merge_requests_merge_request_id(client):
    """Test case for get_v3_projects_id_merge_requests_merge_request_id

    Get a single merge request
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}/merge_requests/{merge_request_id}'.format(id='id_example', merge_request_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_id_merge_requests_merge_request_id_award_emoji(client):
    """Test case for get_v3_projects_id_merge_requests_merge_request_id_award_emoji

    Get a list of project +awardable+ award emoji
    """
    params = [('page', 56),
                    ('per_page', 56)]
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}/merge_requests/{merge_request_id}/award_emoji'.format(id='id_example', merge_request_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_id_merge_requests_merge_request_id_award_emoji_award_id(client):
    """Test case for get_v3_projects_id_merge_requests_merge_request_id_award_emoji_award_id

    Get a specific award emoji
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}/merge_requests/{merge_request_id}/award_emoji/{award_id}'.format(award_id=56, id=56, merge_request_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_id_merge_requests_merge_request_id_changes(client):
    """Test case for get_v3_projects_id_merge_requests_merge_request_id_changes

    Show the merge request changes
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}/merge_requests/{merge_request_id}/changes'.format(id='id_example', merge_request_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_id_merge_requests_merge_request_id_closes_issues(client):
    """Test case for get_v3_projects_id_merge_requests_merge_request_id_closes_issues

    List issues that will be closed on merge
    """
    params = [('page', 56),
                    ('per_page', 56)]
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}/merge_requests/{merge_request_id}/closes_issues'.format(id='id_example', merge_request_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_id_merge_requests_merge_request_id_comments(client):
    """Test case for get_v3_projects_id_merge_requests_merge_request_id_comments

    Get the comments of a merge request
    """
    params = [('page', 56),
                    ('per_page', 56)]
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}/merge_requests/{merge_request_id}/comments'.format(id='id_example', merge_request_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_id_merge_requests_merge_request_id_commits(client):
    """Test case for get_v3_projects_id_merge_requests_merge_request_id_commits

    Get the commits of a merge request
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}/merge_requests/{merge_request_id}/commits'.format(id='id_example', merge_request_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_id_merge_requests_merge_request_id_notes_note_id_award_emoji(client):
    """Test case for get_v3_projects_id_merge_requests_merge_request_id_notes_note_id_award_emoji

    Get a list of project +awardable+ award emoji
    """
    params = [('page', 56),
                    ('per_page', 56)]
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}/merge_requests/{merge_request_id}/notes/{note_id}/award_emoji'.format(id=56, merge_request_id=56, note_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_id_merge_requests_merge_request_id_notes_note_id_award_emoji_award_id(client):
    """Test case for get_v3_projects_id_merge_requests_merge_request_id_notes_note_id_award_emoji_award_id

    Get a specific award emoji
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}/merge_requests/{merge_request_id}/notes/{note_id}/award_emoji/{award_id}'.format(award_id=56, id=56, merge_request_id=56, note_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_id_merge_requests_merge_request_id_time_stats(client):
    """Test case for get_v3_projects_id_merge_requests_merge_request_id_time_stats

    Show time stats for a project merge_request
    """
    headers = { 
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}/merge_requests/{merge_request_id}/time_stats'.format(id='id_example', merge_request_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_id_merge_requests_merge_request_id_versions(client):
    """Test case for get_v3_projects_id_merge_requests_merge_request_id_versions

    Get a list of merge request diff versions
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}/merge_requests/{merge_request_id}/versions'.format(id='id_example', merge_request_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_id_merge_requests_merge_request_id_versions_version_id(client):
    """Test case for get_v3_projects_id_merge_requests_merge_request_id_versions_version_id

    Get a single merge request diff version
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}/merge_requests/{merge_request_id}/versions/{version_id}'.format(id='id_example', merge_request_id=56, version_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_id_merge_requests_noteable_id_notes(client):
    """Test case for get_v3_projects_id_merge_requests_noteable_id_notes

    Get a list of project +noteable+ notes
    """
    params = [('page', 56),
                    ('per_page', 56)]
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}/merge_requests/{noteable_id}/notes'.format(id='id_example', noteable_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_id_merge_requests_noteable_id_notes_note_id(client):
    """Test case for get_v3_projects_id_merge_requests_noteable_id_notes_note_id

    Get a single +noteable+ note
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}/merge_requests/{noteable_id}/notes/{note_id}'.format(id='id_example', note_id=56, noteable_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_get_v3_projects_id_milestones(client):
    """Test case for get_v3_projects_id_milestones

    Get a list of project milestones
    """
    params = [('state', all),
                    ('page', 56),
                    ('per_page', 56)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    data = FormData()
    data.add_field('iid', [56])
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}/milestones'.format(id='id_example'),
        headers=headers,
        data=data,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_id_milestones_milestone_id(client):
    """Test case for get_v3_projects_id_milestones_milestone_id

    Get a single project milestone
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}/milestones/{milestone_id}'.format(id='id_example', milestone_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_id_milestones_milestone_id_issues(client):
    """Test case for get_v3_projects_id_milestones_milestone_id_issues

    Get all issues for a single project milestone
    """
    params = [('page', 56),
                    ('per_page', 56)]
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}/milestones/{milestone_id}/issues'.format(id='id_example', milestone_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_id_notification_settings(client):
    """Test case for get_v3_projects_id_notification_settings

    Get project level notification level settings, defaults to Global
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}/notification_settings'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_id_pipelines(client):
    """Test case for get_v3_projects_id_pipelines

    Get all Pipelines of the project
    """
    params = [('page', 56),
                    ('per_page', 56),
                    ('scope', 'scope_example')]
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}/pipelines'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_id_pipelines_pipeline_id(client):
    """Test case for get_v3_projects_id_pipelines_pipeline_id

    Gets a specific pipeline for the project
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}/pipelines/{pipeline_id}'.format(id='id_example', pipeline_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_id_repository_archive(client):
    """Test case for get_v3_projects_id_repository_archive

    Get an archive of the repository
    """
    params = [('sha', 'sha_example'),
                    ('format', 'format_example')]
    headers = { 
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}/repository/archive'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_id_repository_blobs_sha(client):
    """Test case for get_v3_projects_id_repository_blobs_sha

    Get a raw file contents
    """
    params = [('filepath', 'filepath_example')]
    headers = { 
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}/repository/blobs/{sha}'.format(id='id_example', sha='sha_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_id_repository_branches(client):
    """Test case for get_v3_projects_id_repository_branches

    Get a project repository branches
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}/repository/branches'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_id_repository_branches_branch(client):
    """Test case for get_v3_projects_id_repository_branches_branch

    Get a single branch
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}/repository/branches/{branch}'.format(id='id_example', branch='branch_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_id_repository_commits(client):
    """Test case for get_v3_projects_id_repository_commits

    Get a project repository commits
    """
    params = [('ref_name', 'ref_name_example'),
                    ('since', 'since_example'),
                    ('until', 'until_example'),
                    ('page', 0),
                    ('per_page', 20),
                    ('path', 'path_example')]
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}/repository/commits'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_id_repository_commits_sha(client):
    """Test case for get_v3_projects_id_repository_commits_sha

    Get a specific commit of a project
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}/repository/commits/{sha}'.format(id='id_example', sha='sha_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_id_repository_commits_sha_blob(client):
    """Test case for get_v3_projects_id_repository_commits_sha_blob

    Get a raw file contents
    """
    params = [('filepath', 'filepath_example')]
    headers = { 
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}/repository/commits/{sha}/blob'.format(id='id_example', sha='sha_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_id_repository_commits_sha_builds(client):
    """Test case for get_v3_projects_id_repository_commits_sha_builds

    Get builds for a specific commit of a project
    """
    params = [('scope', 'scope_example'),
                    ('page', 56),
                    ('per_page', 56)]
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}/repository/commits/{sha}/builds'.format(id='id_example', sha='sha_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_id_repository_commits_sha_comments(client):
    """Test case for get_v3_projects_id_repository_commits_sha_comments

    Get a commit's comments
    """
    params = [('page', 56),
                    ('per_page', 56)]
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}/repository/commits/{sha}/comments'.format(id='id_example', sha='sha_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_id_repository_commits_sha_diff(client):
    """Test case for get_v3_projects_id_repository_commits_sha_diff

    Get the diff for a specific commit of a project
    """
    headers = { 
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}/repository/commits/{sha}/diff'.format(id='id_example', sha='sha_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_id_repository_commits_sha_statuses(client):
    """Test case for get_v3_projects_id_repository_commits_sha_statuses

    Get a commit's statuses
    """
    params = [('ref', 'ref_example'),
                    ('stage', 'stage_example'),
                    ('name', 'name_example'),
                    ('all', 'all_example'),
                    ('page', 56),
                    ('per_page', 56)]
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}/repository/commits/{sha}/statuses'.format(id='id_example', sha='sha_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_id_repository_compare(client):
    """Test case for get_v3_projects_id_repository_compare

    Compare two branches, tags, or commits
    """
    params = [('from', '_from_example'),
                    ('to', 'to_example')]
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}/repository/compare'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_id_repository_contributors(client):
    """Test case for get_v3_projects_id_repository_contributors

    Get repository contributors
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}/repository/contributors'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_id_repository_files(client):
    """Test case for get_v3_projects_id_repository_files

    Get a file from repository
    """
    params = [('file_path', 'file_path_example'),
                    ('ref', 'ref_example')]
    headers = { 
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}/repository/files'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_id_repository_raw_blobs_sha(client):
    """Test case for get_v3_projects_id_repository_raw_blobs_sha

    Get a raw blob contents by blob sha
    """
    headers = { 
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}/repository/raw_blobs/{sha}'.format(id='id_example', sha='sha_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_id_repository_tags(client):
    """Test case for get_v3_projects_id_repository_tags

    Get a project repository tags
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}/repository/tags'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_id_repository_tags_tag_name(client):
    """Test case for get_v3_projects_id_repository_tags_tag_name

    Get a single repository tag
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}/repository/tags/{tag_name}'.format(id='id_example', tag_name='tag_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_id_repository_tree(client):
    """Test case for get_v3_projects_id_repository_tree

    Get a project repository tree
    """
    params = [('ref_name', 'ref_name_example'),
                    ('path', 'path_example'),
                    ('recursive', True)]
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}/repository/tree'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_id_runners(client):
    """Test case for get_v3_projects_id_runners

    Get runners available for project
    """
    params = [('scope', 'scope_example'),
                    ('page', 56),
                    ('per_page', 56)]
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}/runners'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_id_services_service_slug(client):
    """Test case for get_v3_projects_id_services_service_slug

    Get the service settings for project
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}/services/{service_slug}'.format(service_slug='service_slug_example', id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_id_snippets(client):
    """Test case for get_v3_projects_id_snippets

    Get all project snippets
    """
    params = [('page', 56),
                    ('per_page', 56)]
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}/snippets'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_id_snippets_noteable_id_notes(client):
    """Test case for get_v3_projects_id_snippets_noteable_id_notes

    Get a list of project +noteable+ notes
    """
    params = [('page', 56),
                    ('per_page', 56)]
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}/snippets/{noteable_id}/notes'.format(id='id_example', noteable_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_id_snippets_noteable_id_notes_note_id(client):
    """Test case for get_v3_projects_id_snippets_noteable_id_notes_note_id

    Get a single +noteable+ note
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}/snippets/{noteable_id}/notes/{note_id}'.format(id='id_example', note_id=56, noteable_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_id_snippets_snippet_id(client):
    """Test case for get_v3_projects_id_snippets_snippet_id

    Get a single project snippet
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}/snippets/{snippet_id}'.format(id='id_example', snippet_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_id_snippets_snippet_id_award_emoji(client):
    """Test case for get_v3_projects_id_snippets_snippet_id_award_emoji

    Get a list of project +awardable+ award emoji
    """
    params = [('page', 56),
                    ('per_page', 56)]
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}/snippets/{snippet_id}/award_emoji'.format(id='id_example', snippet_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_id_snippets_snippet_id_award_emoji_award_id(client):
    """Test case for get_v3_projects_id_snippets_snippet_id_award_emoji_award_id

    Get a specific award emoji
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}/snippets/{snippet_id}/award_emoji/{award_id}'.format(award_id=56, id=56, snippet_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_id_snippets_snippet_id_notes_note_id_award_emoji(client):
    """Test case for get_v3_projects_id_snippets_snippet_id_notes_note_id_award_emoji

    Get a list of project +awardable+ award emoji
    """
    params = [('page', 56),
                    ('per_page', 56)]
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}/snippets/{snippet_id}/notes/{note_id}/award_emoji'.format(id=56, snippet_id=56, note_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_id_snippets_snippet_id_notes_note_id_award_emoji_award_id(client):
    """Test case for get_v3_projects_id_snippets_snippet_id_notes_note_id_award_emoji_award_id

    Get a specific award emoji
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}/snippets/{snippet_id}/notes/{note_id}/award_emoji/{award_id}'.format(award_id=56, id=56, snippet_id=56, note_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_id_snippets_snippet_id_raw(client):
    """Test case for get_v3_projects_id_snippets_snippet_id_raw

    Get a raw project snippet
    """
    headers = { 
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}/snippets/{snippet_id}/raw'.format(id='id_example', snippet_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_id_triggers(client):
    """Test case for get_v3_projects_id_triggers

    Get triggers list
    """
    params = [('page', 56),
                    ('per_page', 56)]
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}/triggers'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_id_triggers_token(client):
    """Test case for get_v3_projects_id_triggers_token

    Get specific trigger of a project
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}/triggers/{token}'.format(id='id_example', token='token_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_id_users(client):
    """Test case for get_v3_projects_id_users

    Get the users list of a project
    """
    params = [('search', 'search_example'),
                    ('page', 56),
                    ('per_page', 56)]
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}/users'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_id_variables(client):
    """Test case for get_v3_projects_id_variables

    Get project variables
    """
    params = [('page', 56),
                    ('per_page', 56)]
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}/variables'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_id_variables_key(client):
    """Test case for get_v3_projects_id_variables_key

    Get a specific variable from a project
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/{id}/variables/{key}'.format(id='id_example', key='key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_owned(client):
    """Test case for get_v3_projects_owned

    Get an owned projects list for authenticated user
    """
    params = [('order_by', created_at),
                    ('sort', desc),
                    ('archived', True),
                    ('visibility', 'visibility_example'),
                    ('search', 'search_example'),
                    ('page', 56),
                    ('per_page', 56),
                    ('simple', True),
                    ('statistics', True)]
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/owned',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_search_query(client):
    """Test case for get_v3_projects_search_query

    Search for projects the current user has access to
    """
    params = [('order_by', created_at),
                    ('sort', desc),
                    ('page', 56),
                    ('per_page', 56)]
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/search/{query}'.format(query='query_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_starred(client):
    """Test case for get_v3_projects_starred

    Gets starred project for the authenticated user
    """
    params = [('order_by', created_at),
                    ('sort', desc),
                    ('archived', True),
                    ('visibility', 'visibility_example'),
                    ('search', 'search_example'),
                    ('page', 56),
                    ('per_page', 56),
                    ('simple', True)]
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/starred',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_projects_visible(client):
    """Test case for get_v3_projects_visible

    Get a list of visible projects for authenticated user
    """
    params = [('order_by', created_at),
                    ('sort', desc),
                    ('archived', True),
                    ('visibility', 'visibility_example'),
                    ('search', 'search_example'),
                    ('page', 56),
                    ('per_page', 56),
                    ('simple', True)]
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/projects/visible',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_v3_projects(client):
    """Test case for post_v3_projects

    Create new project
    """
    body = openapi_server.PostV3ProjectsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/projects',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_v3_projects_fork_id(client):
    """Test case for post_v3_projects_fork_id

    Fork new project for the current user or provided namespace.
    """
    body = openapi_server.PostV3ProjectsForkIdRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/projects/fork/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_v3_projects_id_access_requests(client):
    """Test case for post_v3_projects_id_access_requests

    Requests access for the authenticated user to a project.
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/projects/{id}/access_requests'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_v3_projects_id_archive(client):
    """Test case for post_v3_projects_id_archive

    Archive a project
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/projects/{id}/archive'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_v3_projects_id_boards_board_id_lists(client):
    """Test case for post_v3_projects_id_boards_board_id_lists

    Create a new board list
    """
    body = openapi_server.PostV3ProjectsIdBoardsBoardIdListsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/projects/{id}/boards/{board_id}/lists'.format(id='id_example', board_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_v3_projects_id_builds_build_id_artifacts_keep(client):
    """Test case for post_v3_projects_id_builds_build_id_artifacts_keep

    Keep the artifacts to prevent them from being deleted
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/projects/{id}/builds/{build_id}/artifacts/keep'.format(id='id_example', build_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_v3_projects_id_builds_build_id_cancel(client):
    """Test case for post_v3_projects_id_builds_build_id_cancel

    Cancel a specific build of a project
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/projects/{id}/builds/{build_id}/cancel'.format(id='id_example', build_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_v3_projects_id_builds_build_id_erase(client):
    """Test case for post_v3_projects_id_builds_build_id_erase

    Erase build (remove artifacts and build trace)
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/projects/{id}/builds/{build_id}/erase'.format(id='id_example', build_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_v3_projects_id_builds_build_id_play(client):
    """Test case for post_v3_projects_id_builds_build_id_play

    Trigger a manual build
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/projects/{id}/builds/{build_id}/play'.format(id='id_example', build_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_v3_projects_id_builds_build_id_retry(client):
    """Test case for post_v3_projects_id_builds_build_id_retry

    Retry a specific build of a project
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/projects/{id}/builds/{build_id}/retry'.format(id='id_example', build_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_v3_projects_id_deploy_keys(client):
    """Test case for post_v3_projects_id_deploy_keys

    Add new deploy key to currently authenticated user
    """
    body = openapi_server.PostV3ProjectsIdDeployKeysRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/projects/{id}/deploy_keys'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_v3_projects_id_deploy_keys_key_id_enable(client):
    """Test case for post_v3_projects_id_deploy_keys_key_id_enable

    Enable a deploy key for a project
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/projects/{id}/deploy_keys/{key_id}/enable'.format(id='id_example', key_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_v3_projects_id_environments(client):
    """Test case for post_v3_projects_id_environments

    Creates a new environment
    """
    body = openapi_server.PostV3ProjectsIdEnvironmentsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/projects/{id}/environments'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_v3_projects_id_fork_forked_from_id(client):
    """Test case for post_v3_projects_id_fork_forked_from_id

    Mark this project as forked from another
    """
    headers = { 
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/projects/{id}/fork/{forked_from_id}'.format(id='id_example', forked_from_id='forked_from_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_v3_projects_id_hooks(client):
    """Test case for post_v3_projects_id_hooks

    Add hook to project
    """
    body = openapi_server.PostV3ProjectsIdHooksRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/projects/{id}/hooks'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_v3_projects_id_issues(client):
    """Test case for post_v3_projects_id_issues

    Create a new project issue
    """
    body = openapi_server.PostV3ProjectsIdIssuesRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/projects/{id}/issues'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_v3_projects_id_issues_issue_id_add_spent_time(client):
    """Test case for post_v3_projects_id_issues_issue_id_add_spent_time

    Add spent time for a project issue
    """
    body = openapi_server.PostV3ProjectsIdIssuesIssueIdAddSpentTimeRequest()
    headers = { 
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/projects/{id}/issues/{issue_id}/add_spent_time'.format(id='id_example', issue_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_v3_projects_id_issues_issue_id_award_emoji(client):
    """Test case for post_v3_projects_id_issues_issue_id_award_emoji

    Award a new Emoji
    """
    body = openapi_server.PostV3ProjectsIdIssuesIssueIdAwardEmojiRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/projects/{id}/issues/{issue_id}/award_emoji'.format(id=56, issue_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_v3_projects_id_issues_issue_id_move(client):
    """Test case for post_v3_projects_id_issues_issue_id_move

    Move an existing issue
    """
    body = openapi_server.PostV3ProjectsIdIssuesIssueIdMoveRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/projects/{id}/issues/{issue_id}/move'.format(id='id_example', issue_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_v3_projects_id_issues_issue_id_notes_note_id_award_emoji(client):
    """Test case for post_v3_projects_id_issues_issue_id_notes_note_id_award_emoji

    Award a new Emoji
    """
    body = openapi_server.PostV3ProjectsIdIssuesIssueIdAwardEmojiRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/projects/{id}/issues/{issue_id}/notes/{note_id}/award_emoji'.format(id=56, issue_id=56, note_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_v3_projects_id_issues_issue_id_reset_spent_time(client):
    """Test case for post_v3_projects_id_issues_issue_id_reset_spent_time

    Reset spent time for a project issue
    """
    headers = { 
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/projects/{id}/issues/{issue_id}/reset_spent_time'.format(id='id_example', issue_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_v3_projects_id_issues_issue_id_reset_time_estimate(client):
    """Test case for post_v3_projects_id_issues_issue_id_reset_time_estimate

    Reset the time estimate for a project issue
    """
    headers = { 
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/projects/{id}/issues/{issue_id}/reset_time_estimate'.format(id='id_example', issue_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_v3_projects_id_issues_issue_id_time_estimate(client):
    """Test case for post_v3_projects_id_issues_issue_id_time_estimate

    Set a time estimate for a project issue
    """
    body = openapi_server.PostV3ProjectsIdIssuesIssueIdAddSpentTimeRequest()
    headers = { 
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/projects/{id}/issues/{issue_id}/time_estimate'.format(id='id_example', issue_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_v3_projects_id_issues_issue_id_todo(client):
    """Test case for post_v3_projects_id_issues_issue_id_todo

    Create a todo on an issuable
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/projects/{id}/issues/{issue_id}/todo'.format(id='id_example', issue_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_v3_projects_id_issues_noteable_id_notes(client):
    """Test case for post_v3_projects_id_issues_noteable_id_notes

    Create a new +noteable+ note
    """
    body = openapi_server.PostV3ProjectsIdIssuesNoteableIdNotesRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/projects/{id}/issues/{noteable_id}/notes'.format(id='id_example', noteable_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_v3_projects_id_issues_subscribable_id_subscription(client):
    """Test case for post_v3_projects_id_issues_subscribable_id_subscription

    Subscribe to a resource
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/projects/{id}/issues/{subscribable_id}/subscription'.format(id='id_example', subscribable_id='subscribable_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_v3_projects_id_keys(client):
    """Test case for post_v3_projects_id_keys

    Add new deploy key to currently authenticated user
    """
    body = openapi_server.PostV3ProjectsIdDeployKeysRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/projects/{id}/keys'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_v3_projects_id_keys_key_id_enable(client):
    """Test case for post_v3_projects_id_keys_key_id_enable

    Enable a deploy key for a project
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/projects/{id}/keys/{key_id}/enable'.format(id='id_example', key_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_v3_projects_id_labels(client):
    """Test case for post_v3_projects_id_labels

    Create a new label
    """
    body = openapi_server.PostV3ProjectsIdLabelsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/projects/{id}/labels'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_v3_projects_id_labels_subscribable_id_subscription(client):
    """Test case for post_v3_projects_id_labels_subscribable_id_subscription

    Subscribe to a resource
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/projects/{id}/labels/{subscribable_id}/subscription'.format(id='id_example', subscribable_id='subscribable_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_v3_projects_id_members(client):
    """Test case for post_v3_projects_id_members

    Adds a member to a group or project.
    """
    body = openapi_server.PostV3GroupsIdMembersRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/projects/{id}/members'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_v3_projects_id_merge_request_merge_request_id_cancel_merge_when_build_succeeds(client):
    """Test case for post_v3_projects_id_merge_request_merge_request_id_cancel_merge_when_build_succeeds

    Cancel merge if \"Merge When Pipeline Succeeds\" is enabled
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/projects/{id}/merge_request/{merge_request_id}/cancel_merge_when_build_succeeds'.format(id='id_example', merge_request_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_v3_projects_id_merge_request_merge_request_id_comments(client):
    """Test case for post_v3_projects_id_merge_request_merge_request_id_comments

    Post a comment to a merge request
    """
    body = openapi_server.PostV3ProjectsIdMergeRequestMergeRequestIdCommentsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/projects/{id}/merge_request/{merge_request_id}/comments'.format(id='id_example', merge_request_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_v3_projects_id_merge_request_subscribable_id_subscription(client):
    """Test case for post_v3_projects_id_merge_request_subscribable_id_subscription

    Subscribe to a resource
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/projects/{id}/merge_request/{subscribable_id}/subscription'.format(id='id_example', subscribable_id='subscribable_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_v3_projects_id_merge_requests(client):
    """Test case for post_v3_projects_id_merge_requests

    Create a merge request
    """
    body = openapi_server.PostV3ProjectsIdMergeRequestsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/projects/{id}/merge_requests'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_v3_projects_id_merge_requests_merge_request_id_add_spent_time(client):
    """Test case for post_v3_projects_id_merge_requests_merge_request_id_add_spent_time

    Add spent time for a project merge_request
    """
    body = openapi_server.PostV3ProjectsIdIssuesIssueIdAddSpentTimeRequest()
    headers = { 
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/projects/{id}/merge_requests/{merge_request_id}/add_spent_time'.format(id='id_example', merge_request_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_v3_projects_id_merge_requests_merge_request_id_award_emoji(client):
    """Test case for post_v3_projects_id_merge_requests_merge_request_id_award_emoji

    Award a new Emoji
    """
    body = openapi_server.PostV3ProjectsIdIssuesIssueIdAwardEmojiRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/projects/{id}/merge_requests/{merge_request_id}/award_emoji'.format(id=56, merge_request_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_v3_projects_id_merge_requests_merge_request_id_cancel_merge_when_build_succeeds(client):
    """Test case for post_v3_projects_id_merge_requests_merge_request_id_cancel_merge_when_build_succeeds

    Cancel merge if \"Merge When Pipeline Succeeds\" is enabled
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/projects/{id}/merge_requests/{merge_request_id}/cancel_merge_when_build_succeeds'.format(id='id_example', merge_request_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_v3_projects_id_merge_requests_merge_request_id_comments(client):
    """Test case for post_v3_projects_id_merge_requests_merge_request_id_comments

    Post a comment to a merge request
    """
    body = openapi_server.PostV3ProjectsIdMergeRequestMergeRequestIdCommentsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/projects/{id}/merge_requests/{merge_request_id}/comments'.format(id='id_example', merge_request_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_v3_projects_id_merge_requests_merge_request_id_notes_note_id_award_emoji(client):
    """Test case for post_v3_projects_id_merge_requests_merge_request_id_notes_note_id_award_emoji

    Award a new Emoji
    """
    body = openapi_server.PostV3ProjectsIdIssuesIssueIdAwardEmojiRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/projects/{id}/merge_requests/{merge_request_id}/notes/{note_id}/award_emoji'.format(id=56, merge_request_id=56, note_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_v3_projects_id_merge_requests_merge_request_id_reset_spent_time(client):
    """Test case for post_v3_projects_id_merge_requests_merge_request_id_reset_spent_time

    Reset spent time for a project merge_request
    """
    headers = { 
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/projects/{id}/merge_requests/{merge_request_id}/reset_spent_time'.format(id='id_example', merge_request_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_v3_projects_id_merge_requests_merge_request_id_reset_time_estimate(client):
    """Test case for post_v3_projects_id_merge_requests_merge_request_id_reset_time_estimate

    Reset the time estimate for a project merge_request
    """
    headers = { 
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/projects/{id}/merge_requests/{merge_request_id}/reset_time_estimate'.format(id='id_example', merge_request_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_v3_projects_id_merge_requests_merge_request_id_time_estimate(client):
    """Test case for post_v3_projects_id_merge_requests_merge_request_id_time_estimate

    Set a time estimate for a project merge_request
    """
    body = openapi_server.PostV3ProjectsIdIssuesIssueIdAddSpentTimeRequest()
    headers = { 
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/projects/{id}/merge_requests/{merge_request_id}/time_estimate'.format(id='id_example', merge_request_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_v3_projects_id_merge_requests_merge_request_id_todo(client):
    """Test case for post_v3_projects_id_merge_requests_merge_request_id_todo

    Create a todo on an issuable
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/projects/{id}/merge_requests/{merge_request_id}/todo'.format(id='id_example', merge_request_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_v3_projects_id_merge_requests_noteable_id_notes(client):
    """Test case for post_v3_projects_id_merge_requests_noteable_id_notes

    Create a new +noteable+ note
    """
    body = openapi_server.PostV3ProjectsIdIssuesNoteableIdNotesRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/projects/{id}/merge_requests/{noteable_id}/notes'.format(id='id_example', noteable_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_v3_projects_id_merge_requests_subscribable_id_subscription(client):
    """Test case for post_v3_projects_id_merge_requests_subscribable_id_subscription

    Subscribe to a resource
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/projects/{id}/merge_requests/{subscribable_id}/subscription'.format(id='id_example', subscribable_id='subscribable_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_v3_projects_id_milestones(client):
    """Test case for post_v3_projects_id_milestones

    Create a new project milestone
    """
    body = openapi_server.PostV3ProjectsIdMilestonesRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/projects/{id}/milestones'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_v3_projects_id_pipeline(client):
    """Test case for post_v3_projects_id_pipeline

    Create a new pipeline
    """
    body = openapi_server.PostV3ProjectsIdPipelineRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/projects/{id}/pipeline'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_v3_projects_id_pipelines_pipeline_id_cancel(client):
    """Test case for post_v3_projects_id_pipelines_pipeline_id_cancel

    Cancel all builds in the pipeline
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/projects/{id}/pipelines/{pipeline_id}/cancel'.format(id='id_example', pipeline_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_v3_projects_id_pipelines_pipeline_id_retry(client):
    """Test case for post_v3_projects_id_pipelines_pipeline_id_retry

    Retry failed builds in the pipeline
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/projects/{id}/pipelines/{pipeline_id}/retry'.format(id='id_example', pipeline_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_v3_projects_id_ref_reftrigger_builds(client):
    """Test case for post_v3_projects_id_ref_reftrigger_builds

    Trigger a GitLab project build
    """
    body = openapi_server.PostV3ProjectsIdRefRefTriggerBuildsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/projects/{id}/(ref/{ref}/)trigger/builds'.format(id='id_example', ref='ref_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_v3_projects_id_repository_branches(client):
    """Test case for post_v3_projects_id_repository_branches

    Create branch
    """
    body = openapi_server.PostV3ProjectsIdRepositoryBranchesRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/projects/{id}/repository/branches'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_v3_projects_id_repository_commits(client):
    """Test case for post_v3_projects_id_repository_commits

    Commit multiple file changes as one commit
    """
    body = openapi_server.PostV3ProjectsIdRepositoryCommitsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/projects/{id}/repository/commits'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_v3_projects_id_repository_commits_sha_cherry_pick(client):
    """Test case for post_v3_projects_id_repository_commits_sha_cherry_pick

    Cherry pick commit into a branch
    """
    body = openapi_server.PostV3ProjectsIdRepositoryCommitsShaCherryPickRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/projects/{id}/repository/commits/{sha}/cherry_pick'.format(id='id_example', sha='sha_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_v3_projects_id_repository_commits_sha_comments(client):
    """Test case for post_v3_projects_id_repository_commits_sha_comments

    Post comment to commit
    """
    body = openapi_server.PostV3ProjectsIdRepositoryCommitsShaCommentsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/projects/{id}/repository/commits/{sha}/comments'.format(id='id_example', sha='sha_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_v3_projects_id_repository_files(client):
    """Test case for post_v3_projects_id_repository_files

    Create new file in repository
    """
    body = openapi_server.PutV3ProjectsIdRepositoryFilesRequest()
    headers = { 
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/projects/{id}/repository/files'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_v3_projects_id_repository_tags(client):
    """Test case for post_v3_projects_id_repository_tags

    Create a new repository tag
    """
    body = openapi_server.PostV3ProjectsIdRepositoryTagsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/projects/{id}/repository/tags'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_v3_projects_id_repository_tags_tag_name_release(client):
    """Test case for post_v3_projects_id_repository_tags_tag_name_release

    Add a release note to a tag
    """
    body = openapi_server.PutV3ProjectsIdRepositoryTagsTagNameReleaseRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/projects/{id}/repository/tags/{tag_name}/release'.format(id='id_example', tag_name='tag_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_v3_projects_id_runners(client):
    """Test case for post_v3_projects_id_runners

    Enable a runner for a project
    """
    body = openapi_server.PostV3ProjectsIdRunnersRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/projects/{id}/runners'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_v3_projects_id_services_mattermost_slash_commands_trigger(client):
    """Test case for post_v3_projects_id_services_mattermost_slash_commands_trigger

    Trigger a slash command for mattermost-slash-commands
    """
    body = openapi_server.PutV3ProjectsIdServicesMattermostSlashCommandsRequest()
    headers = { 
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/projects/{id}/services/mattermost_slash_commands/trigger'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_v3_projects_id_services_slack_slash_commands_trigger(client):
    """Test case for post_v3_projects_id_services_slack_slash_commands_trigger

    Trigger a slash command for slack-slash-commands
    """
    body = openapi_server.PutV3ProjectsIdServicesSlackSlashCommandsRequest()
    headers = { 
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/projects/{id}/services/slack_slash_commands/trigger'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_v3_projects_id_share(client):
    """Test case for post_v3_projects_id_share

    Share the project with a group
    """
    body = openapi_server.PostV3ProjectsIdShareRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/projects/{id}/share'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_v3_projects_id_snippets(client):
    """Test case for post_v3_projects_id_snippets

    Create a new project snippet
    """
    body = openapi_server.PostV3ProjectsIdSnippetsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/projects/{id}/snippets'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_v3_projects_id_snippets_noteable_id_notes(client):
    """Test case for post_v3_projects_id_snippets_noteable_id_notes

    Create a new +noteable+ note
    """
    body = openapi_server.PostV3ProjectsIdIssuesNoteableIdNotesRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/projects/{id}/snippets/{noteable_id}/notes'.format(id='id_example', noteable_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_v3_projects_id_snippets_snippet_id_award_emoji(client):
    """Test case for post_v3_projects_id_snippets_snippet_id_award_emoji

    Award a new Emoji
    """
    body = openapi_server.PostV3ProjectsIdIssuesIssueIdAwardEmojiRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/projects/{id}/snippets/{snippet_id}/award_emoji'.format(id=56, snippet_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_v3_projects_id_snippets_snippet_id_notes_note_id_award_emoji(client):
    """Test case for post_v3_projects_id_snippets_snippet_id_notes_note_id_award_emoji

    Award a new Emoji
    """
    body = openapi_server.PostV3ProjectsIdIssuesIssueIdAwardEmojiRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/projects/{id}/snippets/{snippet_id}/notes/{note_id}/award_emoji'.format(id=56, snippet_id=56, note_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_v3_projects_id_star(client):
    """Test case for post_v3_projects_id_star

    Star a project
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/projects/{id}/star'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_v3_projects_id_statuses_sha(client):
    """Test case for post_v3_projects_id_statuses_sha

    Post status to a commit
    """
    body = openapi_server.PostV3ProjectsIdStatusesShaRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/projects/{id}/statuses/{sha}'.format(id='id_example', sha='sha_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_v3_projects_id_triggers(client):
    """Test case for post_v3_projects_id_triggers

    Create a trigger
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/projects/{id}/triggers'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_v3_projects_id_unarchive(client):
    """Test case for post_v3_projects_id_unarchive

    Unarchive a project
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/projects/{id}/unarchive'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_post_v3_projects_id_uploads(client):
    """Test case for post_v3_projects_id_uploads

    Upload a file
    """
    body = openapi_server.PostV3ProjectsIdUploadsRequest()
    headers = { 
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/projects/{id}/uploads'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_v3_projects_id_variables(client):
    """Test case for post_v3_projects_id_variables

    Create a new variable in a project
    """
    body = openapi_server.PostV3ProjectsIdVariablesRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/projects/{id}/variables'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_v3_projects_user_user_id(client):
    """Test case for post_v3_projects_user_user_id

    Create new project for a specified user. Only available to admin users.
    """
    body = openapi_server.PostV3ProjectsUserUserIdRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/projects/user/{user_id}'.format(user_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_v3_projects_id(client):
    """Test case for put_v3_projects_id

    Update an existing project
    """
    body = openapi_server.PutV3ProjectsIdRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/projects/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_v3_projects_id_access_requests_user_id_approve(client):
    """Test case for put_v3_projects_id_access_requests_user_id_approve

    Approves an access request for the given user.
    """
    body = openapi_server.PutV3GroupsIdAccessRequestsUserIdApproveRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/projects/{id}/access_requests/{user_id}/approve'.format(id='id_example', user_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_v3_projects_id_boards_board_id_lists_list_id(client):
    """Test case for put_v3_projects_id_boards_board_id_lists_list_id

    Moves a board list to a new position
    """
    body = openapi_server.PutV3ProjectsIdBoardsBoardIdListsListIdRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/projects/{id}/boards/{board_id}/lists/{list_id}'.format(id='id_example', board_id=56, list_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_v3_projects_id_environments_environment_id(client):
    """Test case for put_v3_projects_id_environments_environment_id

    Updates an existing environment
    """
    body = openapi_server.PutV3ProjectsIdEnvironmentsEnvironmentIdRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/projects/{id}/environments/{environment_id}'.format(id='id_example', environment_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_v3_projects_id_hooks_hook_id(client):
    """Test case for put_v3_projects_id_hooks_hook_id

    Update an existing project hook
    """
    body = openapi_server.PostV3ProjectsIdHooksRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/projects/{id}/hooks/{hook_id}'.format(id='id_example', hook_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_v3_projects_id_issues_issue_id(client):
    """Test case for put_v3_projects_id_issues_issue_id

    Update an existing issue
    """
    body = openapi_server.PutV3ProjectsIdIssuesIssueIdRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/projects/{id}/issues/{issue_id}'.format(id='id_example', issue_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_v3_projects_id_issues_noteable_id_notes_note_id(client):
    """Test case for put_v3_projects_id_issues_noteable_id_notes_note_id

    Update an existing +noteable+ note
    """
    body = openapi_server.PutV3ProjectsIdIssuesNoteableIdNotesNoteIdRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/projects/{id}/issues/{noteable_id}/notes/{note_id}'.format(id='id_example', noteable_id=56, note_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_v3_projects_id_labels(client):
    """Test case for put_v3_projects_id_labels

    Update an existing label. At least one optional parameter is required.
    """
    body = openapi_server.PutV3ProjectsIdLabelsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/projects/{id}/labels'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_v3_projects_id_members_user_id(client):
    """Test case for put_v3_projects_id_members_user_id

    Updates a member of a group or project.
    """
    body = openapi_server.PutV3GroupsIdMembersUserIdRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/projects/{id}/members/{user_id}'.format(id='id_example', user_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_v3_projects_id_merge_request_merge_request_id(client):
    """Test case for put_v3_projects_id_merge_request_merge_request_id

    Update a merge request
    """
    body = openapi_server.PutV3ProjectsIdMergeRequestMergeRequestIdRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/projects/{id}/merge_request/{merge_request_id}'.format(id='id_example', merge_request_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_v3_projects_id_merge_request_merge_request_id_merge(client):
    """Test case for put_v3_projects_id_merge_request_merge_request_id_merge

    Merge a merge request
    """
    body = openapi_server.PutV3ProjectsIdMergeRequestMergeRequestIdMergeRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/projects/{id}/merge_request/{merge_request_id}/merge'.format(id='id_example', merge_request_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_v3_projects_id_merge_requests_merge_request_id(client):
    """Test case for put_v3_projects_id_merge_requests_merge_request_id

    Update a merge request
    """
    body = openapi_server.PutV3ProjectsIdMergeRequestMergeRequestIdRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/projects/{id}/merge_requests/{merge_request_id}'.format(id='id_example', merge_request_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_v3_projects_id_merge_requests_merge_request_id_merge(client):
    """Test case for put_v3_projects_id_merge_requests_merge_request_id_merge

    Merge a merge request
    """
    body = openapi_server.PutV3ProjectsIdMergeRequestMergeRequestIdMergeRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/projects/{id}/merge_requests/{merge_request_id}/merge'.format(id='id_example', merge_request_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_v3_projects_id_merge_requests_noteable_id_notes_note_id(client):
    """Test case for put_v3_projects_id_merge_requests_noteable_id_notes_note_id

    Update an existing +noteable+ note
    """
    body = openapi_server.PutV3ProjectsIdIssuesNoteableIdNotesNoteIdRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/projects/{id}/merge_requests/{noteable_id}/notes/{note_id}'.format(id='id_example', noteable_id=56, note_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_v3_projects_id_milestones_milestone_id(client):
    """Test case for put_v3_projects_id_milestones_milestone_id

    Update an existing project milestone
    """
    body = openapi_server.PutV3ProjectsIdMilestonesMilestoneIdRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/projects/{id}/milestones/{milestone_id}'.format(id='id_example', milestone_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_v3_projects_id_notification_settings(client):
    """Test case for put_v3_projects_id_notification_settings

    Update project level notification level settings, defaults to Global
    """
    body = openapi_server.PutV3ProjectsIdNotificationSettingsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/projects/{id}/notification_settings'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_v3_projects_id_repository_branches_branch_protect(client):
    """Test case for put_v3_projects_id_repository_branches_branch_protect

    Protect a single branch
    """
    body = openapi_server.PutV3ProjectsIdRepositoryBranchesBranchProtectRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/projects/{id}/repository/branches/{branch}/protect'.format(id='id_example', branch='branch_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_v3_projects_id_repository_branches_branch_unprotect(client):
    """Test case for put_v3_projects_id_repository_branches_branch_unprotect

    Unprotect a single branch
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/projects/{id}/repository/branches/{branch}/unprotect'.format(id='id_example', branch='branch_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_v3_projects_id_repository_files(client):
    """Test case for put_v3_projects_id_repository_files

    Update existing file in repository
    """
    body = openapi_server.PutV3ProjectsIdRepositoryFilesRequest()
    headers = { 
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/projects/{id}/repository/files'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_v3_projects_id_repository_tags_tag_name_release(client):
    """Test case for put_v3_projects_id_repository_tags_tag_name_release

    Update a tag's release note
    """
    body = openapi_server.PutV3ProjectsIdRepositoryTagsTagNameReleaseRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/projects/{id}/repository/tags/{tag_name}/release'.format(id='id_example', tag_name='tag_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_v3_projects_id_services_asana(client):
    """Test case for put_v3_projects_id_services_asana

    Set asana service for project
    """
    body = openapi_server.PutV3ProjectsIdServicesAsanaRequest()
    headers = { 
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/projects/{id}/services/asana'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_v3_projects_id_services_assembla(client):
    """Test case for put_v3_projects_id_services_assembla

    Set assembla service for project
    """
    body = openapi_server.PutV3ProjectsIdServicesAssemblaRequest()
    headers = { 
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/projects/{id}/services/assembla'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_v3_projects_id_services_bamboo(client):
    """Test case for put_v3_projects_id_services_bamboo

    Set bamboo service for project
    """
    body = openapi_server.PutV3ProjectsIdServicesBambooRequest()
    headers = { 
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/projects/{id}/services/bamboo'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_v3_projects_id_services_bugzilla(client):
    """Test case for put_v3_projects_id_services_bugzilla

    Set bugzilla service for project
    """
    body = openapi_server.PutV3ProjectsIdServicesBugzillaRequest()
    headers = { 
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/projects/{id}/services/bugzilla'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_v3_projects_id_services_buildkite(client):
    """Test case for put_v3_projects_id_services_buildkite

    Set buildkite service for project
    """
    body = openapi_server.PutV3ProjectsIdServicesBuildkiteRequest()
    headers = { 
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/projects/{id}/services/buildkite'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_v3_projects_id_services_builds_email(client):
    """Test case for put_v3_projects_id_services_builds_email

    Set builds-email service for project
    """
    body = openapi_server.PutV3ProjectsIdServicesBuildsEmailRequest()
    headers = { 
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/projects/{id}/services/builds-email'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_v3_projects_id_services_campfire(client):
    """Test case for put_v3_projects_id_services_campfire

    Set campfire service for project
    """
    body = openapi_server.PutV3ProjectsIdServicesCampfireRequest()
    headers = { 
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/projects/{id}/services/campfire'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_v3_projects_id_services_custom_issue_tracker(client):
    """Test case for put_v3_projects_id_services_custom_issue_tracker

    Set custom-issue-tracker service for project
    """
    body = openapi_server.PutV3ProjectsIdServicesBugzillaRequest()
    headers = { 
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/projects/{id}/services/custom-issue-tracker'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_v3_projects_id_services_drone_ci(client):
    """Test case for put_v3_projects_id_services_drone_ci

    Set drone-ci service for project
    """
    body = openapi_server.PutV3ProjectsIdServicesDroneCiRequest()
    headers = { 
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/projects/{id}/services/drone-ci'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_v3_projects_id_services_emails_on_push(client):
    """Test case for put_v3_projects_id_services_emails_on_push

    Set emails-on-push service for project
    """
    body = openapi_server.PutV3ProjectsIdServicesEmailsOnPushRequest()
    headers = { 
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/projects/{id}/services/emails-on-push'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_v3_projects_id_services_external_wiki(client):
    """Test case for put_v3_projects_id_services_external_wiki

    Set external-wiki service for project
    """
    body = openapi_server.PutV3ProjectsIdServicesExternalWikiRequest()
    headers = { 
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/projects/{id}/services/external-wiki'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_v3_projects_id_services_flowdock(client):
    """Test case for put_v3_projects_id_services_flowdock

    Set flowdock service for project
    """
    body = openapi_server.PutV3ProjectsIdServicesFlowdockRequest()
    headers = { 
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/projects/{id}/services/flowdock'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_v3_projects_id_services_gemnasium(client):
    """Test case for put_v3_projects_id_services_gemnasium

    Set gemnasium service for project
    """
    body = openapi_server.PutV3ProjectsIdServicesGemnasiumRequest()
    headers = { 
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/projects/{id}/services/gemnasium'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_v3_projects_id_services_hipchat(client):
    """Test case for put_v3_projects_id_services_hipchat

    Set hipchat service for project
    """
    body = openapi_server.PutV3ProjectsIdServicesHipchatRequest()
    headers = { 
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/projects/{id}/services/hipchat'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_v3_projects_id_services_irker(client):
    """Test case for put_v3_projects_id_services_irker

    Set irker service for project
    """
    body = openapi_server.PutV3ProjectsIdServicesIrkerRequest()
    headers = { 
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/projects/{id}/services/irker'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_v3_projects_id_services_jira(client):
    """Test case for put_v3_projects_id_services_jira

    Set jira service for project
    """
    body = openapi_server.PutV3ProjectsIdServicesJiraRequest()
    headers = { 
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/projects/{id}/services/jira'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_v3_projects_id_services_kubernetes(client):
    """Test case for put_v3_projects_id_services_kubernetes

    Set kubernetes service for project
    """
    body = openapi_server.PutV3ProjectsIdServicesKubernetesRequest()
    headers = { 
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/projects/{id}/services/kubernetes'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_v3_projects_id_services_mattermost(client):
    """Test case for put_v3_projects_id_services_mattermost

    Set mattermost service for project
    """
    body = openapi_server.PutV3ProjectsIdServicesMattermostRequest()
    headers = { 
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/projects/{id}/services/mattermost'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_v3_projects_id_services_mattermost_slash_commands(client):
    """Test case for put_v3_projects_id_services_mattermost_slash_commands

    Set mattermost-slash-commands service for project
    """
    body = openapi_server.PutV3ProjectsIdServicesMattermostSlashCommandsRequest()
    headers = { 
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/projects/{id}/services/mattermost-slash-commands'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_v3_projects_id_services_pipelines_email(client):
    """Test case for put_v3_projects_id_services_pipelines_email

    Set pipelines-email service for project
    """
    body = openapi_server.PutV3ProjectsIdServicesPipelinesEmailRequest()
    headers = { 
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/projects/{id}/services/pipelines-email'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_v3_projects_id_services_pivotaltracker(client):
    """Test case for put_v3_projects_id_services_pivotaltracker

    Set pivotaltracker service for project
    """
    body = openapi_server.PutV3ProjectsIdServicesPivotaltrackerRequest()
    headers = { 
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/projects/{id}/services/pivotaltracker'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_v3_projects_id_services_pushover(client):
    """Test case for put_v3_projects_id_services_pushover

    Set pushover service for project
    """
    body = openapi_server.PutV3ProjectsIdServicesPushoverRequest()
    headers = { 
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/projects/{id}/services/pushover'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_v3_projects_id_services_redmine(client):
    """Test case for put_v3_projects_id_services_redmine

    Set redmine service for project
    """
    body = openapi_server.PutV3ProjectsIdServicesRedmineRequest()
    headers = { 
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/projects/{id}/services/redmine'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_v3_projects_id_services_slack(client):
    """Test case for put_v3_projects_id_services_slack

    Set slack service for project
    """
    body = openapi_server.PutV3ProjectsIdServicesSlackRequest()
    headers = { 
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/projects/{id}/services/slack'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_v3_projects_id_services_slack_slash_commands(client):
    """Test case for put_v3_projects_id_services_slack_slash_commands

    Set slack-slash-commands service for project
    """
    body = openapi_server.PutV3ProjectsIdServicesSlackSlashCommandsRequest()
    headers = { 
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/projects/{id}/services/slack-slash-commands'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_v3_projects_id_services_teamcity(client):
    """Test case for put_v3_projects_id_services_teamcity

    Set teamcity service for project
    """
    body = openapi_server.PutV3ProjectsIdServicesTeamcityRequest()
    headers = { 
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/projects/{id}/services/teamcity'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_v3_projects_id_snippets_noteable_id_notes_note_id(client):
    """Test case for put_v3_projects_id_snippets_noteable_id_notes_note_id

    Update an existing +noteable+ note
    """
    body = openapi_server.PutV3ProjectsIdIssuesNoteableIdNotesNoteIdRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/projects/{id}/snippets/{noteable_id}/notes/{note_id}'.format(id='id_example', noteable_id=56, note_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_v3_projects_id_snippets_snippet_id(client):
    """Test case for put_v3_projects_id_snippets_snippet_id

    Update an existing project snippet
    """
    body = openapi_server.PutV3ProjectsIdSnippetsSnippetIdRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/projects/{id}/snippets/{snippet_id}'.format(id='id_example', snippet_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_v3_projects_id_variables_key(client):
    """Test case for put_v3_projects_id_variables_key

    Update an existing variable from a project
    """
    body = openapi_server.PutV3ProjectsIdVariablesKeyRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/projects/{id}/variables/{key}'.format(id='id_example', key='key_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

