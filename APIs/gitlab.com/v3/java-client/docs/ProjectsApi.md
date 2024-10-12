# ProjectsApi

All URIs are relative to *https://gitlab.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteV3ProjectsId**](ProjectsApi.md#deleteV3ProjectsId) | **DELETE** /v3/projects/{id} | Remove a project |
| [**deleteV3ProjectsIdAccessRequestsUserId**](ProjectsApi.md#deleteV3ProjectsIdAccessRequestsUserId) | **DELETE** /v3/projects/{id}/access_requests/{user_id} | Denies an access request for the given user. |
| [**deleteV3ProjectsIdBoardsBoardIdListsListId**](ProjectsApi.md#deleteV3ProjectsIdBoardsBoardIdListsListId) | **DELETE** /v3/projects/{id}/boards/{board_id}/lists/{list_id} | Delete a board list |
| [**deleteV3ProjectsIdDeployKeysKeyId**](ProjectsApi.md#deleteV3ProjectsIdDeployKeysKeyId) | **DELETE** /v3/projects/{id}/deploy_keys/{key_id} | Delete deploy key for a project |
| [**deleteV3ProjectsIdDeployKeysKeyIdDisable**](ProjectsApi.md#deleteV3ProjectsIdDeployKeysKeyIdDisable) | **DELETE** /v3/projects/{id}/deploy_keys/{key_id}/disable | Disable a deploy key for a project |
| [**deleteV3ProjectsIdEnvironmentsEnvironmentId**](ProjectsApi.md#deleteV3ProjectsIdEnvironmentsEnvironmentId) | **DELETE** /v3/projects/{id}/environments/{environment_id} | Deletes an existing environment |
| [**deleteV3ProjectsIdFork**](ProjectsApi.md#deleteV3ProjectsIdFork) | **DELETE** /v3/projects/{id}/fork | Remove a forked_from relationship |
| [**deleteV3ProjectsIdHooksHookId**](ProjectsApi.md#deleteV3ProjectsIdHooksHookId) | **DELETE** /v3/projects/{id}/hooks/{hook_id} | Deletes project hook |
| [**deleteV3ProjectsIdIssuesIssueId**](ProjectsApi.md#deleteV3ProjectsIdIssuesIssueId) | **DELETE** /v3/projects/{id}/issues/{issue_id} | Delete a project issue |
| [**deleteV3ProjectsIdIssuesIssueIdAwardEmojiAwardId**](ProjectsApi.md#deleteV3ProjectsIdIssuesIssueIdAwardEmojiAwardId) | **DELETE** /v3/projects/{id}/issues/{issue_id}/award_emoji/{award_id} | Delete a +awardables+ award emoji |
| [**deleteV3ProjectsIdIssuesIssueIdNotesNoteIdAwardEmojiAwardId**](ProjectsApi.md#deleteV3ProjectsIdIssuesIssueIdNotesNoteIdAwardEmojiAwardId) | **DELETE** /v3/projects/{id}/issues/{issue_id}/notes/{note_id}/award_emoji/{award_id} | Delete a +awardables+ award emoji |
| [**deleteV3ProjectsIdIssuesNoteableIdNotesNoteId**](ProjectsApi.md#deleteV3ProjectsIdIssuesNoteableIdNotesNoteId) | **DELETE** /v3/projects/{id}/issues/{noteable_id}/notes/{note_id} | Delete a +noteable+ note |
| [**deleteV3ProjectsIdIssuesSubscribableIdSubscription**](ProjectsApi.md#deleteV3ProjectsIdIssuesSubscribableIdSubscription) | **DELETE** /v3/projects/{id}/issues/{subscribable_id}/subscription | Unsubscribe from a resource |
| [**deleteV3ProjectsIdKeysKeyId**](ProjectsApi.md#deleteV3ProjectsIdKeysKeyId) | **DELETE** /v3/projects/{id}/keys/{key_id} | Delete deploy key for a project |
| [**deleteV3ProjectsIdKeysKeyIdDisable**](ProjectsApi.md#deleteV3ProjectsIdKeysKeyIdDisable) | **DELETE** /v3/projects/{id}/keys/{key_id}/disable | Disable a deploy key for a project |
| [**deleteV3ProjectsIdLabels**](ProjectsApi.md#deleteV3ProjectsIdLabels) | **DELETE** /v3/projects/{id}/labels | Delete an existing label |
| [**deleteV3ProjectsIdLabelsSubscribableIdSubscription**](ProjectsApi.md#deleteV3ProjectsIdLabelsSubscribableIdSubscription) | **DELETE** /v3/projects/{id}/labels/{subscribable_id}/subscription | Unsubscribe from a resource |
| [**deleteV3ProjectsIdMembersUserId**](ProjectsApi.md#deleteV3ProjectsIdMembersUserId) | **DELETE** /v3/projects/{id}/members/{user_id} | Removes a user from a group or project. |
| [**deleteV3ProjectsIdMergeRequestSubscribableIdSubscription**](ProjectsApi.md#deleteV3ProjectsIdMergeRequestSubscribableIdSubscription) | **DELETE** /v3/projects/{id}/merge_request/{subscribable_id}/subscription | Unsubscribe from a resource |
| [**deleteV3ProjectsIdMergeRequestsMergeRequestId**](ProjectsApi.md#deleteV3ProjectsIdMergeRequestsMergeRequestId) | **DELETE** /v3/projects/{id}/merge_requests/{merge_request_id} | Delete a merge request |
| [**deleteV3ProjectsIdMergeRequestsMergeRequestIdAwardEmojiAwardId**](ProjectsApi.md#deleteV3ProjectsIdMergeRequestsMergeRequestIdAwardEmojiAwardId) | **DELETE** /v3/projects/{id}/merge_requests/{merge_request_id}/award_emoji/{award_id} | Delete a +awardables+ award emoji |
| [**deleteV3ProjectsIdMergeRequestsMergeRequestIdNotesNoteIdAwardEmojiAwardId**](ProjectsApi.md#deleteV3ProjectsIdMergeRequestsMergeRequestIdNotesNoteIdAwardEmojiAwardId) | **DELETE** /v3/projects/{id}/merge_requests/{merge_request_id}/notes/{note_id}/award_emoji/{award_id} | Delete a +awardables+ award emoji |
| [**deleteV3ProjectsIdMergeRequestsNoteableIdNotesNoteId**](ProjectsApi.md#deleteV3ProjectsIdMergeRequestsNoteableIdNotesNoteId) | **DELETE** /v3/projects/{id}/merge_requests/{noteable_id}/notes/{note_id} | Delete a +noteable+ note |
| [**deleteV3ProjectsIdMergeRequestsSubscribableIdSubscription**](ProjectsApi.md#deleteV3ProjectsIdMergeRequestsSubscribableIdSubscription) | **DELETE** /v3/projects/{id}/merge_requests/{subscribable_id}/subscription | Unsubscribe from a resource |
| [**deleteV3ProjectsIdRepositoryBranchesBranch**](ProjectsApi.md#deleteV3ProjectsIdRepositoryBranchesBranch) | **DELETE** /v3/projects/{id}/repository/branches/{branch} | Delete a branch |
| [**deleteV3ProjectsIdRepositoryFiles**](ProjectsApi.md#deleteV3ProjectsIdRepositoryFiles) | **DELETE** /v3/projects/{id}/repository/files | Delete an existing file in repository |
| [**deleteV3ProjectsIdRepositoryMergedBranches**](ProjectsApi.md#deleteV3ProjectsIdRepositoryMergedBranches) | **DELETE** /v3/projects/{id}/repository/merged_branches |  |
| [**deleteV3ProjectsIdRepositoryTagsTagName**](ProjectsApi.md#deleteV3ProjectsIdRepositoryTagsTagName) | **DELETE** /v3/projects/{id}/repository/tags/{tag_name} | Delete a repository tag |
| [**deleteV3ProjectsIdRunnersRunnerId**](ProjectsApi.md#deleteV3ProjectsIdRunnersRunnerId) | **DELETE** /v3/projects/{id}/runners/{runner_id} | Disable project&#39;s runner |
| [**deleteV3ProjectsIdServicesServiceSlug**](ProjectsApi.md#deleteV3ProjectsIdServicesServiceSlug) | **DELETE** /v3/projects/{id}/services/{service_slug} | Delete a service for project |
| [**deleteV3ProjectsIdShareGroupId**](ProjectsApi.md#deleteV3ProjectsIdShareGroupId) | **DELETE** /v3/projects/{id}/share/{group_id} |  |
| [**deleteV3ProjectsIdSnippetsNoteableIdNotesNoteId**](ProjectsApi.md#deleteV3ProjectsIdSnippetsNoteableIdNotesNoteId) | **DELETE** /v3/projects/{id}/snippets/{noteable_id}/notes/{note_id} | Delete a +noteable+ note |
| [**deleteV3ProjectsIdSnippetsSnippetId**](ProjectsApi.md#deleteV3ProjectsIdSnippetsSnippetId) | **DELETE** /v3/projects/{id}/snippets/{snippet_id} | Delete a project snippet |
| [**deleteV3ProjectsIdSnippetsSnippetIdAwardEmojiAwardId**](ProjectsApi.md#deleteV3ProjectsIdSnippetsSnippetIdAwardEmojiAwardId) | **DELETE** /v3/projects/{id}/snippets/{snippet_id}/award_emoji/{award_id} | Delete a +awardables+ award emoji |
| [**deleteV3ProjectsIdSnippetsSnippetIdNotesNoteIdAwardEmojiAwardId**](ProjectsApi.md#deleteV3ProjectsIdSnippetsSnippetIdNotesNoteIdAwardEmojiAwardId) | **DELETE** /v3/projects/{id}/snippets/{snippet_id}/notes/{note_id}/award_emoji/{award_id} | Delete a +awardables+ award emoji |
| [**deleteV3ProjectsIdStar**](ProjectsApi.md#deleteV3ProjectsIdStar) | **DELETE** /v3/projects/{id}/star | Unstar a project |
| [**deleteV3ProjectsIdTriggersToken**](ProjectsApi.md#deleteV3ProjectsIdTriggersToken) | **DELETE** /v3/projects/{id}/triggers/{token} | Delete a trigger |
| [**deleteV3ProjectsIdVariablesKey**](ProjectsApi.md#deleteV3ProjectsIdVariablesKey) | **DELETE** /v3/projects/{id}/variables/{key} | Delete an existing variable from a project |
| [**getV3Projects**](ProjectsApi.md#getV3Projects) | **GET** /v3/projects | Get a projects list for authenticated user |
| [**getV3ProjectsAll**](ProjectsApi.md#getV3ProjectsAll) | **GET** /v3/projects/all | Get all projects for admin user |
| [**getV3ProjectsId**](ProjectsApi.md#getV3ProjectsId) | **GET** /v3/projects/{id} | Get a single project |
| [**getV3ProjectsIdAccessRequests**](ProjectsApi.md#getV3ProjectsIdAccessRequests) | **GET** /v3/projects/{id}/access_requests | Gets a list of access requests for a project. |
| [**getV3ProjectsIdBoards**](ProjectsApi.md#getV3ProjectsIdBoards) | **GET** /v3/projects/{id}/boards | Get all project boards |
| [**getV3ProjectsIdBoardsBoardIdLists**](ProjectsApi.md#getV3ProjectsIdBoardsBoardIdLists) | **GET** /v3/projects/{id}/boards/{board_id}/lists | Get the lists of a project board |
| [**getV3ProjectsIdBoardsBoardIdListsListId**](ProjectsApi.md#getV3ProjectsIdBoardsBoardIdListsListId) | **GET** /v3/projects/{id}/boards/{board_id}/lists/{list_id} | Get a list of a project board |
| [**getV3ProjectsIdBuilds**](ProjectsApi.md#getV3ProjectsIdBuilds) | **GET** /v3/projects/{id}/builds | Get a project builds |
| [**getV3ProjectsIdBuildsArtifactsRefNameDownload**](ProjectsApi.md#getV3ProjectsIdBuildsArtifactsRefNameDownload) | **GET** /v3/projects/{id}/builds/artifacts/{ref_name}/download | Download the artifacts file from build |
| [**getV3ProjectsIdBuildsBuildId**](ProjectsApi.md#getV3ProjectsIdBuildsBuildId) | **GET** /v3/projects/{id}/builds/{build_id} | Get a specific build of a project |
| [**getV3ProjectsIdBuildsBuildIdArtifacts**](ProjectsApi.md#getV3ProjectsIdBuildsBuildIdArtifacts) | **GET** /v3/projects/{id}/builds/{build_id}/artifacts | Download the artifacts file from build |
| [**getV3ProjectsIdBuildsBuildIdTrace**](ProjectsApi.md#getV3ProjectsIdBuildsBuildIdTrace) | **GET** /v3/projects/{id}/builds/{build_id}/trace | Get a trace of a specific build of a project |
| [**getV3ProjectsIdDeployKeys**](ProjectsApi.md#getV3ProjectsIdDeployKeys) | **GET** /v3/projects/{id}/deploy_keys | Get a specific project&#39;s deploy keys |
| [**getV3ProjectsIdDeployKeysKeyId**](ProjectsApi.md#getV3ProjectsIdDeployKeysKeyId) | **GET** /v3/projects/{id}/deploy_keys/{key_id} | Get single deploy key |
| [**getV3ProjectsIdDeployments**](ProjectsApi.md#getV3ProjectsIdDeployments) | **GET** /v3/projects/{id}/deployments | Get all deployments of the project |
| [**getV3ProjectsIdDeploymentsDeploymentId**](ProjectsApi.md#getV3ProjectsIdDeploymentsDeploymentId) | **GET** /v3/projects/{id}/deployments/{deployment_id} | Gets a specific deployment |
| [**getV3ProjectsIdEnvironments**](ProjectsApi.md#getV3ProjectsIdEnvironments) | **GET** /v3/projects/{id}/environments | Get all environments of the project |
| [**getV3ProjectsIdEvents**](ProjectsApi.md#getV3ProjectsIdEvents) | **GET** /v3/projects/{id}/events | Get events for a single project |
| [**getV3ProjectsIdHooks**](ProjectsApi.md#getV3ProjectsIdHooks) | **GET** /v3/projects/{id}/hooks | Get project hooks |
| [**getV3ProjectsIdHooksHookId**](ProjectsApi.md#getV3ProjectsIdHooksHookId) | **GET** /v3/projects/{id}/hooks/{hook_id} | Get a project hook |
| [**getV3ProjectsIdIssues**](ProjectsApi.md#getV3ProjectsIdIssues) | **GET** /v3/projects/{id}/issues | Get a list of project issues |
| [**getV3ProjectsIdIssuesIssueId**](ProjectsApi.md#getV3ProjectsIdIssuesIssueId) | **GET** /v3/projects/{id}/issues/{issue_id} | Get a single project issue |
| [**getV3ProjectsIdIssuesIssueIdAwardEmoji**](ProjectsApi.md#getV3ProjectsIdIssuesIssueIdAwardEmoji) | **GET** /v3/projects/{id}/issues/{issue_id}/award_emoji | Get a list of project +awardable+ award emoji |
| [**getV3ProjectsIdIssuesIssueIdAwardEmojiAwardId**](ProjectsApi.md#getV3ProjectsIdIssuesIssueIdAwardEmojiAwardId) | **GET** /v3/projects/{id}/issues/{issue_id}/award_emoji/{award_id} | Get a specific award emoji |
| [**getV3ProjectsIdIssuesIssueIdNotesNoteIdAwardEmoji**](ProjectsApi.md#getV3ProjectsIdIssuesIssueIdNotesNoteIdAwardEmoji) | **GET** /v3/projects/{id}/issues/{issue_id}/notes/{note_id}/award_emoji | Get a list of project +awardable+ award emoji |
| [**getV3ProjectsIdIssuesIssueIdNotesNoteIdAwardEmojiAwardId**](ProjectsApi.md#getV3ProjectsIdIssuesIssueIdNotesNoteIdAwardEmojiAwardId) | **GET** /v3/projects/{id}/issues/{issue_id}/notes/{note_id}/award_emoji/{award_id} | Get a specific award emoji |
| [**getV3ProjectsIdIssuesIssueIdTimeStats**](ProjectsApi.md#getV3ProjectsIdIssuesIssueIdTimeStats) | **GET** /v3/projects/{id}/issues/{issue_id}/time_stats | Show time stats for a project issue |
| [**getV3ProjectsIdIssuesNoteableIdNotes**](ProjectsApi.md#getV3ProjectsIdIssuesNoteableIdNotes) | **GET** /v3/projects/{id}/issues/{noteable_id}/notes | Get a list of project +noteable+ notes |
| [**getV3ProjectsIdIssuesNoteableIdNotesNoteId**](ProjectsApi.md#getV3ProjectsIdIssuesNoteableIdNotesNoteId) | **GET** /v3/projects/{id}/issues/{noteable_id}/notes/{note_id} | Get a single +noteable+ note |
| [**getV3ProjectsIdKeys**](ProjectsApi.md#getV3ProjectsIdKeys) | **GET** /v3/projects/{id}/keys | Get a specific project&#39;s deploy keys |
| [**getV3ProjectsIdKeysKeyId**](ProjectsApi.md#getV3ProjectsIdKeysKeyId) | **GET** /v3/projects/{id}/keys/{key_id} | Get single deploy key |
| [**getV3ProjectsIdLabels**](ProjectsApi.md#getV3ProjectsIdLabels) | **GET** /v3/projects/{id}/labels | Get all labels of the project |
| [**getV3ProjectsIdMembers**](ProjectsApi.md#getV3ProjectsIdMembers) | **GET** /v3/projects/{id}/members | Gets a list of group or project members viewable by the authenticated user. |
| [**getV3ProjectsIdMembersUserId**](ProjectsApi.md#getV3ProjectsIdMembersUserId) | **GET** /v3/projects/{id}/members/{user_id} | Gets a member of a group or project. |
| [**getV3ProjectsIdMergeRequestMergeRequestId**](ProjectsApi.md#getV3ProjectsIdMergeRequestMergeRequestId) | **GET** /v3/projects/{id}/merge_request/{merge_request_id} | Get a single merge request |
| [**getV3ProjectsIdMergeRequestMergeRequestIdChanges**](ProjectsApi.md#getV3ProjectsIdMergeRequestMergeRequestIdChanges) | **GET** /v3/projects/{id}/merge_request/{merge_request_id}/changes | Show the merge request changes |
| [**getV3ProjectsIdMergeRequestMergeRequestIdClosesIssues**](ProjectsApi.md#getV3ProjectsIdMergeRequestMergeRequestIdClosesIssues) | **GET** /v3/projects/{id}/merge_request/{merge_request_id}/closes_issues | List issues that will be closed on merge |
| [**getV3ProjectsIdMergeRequestMergeRequestIdComments**](ProjectsApi.md#getV3ProjectsIdMergeRequestMergeRequestIdComments) | **GET** /v3/projects/{id}/merge_request/{merge_request_id}/comments | Get the comments of a merge request |
| [**getV3ProjectsIdMergeRequestMergeRequestIdCommits**](ProjectsApi.md#getV3ProjectsIdMergeRequestMergeRequestIdCommits) | **GET** /v3/projects/{id}/merge_request/{merge_request_id}/commits | Get the commits of a merge request |
| [**getV3ProjectsIdMergeRequests**](ProjectsApi.md#getV3ProjectsIdMergeRequests) | **GET** /v3/projects/{id}/merge_requests | List merge requests |
| [**getV3ProjectsIdMergeRequestsMergeRequestId**](ProjectsApi.md#getV3ProjectsIdMergeRequestsMergeRequestId) | **GET** /v3/projects/{id}/merge_requests/{merge_request_id} | Get a single merge request |
| [**getV3ProjectsIdMergeRequestsMergeRequestIdAwardEmoji**](ProjectsApi.md#getV3ProjectsIdMergeRequestsMergeRequestIdAwardEmoji) | **GET** /v3/projects/{id}/merge_requests/{merge_request_id}/award_emoji | Get a list of project +awardable+ award emoji |
| [**getV3ProjectsIdMergeRequestsMergeRequestIdAwardEmojiAwardId**](ProjectsApi.md#getV3ProjectsIdMergeRequestsMergeRequestIdAwardEmojiAwardId) | **GET** /v3/projects/{id}/merge_requests/{merge_request_id}/award_emoji/{award_id} | Get a specific award emoji |
| [**getV3ProjectsIdMergeRequestsMergeRequestIdChanges**](ProjectsApi.md#getV3ProjectsIdMergeRequestsMergeRequestIdChanges) | **GET** /v3/projects/{id}/merge_requests/{merge_request_id}/changes | Show the merge request changes |
| [**getV3ProjectsIdMergeRequestsMergeRequestIdClosesIssues**](ProjectsApi.md#getV3ProjectsIdMergeRequestsMergeRequestIdClosesIssues) | **GET** /v3/projects/{id}/merge_requests/{merge_request_id}/closes_issues | List issues that will be closed on merge |
| [**getV3ProjectsIdMergeRequestsMergeRequestIdComments**](ProjectsApi.md#getV3ProjectsIdMergeRequestsMergeRequestIdComments) | **GET** /v3/projects/{id}/merge_requests/{merge_request_id}/comments | Get the comments of a merge request |
| [**getV3ProjectsIdMergeRequestsMergeRequestIdCommits**](ProjectsApi.md#getV3ProjectsIdMergeRequestsMergeRequestIdCommits) | **GET** /v3/projects/{id}/merge_requests/{merge_request_id}/commits | Get the commits of a merge request |
| [**getV3ProjectsIdMergeRequestsMergeRequestIdNotesNoteIdAwardEmoji**](ProjectsApi.md#getV3ProjectsIdMergeRequestsMergeRequestIdNotesNoteIdAwardEmoji) | **GET** /v3/projects/{id}/merge_requests/{merge_request_id}/notes/{note_id}/award_emoji | Get a list of project +awardable+ award emoji |
| [**getV3ProjectsIdMergeRequestsMergeRequestIdNotesNoteIdAwardEmojiAwardId**](ProjectsApi.md#getV3ProjectsIdMergeRequestsMergeRequestIdNotesNoteIdAwardEmojiAwardId) | **GET** /v3/projects/{id}/merge_requests/{merge_request_id}/notes/{note_id}/award_emoji/{award_id} | Get a specific award emoji |
| [**getV3ProjectsIdMergeRequestsMergeRequestIdTimeStats**](ProjectsApi.md#getV3ProjectsIdMergeRequestsMergeRequestIdTimeStats) | **GET** /v3/projects/{id}/merge_requests/{merge_request_id}/time_stats | Show time stats for a project merge_request |
| [**getV3ProjectsIdMergeRequestsMergeRequestIdVersions**](ProjectsApi.md#getV3ProjectsIdMergeRequestsMergeRequestIdVersions) | **GET** /v3/projects/{id}/merge_requests/{merge_request_id}/versions | Get a list of merge request diff versions |
| [**getV3ProjectsIdMergeRequestsMergeRequestIdVersionsVersionId**](ProjectsApi.md#getV3ProjectsIdMergeRequestsMergeRequestIdVersionsVersionId) | **GET** /v3/projects/{id}/merge_requests/{merge_request_id}/versions/{version_id} | Get a single merge request diff version |
| [**getV3ProjectsIdMergeRequestsNoteableIdNotes**](ProjectsApi.md#getV3ProjectsIdMergeRequestsNoteableIdNotes) | **GET** /v3/projects/{id}/merge_requests/{noteable_id}/notes | Get a list of project +noteable+ notes |
| [**getV3ProjectsIdMergeRequestsNoteableIdNotesNoteId**](ProjectsApi.md#getV3ProjectsIdMergeRequestsNoteableIdNotesNoteId) | **GET** /v3/projects/{id}/merge_requests/{noteable_id}/notes/{note_id} | Get a single +noteable+ note |
| [**getV3ProjectsIdMilestones**](ProjectsApi.md#getV3ProjectsIdMilestones) | **GET** /v3/projects/{id}/milestones | Get a list of project milestones |
| [**getV3ProjectsIdMilestonesMilestoneId**](ProjectsApi.md#getV3ProjectsIdMilestonesMilestoneId) | **GET** /v3/projects/{id}/milestones/{milestone_id} | Get a single project milestone |
| [**getV3ProjectsIdMilestonesMilestoneIdIssues**](ProjectsApi.md#getV3ProjectsIdMilestonesMilestoneIdIssues) | **GET** /v3/projects/{id}/milestones/{milestone_id}/issues | Get all issues for a single project milestone |
| [**getV3ProjectsIdNotificationSettings**](ProjectsApi.md#getV3ProjectsIdNotificationSettings) | **GET** /v3/projects/{id}/notification_settings | Get project level notification level settings, defaults to Global |
| [**getV3ProjectsIdPipelines**](ProjectsApi.md#getV3ProjectsIdPipelines) | **GET** /v3/projects/{id}/pipelines | Get all Pipelines of the project |
| [**getV3ProjectsIdPipelinesPipelineId**](ProjectsApi.md#getV3ProjectsIdPipelinesPipelineId) | **GET** /v3/projects/{id}/pipelines/{pipeline_id} | Gets a specific pipeline for the project |
| [**getV3ProjectsIdRepositoryArchive**](ProjectsApi.md#getV3ProjectsIdRepositoryArchive) | **GET** /v3/projects/{id}/repository/archive | Get an archive of the repository |
| [**getV3ProjectsIdRepositoryBlobsSha**](ProjectsApi.md#getV3ProjectsIdRepositoryBlobsSha) | **GET** /v3/projects/{id}/repository/blobs/{sha} | Get a raw file contents |
| [**getV3ProjectsIdRepositoryBranches**](ProjectsApi.md#getV3ProjectsIdRepositoryBranches) | **GET** /v3/projects/{id}/repository/branches | Get a project repository branches |
| [**getV3ProjectsIdRepositoryBranchesBranch**](ProjectsApi.md#getV3ProjectsIdRepositoryBranchesBranch) | **GET** /v3/projects/{id}/repository/branches/{branch} | Get a single branch |
| [**getV3ProjectsIdRepositoryCommits**](ProjectsApi.md#getV3ProjectsIdRepositoryCommits) | **GET** /v3/projects/{id}/repository/commits | Get a project repository commits |
| [**getV3ProjectsIdRepositoryCommitsSha**](ProjectsApi.md#getV3ProjectsIdRepositoryCommitsSha) | **GET** /v3/projects/{id}/repository/commits/{sha} | Get a specific commit of a project |
| [**getV3ProjectsIdRepositoryCommitsShaBlob**](ProjectsApi.md#getV3ProjectsIdRepositoryCommitsShaBlob) | **GET** /v3/projects/{id}/repository/commits/{sha}/blob | Get a raw file contents |
| [**getV3ProjectsIdRepositoryCommitsShaBuilds**](ProjectsApi.md#getV3ProjectsIdRepositoryCommitsShaBuilds) | **GET** /v3/projects/{id}/repository/commits/{sha}/builds | Get builds for a specific commit of a project |
| [**getV3ProjectsIdRepositoryCommitsShaComments**](ProjectsApi.md#getV3ProjectsIdRepositoryCommitsShaComments) | **GET** /v3/projects/{id}/repository/commits/{sha}/comments | Get a commit&#39;s comments |
| [**getV3ProjectsIdRepositoryCommitsShaDiff**](ProjectsApi.md#getV3ProjectsIdRepositoryCommitsShaDiff) | **GET** /v3/projects/{id}/repository/commits/{sha}/diff | Get the diff for a specific commit of a project |
| [**getV3ProjectsIdRepositoryCommitsShaStatuses**](ProjectsApi.md#getV3ProjectsIdRepositoryCommitsShaStatuses) | **GET** /v3/projects/{id}/repository/commits/{sha}/statuses | Get a commit&#39;s statuses |
| [**getV3ProjectsIdRepositoryCompare**](ProjectsApi.md#getV3ProjectsIdRepositoryCompare) | **GET** /v3/projects/{id}/repository/compare | Compare two branches, tags, or commits |
| [**getV3ProjectsIdRepositoryContributors**](ProjectsApi.md#getV3ProjectsIdRepositoryContributors) | **GET** /v3/projects/{id}/repository/contributors | Get repository contributors |
| [**getV3ProjectsIdRepositoryFiles**](ProjectsApi.md#getV3ProjectsIdRepositoryFiles) | **GET** /v3/projects/{id}/repository/files | Get a file from repository |
| [**getV3ProjectsIdRepositoryRawBlobsSha**](ProjectsApi.md#getV3ProjectsIdRepositoryRawBlobsSha) | **GET** /v3/projects/{id}/repository/raw_blobs/{sha} | Get a raw blob contents by blob sha |
| [**getV3ProjectsIdRepositoryTags**](ProjectsApi.md#getV3ProjectsIdRepositoryTags) | **GET** /v3/projects/{id}/repository/tags | Get a project repository tags |
| [**getV3ProjectsIdRepositoryTagsTagName**](ProjectsApi.md#getV3ProjectsIdRepositoryTagsTagName) | **GET** /v3/projects/{id}/repository/tags/{tag_name} | Get a single repository tag |
| [**getV3ProjectsIdRepositoryTree**](ProjectsApi.md#getV3ProjectsIdRepositoryTree) | **GET** /v3/projects/{id}/repository/tree | Get a project repository tree |
| [**getV3ProjectsIdRunners**](ProjectsApi.md#getV3ProjectsIdRunners) | **GET** /v3/projects/{id}/runners | Get runners available for project |
| [**getV3ProjectsIdServicesServiceSlug**](ProjectsApi.md#getV3ProjectsIdServicesServiceSlug) | **GET** /v3/projects/{id}/services/{service_slug} | Get the service settings for project |
| [**getV3ProjectsIdSnippets**](ProjectsApi.md#getV3ProjectsIdSnippets) | **GET** /v3/projects/{id}/snippets | Get all project snippets |
| [**getV3ProjectsIdSnippetsNoteableIdNotes**](ProjectsApi.md#getV3ProjectsIdSnippetsNoteableIdNotes) | **GET** /v3/projects/{id}/snippets/{noteable_id}/notes | Get a list of project +noteable+ notes |
| [**getV3ProjectsIdSnippetsNoteableIdNotesNoteId**](ProjectsApi.md#getV3ProjectsIdSnippetsNoteableIdNotesNoteId) | **GET** /v3/projects/{id}/snippets/{noteable_id}/notes/{note_id} | Get a single +noteable+ note |
| [**getV3ProjectsIdSnippetsSnippetId**](ProjectsApi.md#getV3ProjectsIdSnippetsSnippetId) | **GET** /v3/projects/{id}/snippets/{snippet_id} | Get a single project snippet |
| [**getV3ProjectsIdSnippetsSnippetIdAwardEmoji**](ProjectsApi.md#getV3ProjectsIdSnippetsSnippetIdAwardEmoji) | **GET** /v3/projects/{id}/snippets/{snippet_id}/award_emoji | Get a list of project +awardable+ award emoji |
| [**getV3ProjectsIdSnippetsSnippetIdAwardEmojiAwardId**](ProjectsApi.md#getV3ProjectsIdSnippetsSnippetIdAwardEmojiAwardId) | **GET** /v3/projects/{id}/snippets/{snippet_id}/award_emoji/{award_id} | Get a specific award emoji |
| [**getV3ProjectsIdSnippetsSnippetIdNotesNoteIdAwardEmoji**](ProjectsApi.md#getV3ProjectsIdSnippetsSnippetIdNotesNoteIdAwardEmoji) | **GET** /v3/projects/{id}/snippets/{snippet_id}/notes/{note_id}/award_emoji | Get a list of project +awardable+ award emoji |
| [**getV3ProjectsIdSnippetsSnippetIdNotesNoteIdAwardEmojiAwardId**](ProjectsApi.md#getV3ProjectsIdSnippetsSnippetIdNotesNoteIdAwardEmojiAwardId) | **GET** /v3/projects/{id}/snippets/{snippet_id}/notes/{note_id}/award_emoji/{award_id} | Get a specific award emoji |
| [**getV3ProjectsIdSnippetsSnippetIdRaw**](ProjectsApi.md#getV3ProjectsIdSnippetsSnippetIdRaw) | **GET** /v3/projects/{id}/snippets/{snippet_id}/raw | Get a raw project snippet |
| [**getV3ProjectsIdTriggers**](ProjectsApi.md#getV3ProjectsIdTriggers) | **GET** /v3/projects/{id}/triggers | Get triggers list |
| [**getV3ProjectsIdTriggersToken**](ProjectsApi.md#getV3ProjectsIdTriggersToken) | **GET** /v3/projects/{id}/triggers/{token} | Get specific trigger of a project |
| [**getV3ProjectsIdUsers**](ProjectsApi.md#getV3ProjectsIdUsers) | **GET** /v3/projects/{id}/users | Get the users list of a project |
| [**getV3ProjectsIdVariables**](ProjectsApi.md#getV3ProjectsIdVariables) | **GET** /v3/projects/{id}/variables | Get project variables |
| [**getV3ProjectsIdVariablesKey**](ProjectsApi.md#getV3ProjectsIdVariablesKey) | **GET** /v3/projects/{id}/variables/{key} | Get a specific variable from a project |
| [**getV3ProjectsOwned**](ProjectsApi.md#getV3ProjectsOwned) | **GET** /v3/projects/owned | Get an owned projects list for authenticated user |
| [**getV3ProjectsSearchQuery**](ProjectsApi.md#getV3ProjectsSearchQuery) | **GET** /v3/projects/search/{query} | Search for projects the current user has access to |
| [**getV3ProjectsStarred**](ProjectsApi.md#getV3ProjectsStarred) | **GET** /v3/projects/starred | Gets starred project for the authenticated user |
| [**getV3ProjectsVisible**](ProjectsApi.md#getV3ProjectsVisible) | **GET** /v3/projects/visible | Get a list of visible projects for authenticated user |
| [**postV3Projects**](ProjectsApi.md#postV3Projects) | **POST** /v3/projects | Create new project |
| [**postV3ProjectsForkId**](ProjectsApi.md#postV3ProjectsForkId) | **POST** /v3/projects/fork/{id} | Fork new project for the current user or provided namespace. |
| [**postV3ProjectsIdAccessRequests**](ProjectsApi.md#postV3ProjectsIdAccessRequests) | **POST** /v3/projects/{id}/access_requests | Requests access for the authenticated user to a project. |
| [**postV3ProjectsIdArchive**](ProjectsApi.md#postV3ProjectsIdArchive) | **POST** /v3/projects/{id}/archive | Archive a project |
| [**postV3ProjectsIdBoardsBoardIdLists**](ProjectsApi.md#postV3ProjectsIdBoardsBoardIdLists) | **POST** /v3/projects/{id}/boards/{board_id}/lists | Create a new board list |
| [**postV3ProjectsIdBuildsBuildIdArtifactsKeep**](ProjectsApi.md#postV3ProjectsIdBuildsBuildIdArtifactsKeep) | **POST** /v3/projects/{id}/builds/{build_id}/artifacts/keep | Keep the artifacts to prevent them from being deleted |
| [**postV3ProjectsIdBuildsBuildIdCancel**](ProjectsApi.md#postV3ProjectsIdBuildsBuildIdCancel) | **POST** /v3/projects/{id}/builds/{build_id}/cancel | Cancel a specific build of a project |
| [**postV3ProjectsIdBuildsBuildIdErase**](ProjectsApi.md#postV3ProjectsIdBuildsBuildIdErase) | **POST** /v3/projects/{id}/builds/{build_id}/erase | Erase build (remove artifacts and build trace) |
| [**postV3ProjectsIdBuildsBuildIdPlay**](ProjectsApi.md#postV3ProjectsIdBuildsBuildIdPlay) | **POST** /v3/projects/{id}/builds/{build_id}/play | Trigger a manual build |
| [**postV3ProjectsIdBuildsBuildIdRetry**](ProjectsApi.md#postV3ProjectsIdBuildsBuildIdRetry) | **POST** /v3/projects/{id}/builds/{build_id}/retry | Retry a specific build of a project |
| [**postV3ProjectsIdDeployKeys**](ProjectsApi.md#postV3ProjectsIdDeployKeys) | **POST** /v3/projects/{id}/deploy_keys | Add new deploy key to currently authenticated user |
| [**postV3ProjectsIdDeployKeysKeyIdEnable**](ProjectsApi.md#postV3ProjectsIdDeployKeysKeyIdEnable) | **POST** /v3/projects/{id}/deploy_keys/{key_id}/enable | Enable a deploy key for a project |
| [**postV3ProjectsIdEnvironments**](ProjectsApi.md#postV3ProjectsIdEnvironments) | **POST** /v3/projects/{id}/environments | Creates a new environment |
| [**postV3ProjectsIdForkForkedFromId**](ProjectsApi.md#postV3ProjectsIdForkForkedFromId) | **POST** /v3/projects/{id}/fork/{forked_from_id} | Mark this project as forked from another |
| [**postV3ProjectsIdHooks**](ProjectsApi.md#postV3ProjectsIdHooks) | **POST** /v3/projects/{id}/hooks | Add hook to project |
| [**postV3ProjectsIdIssues**](ProjectsApi.md#postV3ProjectsIdIssues) | **POST** /v3/projects/{id}/issues | Create a new project issue |
| [**postV3ProjectsIdIssuesIssueIdAddSpentTime**](ProjectsApi.md#postV3ProjectsIdIssuesIssueIdAddSpentTime) | **POST** /v3/projects/{id}/issues/{issue_id}/add_spent_time | Add spent time for a project issue |
| [**postV3ProjectsIdIssuesIssueIdAwardEmoji**](ProjectsApi.md#postV3ProjectsIdIssuesIssueIdAwardEmoji) | **POST** /v3/projects/{id}/issues/{issue_id}/award_emoji | Award a new Emoji |
| [**postV3ProjectsIdIssuesIssueIdMove**](ProjectsApi.md#postV3ProjectsIdIssuesIssueIdMove) | **POST** /v3/projects/{id}/issues/{issue_id}/move | Move an existing issue |
| [**postV3ProjectsIdIssuesIssueIdNotesNoteIdAwardEmoji**](ProjectsApi.md#postV3ProjectsIdIssuesIssueIdNotesNoteIdAwardEmoji) | **POST** /v3/projects/{id}/issues/{issue_id}/notes/{note_id}/award_emoji | Award a new Emoji |
| [**postV3ProjectsIdIssuesIssueIdResetSpentTime**](ProjectsApi.md#postV3ProjectsIdIssuesIssueIdResetSpentTime) | **POST** /v3/projects/{id}/issues/{issue_id}/reset_spent_time | Reset spent time for a project issue |
| [**postV3ProjectsIdIssuesIssueIdResetTimeEstimate**](ProjectsApi.md#postV3ProjectsIdIssuesIssueIdResetTimeEstimate) | **POST** /v3/projects/{id}/issues/{issue_id}/reset_time_estimate | Reset the time estimate for a project issue |
| [**postV3ProjectsIdIssuesIssueIdTimeEstimate**](ProjectsApi.md#postV3ProjectsIdIssuesIssueIdTimeEstimate) | **POST** /v3/projects/{id}/issues/{issue_id}/time_estimate | Set a time estimate for a project issue |
| [**postV3ProjectsIdIssuesIssueIdTodo**](ProjectsApi.md#postV3ProjectsIdIssuesIssueIdTodo) | **POST** /v3/projects/{id}/issues/{issue_id}/todo | Create a todo on an issuable |
| [**postV3ProjectsIdIssuesNoteableIdNotes**](ProjectsApi.md#postV3ProjectsIdIssuesNoteableIdNotes) | **POST** /v3/projects/{id}/issues/{noteable_id}/notes | Create a new +noteable+ note |
| [**postV3ProjectsIdIssuesSubscribableIdSubscription**](ProjectsApi.md#postV3ProjectsIdIssuesSubscribableIdSubscription) | **POST** /v3/projects/{id}/issues/{subscribable_id}/subscription | Subscribe to a resource |
| [**postV3ProjectsIdKeys**](ProjectsApi.md#postV3ProjectsIdKeys) | **POST** /v3/projects/{id}/keys | Add new deploy key to currently authenticated user |
| [**postV3ProjectsIdKeysKeyIdEnable**](ProjectsApi.md#postV3ProjectsIdKeysKeyIdEnable) | **POST** /v3/projects/{id}/keys/{key_id}/enable | Enable a deploy key for a project |
| [**postV3ProjectsIdLabels**](ProjectsApi.md#postV3ProjectsIdLabels) | **POST** /v3/projects/{id}/labels | Create a new label |
| [**postV3ProjectsIdLabelsSubscribableIdSubscription**](ProjectsApi.md#postV3ProjectsIdLabelsSubscribableIdSubscription) | **POST** /v3/projects/{id}/labels/{subscribable_id}/subscription | Subscribe to a resource |
| [**postV3ProjectsIdMembers**](ProjectsApi.md#postV3ProjectsIdMembers) | **POST** /v3/projects/{id}/members | Adds a member to a group or project. |
| [**postV3ProjectsIdMergeRequestMergeRequestIdCancelMergeWhenBuildSucceeds**](ProjectsApi.md#postV3ProjectsIdMergeRequestMergeRequestIdCancelMergeWhenBuildSucceeds) | **POST** /v3/projects/{id}/merge_request/{merge_request_id}/cancel_merge_when_build_succeeds | Cancel merge if \&quot;Merge When Pipeline Succeeds\&quot; is enabled |
| [**postV3ProjectsIdMergeRequestMergeRequestIdComments**](ProjectsApi.md#postV3ProjectsIdMergeRequestMergeRequestIdComments) | **POST** /v3/projects/{id}/merge_request/{merge_request_id}/comments | Post a comment to a merge request |
| [**postV3ProjectsIdMergeRequestSubscribableIdSubscription**](ProjectsApi.md#postV3ProjectsIdMergeRequestSubscribableIdSubscription) | **POST** /v3/projects/{id}/merge_request/{subscribable_id}/subscription | Subscribe to a resource |
| [**postV3ProjectsIdMergeRequests**](ProjectsApi.md#postV3ProjectsIdMergeRequests) | **POST** /v3/projects/{id}/merge_requests | Create a merge request |
| [**postV3ProjectsIdMergeRequestsMergeRequestIdAddSpentTime**](ProjectsApi.md#postV3ProjectsIdMergeRequestsMergeRequestIdAddSpentTime) | **POST** /v3/projects/{id}/merge_requests/{merge_request_id}/add_spent_time | Add spent time for a project merge_request |
| [**postV3ProjectsIdMergeRequestsMergeRequestIdAwardEmoji**](ProjectsApi.md#postV3ProjectsIdMergeRequestsMergeRequestIdAwardEmoji) | **POST** /v3/projects/{id}/merge_requests/{merge_request_id}/award_emoji | Award a new Emoji |
| [**postV3ProjectsIdMergeRequestsMergeRequestIdCancelMergeWhenBuildSucceeds**](ProjectsApi.md#postV3ProjectsIdMergeRequestsMergeRequestIdCancelMergeWhenBuildSucceeds) | **POST** /v3/projects/{id}/merge_requests/{merge_request_id}/cancel_merge_when_build_succeeds | Cancel merge if \&quot;Merge When Pipeline Succeeds\&quot; is enabled |
| [**postV3ProjectsIdMergeRequestsMergeRequestIdComments**](ProjectsApi.md#postV3ProjectsIdMergeRequestsMergeRequestIdComments) | **POST** /v3/projects/{id}/merge_requests/{merge_request_id}/comments | Post a comment to a merge request |
| [**postV3ProjectsIdMergeRequestsMergeRequestIdNotesNoteIdAwardEmoji**](ProjectsApi.md#postV3ProjectsIdMergeRequestsMergeRequestIdNotesNoteIdAwardEmoji) | **POST** /v3/projects/{id}/merge_requests/{merge_request_id}/notes/{note_id}/award_emoji | Award a new Emoji |
| [**postV3ProjectsIdMergeRequestsMergeRequestIdResetSpentTime**](ProjectsApi.md#postV3ProjectsIdMergeRequestsMergeRequestIdResetSpentTime) | **POST** /v3/projects/{id}/merge_requests/{merge_request_id}/reset_spent_time | Reset spent time for a project merge_request |
| [**postV3ProjectsIdMergeRequestsMergeRequestIdResetTimeEstimate**](ProjectsApi.md#postV3ProjectsIdMergeRequestsMergeRequestIdResetTimeEstimate) | **POST** /v3/projects/{id}/merge_requests/{merge_request_id}/reset_time_estimate | Reset the time estimate for a project merge_request |
| [**postV3ProjectsIdMergeRequestsMergeRequestIdTimeEstimate**](ProjectsApi.md#postV3ProjectsIdMergeRequestsMergeRequestIdTimeEstimate) | **POST** /v3/projects/{id}/merge_requests/{merge_request_id}/time_estimate | Set a time estimate for a project merge_request |
| [**postV3ProjectsIdMergeRequestsMergeRequestIdTodo**](ProjectsApi.md#postV3ProjectsIdMergeRequestsMergeRequestIdTodo) | **POST** /v3/projects/{id}/merge_requests/{merge_request_id}/todo | Create a todo on an issuable |
| [**postV3ProjectsIdMergeRequestsNoteableIdNotes**](ProjectsApi.md#postV3ProjectsIdMergeRequestsNoteableIdNotes) | **POST** /v3/projects/{id}/merge_requests/{noteable_id}/notes | Create a new +noteable+ note |
| [**postV3ProjectsIdMergeRequestsSubscribableIdSubscription**](ProjectsApi.md#postV3ProjectsIdMergeRequestsSubscribableIdSubscription) | **POST** /v3/projects/{id}/merge_requests/{subscribable_id}/subscription | Subscribe to a resource |
| [**postV3ProjectsIdMilestones**](ProjectsApi.md#postV3ProjectsIdMilestones) | **POST** /v3/projects/{id}/milestones | Create a new project milestone |
| [**postV3ProjectsIdPipeline**](ProjectsApi.md#postV3ProjectsIdPipeline) | **POST** /v3/projects/{id}/pipeline | Create a new pipeline |
| [**postV3ProjectsIdPipelinesPipelineIdCancel**](ProjectsApi.md#postV3ProjectsIdPipelinesPipelineIdCancel) | **POST** /v3/projects/{id}/pipelines/{pipeline_id}/cancel | Cancel all builds in the pipeline |
| [**postV3ProjectsIdPipelinesPipelineIdRetry**](ProjectsApi.md#postV3ProjectsIdPipelinesPipelineIdRetry) | **POST** /v3/projects/{id}/pipelines/{pipeline_id}/retry | Retry failed builds in the pipeline |
| [**postV3ProjectsIdRefReftriggerBuilds**](ProjectsApi.md#postV3ProjectsIdRefReftriggerBuilds) | **POST** /v3/projects/{id}/(ref/{ref}/)trigger/builds | Trigger a GitLab project build |
| [**postV3ProjectsIdRepositoryBranches**](ProjectsApi.md#postV3ProjectsIdRepositoryBranches) | **POST** /v3/projects/{id}/repository/branches | Create branch |
| [**postV3ProjectsIdRepositoryCommits**](ProjectsApi.md#postV3ProjectsIdRepositoryCommits) | **POST** /v3/projects/{id}/repository/commits | Commit multiple file changes as one commit |
| [**postV3ProjectsIdRepositoryCommitsShaCherryPick**](ProjectsApi.md#postV3ProjectsIdRepositoryCommitsShaCherryPick) | **POST** /v3/projects/{id}/repository/commits/{sha}/cherry_pick | Cherry pick commit into a branch |
| [**postV3ProjectsIdRepositoryCommitsShaComments**](ProjectsApi.md#postV3ProjectsIdRepositoryCommitsShaComments) | **POST** /v3/projects/{id}/repository/commits/{sha}/comments | Post comment to commit |
| [**postV3ProjectsIdRepositoryFiles**](ProjectsApi.md#postV3ProjectsIdRepositoryFiles) | **POST** /v3/projects/{id}/repository/files | Create new file in repository |
| [**postV3ProjectsIdRepositoryTags**](ProjectsApi.md#postV3ProjectsIdRepositoryTags) | **POST** /v3/projects/{id}/repository/tags | Create a new repository tag |
| [**postV3ProjectsIdRepositoryTagsTagNameRelease**](ProjectsApi.md#postV3ProjectsIdRepositoryTagsTagNameRelease) | **POST** /v3/projects/{id}/repository/tags/{tag_name}/release | Add a release note to a tag |
| [**postV3ProjectsIdRunners**](ProjectsApi.md#postV3ProjectsIdRunners) | **POST** /v3/projects/{id}/runners | Enable a runner for a project |
| [**postV3ProjectsIdServicesMattermostSlashCommandsTrigger**](ProjectsApi.md#postV3ProjectsIdServicesMattermostSlashCommandsTrigger) | **POST** /v3/projects/{id}/services/mattermost_slash_commands/trigger | Trigger a slash command for mattermost-slash-commands |
| [**postV3ProjectsIdServicesSlackSlashCommandsTrigger**](ProjectsApi.md#postV3ProjectsIdServicesSlackSlashCommandsTrigger) | **POST** /v3/projects/{id}/services/slack_slash_commands/trigger | Trigger a slash command for slack-slash-commands |
| [**postV3ProjectsIdShare**](ProjectsApi.md#postV3ProjectsIdShare) | **POST** /v3/projects/{id}/share | Share the project with a group |
| [**postV3ProjectsIdSnippets**](ProjectsApi.md#postV3ProjectsIdSnippets) | **POST** /v3/projects/{id}/snippets | Create a new project snippet |
| [**postV3ProjectsIdSnippetsNoteableIdNotes**](ProjectsApi.md#postV3ProjectsIdSnippetsNoteableIdNotes) | **POST** /v3/projects/{id}/snippets/{noteable_id}/notes | Create a new +noteable+ note |
| [**postV3ProjectsIdSnippetsSnippetIdAwardEmoji**](ProjectsApi.md#postV3ProjectsIdSnippetsSnippetIdAwardEmoji) | **POST** /v3/projects/{id}/snippets/{snippet_id}/award_emoji | Award a new Emoji |
| [**postV3ProjectsIdSnippetsSnippetIdNotesNoteIdAwardEmoji**](ProjectsApi.md#postV3ProjectsIdSnippetsSnippetIdNotesNoteIdAwardEmoji) | **POST** /v3/projects/{id}/snippets/{snippet_id}/notes/{note_id}/award_emoji | Award a new Emoji |
| [**postV3ProjectsIdStar**](ProjectsApi.md#postV3ProjectsIdStar) | **POST** /v3/projects/{id}/star | Star a project |
| [**postV3ProjectsIdStatusesSha**](ProjectsApi.md#postV3ProjectsIdStatusesSha) | **POST** /v3/projects/{id}/statuses/{sha} | Post status to a commit |
| [**postV3ProjectsIdTriggers**](ProjectsApi.md#postV3ProjectsIdTriggers) | **POST** /v3/projects/{id}/triggers | Create a trigger |
| [**postV3ProjectsIdUnarchive**](ProjectsApi.md#postV3ProjectsIdUnarchive) | **POST** /v3/projects/{id}/unarchive | Unarchive a project |
| [**postV3ProjectsIdUploads**](ProjectsApi.md#postV3ProjectsIdUploads) | **POST** /v3/projects/{id}/uploads | Upload a file |
| [**postV3ProjectsIdVariables**](ProjectsApi.md#postV3ProjectsIdVariables) | **POST** /v3/projects/{id}/variables | Create a new variable in a project |
| [**postV3ProjectsUserUserId**](ProjectsApi.md#postV3ProjectsUserUserId) | **POST** /v3/projects/user/{user_id} | Create new project for a specified user. Only available to admin users. |
| [**putV3ProjectsId**](ProjectsApi.md#putV3ProjectsId) | **PUT** /v3/projects/{id} | Update an existing project |
| [**putV3ProjectsIdAccessRequestsUserIdApprove**](ProjectsApi.md#putV3ProjectsIdAccessRequestsUserIdApprove) | **PUT** /v3/projects/{id}/access_requests/{user_id}/approve | Approves an access request for the given user. |
| [**putV3ProjectsIdBoardsBoardIdListsListId**](ProjectsApi.md#putV3ProjectsIdBoardsBoardIdListsListId) | **PUT** /v3/projects/{id}/boards/{board_id}/lists/{list_id} | Moves a board list to a new position |
| [**putV3ProjectsIdEnvironmentsEnvironmentId**](ProjectsApi.md#putV3ProjectsIdEnvironmentsEnvironmentId) | **PUT** /v3/projects/{id}/environments/{environment_id} | Updates an existing environment |
| [**putV3ProjectsIdHooksHookId**](ProjectsApi.md#putV3ProjectsIdHooksHookId) | **PUT** /v3/projects/{id}/hooks/{hook_id} | Update an existing project hook |
| [**putV3ProjectsIdIssuesIssueId**](ProjectsApi.md#putV3ProjectsIdIssuesIssueId) | **PUT** /v3/projects/{id}/issues/{issue_id} | Update an existing issue |
| [**putV3ProjectsIdIssuesNoteableIdNotesNoteId**](ProjectsApi.md#putV3ProjectsIdIssuesNoteableIdNotesNoteId) | **PUT** /v3/projects/{id}/issues/{noteable_id}/notes/{note_id} | Update an existing +noteable+ note |
| [**putV3ProjectsIdLabels**](ProjectsApi.md#putV3ProjectsIdLabels) | **PUT** /v3/projects/{id}/labels | Update an existing label. At least one optional parameter is required. |
| [**putV3ProjectsIdMembersUserId**](ProjectsApi.md#putV3ProjectsIdMembersUserId) | **PUT** /v3/projects/{id}/members/{user_id} | Updates a member of a group or project. |
| [**putV3ProjectsIdMergeRequestMergeRequestId**](ProjectsApi.md#putV3ProjectsIdMergeRequestMergeRequestId) | **PUT** /v3/projects/{id}/merge_request/{merge_request_id} | Update a merge request |
| [**putV3ProjectsIdMergeRequestMergeRequestIdMerge**](ProjectsApi.md#putV3ProjectsIdMergeRequestMergeRequestIdMerge) | **PUT** /v3/projects/{id}/merge_request/{merge_request_id}/merge | Merge a merge request |
| [**putV3ProjectsIdMergeRequestsMergeRequestId**](ProjectsApi.md#putV3ProjectsIdMergeRequestsMergeRequestId) | **PUT** /v3/projects/{id}/merge_requests/{merge_request_id} | Update a merge request |
| [**putV3ProjectsIdMergeRequestsMergeRequestIdMerge**](ProjectsApi.md#putV3ProjectsIdMergeRequestsMergeRequestIdMerge) | **PUT** /v3/projects/{id}/merge_requests/{merge_request_id}/merge | Merge a merge request |
| [**putV3ProjectsIdMergeRequestsNoteableIdNotesNoteId**](ProjectsApi.md#putV3ProjectsIdMergeRequestsNoteableIdNotesNoteId) | **PUT** /v3/projects/{id}/merge_requests/{noteable_id}/notes/{note_id} | Update an existing +noteable+ note |
| [**putV3ProjectsIdMilestonesMilestoneId**](ProjectsApi.md#putV3ProjectsIdMilestonesMilestoneId) | **PUT** /v3/projects/{id}/milestones/{milestone_id} | Update an existing project milestone |
| [**putV3ProjectsIdNotificationSettings**](ProjectsApi.md#putV3ProjectsIdNotificationSettings) | **PUT** /v3/projects/{id}/notification_settings | Update project level notification level settings, defaults to Global |
| [**putV3ProjectsIdRepositoryBranchesBranchProtect**](ProjectsApi.md#putV3ProjectsIdRepositoryBranchesBranchProtect) | **PUT** /v3/projects/{id}/repository/branches/{branch}/protect | Protect a single branch |
| [**putV3ProjectsIdRepositoryBranchesBranchUnprotect**](ProjectsApi.md#putV3ProjectsIdRepositoryBranchesBranchUnprotect) | **PUT** /v3/projects/{id}/repository/branches/{branch}/unprotect | Unprotect a single branch |
| [**putV3ProjectsIdRepositoryFiles**](ProjectsApi.md#putV3ProjectsIdRepositoryFiles) | **PUT** /v3/projects/{id}/repository/files | Update existing file in repository |
| [**putV3ProjectsIdRepositoryTagsTagNameRelease**](ProjectsApi.md#putV3ProjectsIdRepositoryTagsTagNameRelease) | **PUT** /v3/projects/{id}/repository/tags/{tag_name}/release | Update a tag&#39;s release note |
| [**putV3ProjectsIdServicesAsana**](ProjectsApi.md#putV3ProjectsIdServicesAsana) | **PUT** /v3/projects/{id}/services/asana | Set asana service for project |
| [**putV3ProjectsIdServicesAssembla**](ProjectsApi.md#putV3ProjectsIdServicesAssembla) | **PUT** /v3/projects/{id}/services/assembla | Set assembla service for project |
| [**putV3ProjectsIdServicesBamboo**](ProjectsApi.md#putV3ProjectsIdServicesBamboo) | **PUT** /v3/projects/{id}/services/bamboo | Set bamboo service for project |
| [**putV3ProjectsIdServicesBugzilla**](ProjectsApi.md#putV3ProjectsIdServicesBugzilla) | **PUT** /v3/projects/{id}/services/bugzilla | Set bugzilla service for project |
| [**putV3ProjectsIdServicesBuildkite**](ProjectsApi.md#putV3ProjectsIdServicesBuildkite) | **PUT** /v3/projects/{id}/services/buildkite | Set buildkite service for project |
| [**putV3ProjectsIdServicesBuildsEmail**](ProjectsApi.md#putV3ProjectsIdServicesBuildsEmail) | **PUT** /v3/projects/{id}/services/builds-email | Set builds-email service for project |
| [**putV3ProjectsIdServicesCampfire**](ProjectsApi.md#putV3ProjectsIdServicesCampfire) | **PUT** /v3/projects/{id}/services/campfire | Set campfire service for project |
| [**putV3ProjectsIdServicesCustomIssueTracker**](ProjectsApi.md#putV3ProjectsIdServicesCustomIssueTracker) | **PUT** /v3/projects/{id}/services/custom-issue-tracker | Set custom-issue-tracker service for project |
| [**putV3ProjectsIdServicesDroneCi**](ProjectsApi.md#putV3ProjectsIdServicesDroneCi) | **PUT** /v3/projects/{id}/services/drone-ci | Set drone-ci service for project |
| [**putV3ProjectsIdServicesEmailsOnPush**](ProjectsApi.md#putV3ProjectsIdServicesEmailsOnPush) | **PUT** /v3/projects/{id}/services/emails-on-push | Set emails-on-push service for project |
| [**putV3ProjectsIdServicesExternalWiki**](ProjectsApi.md#putV3ProjectsIdServicesExternalWiki) | **PUT** /v3/projects/{id}/services/external-wiki | Set external-wiki service for project |
| [**putV3ProjectsIdServicesFlowdock**](ProjectsApi.md#putV3ProjectsIdServicesFlowdock) | **PUT** /v3/projects/{id}/services/flowdock | Set flowdock service for project |
| [**putV3ProjectsIdServicesGemnasium**](ProjectsApi.md#putV3ProjectsIdServicesGemnasium) | **PUT** /v3/projects/{id}/services/gemnasium | Set gemnasium service for project |
| [**putV3ProjectsIdServicesHipchat**](ProjectsApi.md#putV3ProjectsIdServicesHipchat) | **PUT** /v3/projects/{id}/services/hipchat | Set hipchat service for project |
| [**putV3ProjectsIdServicesIrker**](ProjectsApi.md#putV3ProjectsIdServicesIrker) | **PUT** /v3/projects/{id}/services/irker | Set irker service for project |
| [**putV3ProjectsIdServicesJira**](ProjectsApi.md#putV3ProjectsIdServicesJira) | **PUT** /v3/projects/{id}/services/jira | Set jira service for project |
| [**putV3ProjectsIdServicesKubernetes**](ProjectsApi.md#putV3ProjectsIdServicesKubernetes) | **PUT** /v3/projects/{id}/services/kubernetes | Set kubernetes service for project |
| [**putV3ProjectsIdServicesMattermost**](ProjectsApi.md#putV3ProjectsIdServicesMattermost) | **PUT** /v3/projects/{id}/services/mattermost | Set mattermost service for project |
| [**putV3ProjectsIdServicesMattermostSlashCommands**](ProjectsApi.md#putV3ProjectsIdServicesMattermostSlashCommands) | **PUT** /v3/projects/{id}/services/mattermost-slash-commands | Set mattermost-slash-commands service for project |
| [**putV3ProjectsIdServicesPipelinesEmail**](ProjectsApi.md#putV3ProjectsIdServicesPipelinesEmail) | **PUT** /v3/projects/{id}/services/pipelines-email | Set pipelines-email service for project |
| [**putV3ProjectsIdServicesPivotaltracker**](ProjectsApi.md#putV3ProjectsIdServicesPivotaltracker) | **PUT** /v3/projects/{id}/services/pivotaltracker | Set pivotaltracker service for project |
| [**putV3ProjectsIdServicesPushover**](ProjectsApi.md#putV3ProjectsIdServicesPushover) | **PUT** /v3/projects/{id}/services/pushover | Set pushover service for project |
| [**putV3ProjectsIdServicesRedmine**](ProjectsApi.md#putV3ProjectsIdServicesRedmine) | **PUT** /v3/projects/{id}/services/redmine | Set redmine service for project |
| [**putV3ProjectsIdServicesSlack**](ProjectsApi.md#putV3ProjectsIdServicesSlack) | **PUT** /v3/projects/{id}/services/slack | Set slack service for project |
| [**putV3ProjectsIdServicesSlackSlashCommands**](ProjectsApi.md#putV3ProjectsIdServicesSlackSlashCommands) | **PUT** /v3/projects/{id}/services/slack-slash-commands | Set slack-slash-commands service for project |
| [**putV3ProjectsIdServicesTeamcity**](ProjectsApi.md#putV3ProjectsIdServicesTeamcity) | **PUT** /v3/projects/{id}/services/teamcity | Set teamcity service for project |
| [**putV3ProjectsIdSnippetsNoteableIdNotesNoteId**](ProjectsApi.md#putV3ProjectsIdSnippetsNoteableIdNotesNoteId) | **PUT** /v3/projects/{id}/snippets/{noteable_id}/notes/{note_id} | Update an existing +noteable+ note |
| [**putV3ProjectsIdSnippetsSnippetId**](ProjectsApi.md#putV3ProjectsIdSnippetsSnippetId) | **PUT** /v3/projects/{id}/snippets/{snippet_id} | Update an existing project snippet |
| [**putV3ProjectsIdVariablesKey**](ProjectsApi.md#putV3ProjectsIdVariablesKey) | **PUT** /v3/projects/{id}/variables/{key} | Update an existing variable from a project |


<a id="deleteV3ProjectsId"></a>
# **deleteV3ProjectsId**
> deleteV3ProjectsId(id)

Remove a project

Remove a project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    try {
      apiInstance.deleteV3ProjectsId(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#deleteV3ProjectsId");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |

### Return type

null (empty response body)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Remove a project |  -  |

<a id="deleteV3ProjectsIdAccessRequestsUserId"></a>
# **deleteV3ProjectsIdAccessRequestsUserId**
> deleteV3ProjectsIdAccessRequestsUserId(id, userId)

Denies an access request for the given user.

This feature was introduced in GitLab 8.11.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The project ID
    Integer userId = 56; // Integer | The user ID of the access requester
    try {
      apiInstance.deleteV3ProjectsIdAccessRequestsUserId(id, userId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#deleteV3ProjectsIdAccessRequestsUserId");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The project ID | |
| **userId** | **Integer**| The user ID of the access requester | |

### Return type

null (empty response body)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Denies an access request for the given user. |  -  |

<a id="deleteV3ProjectsIdBoardsBoardIdListsListId"></a>
# **deleteV3ProjectsIdBoardsBoardIdListsListId**
> ModelList deleteV3ProjectsIdBoardsBoardIdListsListId(id, boardId, listId)

Delete a board list

This feature was introduced in 8.13

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    Integer boardId = 56; // Integer | The ID of a board
    Integer listId = 56; // Integer | The ID of a board list
    try {
      ModelList result = apiInstance.deleteV3ProjectsIdBoardsBoardIdListsListId(id, boardId, listId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#deleteV3ProjectsIdBoardsBoardIdListsListId");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **boardId** | **Integer**| The ID of a board | |
| **listId** | **Integer**| The ID of a board list | |

### Return type

[**ModelList**](ModelList.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Delete a board list |  -  |

<a id="deleteV3ProjectsIdDeployKeysKeyId"></a>
# **deleteV3ProjectsIdDeployKeysKeyId**
> SSHKey deleteV3ProjectsIdDeployKeysKeyId(id, keyId)

Delete deploy key for a project

Delete deploy key for a project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of the project
    Integer keyId = 56; // Integer | The ID of the deploy key
    try {
      SSHKey result = apiInstance.deleteV3ProjectsIdDeployKeysKeyId(id, keyId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#deleteV3ProjectsIdDeployKeysKeyId");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of the project | |
| **keyId** | **Integer**| The ID of the deploy key | |

### Return type

[**SSHKey**](SSHKey.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Delete deploy key for a project |  -  |

<a id="deleteV3ProjectsIdDeployKeysKeyIdDisable"></a>
# **deleteV3ProjectsIdDeployKeysKeyIdDisable**
> SSHKey deleteV3ProjectsIdDeployKeysKeyIdDisable(id, keyId)

Disable a deploy key for a project

This feature was added in GitLab 8.11

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of the project
    Integer keyId = 56; // Integer | The ID of the deploy key
    try {
      SSHKey result = apiInstance.deleteV3ProjectsIdDeployKeysKeyIdDisable(id, keyId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#deleteV3ProjectsIdDeployKeysKeyIdDisable");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of the project | |
| **keyId** | **Integer**| The ID of the deploy key | |

### Return type

[**SSHKey**](SSHKey.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Disable a deploy key for a project |  -  |

<a id="deleteV3ProjectsIdEnvironmentsEnvironmentId"></a>
# **deleteV3ProjectsIdEnvironmentsEnvironmentId**
> Environment deleteV3ProjectsIdEnvironmentsEnvironmentId(id, environmentId)

Deletes an existing environment

This feature was introduced in GitLab 8.11.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The project ID
    Integer environmentId = 56; // Integer | The environment ID
    try {
      Environment result = apiInstance.deleteV3ProjectsIdEnvironmentsEnvironmentId(id, environmentId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#deleteV3ProjectsIdEnvironmentsEnvironmentId");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The project ID | |
| **environmentId** | **Integer**| The environment ID | |

### Return type

[**Environment**](Environment.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Deletes an existing environment |  -  |

<a id="deleteV3ProjectsIdFork"></a>
# **deleteV3ProjectsIdFork**
> deleteV3ProjectsIdFork(id)

Remove a forked_from relationship

Remove a forked_from relationship

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    try {
      apiInstance.deleteV3ProjectsIdFork(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#deleteV3ProjectsIdFork");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |

### Return type

null (empty response body)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Remove a forked_from relationship |  -  |

<a id="deleteV3ProjectsIdHooksHookId"></a>
# **deleteV3ProjectsIdHooksHookId**
> ProjectHook deleteV3ProjectsIdHooksHookId(id, hookId)

Deletes project hook

Deletes project hook

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    Integer hookId = 56; // Integer | The ID of the hook to delete
    try {
      ProjectHook result = apiInstance.deleteV3ProjectsIdHooksHookId(id, hookId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#deleteV3ProjectsIdHooksHookId");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **hookId** | **Integer**| The ID of the hook to delete | |

### Return type

[**ProjectHook**](ProjectHook.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Deletes project hook |  -  |

<a id="deleteV3ProjectsIdIssuesIssueId"></a>
# **deleteV3ProjectsIdIssuesIssueId**
> deleteV3ProjectsIdIssuesIssueId(id, issueId)

Delete a project issue

Delete a project issue

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    Integer issueId = 56; // Integer | The ID of a project issue
    try {
      apiInstance.deleteV3ProjectsIdIssuesIssueId(id, issueId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#deleteV3ProjectsIdIssuesIssueId");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **issueId** | **Integer**| The ID of a project issue | |

### Return type

null (empty response body)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Delete a project issue |  -  |

<a id="deleteV3ProjectsIdIssuesIssueIdAwardEmojiAwardId"></a>
# **deleteV3ProjectsIdIssuesIssueIdAwardEmojiAwardId**
> AwardEmoji deleteV3ProjectsIdIssuesIssueIdAwardEmojiAwardId(awardId, id, issueId)

Delete a +awardables+ award emoji

This feature was introduced in 8.9

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    Integer awardId = 56; // Integer | The ID of an award emoji
    Integer id = 56; // Integer | 
    Integer issueId = 56; // Integer | 
    try {
      AwardEmoji result = apiInstance.deleteV3ProjectsIdIssuesIssueIdAwardEmojiAwardId(awardId, id, issueId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#deleteV3ProjectsIdIssuesIssueIdAwardEmojiAwardId");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **awardId** | **Integer**| The ID of an award emoji | |
| **id** | **Integer**|  | |
| **issueId** | **Integer**|  | |

### Return type

[**AwardEmoji**](AwardEmoji.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Delete a +awardables+ award emoji |  -  |

<a id="deleteV3ProjectsIdIssuesIssueIdNotesNoteIdAwardEmojiAwardId"></a>
# **deleteV3ProjectsIdIssuesIssueIdNotesNoteIdAwardEmojiAwardId**
> AwardEmoji deleteV3ProjectsIdIssuesIssueIdNotesNoteIdAwardEmojiAwardId(awardId, id, issueId, noteId)

Delete a +awardables+ award emoji

This feature was introduced in 8.9

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    Integer awardId = 56; // Integer | The ID of an award emoji
    Integer id = 56; // Integer | 
    Integer issueId = 56; // Integer | 
    Integer noteId = 56; // Integer | 
    try {
      AwardEmoji result = apiInstance.deleteV3ProjectsIdIssuesIssueIdNotesNoteIdAwardEmojiAwardId(awardId, id, issueId, noteId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#deleteV3ProjectsIdIssuesIssueIdNotesNoteIdAwardEmojiAwardId");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **awardId** | **Integer**| The ID of an award emoji | |
| **id** | **Integer**|  | |
| **issueId** | **Integer**|  | |
| **noteId** | **Integer**|  | |

### Return type

[**AwardEmoji**](AwardEmoji.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Delete a +awardables+ award emoji |  -  |

<a id="deleteV3ProjectsIdIssuesNoteableIdNotesNoteId"></a>
# **deleteV3ProjectsIdIssuesNoteableIdNotesNoteId**
> Note deleteV3ProjectsIdIssuesNoteableIdNotesNoteId(id, noteableId, noteId)

Delete a +noteable+ note

Delete a +noteable+ note

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    Integer noteableId = 56; // Integer | The ID of the noteable
    Integer noteId = 56; // Integer | The ID of a note
    try {
      Note result = apiInstance.deleteV3ProjectsIdIssuesNoteableIdNotesNoteId(id, noteableId, noteId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#deleteV3ProjectsIdIssuesNoteableIdNotesNoteId");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **noteableId** | **Integer**| The ID of the noteable | |
| **noteId** | **Integer**| The ID of a note | |

### Return type

[**Note**](Note.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Delete a +noteable+ note |  -  |

<a id="deleteV3ProjectsIdIssuesSubscribableIdSubscription"></a>
# **deleteV3ProjectsIdIssuesSubscribableIdSubscription**
> Issue deleteV3ProjectsIdIssuesSubscribableIdSubscription(id, subscribableId)

Unsubscribe from a resource

Unsubscribe from a resource

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    String subscribableId = "subscribableId_example"; // String | The ID of a resource
    try {
      Issue result = apiInstance.deleteV3ProjectsIdIssuesSubscribableIdSubscription(id, subscribableId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#deleteV3ProjectsIdIssuesSubscribableIdSubscription");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **subscribableId** | **String**| The ID of a resource | |

### Return type

[**Issue**](Issue.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Unsubscribe from a resource |  -  |

<a id="deleteV3ProjectsIdKeysKeyId"></a>
# **deleteV3ProjectsIdKeysKeyId**
> SSHKey deleteV3ProjectsIdKeysKeyId(id, keyId)

Delete deploy key for a project

Delete deploy key for a project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of the project
    Integer keyId = 56; // Integer | The ID of the deploy key
    try {
      SSHKey result = apiInstance.deleteV3ProjectsIdKeysKeyId(id, keyId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#deleteV3ProjectsIdKeysKeyId");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of the project | |
| **keyId** | **Integer**| The ID of the deploy key | |

### Return type

[**SSHKey**](SSHKey.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Delete deploy key for a project |  -  |

<a id="deleteV3ProjectsIdKeysKeyIdDisable"></a>
# **deleteV3ProjectsIdKeysKeyIdDisable**
> SSHKey deleteV3ProjectsIdKeysKeyIdDisable(id, keyId)

Disable a deploy key for a project

This feature was added in GitLab 8.11

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of the project
    Integer keyId = 56; // Integer | The ID of the deploy key
    try {
      SSHKey result = apiInstance.deleteV3ProjectsIdKeysKeyIdDisable(id, keyId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#deleteV3ProjectsIdKeysKeyIdDisable");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of the project | |
| **keyId** | **Integer**| The ID of the deploy key | |

### Return type

[**SSHKey**](SSHKey.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Disable a deploy key for a project |  -  |

<a id="deleteV3ProjectsIdLabels"></a>
# **deleteV3ProjectsIdLabels**
> Label deleteV3ProjectsIdLabels(id, name)

Delete an existing label

Delete an existing label

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    String name = "name_example"; // String | The name of the label to be deleted
    try {
      Label result = apiInstance.deleteV3ProjectsIdLabels(id, name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#deleteV3ProjectsIdLabels");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **name** | **String**| The name of the label to be deleted | |

### Return type

[**Label**](Label.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Delete an existing label |  -  |

<a id="deleteV3ProjectsIdLabelsSubscribableIdSubscription"></a>
# **deleteV3ProjectsIdLabelsSubscribableIdSubscription**
> Label deleteV3ProjectsIdLabelsSubscribableIdSubscription(id, subscribableId)

Unsubscribe from a resource

Unsubscribe from a resource

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    String subscribableId = "subscribableId_example"; // String | The ID of a resource
    try {
      Label result = apiInstance.deleteV3ProjectsIdLabelsSubscribableIdSubscription(id, subscribableId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#deleteV3ProjectsIdLabelsSubscribableIdSubscription");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **subscribableId** | **String**| The ID of a resource | |

### Return type

[**Label**](Label.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Unsubscribe from a resource |  -  |

<a id="deleteV3ProjectsIdMembersUserId"></a>
# **deleteV3ProjectsIdMembersUserId**
> deleteV3ProjectsIdMembersUserId(id, userId)

Removes a user from a group or project.

Removes a user from a group or project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The project ID
    Integer userId = 56; // Integer | The user ID of the member
    try {
      apiInstance.deleteV3ProjectsIdMembersUserId(id, userId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#deleteV3ProjectsIdMembersUserId");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The project ID | |
| **userId** | **Integer**| The user ID of the member | |

### Return type

null (empty response body)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Removes a user from a group or project. |  -  |

<a id="deleteV3ProjectsIdMergeRequestSubscribableIdSubscription"></a>
# **deleteV3ProjectsIdMergeRequestSubscribableIdSubscription**
> MergeRequest deleteV3ProjectsIdMergeRequestSubscribableIdSubscription(id, subscribableId)

Unsubscribe from a resource

Unsubscribe from a resource

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    String subscribableId = "subscribableId_example"; // String | The ID of a resource
    try {
      MergeRequest result = apiInstance.deleteV3ProjectsIdMergeRequestSubscribableIdSubscription(id, subscribableId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#deleteV3ProjectsIdMergeRequestSubscribableIdSubscription");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **subscribableId** | **String**| The ID of a resource | |

### Return type

[**MergeRequest**](MergeRequest.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Unsubscribe from a resource |  -  |

<a id="deleteV3ProjectsIdMergeRequestsMergeRequestId"></a>
# **deleteV3ProjectsIdMergeRequestsMergeRequestId**
> deleteV3ProjectsIdMergeRequestsMergeRequestId(id, mergeRequestId)

Delete a merge request

Delete a merge request

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    Integer mergeRequestId = 56; // Integer | The ID of a merge request
    try {
      apiInstance.deleteV3ProjectsIdMergeRequestsMergeRequestId(id, mergeRequestId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#deleteV3ProjectsIdMergeRequestsMergeRequestId");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **mergeRequestId** | **Integer**| The ID of a merge request | |

### Return type

null (empty response body)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Delete a merge request |  -  |

<a id="deleteV3ProjectsIdMergeRequestsMergeRequestIdAwardEmojiAwardId"></a>
# **deleteV3ProjectsIdMergeRequestsMergeRequestIdAwardEmojiAwardId**
> AwardEmoji deleteV3ProjectsIdMergeRequestsMergeRequestIdAwardEmojiAwardId(awardId, id, mergeRequestId)

Delete a +awardables+ award emoji

This feature was introduced in 8.9

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    Integer awardId = 56; // Integer | The ID of an award emoji
    Integer id = 56; // Integer | 
    Integer mergeRequestId = 56; // Integer | 
    try {
      AwardEmoji result = apiInstance.deleteV3ProjectsIdMergeRequestsMergeRequestIdAwardEmojiAwardId(awardId, id, mergeRequestId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#deleteV3ProjectsIdMergeRequestsMergeRequestIdAwardEmojiAwardId");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **awardId** | **Integer**| The ID of an award emoji | |
| **id** | **Integer**|  | |
| **mergeRequestId** | **Integer**|  | |

### Return type

[**AwardEmoji**](AwardEmoji.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Delete a +awardables+ award emoji |  -  |

<a id="deleteV3ProjectsIdMergeRequestsMergeRequestIdNotesNoteIdAwardEmojiAwardId"></a>
# **deleteV3ProjectsIdMergeRequestsMergeRequestIdNotesNoteIdAwardEmojiAwardId**
> AwardEmoji deleteV3ProjectsIdMergeRequestsMergeRequestIdNotesNoteIdAwardEmojiAwardId(awardId, id, mergeRequestId, noteId)

Delete a +awardables+ award emoji

This feature was introduced in 8.9

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    Integer awardId = 56; // Integer | The ID of an award emoji
    Integer id = 56; // Integer | 
    Integer mergeRequestId = 56; // Integer | 
    Integer noteId = 56; // Integer | 
    try {
      AwardEmoji result = apiInstance.deleteV3ProjectsIdMergeRequestsMergeRequestIdNotesNoteIdAwardEmojiAwardId(awardId, id, mergeRequestId, noteId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#deleteV3ProjectsIdMergeRequestsMergeRequestIdNotesNoteIdAwardEmojiAwardId");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **awardId** | **Integer**| The ID of an award emoji | |
| **id** | **Integer**|  | |
| **mergeRequestId** | **Integer**|  | |
| **noteId** | **Integer**|  | |

### Return type

[**AwardEmoji**](AwardEmoji.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Delete a +awardables+ award emoji |  -  |

<a id="deleteV3ProjectsIdMergeRequestsNoteableIdNotesNoteId"></a>
# **deleteV3ProjectsIdMergeRequestsNoteableIdNotesNoteId**
> Note deleteV3ProjectsIdMergeRequestsNoteableIdNotesNoteId(id, noteableId, noteId)

Delete a +noteable+ note

Delete a +noteable+ note

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    Integer noteableId = 56; // Integer | The ID of the noteable
    Integer noteId = 56; // Integer | The ID of a note
    try {
      Note result = apiInstance.deleteV3ProjectsIdMergeRequestsNoteableIdNotesNoteId(id, noteableId, noteId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#deleteV3ProjectsIdMergeRequestsNoteableIdNotesNoteId");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **noteableId** | **Integer**| The ID of the noteable | |
| **noteId** | **Integer**| The ID of a note | |

### Return type

[**Note**](Note.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Delete a +noteable+ note |  -  |

<a id="deleteV3ProjectsIdMergeRequestsSubscribableIdSubscription"></a>
# **deleteV3ProjectsIdMergeRequestsSubscribableIdSubscription**
> MergeRequest deleteV3ProjectsIdMergeRequestsSubscribableIdSubscription(id, subscribableId)

Unsubscribe from a resource

Unsubscribe from a resource

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    String subscribableId = "subscribableId_example"; // String | The ID of a resource
    try {
      MergeRequest result = apiInstance.deleteV3ProjectsIdMergeRequestsSubscribableIdSubscription(id, subscribableId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#deleteV3ProjectsIdMergeRequestsSubscribableIdSubscription");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **subscribableId** | **String**| The ID of a resource | |

### Return type

[**MergeRequest**](MergeRequest.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Unsubscribe from a resource |  -  |

<a id="deleteV3ProjectsIdRepositoryBranchesBranch"></a>
# **deleteV3ProjectsIdRepositoryBranchesBranch**
> deleteV3ProjectsIdRepositoryBranchesBranch(id, branch)

Delete a branch

Delete a branch

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    String branch = "branch_example"; // String | The name of the branch
    try {
      apiInstance.deleteV3ProjectsIdRepositoryBranchesBranch(id, branch);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#deleteV3ProjectsIdRepositoryBranchesBranch");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **branch** | **String**| The name of the branch | |

### Return type

null (empty response body)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Delete a branch |  -  |

<a id="deleteV3ProjectsIdRepositoryFiles"></a>
# **deleteV3ProjectsIdRepositoryFiles**
> deleteV3ProjectsIdRepositoryFiles(id, filePath, branchName, commitMessage, authorEmail, authorName)

Delete an existing file in repository

Delete an existing file in repository

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The project ID
    String filePath = "filePath_example"; // String | The path to new file. Ex. lib/class.rb
    String branchName = "branchName_example"; // String | The name of branch
    String commitMessage = "commitMessage_example"; // String | Commit Message
    String authorEmail = "authorEmail_example"; // String | The email of the author
    String authorName = "authorName_example"; // String | The name of the author
    try {
      apiInstance.deleteV3ProjectsIdRepositoryFiles(id, filePath, branchName, commitMessage, authorEmail, authorName);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#deleteV3ProjectsIdRepositoryFiles");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The project ID | |
| **filePath** | **String**| The path to new file. Ex. lib/class.rb | |
| **branchName** | **String**| The name of branch | |
| **commitMessage** | **String**| Commit Message | |
| **authorEmail** | **String**| The email of the author | [optional] |
| **authorName** | **String**| The name of the author | [optional] |

### Return type

null (empty response body)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Delete an existing file in repository |  -  |

<a id="deleteV3ProjectsIdRepositoryMergedBranches"></a>
# **deleteV3ProjectsIdRepositoryMergedBranches**
> deleteV3ProjectsIdRepositoryMergedBranches(id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    try {
      apiInstance.deleteV3ProjectsIdRepositoryMergedBranches(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#deleteV3ProjectsIdRepositoryMergedBranches");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |

### Return type

null (empty response body)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | deleted MergedBranch |  -  |

<a id="deleteV3ProjectsIdRepositoryTagsTagName"></a>
# **deleteV3ProjectsIdRepositoryTagsTagName**
> deleteV3ProjectsIdRepositoryTagsTagName(id, tagName)

Delete a repository tag

Delete a repository tag

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    String tagName = "tagName_example"; // String | The name of the tag
    try {
      apiInstance.deleteV3ProjectsIdRepositoryTagsTagName(id, tagName);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#deleteV3ProjectsIdRepositoryTagsTagName");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **tagName** | **String**| The name of the tag | |

### Return type

null (empty response body)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Delete a repository tag |  -  |

<a id="deleteV3ProjectsIdRunnersRunnerId"></a>
# **deleteV3ProjectsIdRunnersRunnerId**
> Runner deleteV3ProjectsIdRunnersRunnerId(id, runnerId)

Disable project&#39;s runner

Disable project&#39;s runner

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    Integer runnerId = 56; // Integer | The ID of the runner
    try {
      Runner result = apiInstance.deleteV3ProjectsIdRunnersRunnerId(id, runnerId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#deleteV3ProjectsIdRunnersRunnerId");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **runnerId** | **Integer**| The ID of the runner | |

### Return type

[**Runner**](Runner.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Disable project&#39;s runner |  -  |

<a id="deleteV3ProjectsIdServicesServiceSlug"></a>
# **deleteV3ProjectsIdServicesServiceSlug**
> deleteV3ProjectsIdServicesServiceSlug(serviceSlug, id)

Delete a service for project

Delete a service for project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String serviceSlug = "asana"; // String | The name of the service
    Integer id = 56; // Integer | 
    try {
      apiInstance.deleteV3ProjectsIdServicesServiceSlug(serviceSlug, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#deleteV3ProjectsIdServicesServiceSlug");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **serviceSlug** | **String**| The name of the service | [enum: asana, assembla, bamboo, bugzilla, buildkite, builds-email, campfire, custom-issue-tracker, drone-ci, emails-on-push, external-wiki, flowdock, gemnasium, hipchat, irker, jira, kubernetes, mattermost-slash-commands, slack-slash-commands, pipelines-email, pivotaltracker, pushover, redmine, slack, mattermost, teamcity] |
| **id** | **Integer**|  | |

### Return type

null (empty response body)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Delete a service for project |  -  |

<a id="deleteV3ProjectsIdShareGroupId"></a>
# **deleteV3ProjectsIdShareGroupId**
> deleteV3ProjectsIdShareGroupId(id, groupId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    Integer groupId = 56; // Integer | The ID of the group
    try {
      apiInstance.deleteV3ProjectsIdShareGroupId(id, groupId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#deleteV3ProjectsIdShareGroupId");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **groupId** | **Integer**| The ID of the group | |

### Return type

null (empty response body)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | deleted Share |  -  |

<a id="deleteV3ProjectsIdSnippetsNoteableIdNotesNoteId"></a>
# **deleteV3ProjectsIdSnippetsNoteableIdNotesNoteId**
> Note deleteV3ProjectsIdSnippetsNoteableIdNotesNoteId(id, noteableId, noteId)

Delete a +noteable+ note

Delete a +noteable+ note

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    Integer noteableId = 56; // Integer | The ID of the noteable
    Integer noteId = 56; // Integer | The ID of a note
    try {
      Note result = apiInstance.deleteV3ProjectsIdSnippetsNoteableIdNotesNoteId(id, noteableId, noteId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#deleteV3ProjectsIdSnippetsNoteableIdNotesNoteId");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **noteableId** | **Integer**| The ID of the noteable | |
| **noteId** | **Integer**| The ID of a note | |

### Return type

[**Note**](Note.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Delete a +noteable+ note |  -  |

<a id="deleteV3ProjectsIdSnippetsSnippetId"></a>
# **deleteV3ProjectsIdSnippetsSnippetId**
> deleteV3ProjectsIdSnippetsSnippetId(id, snippetId)

Delete a project snippet

Delete a project snippet

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    Integer snippetId = 56; // Integer | The ID of a project snippet
    try {
      apiInstance.deleteV3ProjectsIdSnippetsSnippetId(id, snippetId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#deleteV3ProjectsIdSnippetsSnippetId");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **snippetId** | **Integer**| The ID of a project snippet | |

### Return type

null (empty response body)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Delete a project snippet |  -  |

<a id="deleteV3ProjectsIdSnippetsSnippetIdAwardEmojiAwardId"></a>
# **deleteV3ProjectsIdSnippetsSnippetIdAwardEmojiAwardId**
> AwardEmoji deleteV3ProjectsIdSnippetsSnippetIdAwardEmojiAwardId(awardId, id, snippetId)

Delete a +awardables+ award emoji

This feature was introduced in 8.9

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    Integer awardId = 56; // Integer | The ID of an award emoji
    Integer id = 56; // Integer | 
    Integer snippetId = 56; // Integer | 
    try {
      AwardEmoji result = apiInstance.deleteV3ProjectsIdSnippetsSnippetIdAwardEmojiAwardId(awardId, id, snippetId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#deleteV3ProjectsIdSnippetsSnippetIdAwardEmojiAwardId");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **awardId** | **Integer**| The ID of an award emoji | |
| **id** | **Integer**|  | |
| **snippetId** | **Integer**|  | |

### Return type

[**AwardEmoji**](AwardEmoji.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Delete a +awardables+ award emoji |  -  |

<a id="deleteV3ProjectsIdSnippetsSnippetIdNotesNoteIdAwardEmojiAwardId"></a>
# **deleteV3ProjectsIdSnippetsSnippetIdNotesNoteIdAwardEmojiAwardId**
> AwardEmoji deleteV3ProjectsIdSnippetsSnippetIdNotesNoteIdAwardEmojiAwardId(awardId, id, snippetId, noteId)

Delete a +awardables+ award emoji

This feature was introduced in 8.9

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    Integer awardId = 56; // Integer | The ID of an award emoji
    Integer id = 56; // Integer | 
    Integer snippetId = 56; // Integer | 
    Integer noteId = 56; // Integer | 
    try {
      AwardEmoji result = apiInstance.deleteV3ProjectsIdSnippetsSnippetIdNotesNoteIdAwardEmojiAwardId(awardId, id, snippetId, noteId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#deleteV3ProjectsIdSnippetsSnippetIdNotesNoteIdAwardEmojiAwardId");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **awardId** | **Integer**| The ID of an award emoji | |
| **id** | **Integer**|  | |
| **snippetId** | **Integer**|  | |
| **noteId** | **Integer**|  | |

### Return type

[**AwardEmoji**](AwardEmoji.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Delete a +awardables+ award emoji |  -  |

<a id="deleteV3ProjectsIdStar"></a>
# **deleteV3ProjectsIdStar**
> Project deleteV3ProjectsIdStar(id)

Unstar a project

Unstar a project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    try {
      Project result = apiInstance.deleteV3ProjectsIdStar(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#deleteV3ProjectsIdStar");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |

### Return type

[**Project**](Project.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Unstar a project |  -  |

<a id="deleteV3ProjectsIdTriggersToken"></a>
# **deleteV3ProjectsIdTriggersToken**
> Trigger deleteV3ProjectsIdTriggersToken(id, token)

Delete a trigger

Delete a trigger

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    String token = "token_example"; // String | The unique token of trigger
    try {
      Trigger result = apiInstance.deleteV3ProjectsIdTriggersToken(id, token);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#deleteV3ProjectsIdTriggersToken");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **token** | **String**| The unique token of trigger | |

### Return type

[**Trigger**](Trigger.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Delete a trigger |  -  |

<a id="deleteV3ProjectsIdVariablesKey"></a>
# **deleteV3ProjectsIdVariablesKey**
> Variable deleteV3ProjectsIdVariablesKey(id, key)

Delete an existing variable from a project

Delete an existing variable from a project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    String key = "key_example"; // String | The key of the variable
    try {
      Variable result = apiInstance.deleteV3ProjectsIdVariablesKey(id, key);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#deleteV3ProjectsIdVariablesKey");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **key** | **String**| The key of the variable | |

### Return type

[**Variable**](Variable.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Delete an existing variable from a project |  -  |

<a id="getV3Projects"></a>
# **getV3Projects**
> BasicProjectDetails getV3Projects(orderBy, sort, archived, visibility, search, page, perPage, simple)

Get a projects list for authenticated user

Get a projects list for authenticated user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String orderBy = "id"; // String | Return projects ordered by field
    String sort = "asc"; // String | Return projects sorted in ascending and descending order
    Boolean archived = true; // Boolean | Limit by archived status
    String visibility = "public"; // String | Limit by visibility
    String search = "search_example"; // String | Return list of authorized projects matching the search criteria
    Integer page = 56; // Integer | Current page number
    Integer perPage = 56; // Integer | Number of items per page
    Boolean simple = true; // Boolean | Return only the ID, URL, name, and path of each project
    try {
      BasicProjectDetails result = apiInstance.getV3Projects(orderBy, sort, archived, visibility, search, page, perPage, simple);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3Projects");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **orderBy** | **String**| Return projects ordered by field | [optional] [default to created_at] [enum: id, name, path, created_at, updated_at, last_activity_at] |
| **sort** | **String**| Return projects sorted in ascending and descending order | [optional] [default to desc] [enum: asc, desc] |
| **archived** | **Boolean**| Limit by archived status | [optional] |
| **visibility** | **String**| Limit by visibility | [optional] [enum: public, internal, private] |
| **search** | **String**| Return list of authorized projects matching the search criteria | [optional] |
| **page** | **Integer**| Current page number | [optional] |
| **perPage** | **Integer**| Number of items per page | [optional] |
| **simple** | **Boolean**| Return only the ID, URL, name, and path of each project | [optional] |

### Return type

[**BasicProjectDetails**](BasicProjectDetails.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get a projects list for authenticated user |  -  |

<a id="getV3ProjectsAll"></a>
# **getV3ProjectsAll**
> BasicProjectDetails getV3ProjectsAll(orderBy, sort, archived, visibility, search, page, perPage, simple, statistics)

Get all projects for admin user

Get all projects for admin user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String orderBy = "id"; // String | Return projects ordered by field
    String sort = "asc"; // String | Return projects sorted in ascending and descending order
    Boolean archived = true; // Boolean | Limit by archived status
    String visibility = "public"; // String | Limit by visibility
    String search = "search_example"; // String | Return list of authorized projects matching the search criteria
    Integer page = 56; // Integer | Current page number
    Integer perPage = 56; // Integer | Number of items per page
    Boolean simple = true; // Boolean | Return only the ID, URL, name, and path of each project
    Boolean statistics = true; // Boolean | Include project statistics
    try {
      BasicProjectDetails result = apiInstance.getV3ProjectsAll(orderBy, sort, archived, visibility, search, page, perPage, simple, statistics);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsAll");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **orderBy** | **String**| Return projects ordered by field | [optional] [default to created_at] [enum: id, name, path, created_at, updated_at, last_activity_at] |
| **sort** | **String**| Return projects sorted in ascending and descending order | [optional] [default to desc] [enum: asc, desc] |
| **archived** | **Boolean**| Limit by archived status | [optional] |
| **visibility** | **String**| Limit by visibility | [optional] [enum: public, internal, private] |
| **search** | **String**| Return list of authorized projects matching the search criteria | [optional] |
| **page** | **Integer**| Current page number | [optional] |
| **perPage** | **Integer**| Number of items per page | [optional] |
| **simple** | **Boolean**| Return only the ID, URL, name, and path of each project | [optional] |
| **statistics** | **Boolean**| Include project statistics | [optional] |

### Return type

[**BasicProjectDetails**](BasicProjectDetails.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get all projects for admin user |  -  |

<a id="getV3ProjectsId"></a>
# **getV3ProjectsId**
> ProjectWithAccess getV3ProjectsId(id)

Get a single project

Get a single project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    try {
      ProjectWithAccess result = apiInstance.getV3ProjectsId(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsId");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |

### Return type

[**ProjectWithAccess**](ProjectWithAccess.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get a single project |  -  |

<a id="getV3ProjectsIdAccessRequests"></a>
# **getV3ProjectsIdAccessRequests**
> AccessRequester getV3ProjectsIdAccessRequests(id, page, perPage)

Gets a list of access requests for a project.

This feature was introduced in GitLab 8.11.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The project ID
    Integer page = 56; // Integer | Current page number
    Integer perPage = 56; // Integer | Number of items per page
    try {
      AccessRequester result = apiInstance.getV3ProjectsIdAccessRequests(id, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsIdAccessRequests");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The project ID | |
| **page** | **Integer**| Current page number | [optional] |
| **perPage** | **Integer**| Number of items per page | [optional] |

### Return type

[**AccessRequester**](AccessRequester.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Gets a list of access requests for a project. |  -  |

<a id="getV3ProjectsIdBoards"></a>
# **getV3ProjectsIdBoards**
> Board getV3ProjectsIdBoards(id)

Get all project boards

This feature was introduced in 8.13

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    try {
      Board result = apiInstance.getV3ProjectsIdBoards(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsIdBoards");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |

### Return type

[**Board**](Board.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get all project boards |  -  |

<a id="getV3ProjectsIdBoardsBoardIdLists"></a>
# **getV3ProjectsIdBoardsBoardIdLists**
> ModelList getV3ProjectsIdBoardsBoardIdLists(id, boardId)

Get the lists of a project board

Does not include &#x60;backlog&#x60; and &#x60;done&#x60; lists. This feature was introduced in 8.13

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    Integer boardId = 56; // Integer | The ID of a board
    try {
      ModelList result = apiInstance.getV3ProjectsIdBoardsBoardIdLists(id, boardId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsIdBoardsBoardIdLists");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **boardId** | **Integer**| The ID of a board | |

### Return type

[**ModelList**](ModelList.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get the lists of a project board |  -  |

<a id="getV3ProjectsIdBoardsBoardIdListsListId"></a>
# **getV3ProjectsIdBoardsBoardIdListsListId**
> ModelList getV3ProjectsIdBoardsBoardIdListsListId(id, boardId, listId)

Get a list of a project board

This feature was introduced in 8.13

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    Integer boardId = 56; // Integer | The ID of a board
    Integer listId = 56; // Integer | The ID of a list
    try {
      ModelList result = apiInstance.getV3ProjectsIdBoardsBoardIdListsListId(id, boardId, listId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsIdBoardsBoardIdListsListId");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **boardId** | **Integer**| The ID of a board | |
| **listId** | **Integer**| The ID of a list | |

### Return type

[**ModelList**](ModelList.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get a list of a project board |  -  |

<a id="getV3ProjectsIdBuilds"></a>
# **getV3ProjectsIdBuilds**
> Build getV3ProjectsIdBuilds(id, scope, page, perPage)

Get a project builds

Get a project builds

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    String scope = "pending"; // String | The scope of builds to show
    Integer page = 56; // Integer | Current page number
    Integer perPage = 56; // Integer | Number of items per page
    try {
      Build result = apiInstance.getV3ProjectsIdBuilds(id, scope, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsIdBuilds");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **scope** | **String**| The scope of builds to show | [optional] [enum: pending, running, failed, success, canceled] |
| **page** | **Integer**| Current page number | [optional] |
| **perPage** | **Integer**| Number of items per page | [optional] |

### Return type

[**Build**](Build.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get a project builds |  -  |

<a id="getV3ProjectsIdBuildsArtifactsRefNameDownload"></a>
# **getV3ProjectsIdBuildsArtifactsRefNameDownload**
> getV3ProjectsIdBuildsArtifactsRefNameDownload(id, refName, job)

Download the artifacts file from build

This feature was introduced in GitLab 8.10

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    String refName = "refName_example"; // String | The ref from repository
    String job = "job_example"; // String | The name for the build
    try {
      apiInstance.getV3ProjectsIdBuildsArtifactsRefNameDownload(id, refName, job);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsIdBuildsArtifactsRefNameDownload");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **refName** | **String**| The ref from repository | |
| **job** | **String**| The name for the build | |

### Return type

null (empty response body)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Download the artifacts file from build |  -  |

<a id="getV3ProjectsIdBuildsBuildId"></a>
# **getV3ProjectsIdBuildsBuildId**
> Build getV3ProjectsIdBuildsBuildId(id, buildId)

Get a specific build of a project

Get a specific build of a project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    Integer buildId = 56; // Integer | The ID of a build
    try {
      Build result = apiInstance.getV3ProjectsIdBuildsBuildId(id, buildId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsIdBuildsBuildId");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **buildId** | **Integer**| The ID of a build | |

### Return type

[**Build**](Build.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get a specific build of a project |  -  |

<a id="getV3ProjectsIdBuildsBuildIdArtifacts"></a>
# **getV3ProjectsIdBuildsBuildIdArtifacts**
> getV3ProjectsIdBuildsBuildIdArtifacts(id, buildId)

Download the artifacts file from build

This feature was introduced in GitLab 8.5

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    Integer buildId = 56; // Integer | The ID of a build
    try {
      apiInstance.getV3ProjectsIdBuildsBuildIdArtifacts(id, buildId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsIdBuildsBuildIdArtifacts");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **buildId** | **Integer**| The ID of a build | |

### Return type

null (empty response body)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Download the artifacts file from build |  -  |

<a id="getV3ProjectsIdBuildsBuildIdTrace"></a>
# **getV3ProjectsIdBuildsBuildIdTrace**
> getV3ProjectsIdBuildsBuildIdTrace(id, buildId)

Get a trace of a specific build of a project

Get a trace of a specific build of a project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    Integer buildId = 56; // Integer | The ID of a build
    try {
      apiInstance.getV3ProjectsIdBuildsBuildIdTrace(id, buildId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsIdBuildsBuildIdTrace");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **buildId** | **Integer**| The ID of a build | |

### Return type

null (empty response body)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get a trace of a specific build of a project |  -  |

<a id="getV3ProjectsIdDeployKeys"></a>
# **getV3ProjectsIdDeployKeys**
> SSHKey getV3ProjectsIdDeployKeys(id)

Get a specific project&#39;s deploy keys

Get a specific project&#39;s deploy keys

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of the project
    try {
      SSHKey result = apiInstance.getV3ProjectsIdDeployKeys(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsIdDeployKeys");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of the project | |

### Return type

[**SSHKey**](SSHKey.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get a specific project&#39;s deploy keys |  -  |

<a id="getV3ProjectsIdDeployKeysKeyId"></a>
# **getV3ProjectsIdDeployKeysKeyId**
> SSHKey getV3ProjectsIdDeployKeysKeyId(id, keyId)

Get single deploy key

Get single deploy key

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of the project
    Integer keyId = 56; // Integer | The ID of the deploy key
    try {
      SSHKey result = apiInstance.getV3ProjectsIdDeployKeysKeyId(id, keyId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsIdDeployKeysKeyId");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of the project | |
| **keyId** | **Integer**| The ID of the deploy key | |

### Return type

[**SSHKey**](SSHKey.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get single deploy key |  -  |

<a id="getV3ProjectsIdDeployments"></a>
# **getV3ProjectsIdDeployments**
> Deployment getV3ProjectsIdDeployments(id, page, perPage)

Get all deployments of the project

This feature was introduced in GitLab 8.11.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The project ID
    Integer page = 56; // Integer | Current page number
    Integer perPage = 56; // Integer | Number of items per page
    try {
      Deployment result = apiInstance.getV3ProjectsIdDeployments(id, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsIdDeployments");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The project ID | |
| **page** | **Integer**| Current page number | [optional] |
| **perPage** | **Integer**| Number of items per page | [optional] |

### Return type

[**Deployment**](Deployment.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get all deployments of the project |  -  |

<a id="getV3ProjectsIdDeploymentsDeploymentId"></a>
# **getV3ProjectsIdDeploymentsDeploymentId**
> Deployment getV3ProjectsIdDeploymentsDeploymentId(id, deploymentId)

Gets a specific deployment

This feature was introduced in GitLab 8.11.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The project ID
    Integer deploymentId = 56; // Integer | The deployment ID
    try {
      Deployment result = apiInstance.getV3ProjectsIdDeploymentsDeploymentId(id, deploymentId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsIdDeploymentsDeploymentId");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The project ID | |
| **deploymentId** | **Integer**| The deployment ID | |

### Return type

[**Deployment**](Deployment.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Gets a specific deployment |  -  |

<a id="getV3ProjectsIdEnvironments"></a>
# **getV3ProjectsIdEnvironments**
> Environment getV3ProjectsIdEnvironments(id, page, perPage)

Get all environments of the project

This feature was introduced in GitLab 8.11.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The project ID
    Integer page = 56; // Integer | Current page number
    Integer perPage = 56; // Integer | Number of items per page
    try {
      Environment result = apiInstance.getV3ProjectsIdEnvironments(id, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsIdEnvironments");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The project ID | |
| **page** | **Integer**| Current page number | [optional] |
| **perPage** | **Integer**| Number of items per page | [optional] |

### Return type

[**Environment**](Environment.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get all environments of the project |  -  |

<a id="getV3ProjectsIdEvents"></a>
# **getV3ProjectsIdEvents**
> Event getV3ProjectsIdEvents(id, page, perPage)

Get events for a single project

Get events for a single project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    Integer page = 56; // Integer | Current page number
    Integer perPage = 56; // Integer | Number of items per page
    try {
      Event result = apiInstance.getV3ProjectsIdEvents(id, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsIdEvents");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **page** | **Integer**| Current page number | [optional] |
| **perPage** | **Integer**| Number of items per page | [optional] |

### Return type

[**Event**](Event.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get events for a single project |  -  |

<a id="getV3ProjectsIdHooks"></a>
# **getV3ProjectsIdHooks**
> ProjectHook getV3ProjectsIdHooks(id, page, perPage)

Get project hooks

Get project hooks

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    Integer page = 56; // Integer | Current page number
    Integer perPage = 56; // Integer | Number of items per page
    try {
      ProjectHook result = apiInstance.getV3ProjectsIdHooks(id, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsIdHooks");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **page** | **Integer**| Current page number | [optional] |
| **perPage** | **Integer**| Number of items per page | [optional] |

### Return type

[**ProjectHook**](ProjectHook.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get project hooks |  -  |

<a id="getV3ProjectsIdHooksHookId"></a>
# **getV3ProjectsIdHooksHookId**
> ProjectHook getV3ProjectsIdHooksHookId(id, hookId)

Get a project hook

Get a project hook

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    Integer hookId = 56; // Integer | The ID of a project hook
    try {
      ProjectHook result = apiInstance.getV3ProjectsIdHooksHookId(id, hookId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsIdHooksHookId");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **hookId** | **Integer**| The ID of a project hook | |

### Return type

[**ProjectHook**](ProjectHook.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get a project hook |  -  |

<a id="getV3ProjectsIdIssues"></a>
# **getV3ProjectsIdIssues**
> Issue getV3ProjectsIdIssues(id, state, iid, labels, milestone, orderBy, sort, page, perPage)

Get a list of project issues

Get a list of project issues

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    String state = "opened"; // String | Return opened, closed, or all issues
    Integer iid = 56; // Integer | Return the issue having the given `iid`
    String labels = "labels_example"; // String | Comma-separated list of label names
    String milestone = "milestone_example"; // String | Return issues for a specific milestone
    String orderBy = "created_at"; // String | Return issues ordered by `created_at` or `updated_at` fields.
    String sort = "asc"; // String | Return issues sorted in `asc` or `desc` order.
    Integer page = 56; // Integer | Current page number
    Integer perPage = 56; // Integer | Number of items per page
    try {
      Issue result = apiInstance.getV3ProjectsIdIssues(id, state, iid, labels, milestone, orderBy, sort, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsIdIssues");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **state** | **String**| Return opened, closed, or all issues | [optional] [default to all] [enum: opened, closed, all] |
| **iid** | **Integer**| Return the issue having the given &#x60;iid&#x60; | [optional] |
| **labels** | **String**| Comma-separated list of label names | [optional] |
| **milestone** | **String**| Return issues for a specific milestone | [optional] |
| **orderBy** | **String**| Return issues ordered by &#x60;created_at&#x60; or &#x60;updated_at&#x60; fields. | [optional] [default to created_at] [enum: created_at, updated_at] |
| **sort** | **String**| Return issues sorted in &#x60;asc&#x60; or &#x60;desc&#x60; order. | [optional] [default to desc] [enum: asc, desc] |
| **page** | **Integer**| Current page number | [optional] |
| **perPage** | **Integer**| Number of items per page | [optional] |

### Return type

[**Issue**](Issue.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get a list of project issues |  -  |

<a id="getV3ProjectsIdIssuesIssueId"></a>
# **getV3ProjectsIdIssuesIssueId**
> Issue getV3ProjectsIdIssuesIssueId(id, issueId)

Get a single project issue

Get a single project issue

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    Integer issueId = 56; // Integer | The ID of a project issue
    try {
      Issue result = apiInstance.getV3ProjectsIdIssuesIssueId(id, issueId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsIdIssuesIssueId");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **issueId** | **Integer**| The ID of a project issue | |

### Return type

[**Issue**](Issue.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get a single project issue |  -  |

<a id="getV3ProjectsIdIssuesIssueIdAwardEmoji"></a>
# **getV3ProjectsIdIssuesIssueIdAwardEmoji**
> AwardEmoji getV3ProjectsIdIssuesIssueIdAwardEmoji(id, issueId, page, perPage)

Get a list of project +awardable+ award emoji

This feature was introduced in 8.9

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    Integer issueId = 56; // Integer | The ID of an Issue, Merge Request or Snippet
    Integer page = 56; // Integer | Current page number
    Integer perPage = 56; // Integer | Number of items per page
    try {
      AwardEmoji result = apiInstance.getV3ProjectsIdIssuesIssueIdAwardEmoji(id, issueId, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsIdIssuesIssueIdAwardEmoji");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **issueId** | **Integer**| The ID of an Issue, Merge Request or Snippet | |
| **page** | **Integer**| Current page number | [optional] |
| **perPage** | **Integer**| Number of items per page | [optional] |

### Return type

[**AwardEmoji**](AwardEmoji.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get a list of project +awardable+ award emoji |  -  |

<a id="getV3ProjectsIdIssuesIssueIdAwardEmojiAwardId"></a>
# **getV3ProjectsIdIssuesIssueIdAwardEmojiAwardId**
> AwardEmoji getV3ProjectsIdIssuesIssueIdAwardEmojiAwardId(awardId, id, issueId)

Get a specific award emoji

This feature was introduced in 8.9

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    Integer awardId = 56; // Integer | The ID of the award
    Integer id = 56; // Integer | 
    Integer issueId = 56; // Integer | 
    try {
      AwardEmoji result = apiInstance.getV3ProjectsIdIssuesIssueIdAwardEmojiAwardId(awardId, id, issueId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsIdIssuesIssueIdAwardEmojiAwardId");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **awardId** | **Integer**| The ID of the award | |
| **id** | **Integer**|  | |
| **issueId** | **Integer**|  | |

### Return type

[**AwardEmoji**](AwardEmoji.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get a specific award emoji |  -  |

<a id="getV3ProjectsIdIssuesIssueIdNotesNoteIdAwardEmoji"></a>
# **getV3ProjectsIdIssuesIssueIdNotesNoteIdAwardEmoji**
> AwardEmoji getV3ProjectsIdIssuesIssueIdNotesNoteIdAwardEmoji(id, issueId, noteId, page, perPage)

Get a list of project +awardable+ award emoji

This feature was introduced in 8.9

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    Integer id = 56; // Integer | 
    Integer issueId = 56; // Integer | 
    Integer noteId = 56; // Integer | 
    Integer page = 56; // Integer | Current page number
    Integer perPage = 56; // Integer | Number of items per page
    try {
      AwardEmoji result = apiInstance.getV3ProjectsIdIssuesIssueIdNotesNoteIdAwardEmoji(id, issueId, noteId, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsIdIssuesIssueIdNotesNoteIdAwardEmoji");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**|  | |
| **issueId** | **Integer**|  | |
| **noteId** | **Integer**|  | |
| **page** | **Integer**| Current page number | [optional] |
| **perPage** | **Integer**| Number of items per page | [optional] |

### Return type

[**AwardEmoji**](AwardEmoji.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get a list of project +awardable+ award emoji |  -  |

<a id="getV3ProjectsIdIssuesIssueIdNotesNoteIdAwardEmojiAwardId"></a>
# **getV3ProjectsIdIssuesIssueIdNotesNoteIdAwardEmojiAwardId**
> AwardEmoji getV3ProjectsIdIssuesIssueIdNotesNoteIdAwardEmojiAwardId(awardId, id, issueId, noteId)

Get a specific award emoji

This feature was introduced in 8.9

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    Integer awardId = 56; // Integer | The ID of the award
    Integer id = 56; // Integer | 
    Integer issueId = 56; // Integer | 
    Integer noteId = 56; // Integer | 
    try {
      AwardEmoji result = apiInstance.getV3ProjectsIdIssuesIssueIdNotesNoteIdAwardEmojiAwardId(awardId, id, issueId, noteId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsIdIssuesIssueIdNotesNoteIdAwardEmojiAwardId");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **awardId** | **Integer**| The ID of the award | |
| **id** | **Integer**|  | |
| **issueId** | **Integer**|  | |
| **noteId** | **Integer**|  | |

### Return type

[**AwardEmoji**](AwardEmoji.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get a specific award emoji |  -  |

<a id="getV3ProjectsIdIssuesIssueIdTimeStats"></a>
# **getV3ProjectsIdIssuesIssueIdTimeStats**
> getV3ProjectsIdIssuesIssueIdTimeStats(id, issueId)

Show time stats for a project issue

Show time stats for a project issue

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    Integer issueId = 56; // Integer | The ID of a project issue
    try {
      apiInstance.getV3ProjectsIdIssuesIssueIdTimeStats(id, issueId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsIdIssuesIssueIdTimeStats");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **issueId** | **Integer**| The ID of a project issue | |

### Return type

null (empty response body)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Show time stats for a project issue |  -  |

<a id="getV3ProjectsIdIssuesNoteableIdNotes"></a>
# **getV3ProjectsIdIssuesNoteableIdNotes**
> Note getV3ProjectsIdIssuesNoteableIdNotes(id, noteableId, page, perPage)

Get a list of project +noteable+ notes

Get a list of project +noteable+ notes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    Integer noteableId = 56; // Integer | The ID of the noteable
    Integer page = 56; // Integer | Current page number
    Integer perPage = 56; // Integer | Number of items per page
    try {
      Note result = apiInstance.getV3ProjectsIdIssuesNoteableIdNotes(id, noteableId, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsIdIssuesNoteableIdNotes");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **noteableId** | **Integer**| The ID of the noteable | |
| **page** | **Integer**| Current page number | [optional] |
| **perPage** | **Integer**| Number of items per page | [optional] |

### Return type

[**Note**](Note.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get a list of project +noteable+ notes |  -  |

<a id="getV3ProjectsIdIssuesNoteableIdNotesNoteId"></a>
# **getV3ProjectsIdIssuesNoteableIdNotesNoteId**
> Note getV3ProjectsIdIssuesNoteableIdNotesNoteId(id, noteId, noteableId)

Get a single +noteable+ note

Get a single +noteable+ note

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    Integer noteId = 56; // Integer | The ID of a note
    Integer noteableId = 56; // Integer | The ID of the noteable
    try {
      Note result = apiInstance.getV3ProjectsIdIssuesNoteableIdNotesNoteId(id, noteId, noteableId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsIdIssuesNoteableIdNotesNoteId");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **noteId** | **Integer**| The ID of a note | |
| **noteableId** | **Integer**| The ID of the noteable | |

### Return type

[**Note**](Note.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get a single +noteable+ note |  -  |

<a id="getV3ProjectsIdKeys"></a>
# **getV3ProjectsIdKeys**
> SSHKey getV3ProjectsIdKeys(id)

Get a specific project&#39;s deploy keys

Get a specific project&#39;s deploy keys

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of the project
    try {
      SSHKey result = apiInstance.getV3ProjectsIdKeys(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsIdKeys");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of the project | |

### Return type

[**SSHKey**](SSHKey.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get a specific project&#39;s deploy keys |  -  |

<a id="getV3ProjectsIdKeysKeyId"></a>
# **getV3ProjectsIdKeysKeyId**
> SSHKey getV3ProjectsIdKeysKeyId(id, keyId)

Get single deploy key

Get single deploy key

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of the project
    Integer keyId = 56; // Integer | The ID of the deploy key
    try {
      SSHKey result = apiInstance.getV3ProjectsIdKeysKeyId(id, keyId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsIdKeysKeyId");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of the project | |
| **keyId** | **Integer**| The ID of the deploy key | |

### Return type

[**SSHKey**](SSHKey.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get single deploy key |  -  |

<a id="getV3ProjectsIdLabels"></a>
# **getV3ProjectsIdLabels**
> Label getV3ProjectsIdLabels(id)

Get all labels of the project

Get all labels of the project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    try {
      Label result = apiInstance.getV3ProjectsIdLabels(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsIdLabels");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |

### Return type

[**Label**](Label.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get all labels of the project |  -  |

<a id="getV3ProjectsIdMembers"></a>
# **getV3ProjectsIdMembers**
> Member getV3ProjectsIdMembers(id, query, page, perPage)

Gets a list of group or project members viewable by the authenticated user.

Gets a list of group or project members viewable by the authenticated user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The project ID
    String query = "query_example"; // String | A query string to search for members
    Integer page = 56; // Integer | Current page number
    Integer perPage = 56; // Integer | Number of items per page
    try {
      Member result = apiInstance.getV3ProjectsIdMembers(id, query, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsIdMembers");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The project ID | |
| **query** | **String**| A query string to search for members | [optional] |
| **page** | **Integer**| Current page number | [optional] |
| **perPage** | **Integer**| Number of items per page | [optional] |

### Return type

[**Member**](Member.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Gets a list of group or project members viewable by the authenticated user. |  -  |

<a id="getV3ProjectsIdMembersUserId"></a>
# **getV3ProjectsIdMembersUserId**
> Member getV3ProjectsIdMembersUserId(id, userId)

Gets a member of a group or project.

Gets a member of a group or project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The project ID
    Integer userId = 56; // Integer | The user ID of the member
    try {
      Member result = apiInstance.getV3ProjectsIdMembersUserId(id, userId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsIdMembersUserId");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The project ID | |
| **userId** | **Integer**| The user ID of the member | |

### Return type

[**Member**](Member.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Gets a member of a group or project. |  -  |

<a id="getV3ProjectsIdMergeRequestMergeRequestId"></a>
# **getV3ProjectsIdMergeRequestMergeRequestId**
> MergeRequest getV3ProjectsIdMergeRequestMergeRequestId(id, mergeRequestId)

Get a single merge request

This endpoint is deprecated and will be removed in GitLab 9.0.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    Integer mergeRequestId = 56; // Integer | The ID of a merge request
    try {
      MergeRequest result = apiInstance.getV3ProjectsIdMergeRequestMergeRequestId(id, mergeRequestId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsIdMergeRequestMergeRequestId");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **mergeRequestId** | **Integer**| The ID of a merge request | |

### Return type

[**MergeRequest**](MergeRequest.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get a single merge request |  -  |

<a id="getV3ProjectsIdMergeRequestMergeRequestIdChanges"></a>
# **getV3ProjectsIdMergeRequestMergeRequestIdChanges**
> MergeRequestChanges getV3ProjectsIdMergeRequestMergeRequestIdChanges(id, mergeRequestId)

Show the merge request changes

Show the merge request changes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    Integer mergeRequestId = 56; // Integer | 
    try {
      MergeRequestChanges result = apiInstance.getV3ProjectsIdMergeRequestMergeRequestIdChanges(id, mergeRequestId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsIdMergeRequestMergeRequestIdChanges");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **mergeRequestId** | **Integer**|  | |

### Return type

[**MergeRequestChanges**](MergeRequestChanges.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Show the merge request changes |  -  |

<a id="getV3ProjectsIdMergeRequestMergeRequestIdClosesIssues"></a>
# **getV3ProjectsIdMergeRequestMergeRequestIdClosesIssues**
> MRNote getV3ProjectsIdMergeRequestMergeRequestIdClosesIssues(id, mergeRequestId, page, perPage)

List issues that will be closed on merge

List issues that will be closed on merge

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    Integer mergeRequestId = 56; // Integer | 
    Integer page = 56; // Integer | Current page number
    Integer perPage = 56; // Integer | Number of items per page
    try {
      MRNote result = apiInstance.getV3ProjectsIdMergeRequestMergeRequestIdClosesIssues(id, mergeRequestId, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsIdMergeRequestMergeRequestIdClosesIssues");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **mergeRequestId** | **Integer**|  | |
| **page** | **Integer**| Current page number | [optional] |
| **perPage** | **Integer**| Number of items per page | [optional] |

### Return type

[**MRNote**](MRNote.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List issues that will be closed on merge |  -  |

<a id="getV3ProjectsIdMergeRequestMergeRequestIdComments"></a>
# **getV3ProjectsIdMergeRequestMergeRequestIdComments**
> MRNote getV3ProjectsIdMergeRequestMergeRequestIdComments(id, mergeRequestId, page, perPage)

Get the comments of a merge request

Duplicate. DEPRECATED and WILL BE REMOVED in 9.0

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    Integer mergeRequestId = 56; // Integer | 
    Integer page = 56; // Integer | Current page number
    Integer perPage = 56; // Integer | Number of items per page
    try {
      MRNote result = apiInstance.getV3ProjectsIdMergeRequestMergeRequestIdComments(id, mergeRequestId, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsIdMergeRequestMergeRequestIdComments");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **mergeRequestId** | **Integer**|  | |
| **page** | **Integer**| Current page number | [optional] |
| **perPage** | **Integer**| Number of items per page | [optional] |

### Return type

[**MRNote**](MRNote.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get the comments of a merge request |  -  |

<a id="getV3ProjectsIdMergeRequestMergeRequestIdCommits"></a>
# **getV3ProjectsIdMergeRequestMergeRequestIdCommits**
> RepoCommit getV3ProjectsIdMergeRequestMergeRequestIdCommits(id, mergeRequestId)

Get the commits of a merge request

Get the commits of a merge request

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    Integer mergeRequestId = 56; // Integer | 
    try {
      RepoCommit result = apiInstance.getV3ProjectsIdMergeRequestMergeRequestIdCommits(id, mergeRequestId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsIdMergeRequestMergeRequestIdCommits");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **mergeRequestId** | **Integer**|  | |

### Return type

[**RepoCommit**](RepoCommit.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get the commits of a merge request |  -  |

<a id="getV3ProjectsIdMergeRequests"></a>
# **getV3ProjectsIdMergeRequests**
> MergeRequest getV3ProjectsIdMergeRequests(id, state, orderBy, sort, page, perPage, iid)

List merge requests

List merge requests

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    String state = "opened"; // String | Return opened, closed, merged, or all merge requests
    String orderBy = "created_at"; // String | Return merge requests ordered by `created_at` or `updated_at` fields.
    String sort = "asc"; // String | Return merge requests sorted in `asc` or `desc` order.
    Integer page = 56; // Integer | Current page number
    Integer perPage = 56; // Integer | Number of items per page
    List<Integer> iid = Arrays.asList(); // List<Integer> | The IID of the merge requests
    try {
      MergeRequest result = apiInstance.getV3ProjectsIdMergeRequests(id, state, orderBy, sort, page, perPage, iid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsIdMergeRequests");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **state** | **String**| Return opened, closed, merged, or all merge requests | [optional] [default to all] [enum: opened, closed, merged, all] |
| **orderBy** | **String**| Return merge requests ordered by &#x60;created_at&#x60; or &#x60;updated_at&#x60; fields. | [optional] [default to created_at] [enum: created_at, updated_at] |
| **sort** | **String**| Return merge requests sorted in &#x60;asc&#x60; or &#x60;desc&#x60; order. | [optional] [default to desc] [enum: asc, desc] |
| **page** | **Integer**| Current page number | [optional] |
| **perPage** | **Integer**| Number of items per page | [optional] |
| **iid** | [**List&lt;Integer&gt;**](Integer.md)| The IID of the merge requests | [optional] |

### Return type

[**MergeRequest**](MergeRequest.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List merge requests |  -  |

<a id="getV3ProjectsIdMergeRequestsMergeRequestId"></a>
# **getV3ProjectsIdMergeRequestsMergeRequestId**
> MergeRequest getV3ProjectsIdMergeRequestsMergeRequestId(id, mergeRequestId)

Get a single merge request

Get a single merge request

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    Integer mergeRequestId = 56; // Integer | 
    try {
      MergeRequest result = apiInstance.getV3ProjectsIdMergeRequestsMergeRequestId(id, mergeRequestId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsIdMergeRequestsMergeRequestId");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **mergeRequestId** | **Integer**|  | |

### Return type

[**MergeRequest**](MergeRequest.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get a single merge request |  -  |

<a id="getV3ProjectsIdMergeRequestsMergeRequestIdAwardEmoji"></a>
# **getV3ProjectsIdMergeRequestsMergeRequestIdAwardEmoji**
> AwardEmoji getV3ProjectsIdMergeRequestsMergeRequestIdAwardEmoji(id, mergeRequestId, page, perPage)

Get a list of project +awardable+ award emoji

This feature was introduced in 8.9

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    Integer mergeRequestId = 56; // Integer | The ID of an Issue, Merge Request or Snippet
    Integer page = 56; // Integer | Current page number
    Integer perPage = 56; // Integer | Number of items per page
    try {
      AwardEmoji result = apiInstance.getV3ProjectsIdMergeRequestsMergeRequestIdAwardEmoji(id, mergeRequestId, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsIdMergeRequestsMergeRequestIdAwardEmoji");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **mergeRequestId** | **Integer**| The ID of an Issue, Merge Request or Snippet | |
| **page** | **Integer**| Current page number | [optional] |
| **perPage** | **Integer**| Number of items per page | [optional] |

### Return type

[**AwardEmoji**](AwardEmoji.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get a list of project +awardable+ award emoji |  -  |

<a id="getV3ProjectsIdMergeRequestsMergeRequestIdAwardEmojiAwardId"></a>
# **getV3ProjectsIdMergeRequestsMergeRequestIdAwardEmojiAwardId**
> AwardEmoji getV3ProjectsIdMergeRequestsMergeRequestIdAwardEmojiAwardId(awardId, id, mergeRequestId)

Get a specific award emoji

This feature was introduced in 8.9

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    Integer awardId = 56; // Integer | The ID of the award
    Integer id = 56; // Integer | 
    Integer mergeRequestId = 56; // Integer | 
    try {
      AwardEmoji result = apiInstance.getV3ProjectsIdMergeRequestsMergeRequestIdAwardEmojiAwardId(awardId, id, mergeRequestId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsIdMergeRequestsMergeRequestIdAwardEmojiAwardId");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **awardId** | **Integer**| The ID of the award | |
| **id** | **Integer**|  | |
| **mergeRequestId** | **Integer**|  | |

### Return type

[**AwardEmoji**](AwardEmoji.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get a specific award emoji |  -  |

<a id="getV3ProjectsIdMergeRequestsMergeRequestIdChanges"></a>
# **getV3ProjectsIdMergeRequestsMergeRequestIdChanges**
> MergeRequestChanges getV3ProjectsIdMergeRequestsMergeRequestIdChanges(id, mergeRequestId)

Show the merge request changes

Show the merge request changes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    Integer mergeRequestId = 56; // Integer | 
    try {
      MergeRequestChanges result = apiInstance.getV3ProjectsIdMergeRequestsMergeRequestIdChanges(id, mergeRequestId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsIdMergeRequestsMergeRequestIdChanges");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **mergeRequestId** | **Integer**|  | |

### Return type

[**MergeRequestChanges**](MergeRequestChanges.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Show the merge request changes |  -  |

<a id="getV3ProjectsIdMergeRequestsMergeRequestIdClosesIssues"></a>
# **getV3ProjectsIdMergeRequestsMergeRequestIdClosesIssues**
> MRNote getV3ProjectsIdMergeRequestsMergeRequestIdClosesIssues(id, mergeRequestId, page, perPage)

List issues that will be closed on merge

List issues that will be closed on merge

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    Integer mergeRequestId = 56; // Integer | 
    Integer page = 56; // Integer | Current page number
    Integer perPage = 56; // Integer | Number of items per page
    try {
      MRNote result = apiInstance.getV3ProjectsIdMergeRequestsMergeRequestIdClosesIssues(id, mergeRequestId, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsIdMergeRequestsMergeRequestIdClosesIssues");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **mergeRequestId** | **Integer**|  | |
| **page** | **Integer**| Current page number | [optional] |
| **perPage** | **Integer**| Number of items per page | [optional] |

### Return type

[**MRNote**](MRNote.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List issues that will be closed on merge |  -  |

<a id="getV3ProjectsIdMergeRequestsMergeRequestIdComments"></a>
# **getV3ProjectsIdMergeRequestsMergeRequestIdComments**
> MRNote getV3ProjectsIdMergeRequestsMergeRequestIdComments(id, mergeRequestId, page, perPage)

Get the comments of a merge request

Duplicate. DEPRECATED and WILL BE REMOVED in 9.0

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    Integer mergeRequestId = 56; // Integer | 
    Integer page = 56; // Integer | Current page number
    Integer perPage = 56; // Integer | Number of items per page
    try {
      MRNote result = apiInstance.getV3ProjectsIdMergeRequestsMergeRequestIdComments(id, mergeRequestId, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsIdMergeRequestsMergeRequestIdComments");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **mergeRequestId** | **Integer**|  | |
| **page** | **Integer**| Current page number | [optional] |
| **perPage** | **Integer**| Number of items per page | [optional] |

### Return type

[**MRNote**](MRNote.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get the comments of a merge request |  -  |

<a id="getV3ProjectsIdMergeRequestsMergeRequestIdCommits"></a>
# **getV3ProjectsIdMergeRequestsMergeRequestIdCommits**
> RepoCommit getV3ProjectsIdMergeRequestsMergeRequestIdCommits(id, mergeRequestId)

Get the commits of a merge request

Get the commits of a merge request

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    Integer mergeRequestId = 56; // Integer | 
    try {
      RepoCommit result = apiInstance.getV3ProjectsIdMergeRequestsMergeRequestIdCommits(id, mergeRequestId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsIdMergeRequestsMergeRequestIdCommits");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **mergeRequestId** | **Integer**|  | |

### Return type

[**RepoCommit**](RepoCommit.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get the commits of a merge request |  -  |

<a id="getV3ProjectsIdMergeRequestsMergeRequestIdNotesNoteIdAwardEmoji"></a>
# **getV3ProjectsIdMergeRequestsMergeRequestIdNotesNoteIdAwardEmoji**
> AwardEmoji getV3ProjectsIdMergeRequestsMergeRequestIdNotesNoteIdAwardEmoji(id, mergeRequestId, noteId, page, perPage)

Get a list of project +awardable+ award emoji

This feature was introduced in 8.9

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    Integer id = 56; // Integer | 
    Integer mergeRequestId = 56; // Integer | 
    Integer noteId = 56; // Integer | 
    Integer page = 56; // Integer | Current page number
    Integer perPage = 56; // Integer | Number of items per page
    try {
      AwardEmoji result = apiInstance.getV3ProjectsIdMergeRequestsMergeRequestIdNotesNoteIdAwardEmoji(id, mergeRequestId, noteId, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsIdMergeRequestsMergeRequestIdNotesNoteIdAwardEmoji");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**|  | |
| **mergeRequestId** | **Integer**|  | |
| **noteId** | **Integer**|  | |
| **page** | **Integer**| Current page number | [optional] |
| **perPage** | **Integer**| Number of items per page | [optional] |

### Return type

[**AwardEmoji**](AwardEmoji.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get a list of project +awardable+ award emoji |  -  |

<a id="getV3ProjectsIdMergeRequestsMergeRequestIdNotesNoteIdAwardEmojiAwardId"></a>
# **getV3ProjectsIdMergeRequestsMergeRequestIdNotesNoteIdAwardEmojiAwardId**
> AwardEmoji getV3ProjectsIdMergeRequestsMergeRequestIdNotesNoteIdAwardEmojiAwardId(awardId, id, mergeRequestId, noteId)

Get a specific award emoji

This feature was introduced in 8.9

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    Integer awardId = 56; // Integer | The ID of the award
    Integer id = 56; // Integer | 
    Integer mergeRequestId = 56; // Integer | 
    Integer noteId = 56; // Integer | 
    try {
      AwardEmoji result = apiInstance.getV3ProjectsIdMergeRequestsMergeRequestIdNotesNoteIdAwardEmojiAwardId(awardId, id, mergeRequestId, noteId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsIdMergeRequestsMergeRequestIdNotesNoteIdAwardEmojiAwardId");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **awardId** | **Integer**| The ID of the award | |
| **id** | **Integer**|  | |
| **mergeRequestId** | **Integer**|  | |
| **noteId** | **Integer**|  | |

### Return type

[**AwardEmoji**](AwardEmoji.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get a specific award emoji |  -  |

<a id="getV3ProjectsIdMergeRequestsMergeRequestIdTimeStats"></a>
# **getV3ProjectsIdMergeRequestsMergeRequestIdTimeStats**
> getV3ProjectsIdMergeRequestsMergeRequestIdTimeStats(id, mergeRequestId)

Show time stats for a project merge_request

Show time stats for a project merge_request

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    Integer mergeRequestId = 56; // Integer | The ID of a project merge_request
    try {
      apiInstance.getV3ProjectsIdMergeRequestsMergeRequestIdTimeStats(id, mergeRequestId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsIdMergeRequestsMergeRequestIdTimeStats");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **mergeRequestId** | **Integer**| The ID of a project merge_request | |

### Return type

null (empty response body)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Show time stats for a project merge_request |  -  |

<a id="getV3ProjectsIdMergeRequestsMergeRequestIdVersions"></a>
# **getV3ProjectsIdMergeRequestsMergeRequestIdVersions**
> MergeRequestDiff getV3ProjectsIdMergeRequestsMergeRequestIdVersions(id, mergeRequestId)

Get a list of merge request diff versions

This feature was introduced in GitLab 8.12.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    Integer mergeRequestId = 56; // Integer | The ID of a merge request
    try {
      MergeRequestDiff result = apiInstance.getV3ProjectsIdMergeRequestsMergeRequestIdVersions(id, mergeRequestId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsIdMergeRequestsMergeRequestIdVersions");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **mergeRequestId** | **Integer**| The ID of a merge request | |

### Return type

[**MergeRequestDiff**](MergeRequestDiff.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get a list of merge request diff versions |  -  |

<a id="getV3ProjectsIdMergeRequestsMergeRequestIdVersionsVersionId"></a>
# **getV3ProjectsIdMergeRequestsMergeRequestIdVersionsVersionId**
> MergeRequestDiffFull getV3ProjectsIdMergeRequestsMergeRequestIdVersionsVersionId(id, mergeRequestId, versionId)

Get a single merge request diff version

This feature was introduced in GitLab 8.12.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    Integer mergeRequestId = 56; // Integer | The ID of a merge request
    Integer versionId = 56; // Integer | The ID of a merge request diff version
    try {
      MergeRequestDiffFull result = apiInstance.getV3ProjectsIdMergeRequestsMergeRequestIdVersionsVersionId(id, mergeRequestId, versionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsIdMergeRequestsMergeRequestIdVersionsVersionId");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **mergeRequestId** | **Integer**| The ID of a merge request | |
| **versionId** | **Integer**| The ID of a merge request diff version | |

### Return type

[**MergeRequestDiffFull**](MergeRequestDiffFull.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get a single merge request diff version |  -  |

<a id="getV3ProjectsIdMergeRequestsNoteableIdNotes"></a>
# **getV3ProjectsIdMergeRequestsNoteableIdNotes**
> Note getV3ProjectsIdMergeRequestsNoteableIdNotes(id, noteableId, page, perPage)

Get a list of project +noteable+ notes

Get a list of project +noteable+ notes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    Integer noteableId = 56; // Integer | The ID of the noteable
    Integer page = 56; // Integer | Current page number
    Integer perPage = 56; // Integer | Number of items per page
    try {
      Note result = apiInstance.getV3ProjectsIdMergeRequestsNoteableIdNotes(id, noteableId, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsIdMergeRequestsNoteableIdNotes");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **noteableId** | **Integer**| The ID of the noteable | |
| **page** | **Integer**| Current page number | [optional] |
| **perPage** | **Integer**| Number of items per page | [optional] |

### Return type

[**Note**](Note.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get a list of project +noteable+ notes |  -  |

<a id="getV3ProjectsIdMergeRequestsNoteableIdNotesNoteId"></a>
# **getV3ProjectsIdMergeRequestsNoteableIdNotesNoteId**
> Note getV3ProjectsIdMergeRequestsNoteableIdNotesNoteId(id, noteId, noteableId)

Get a single +noteable+ note

Get a single +noteable+ note

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    Integer noteId = 56; // Integer | The ID of a note
    Integer noteableId = 56; // Integer | The ID of the noteable
    try {
      Note result = apiInstance.getV3ProjectsIdMergeRequestsNoteableIdNotesNoteId(id, noteId, noteableId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsIdMergeRequestsNoteableIdNotesNoteId");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **noteId** | **Integer**| The ID of a note | |
| **noteableId** | **Integer**| The ID of the noteable | |

### Return type

[**Note**](Note.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get a single +noteable+ note |  -  |

<a id="getV3ProjectsIdMilestones"></a>
# **getV3ProjectsIdMilestones**
> Milestone getV3ProjectsIdMilestones(id, state, page, perPage, iid)

Get a list of project milestones

Get a list of project milestones

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    String state = "active"; // String | Return \"active\", \"closed\", or \"all\" milestones
    Integer page = 56; // Integer | Current page number
    Integer perPage = 56; // Integer | Number of items per page
    List<Integer> iid = Arrays.asList(); // List<Integer> | The IID of the milestone
    try {
      Milestone result = apiInstance.getV3ProjectsIdMilestones(id, state, page, perPage, iid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsIdMilestones");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **state** | **String**| Return \&quot;active\&quot;, \&quot;closed\&quot;, or \&quot;all\&quot; milestones | [optional] [default to all] [enum: active, closed, all] |
| **page** | **Integer**| Current page number | [optional] |
| **perPage** | **Integer**| Number of items per page | [optional] |
| **iid** | [**List&lt;Integer&gt;**](Integer.md)| The IID of the milestone | [optional] |

### Return type

[**Milestone**](Milestone.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get a list of project milestones |  -  |

<a id="getV3ProjectsIdMilestonesMilestoneId"></a>
# **getV3ProjectsIdMilestonesMilestoneId**
> Milestone getV3ProjectsIdMilestonesMilestoneId(id, milestoneId)

Get a single project milestone

Get a single project milestone

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    Integer milestoneId = 56; // Integer | The ID of a project milestone
    try {
      Milestone result = apiInstance.getV3ProjectsIdMilestonesMilestoneId(id, milestoneId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsIdMilestonesMilestoneId");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **milestoneId** | **Integer**| The ID of a project milestone | |

### Return type

[**Milestone**](Milestone.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get a single project milestone |  -  |

<a id="getV3ProjectsIdMilestonesMilestoneIdIssues"></a>
# **getV3ProjectsIdMilestonesMilestoneIdIssues**
> Issue getV3ProjectsIdMilestonesMilestoneIdIssues(id, milestoneId, page, perPage)

Get all issues for a single project milestone

Get all issues for a single project milestone

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    Integer milestoneId = 56; // Integer | The ID of a project milestone
    Integer page = 56; // Integer | Current page number
    Integer perPage = 56; // Integer | Number of items per page
    try {
      Issue result = apiInstance.getV3ProjectsIdMilestonesMilestoneIdIssues(id, milestoneId, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsIdMilestonesMilestoneIdIssues");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **milestoneId** | **Integer**| The ID of a project milestone | |
| **page** | **Integer**| Current page number | [optional] |
| **perPage** | **Integer**| Number of items per page | [optional] |

### Return type

[**Issue**](Issue.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get all issues for a single project milestone |  -  |

<a id="getV3ProjectsIdNotificationSettings"></a>
# **getV3ProjectsIdNotificationSettings**
> NotificationSetting getV3ProjectsIdNotificationSettings(id)

Get project level notification level settings, defaults to Global

This feature was introduced in GitLab 8.12

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The group ID or project ID or project NAMESPACE/PROJECT_NAME
    try {
      NotificationSetting result = apiInstance.getV3ProjectsIdNotificationSettings(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsIdNotificationSettings");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The group ID or project ID or project NAMESPACE/PROJECT_NAME | |

### Return type

[**NotificationSetting**](NotificationSetting.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get project level notification level settings, defaults to Global |  -  |

<a id="getV3ProjectsIdPipelines"></a>
# **getV3ProjectsIdPipelines**
> Pipeline getV3ProjectsIdPipelines(id, page, perPage, scope)

Get all Pipelines of the project

This feature was introduced in GitLab 8.11.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The project ID
    Integer page = 56; // Integer | Current page number
    Integer perPage = 56; // Integer | Number of items per page
    String scope = "running"; // String | Either running, branches, or tags
    try {
      Pipeline result = apiInstance.getV3ProjectsIdPipelines(id, page, perPage, scope);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsIdPipelines");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The project ID | |
| **page** | **Integer**| Current page number | [optional] |
| **perPage** | **Integer**| Number of items per page | [optional] |
| **scope** | **String**| Either running, branches, or tags | [optional] [enum: running, branches, tags] |

### Return type

[**Pipeline**](Pipeline.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get all Pipelines of the project |  -  |

<a id="getV3ProjectsIdPipelinesPipelineId"></a>
# **getV3ProjectsIdPipelinesPipelineId**
> Pipeline getV3ProjectsIdPipelinesPipelineId(id, pipelineId)

Gets a specific pipeline for the project

This feature was introduced in GitLab 8.11

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The project ID
    Integer pipelineId = 56; // Integer | The pipeline ID
    try {
      Pipeline result = apiInstance.getV3ProjectsIdPipelinesPipelineId(id, pipelineId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsIdPipelinesPipelineId");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The project ID | |
| **pipelineId** | **Integer**| The pipeline ID | |

### Return type

[**Pipeline**](Pipeline.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Gets a specific pipeline for the project |  -  |

<a id="getV3ProjectsIdRepositoryArchive"></a>
# **getV3ProjectsIdRepositoryArchive**
> getV3ProjectsIdRepositoryArchive(id, sha, format)

Get an archive of the repository

Get an archive of the repository

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    String sha = "sha_example"; // String | The commit sha of the archive to be downloaded
    String format = "format_example"; // String | The archive format
    try {
      apiInstance.getV3ProjectsIdRepositoryArchive(id, sha, format);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsIdRepositoryArchive");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **sha** | **String**| The commit sha of the archive to be downloaded | [optional] |
| **format** | **String**| The archive format | [optional] |

### Return type

null (empty response body)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get an archive of the repository |  -  |

<a id="getV3ProjectsIdRepositoryBlobsSha"></a>
# **getV3ProjectsIdRepositoryBlobsSha**
> getV3ProjectsIdRepositoryBlobsSha(id, sha, filepath)

Get a raw file contents

Get a raw file contents

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    String sha = "sha_example"; // String | The commit, branch name, or tag name
    String filepath = "filepath_example"; // String | The path to the file to display
    try {
      apiInstance.getV3ProjectsIdRepositoryBlobsSha(id, sha, filepath);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsIdRepositoryBlobsSha");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **sha** | **String**| The commit, branch name, or tag name | |
| **filepath** | **String**| The path to the file to display | |

### Return type

null (empty response body)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get a raw file contents |  -  |

<a id="getV3ProjectsIdRepositoryBranches"></a>
# **getV3ProjectsIdRepositoryBranches**
> RepoBranch getV3ProjectsIdRepositoryBranches(id)

Get a project repository branches

Get a project repository branches

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    try {
      RepoBranch result = apiInstance.getV3ProjectsIdRepositoryBranches(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsIdRepositoryBranches");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |

### Return type

[**RepoBranch**](RepoBranch.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get a project repository branches |  -  |

<a id="getV3ProjectsIdRepositoryBranchesBranch"></a>
# **getV3ProjectsIdRepositoryBranchesBranch**
> RepoBranch getV3ProjectsIdRepositoryBranchesBranch(id, branch)

Get a single branch

Get a single branch

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    String branch = "branch_example"; // String | The name of the branch
    try {
      RepoBranch result = apiInstance.getV3ProjectsIdRepositoryBranchesBranch(id, branch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsIdRepositoryBranchesBranch");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **branch** | **String**| The name of the branch | |

### Return type

[**RepoBranch**](RepoBranch.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get a single branch |  -  |

<a id="getV3ProjectsIdRepositoryCommits"></a>
# **getV3ProjectsIdRepositoryCommits**
> RepoCommit getV3ProjectsIdRepositoryCommits(id, refName, since, until, page, perPage, path)

Get a project repository commits

Get a project repository commits

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    String refName = "refName_example"; // String | The name of a repository branch or tag, if not given the default branch is used
    String since = "since_example"; // String | Only commits after or in this date will be returned
    String until = "until_example"; // String | Only commits before or in this date will be returned
    Integer page = 0; // Integer | The page for pagination
    Integer perPage = 20; // Integer | The number of results per page
    String path = "path_example"; // String | The file path
    try {
      RepoCommit result = apiInstance.getV3ProjectsIdRepositoryCommits(id, refName, since, until, page, perPage, path);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsIdRepositoryCommits");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **refName** | **String**| The name of a repository branch or tag, if not given the default branch is used | [optional] |
| **since** | **String**| Only commits after or in this date will be returned | [optional] |
| **until** | **String**| Only commits before or in this date will be returned | [optional] |
| **page** | **Integer**| The page for pagination | [optional] [default to 0] |
| **perPage** | **Integer**| The number of results per page | [optional] [default to 20] |
| **path** | **String**| The file path | [optional] |

### Return type

[**RepoCommit**](RepoCommit.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get a project repository commits |  -  |

<a id="getV3ProjectsIdRepositoryCommitsSha"></a>
# **getV3ProjectsIdRepositoryCommitsSha**
> RepoCommitDetail getV3ProjectsIdRepositoryCommitsSha(id, sha)

Get a specific commit of a project

Get a specific commit of a project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    String sha = "sha_example"; // String | A commit sha, or the name of a branch or tag
    try {
      RepoCommitDetail result = apiInstance.getV3ProjectsIdRepositoryCommitsSha(id, sha);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsIdRepositoryCommitsSha");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **sha** | **String**| A commit sha, or the name of a branch or tag | |

### Return type

[**RepoCommitDetail**](RepoCommitDetail.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get a specific commit of a project |  -  |
| **404** | Not Found |  -  |

<a id="getV3ProjectsIdRepositoryCommitsShaBlob"></a>
# **getV3ProjectsIdRepositoryCommitsShaBlob**
> getV3ProjectsIdRepositoryCommitsShaBlob(id, sha, filepath)

Get a raw file contents

Get a raw file contents

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    String sha = "sha_example"; // String | The commit, branch name, or tag name
    String filepath = "filepath_example"; // String | The path to the file to display
    try {
      apiInstance.getV3ProjectsIdRepositoryCommitsShaBlob(id, sha, filepath);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsIdRepositoryCommitsShaBlob");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **sha** | **String**| The commit, branch name, or tag name | |
| **filepath** | **String**| The path to the file to display | |

### Return type

null (empty response body)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get a raw file contents |  -  |

<a id="getV3ProjectsIdRepositoryCommitsShaBuilds"></a>
# **getV3ProjectsIdRepositoryCommitsShaBuilds**
> Build getV3ProjectsIdRepositoryCommitsShaBuilds(id, sha, scope, page, perPage)

Get builds for a specific commit of a project

Get builds for a specific commit of a project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    String sha = "sha_example"; // String | The SHA id of a commit
    String scope = "pending"; // String | The scope of builds to show
    Integer page = 56; // Integer | Current page number
    Integer perPage = 56; // Integer | Number of items per page
    try {
      Build result = apiInstance.getV3ProjectsIdRepositoryCommitsShaBuilds(id, sha, scope, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsIdRepositoryCommitsShaBuilds");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **sha** | **String**| The SHA id of a commit | |
| **scope** | **String**| The scope of builds to show | [optional] [enum: pending, running, failed, success, canceled] |
| **page** | **Integer**| Current page number | [optional] |
| **perPage** | **Integer**| Number of items per page | [optional] |

### Return type

[**Build**](Build.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get builds for a specific commit of a project |  -  |

<a id="getV3ProjectsIdRepositoryCommitsShaComments"></a>
# **getV3ProjectsIdRepositoryCommitsShaComments**
> CommitNote getV3ProjectsIdRepositoryCommitsShaComments(id, sha, page, perPage)

Get a commit&#39;s comments

Get a commit&#39;s comments

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    String sha = "sha_example"; // String | A commit sha, or the name of a branch or tag
    Integer page = 56; // Integer | Current page number
    Integer perPage = 56; // Integer | Number of items per page
    try {
      CommitNote result = apiInstance.getV3ProjectsIdRepositoryCommitsShaComments(id, sha, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsIdRepositoryCommitsShaComments");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **sha** | **String**| A commit sha, or the name of a branch or tag | |
| **page** | **Integer**| Current page number | [optional] |
| **perPage** | **Integer**| Number of items per page | [optional] |

### Return type

[**CommitNote**](CommitNote.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get a commit&#39;s comments |  -  |
| **404** | Not Found |  -  |

<a id="getV3ProjectsIdRepositoryCommitsShaDiff"></a>
# **getV3ProjectsIdRepositoryCommitsShaDiff**
> getV3ProjectsIdRepositoryCommitsShaDiff(id, sha)

Get the diff for a specific commit of a project

Get the diff for a specific commit of a project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    String sha = "sha_example"; // String | A commit sha, or the name of a branch or tag
    try {
      apiInstance.getV3ProjectsIdRepositoryCommitsShaDiff(id, sha);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsIdRepositoryCommitsShaDiff");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **sha** | **String**| A commit sha, or the name of a branch or tag | |

### Return type

null (empty response body)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get the diff for a specific commit of a project |  -  |
| **404** | Not Found |  -  |

<a id="getV3ProjectsIdRepositoryCommitsShaStatuses"></a>
# **getV3ProjectsIdRepositoryCommitsShaStatuses**
> CommitStatus getV3ProjectsIdRepositoryCommitsShaStatuses(id, sha, ref, stage, name, all, page, perPage)

Get a commit&#39;s statuses

Get a commit&#39;s statuses

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    String sha = "sha_example"; // String | The commit hash
    String ref = "ref_example"; // String | The ref
    String stage = "stage_example"; // String | The stage
    String name = "name_example"; // String | The name
    String all = "all_example"; // String | Show all statuses, default: false
    Integer page = 56; // Integer | Current page number
    Integer perPage = 56; // Integer | Number of items per page
    try {
      CommitStatus result = apiInstance.getV3ProjectsIdRepositoryCommitsShaStatuses(id, sha, ref, stage, name, all, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsIdRepositoryCommitsShaStatuses");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **sha** | **String**| The commit hash | |
| **ref** | **String**| The ref | [optional] |
| **stage** | **String**| The stage | [optional] |
| **name** | **String**| The name | [optional] |
| **all** | **String**| Show all statuses, default: false | [optional] |
| **page** | **Integer**| Current page number | [optional] |
| **perPage** | **Integer**| Number of items per page | [optional] |

### Return type

[**CommitStatus**](CommitStatus.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get a commit&#39;s statuses |  -  |

<a id="getV3ProjectsIdRepositoryCompare"></a>
# **getV3ProjectsIdRepositoryCompare**
> Compare getV3ProjectsIdRepositoryCompare(id, from, to)

Compare two branches, tags, or commits

Compare two branches, tags, or commits

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    String from = "from_example"; // String | The commit, branch name, or tag name to start comparison
    String to = "to_example"; // String | The commit, branch name, or tag name to stop comparison
    try {
      Compare result = apiInstance.getV3ProjectsIdRepositoryCompare(id, from, to);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsIdRepositoryCompare");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **from** | **String**| The commit, branch name, or tag name to start comparison | |
| **to** | **String**| The commit, branch name, or tag name to stop comparison | |

### Return type

[**Compare**](Compare.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Compare two branches, tags, or commits |  -  |

<a id="getV3ProjectsIdRepositoryContributors"></a>
# **getV3ProjectsIdRepositoryContributors**
> Contributor getV3ProjectsIdRepositoryContributors(id)

Get repository contributors

Get repository contributors

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    try {
      Contributor result = apiInstance.getV3ProjectsIdRepositoryContributors(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsIdRepositoryContributors");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |

### Return type

[**Contributor**](Contributor.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get repository contributors |  -  |

<a id="getV3ProjectsIdRepositoryFiles"></a>
# **getV3ProjectsIdRepositoryFiles**
> getV3ProjectsIdRepositoryFiles(id, filePath, ref)

Get a file from repository

Get a file from repository

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The project ID
    String filePath = "filePath_example"; // String | The path to the file. Ex. lib/class.rb
    String ref = "ref_example"; // String | The name of branch, tag, or commit
    try {
      apiInstance.getV3ProjectsIdRepositoryFiles(id, filePath, ref);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsIdRepositoryFiles");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The project ID | |
| **filePath** | **String**| The path to the file. Ex. lib/class.rb | |
| **ref** | **String**| The name of branch, tag, or commit | |

### Return type

null (empty response body)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get a file from repository |  -  |

<a id="getV3ProjectsIdRepositoryRawBlobsSha"></a>
# **getV3ProjectsIdRepositoryRawBlobsSha**
> getV3ProjectsIdRepositoryRawBlobsSha(id, sha)

Get a raw blob contents by blob sha

Get a raw blob contents by blob sha

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    String sha = "sha_example"; // String | The commit, branch name, or tag name
    try {
      apiInstance.getV3ProjectsIdRepositoryRawBlobsSha(id, sha);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsIdRepositoryRawBlobsSha");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **sha** | **String**| The commit, branch name, or tag name | |

### Return type

null (empty response body)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get a raw blob contents by blob sha |  -  |

<a id="getV3ProjectsIdRepositoryTags"></a>
# **getV3ProjectsIdRepositoryTags**
> RepoTag getV3ProjectsIdRepositoryTags(id)

Get a project repository tags

Get a project repository tags

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    try {
      RepoTag result = apiInstance.getV3ProjectsIdRepositoryTags(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsIdRepositoryTags");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |

### Return type

[**RepoTag**](RepoTag.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get a project repository tags |  -  |

<a id="getV3ProjectsIdRepositoryTagsTagName"></a>
# **getV3ProjectsIdRepositoryTagsTagName**
> RepoTag getV3ProjectsIdRepositoryTagsTagName(id, tagName)

Get a single repository tag

Get a single repository tag

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    String tagName = "tagName_example"; // String | The name of the tag
    try {
      RepoTag result = apiInstance.getV3ProjectsIdRepositoryTagsTagName(id, tagName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsIdRepositoryTagsTagName");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **tagName** | **String**| The name of the tag | |

### Return type

[**RepoTag**](RepoTag.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get a single repository tag |  -  |

<a id="getV3ProjectsIdRepositoryTree"></a>
# **getV3ProjectsIdRepositoryTree**
> RepoTreeObject getV3ProjectsIdRepositoryTree(id, refName, path, recursive)

Get a project repository tree

Get a project repository tree

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    String refName = "refName_example"; // String | The name of a repository branch or tag, if not given the default branch is used
    String path = "path_example"; // String | The path of the tree
    Boolean recursive = true; // Boolean | Used to get a recursive tree
    try {
      RepoTreeObject result = apiInstance.getV3ProjectsIdRepositoryTree(id, refName, path, recursive);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsIdRepositoryTree");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **refName** | **String**| The name of a repository branch or tag, if not given the default branch is used | [optional] |
| **path** | **String**| The path of the tree | [optional] |
| **recursive** | **Boolean**| Used to get a recursive tree | [optional] |

### Return type

[**RepoTreeObject**](RepoTreeObject.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get a project repository tree |  -  |

<a id="getV3ProjectsIdRunners"></a>
# **getV3ProjectsIdRunners**
> Runner getV3ProjectsIdRunners(id, scope, page, perPage)

Get runners available for project

Get runners available for project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    String scope = "active"; // String | The scope of specific runners to show
    Integer page = 56; // Integer | Current page number
    Integer perPage = 56; // Integer | Number of items per page
    try {
      Runner result = apiInstance.getV3ProjectsIdRunners(id, scope, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsIdRunners");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **scope** | **String**| The scope of specific runners to show | [optional] [enum: active, paused, online, specific, shared] |
| **page** | **Integer**| Current page number | [optional] |
| **perPage** | **Integer**| Number of items per page | [optional] |

### Return type

[**Runner**](Runner.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get runners available for project |  -  |

<a id="getV3ProjectsIdServicesServiceSlug"></a>
# **getV3ProjectsIdServicesServiceSlug**
> ProjectService getV3ProjectsIdServicesServiceSlug(serviceSlug, id)

Get the service settings for project

Get the service settings for project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String serviceSlug = "asana"; // String | The name of the service
    Integer id = 56; // Integer | 
    try {
      ProjectService result = apiInstance.getV3ProjectsIdServicesServiceSlug(serviceSlug, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsIdServicesServiceSlug");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **serviceSlug** | **String**| The name of the service | [enum: asana, assembla, bamboo, bugzilla, buildkite, builds-email, campfire, custom-issue-tracker, drone-ci, emails-on-push, external-wiki, flowdock, gemnasium, hipchat, irker, jira, kubernetes, mattermost-slash-commands, slack-slash-commands, pipelines-email, pivotaltracker, pushover, redmine, slack, mattermost, teamcity] |
| **id** | **Integer**|  | |

### Return type

[**ProjectService**](ProjectService.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get the service settings for project |  -  |

<a id="getV3ProjectsIdSnippets"></a>
# **getV3ProjectsIdSnippets**
> ProjectSnippet getV3ProjectsIdSnippets(id, page, perPage)

Get all project snippets

Get all project snippets

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    Integer page = 56; // Integer | Current page number
    Integer perPage = 56; // Integer | Number of items per page
    try {
      ProjectSnippet result = apiInstance.getV3ProjectsIdSnippets(id, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsIdSnippets");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **page** | **Integer**| Current page number | [optional] |
| **perPage** | **Integer**| Number of items per page | [optional] |

### Return type

[**ProjectSnippet**](ProjectSnippet.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get all project snippets |  -  |

<a id="getV3ProjectsIdSnippetsNoteableIdNotes"></a>
# **getV3ProjectsIdSnippetsNoteableIdNotes**
> Note getV3ProjectsIdSnippetsNoteableIdNotes(id, noteableId, page, perPage)

Get a list of project +noteable+ notes

Get a list of project +noteable+ notes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    Integer noteableId = 56; // Integer | The ID of the noteable
    Integer page = 56; // Integer | Current page number
    Integer perPage = 56; // Integer | Number of items per page
    try {
      Note result = apiInstance.getV3ProjectsIdSnippetsNoteableIdNotes(id, noteableId, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsIdSnippetsNoteableIdNotes");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **noteableId** | **Integer**| The ID of the noteable | |
| **page** | **Integer**| Current page number | [optional] |
| **perPage** | **Integer**| Number of items per page | [optional] |

### Return type

[**Note**](Note.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get a list of project +noteable+ notes |  -  |

<a id="getV3ProjectsIdSnippetsNoteableIdNotesNoteId"></a>
# **getV3ProjectsIdSnippetsNoteableIdNotesNoteId**
> Note getV3ProjectsIdSnippetsNoteableIdNotesNoteId(id, noteId, noteableId)

Get a single +noteable+ note

Get a single +noteable+ note

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    Integer noteId = 56; // Integer | The ID of a note
    Integer noteableId = 56; // Integer | The ID of the noteable
    try {
      Note result = apiInstance.getV3ProjectsIdSnippetsNoteableIdNotesNoteId(id, noteId, noteableId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsIdSnippetsNoteableIdNotesNoteId");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **noteId** | **Integer**| The ID of a note | |
| **noteableId** | **Integer**| The ID of the noteable | |

### Return type

[**Note**](Note.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get a single +noteable+ note |  -  |

<a id="getV3ProjectsIdSnippetsSnippetId"></a>
# **getV3ProjectsIdSnippetsSnippetId**
> ProjectSnippet getV3ProjectsIdSnippetsSnippetId(id, snippetId)

Get a single project snippet

Get a single project snippet

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    Integer snippetId = 56; // Integer | The ID of a project snippet
    try {
      ProjectSnippet result = apiInstance.getV3ProjectsIdSnippetsSnippetId(id, snippetId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsIdSnippetsSnippetId");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **snippetId** | **Integer**| The ID of a project snippet | |

### Return type

[**ProjectSnippet**](ProjectSnippet.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get a single project snippet |  -  |

<a id="getV3ProjectsIdSnippetsSnippetIdAwardEmoji"></a>
# **getV3ProjectsIdSnippetsSnippetIdAwardEmoji**
> AwardEmoji getV3ProjectsIdSnippetsSnippetIdAwardEmoji(id, snippetId, page, perPage)

Get a list of project +awardable+ award emoji

This feature was introduced in 8.9

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    Integer snippetId = 56; // Integer | The ID of an Issue, Merge Request or Snippet
    Integer page = 56; // Integer | Current page number
    Integer perPage = 56; // Integer | Number of items per page
    try {
      AwardEmoji result = apiInstance.getV3ProjectsIdSnippetsSnippetIdAwardEmoji(id, snippetId, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsIdSnippetsSnippetIdAwardEmoji");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **snippetId** | **Integer**| The ID of an Issue, Merge Request or Snippet | |
| **page** | **Integer**| Current page number | [optional] |
| **perPage** | **Integer**| Number of items per page | [optional] |

### Return type

[**AwardEmoji**](AwardEmoji.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get a list of project +awardable+ award emoji |  -  |

<a id="getV3ProjectsIdSnippetsSnippetIdAwardEmojiAwardId"></a>
# **getV3ProjectsIdSnippetsSnippetIdAwardEmojiAwardId**
> AwardEmoji getV3ProjectsIdSnippetsSnippetIdAwardEmojiAwardId(awardId, id, snippetId)

Get a specific award emoji

This feature was introduced in 8.9

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    Integer awardId = 56; // Integer | The ID of the award
    Integer id = 56; // Integer | 
    Integer snippetId = 56; // Integer | 
    try {
      AwardEmoji result = apiInstance.getV3ProjectsIdSnippetsSnippetIdAwardEmojiAwardId(awardId, id, snippetId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsIdSnippetsSnippetIdAwardEmojiAwardId");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **awardId** | **Integer**| The ID of the award | |
| **id** | **Integer**|  | |
| **snippetId** | **Integer**|  | |

### Return type

[**AwardEmoji**](AwardEmoji.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get a specific award emoji |  -  |

<a id="getV3ProjectsIdSnippetsSnippetIdNotesNoteIdAwardEmoji"></a>
# **getV3ProjectsIdSnippetsSnippetIdNotesNoteIdAwardEmoji**
> AwardEmoji getV3ProjectsIdSnippetsSnippetIdNotesNoteIdAwardEmoji(id, snippetId, noteId, page, perPage)

Get a list of project +awardable+ award emoji

This feature was introduced in 8.9

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    Integer id = 56; // Integer | 
    Integer snippetId = 56; // Integer | 
    Integer noteId = 56; // Integer | 
    Integer page = 56; // Integer | Current page number
    Integer perPage = 56; // Integer | Number of items per page
    try {
      AwardEmoji result = apiInstance.getV3ProjectsIdSnippetsSnippetIdNotesNoteIdAwardEmoji(id, snippetId, noteId, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsIdSnippetsSnippetIdNotesNoteIdAwardEmoji");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**|  | |
| **snippetId** | **Integer**|  | |
| **noteId** | **Integer**|  | |
| **page** | **Integer**| Current page number | [optional] |
| **perPage** | **Integer**| Number of items per page | [optional] |

### Return type

[**AwardEmoji**](AwardEmoji.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get a list of project +awardable+ award emoji |  -  |

<a id="getV3ProjectsIdSnippetsSnippetIdNotesNoteIdAwardEmojiAwardId"></a>
# **getV3ProjectsIdSnippetsSnippetIdNotesNoteIdAwardEmojiAwardId**
> AwardEmoji getV3ProjectsIdSnippetsSnippetIdNotesNoteIdAwardEmojiAwardId(awardId, id, snippetId, noteId)

Get a specific award emoji

This feature was introduced in 8.9

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    Integer awardId = 56; // Integer | The ID of the award
    Integer id = 56; // Integer | 
    Integer snippetId = 56; // Integer | 
    Integer noteId = 56; // Integer | 
    try {
      AwardEmoji result = apiInstance.getV3ProjectsIdSnippetsSnippetIdNotesNoteIdAwardEmojiAwardId(awardId, id, snippetId, noteId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsIdSnippetsSnippetIdNotesNoteIdAwardEmojiAwardId");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **awardId** | **Integer**| The ID of the award | |
| **id** | **Integer**|  | |
| **snippetId** | **Integer**|  | |
| **noteId** | **Integer**|  | |

### Return type

[**AwardEmoji**](AwardEmoji.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get a specific award emoji |  -  |

<a id="getV3ProjectsIdSnippetsSnippetIdRaw"></a>
# **getV3ProjectsIdSnippetsSnippetIdRaw**
> getV3ProjectsIdSnippetsSnippetIdRaw(id, snippetId)

Get a raw project snippet

Get a raw project snippet

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    Integer snippetId = 56; // Integer | The ID of a project snippet
    try {
      apiInstance.getV3ProjectsIdSnippetsSnippetIdRaw(id, snippetId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsIdSnippetsSnippetIdRaw");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **snippetId** | **Integer**| The ID of a project snippet | |

### Return type

null (empty response body)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get a raw project snippet |  -  |

<a id="getV3ProjectsIdTriggers"></a>
# **getV3ProjectsIdTriggers**
> Trigger getV3ProjectsIdTriggers(id, page, perPage)

Get triggers list

Get triggers list

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    Integer page = 56; // Integer | Current page number
    Integer perPage = 56; // Integer | Number of items per page
    try {
      Trigger result = apiInstance.getV3ProjectsIdTriggers(id, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsIdTriggers");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **page** | **Integer**| Current page number | [optional] |
| **perPage** | **Integer**| Number of items per page | [optional] |

### Return type

[**Trigger**](Trigger.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get triggers list |  -  |

<a id="getV3ProjectsIdTriggersToken"></a>
# **getV3ProjectsIdTriggersToken**
> Trigger getV3ProjectsIdTriggersToken(id, token)

Get specific trigger of a project

Get specific trigger of a project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    String token = "token_example"; // String | The unique token of trigger
    try {
      Trigger result = apiInstance.getV3ProjectsIdTriggersToken(id, token);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsIdTriggersToken");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **token** | **String**| The unique token of trigger | |

### Return type

[**Trigger**](Trigger.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get specific trigger of a project |  -  |

<a id="getV3ProjectsIdUsers"></a>
# **getV3ProjectsIdUsers**
> UserBasic getV3ProjectsIdUsers(id, search, page, perPage)

Get the users list of a project

Get the users list of a project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    String search = "search_example"; // String | Return list of users matching the search criteria
    Integer page = 56; // Integer | Current page number
    Integer perPage = 56; // Integer | Number of items per page
    try {
      UserBasic result = apiInstance.getV3ProjectsIdUsers(id, search, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsIdUsers");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **search** | **String**| Return list of users matching the search criteria | [optional] |
| **page** | **Integer**| Current page number | [optional] |
| **perPage** | **Integer**| Number of items per page | [optional] |

### Return type

[**UserBasic**](UserBasic.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get the users list of a project |  -  |

<a id="getV3ProjectsIdVariables"></a>
# **getV3ProjectsIdVariables**
> Variable getV3ProjectsIdVariables(id, page, perPage)

Get project variables

Get project variables

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    Integer page = 56; // Integer | Current page number
    Integer perPage = 56; // Integer | Number of items per page
    try {
      Variable result = apiInstance.getV3ProjectsIdVariables(id, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsIdVariables");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **page** | **Integer**| Current page number | [optional] |
| **perPage** | **Integer**| Number of items per page | [optional] |

### Return type

[**Variable**](Variable.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get project variables |  -  |

<a id="getV3ProjectsIdVariablesKey"></a>
# **getV3ProjectsIdVariablesKey**
> Variable getV3ProjectsIdVariablesKey(id, key)

Get a specific variable from a project

Get a specific variable from a project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    String key = "key_example"; // String | The key of the variable
    try {
      Variable result = apiInstance.getV3ProjectsIdVariablesKey(id, key);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsIdVariablesKey");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **key** | **String**| The key of the variable | |

### Return type

[**Variable**](Variable.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get a specific variable from a project |  -  |

<a id="getV3ProjectsOwned"></a>
# **getV3ProjectsOwned**
> BasicProjectDetails getV3ProjectsOwned(orderBy, sort, archived, visibility, search, page, perPage, simple, statistics)

Get an owned projects list for authenticated user

Get an owned projects list for authenticated user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String orderBy = "id"; // String | Return projects ordered by field
    String sort = "asc"; // String | Return projects sorted in ascending and descending order
    Boolean archived = true; // Boolean | Limit by archived status
    String visibility = "public"; // String | Limit by visibility
    String search = "search_example"; // String | Return list of authorized projects matching the search criteria
    Integer page = 56; // Integer | Current page number
    Integer perPage = 56; // Integer | Number of items per page
    Boolean simple = true; // Boolean | Return only the ID, URL, name, and path of each project
    Boolean statistics = true; // Boolean | Include project statistics
    try {
      BasicProjectDetails result = apiInstance.getV3ProjectsOwned(orderBy, sort, archived, visibility, search, page, perPage, simple, statistics);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsOwned");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **orderBy** | **String**| Return projects ordered by field | [optional] [default to created_at] [enum: id, name, path, created_at, updated_at, last_activity_at] |
| **sort** | **String**| Return projects sorted in ascending and descending order | [optional] [default to desc] [enum: asc, desc] |
| **archived** | **Boolean**| Limit by archived status | [optional] |
| **visibility** | **String**| Limit by visibility | [optional] [enum: public, internal, private] |
| **search** | **String**| Return list of authorized projects matching the search criteria | [optional] |
| **page** | **Integer**| Current page number | [optional] |
| **perPage** | **Integer**| Number of items per page | [optional] |
| **simple** | **Boolean**| Return only the ID, URL, name, and path of each project | [optional] |
| **statistics** | **Boolean**| Include project statistics | [optional] |

### Return type

[**BasicProjectDetails**](BasicProjectDetails.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get an owned projects list for authenticated user |  -  |

<a id="getV3ProjectsSearchQuery"></a>
# **getV3ProjectsSearchQuery**
> Project getV3ProjectsSearchQuery(query, orderBy, sort, page, perPage)

Search for projects the current user has access to

Search for projects the current user has access to

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String query = "query_example"; // String | The project name to be searched
    String orderBy = "id"; // String | Return projects ordered by field
    String sort = "asc"; // String | Return projects sorted in ascending and descending order
    Integer page = 56; // Integer | Current page number
    Integer perPage = 56; // Integer | Number of items per page
    try {
      Project result = apiInstance.getV3ProjectsSearchQuery(query, orderBy, sort, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsSearchQuery");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **query** | **String**| The project name to be searched | |
| **orderBy** | **String**| Return projects ordered by field | [optional] [default to created_at] [enum: id, name, path, created_at, updated_at, last_activity_at] |
| **sort** | **String**| Return projects sorted in ascending and descending order | [optional] [default to desc] [enum: asc, desc] |
| **page** | **Integer**| Current page number | [optional] |
| **perPage** | **Integer**| Number of items per page | [optional] |

### Return type

[**Project**](Project.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Search for projects the current user has access to |  -  |

<a id="getV3ProjectsStarred"></a>
# **getV3ProjectsStarred**
> BasicProjectDetails getV3ProjectsStarred(orderBy, sort, archived, visibility, search, page, perPage, simple)

Gets starred project for the authenticated user

Gets starred project for the authenticated user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String orderBy = "id"; // String | Return projects ordered by field
    String sort = "asc"; // String | Return projects sorted in ascending and descending order
    Boolean archived = true; // Boolean | Limit by archived status
    String visibility = "public"; // String | Limit by visibility
    String search = "search_example"; // String | Return list of authorized projects matching the search criteria
    Integer page = 56; // Integer | Current page number
    Integer perPage = 56; // Integer | Number of items per page
    Boolean simple = true; // Boolean | Return only the ID, URL, name, and path of each project
    try {
      BasicProjectDetails result = apiInstance.getV3ProjectsStarred(orderBy, sort, archived, visibility, search, page, perPage, simple);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsStarred");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **orderBy** | **String**| Return projects ordered by field | [optional] [default to created_at] [enum: id, name, path, created_at, updated_at, last_activity_at] |
| **sort** | **String**| Return projects sorted in ascending and descending order | [optional] [default to desc] [enum: asc, desc] |
| **archived** | **Boolean**| Limit by archived status | [optional] |
| **visibility** | **String**| Limit by visibility | [optional] [enum: public, internal, private] |
| **search** | **String**| Return list of authorized projects matching the search criteria | [optional] |
| **page** | **Integer**| Current page number | [optional] |
| **perPage** | **Integer**| Number of items per page | [optional] |
| **simple** | **Boolean**| Return only the ID, URL, name, and path of each project | [optional] |

### Return type

[**BasicProjectDetails**](BasicProjectDetails.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Gets starred project for the authenticated user |  -  |

<a id="getV3ProjectsVisible"></a>
# **getV3ProjectsVisible**
> BasicProjectDetails getV3ProjectsVisible(orderBy, sort, archived, visibility, search, page, perPage, simple)

Get a list of visible projects for authenticated user

Get a list of visible projects for authenticated user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String orderBy = "id"; // String | Return projects ordered by field
    String sort = "asc"; // String | Return projects sorted in ascending and descending order
    Boolean archived = true; // Boolean | Limit by archived status
    String visibility = "public"; // String | Limit by visibility
    String search = "search_example"; // String | Return list of authorized projects matching the search criteria
    Integer page = 56; // Integer | Current page number
    Integer perPage = 56; // Integer | Number of items per page
    Boolean simple = true; // Boolean | Return only the ID, URL, name, and path of each project
    try {
      BasicProjectDetails result = apiInstance.getV3ProjectsVisible(orderBy, sort, archived, visibility, search, page, perPage, simple);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getV3ProjectsVisible");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **orderBy** | **String**| Return projects ordered by field | [optional] [default to created_at] [enum: id, name, path, created_at, updated_at, last_activity_at] |
| **sort** | **String**| Return projects sorted in ascending and descending order | [optional] [default to desc] [enum: asc, desc] |
| **archived** | **Boolean**| Limit by archived status | [optional] |
| **visibility** | **String**| Limit by visibility | [optional] [enum: public, internal, private] |
| **search** | **String**| Return list of authorized projects matching the search criteria | [optional] |
| **page** | **Integer**| Current page number | [optional] |
| **perPage** | **Integer**| Number of items per page | [optional] |
| **simple** | **Boolean**| Return only the ID, URL, name, and path of each project | [optional] |

### Return type

[**BasicProjectDetails**](BasicProjectDetails.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get a list of visible projects for authenticated user |  -  |

<a id="postV3Projects"></a>
# **postV3Projects**
> Project postV3Projects(postV3ProjectsRequest)

Create new project

Create new project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    PostV3ProjectsRequest postV3ProjectsRequest = new PostV3ProjectsRequest(); // PostV3ProjectsRequest | 
    try {
      Project result = apiInstance.postV3Projects(postV3ProjectsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#postV3Projects");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **postV3ProjectsRequest** | [**PostV3ProjectsRequest**](PostV3ProjectsRequest.md)|  | |

### Return type

[**Project**](Project.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Create new project |  -  |

<a id="postV3ProjectsForkId"></a>
# **postV3ProjectsForkId**
> Project postV3ProjectsForkId(id, postV3ProjectsForkIdRequest)

Fork new project for the current user or provided namespace.

Fork new project for the current user or provided namespace.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    PostV3ProjectsForkIdRequest postV3ProjectsForkIdRequest = new PostV3ProjectsForkIdRequest(); // PostV3ProjectsForkIdRequest | 
    try {
      Project result = apiInstance.postV3ProjectsForkId(id, postV3ProjectsForkIdRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#postV3ProjectsForkId");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **postV3ProjectsForkIdRequest** | [**PostV3ProjectsForkIdRequest**](PostV3ProjectsForkIdRequest.md)|  | [optional] |

### Return type

[**Project**](Project.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Fork new project for the current user or provided namespace. |  -  |

<a id="postV3ProjectsIdAccessRequests"></a>
# **postV3ProjectsIdAccessRequests**
> AccessRequester postV3ProjectsIdAccessRequests(id)

Requests access for the authenticated user to a project.

This feature was introduced in GitLab 8.11.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The project ID
    try {
      AccessRequester result = apiInstance.postV3ProjectsIdAccessRequests(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#postV3ProjectsIdAccessRequests");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The project ID | |

### Return type

[**AccessRequester**](AccessRequester.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Requests access for the authenticated user to a project. |  -  |

<a id="postV3ProjectsIdArchive"></a>
# **postV3ProjectsIdArchive**
> Project postV3ProjectsIdArchive(id)

Archive a project

Archive a project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    try {
      Project result = apiInstance.postV3ProjectsIdArchive(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#postV3ProjectsIdArchive");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |

### Return type

[**Project**](Project.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Archive a project |  -  |

<a id="postV3ProjectsIdBoardsBoardIdLists"></a>
# **postV3ProjectsIdBoardsBoardIdLists**
> ModelList postV3ProjectsIdBoardsBoardIdLists(id, boardId, postV3ProjectsIdBoardsBoardIdListsRequest)

Create a new board list

This feature was introduced in 8.13

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    Integer boardId = 56; // Integer | The ID of a board
    PostV3ProjectsIdBoardsBoardIdListsRequest postV3ProjectsIdBoardsBoardIdListsRequest = new PostV3ProjectsIdBoardsBoardIdListsRequest(); // PostV3ProjectsIdBoardsBoardIdListsRequest | 
    try {
      ModelList result = apiInstance.postV3ProjectsIdBoardsBoardIdLists(id, boardId, postV3ProjectsIdBoardsBoardIdListsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#postV3ProjectsIdBoardsBoardIdLists");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **boardId** | **Integer**| The ID of a board | |
| **postV3ProjectsIdBoardsBoardIdListsRequest** | [**PostV3ProjectsIdBoardsBoardIdListsRequest**](PostV3ProjectsIdBoardsBoardIdListsRequest.md)|  | |

### Return type

[**ModelList**](ModelList.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Create a new board list |  -  |

<a id="postV3ProjectsIdBuildsBuildIdArtifactsKeep"></a>
# **postV3ProjectsIdBuildsBuildIdArtifactsKeep**
> Build postV3ProjectsIdBuildsBuildIdArtifactsKeep(id, buildId)

Keep the artifacts to prevent them from being deleted

Keep the artifacts to prevent them from being deleted

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    Integer buildId = 56; // Integer | The ID of a build
    try {
      Build result = apiInstance.postV3ProjectsIdBuildsBuildIdArtifactsKeep(id, buildId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#postV3ProjectsIdBuildsBuildIdArtifactsKeep");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **buildId** | **Integer**| The ID of a build | |

### Return type

[**Build**](Build.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Keep the artifacts to prevent them from being deleted |  -  |

<a id="postV3ProjectsIdBuildsBuildIdCancel"></a>
# **postV3ProjectsIdBuildsBuildIdCancel**
> Build postV3ProjectsIdBuildsBuildIdCancel(id, buildId)

Cancel a specific build of a project

Cancel a specific build of a project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    Integer buildId = 56; // Integer | The ID of a build
    try {
      Build result = apiInstance.postV3ProjectsIdBuildsBuildIdCancel(id, buildId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#postV3ProjectsIdBuildsBuildIdCancel");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **buildId** | **Integer**| The ID of a build | |

### Return type

[**Build**](Build.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Cancel a specific build of a project |  -  |

<a id="postV3ProjectsIdBuildsBuildIdErase"></a>
# **postV3ProjectsIdBuildsBuildIdErase**
> Build postV3ProjectsIdBuildsBuildIdErase(id, buildId)

Erase build (remove artifacts and build trace)

Erase build (remove artifacts and build trace)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    Integer buildId = 56; // Integer | The ID of a build
    try {
      Build result = apiInstance.postV3ProjectsIdBuildsBuildIdErase(id, buildId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#postV3ProjectsIdBuildsBuildIdErase");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **buildId** | **Integer**| The ID of a build | |

### Return type

[**Build**](Build.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Erase build (remove artifacts and build trace) |  -  |

<a id="postV3ProjectsIdBuildsBuildIdPlay"></a>
# **postV3ProjectsIdBuildsBuildIdPlay**
> Build postV3ProjectsIdBuildsBuildIdPlay(id, buildId)

Trigger a manual build

This feature was added in GitLab 8.11

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    Integer buildId = 56; // Integer | The ID of a Build
    try {
      Build result = apiInstance.postV3ProjectsIdBuildsBuildIdPlay(id, buildId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#postV3ProjectsIdBuildsBuildIdPlay");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **buildId** | **Integer**| The ID of a Build | |

### Return type

[**Build**](Build.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Trigger a manual build |  -  |

<a id="postV3ProjectsIdBuildsBuildIdRetry"></a>
# **postV3ProjectsIdBuildsBuildIdRetry**
> Build postV3ProjectsIdBuildsBuildIdRetry(id, buildId)

Retry a specific build of a project

Retry a specific build of a project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    Integer buildId = 56; // Integer | The ID of a build
    try {
      Build result = apiInstance.postV3ProjectsIdBuildsBuildIdRetry(id, buildId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#postV3ProjectsIdBuildsBuildIdRetry");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **buildId** | **Integer**| The ID of a build | |

### Return type

[**Build**](Build.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Retry a specific build of a project |  -  |

<a id="postV3ProjectsIdDeployKeys"></a>
# **postV3ProjectsIdDeployKeys**
> SSHKey postV3ProjectsIdDeployKeys(id, postV3ProjectsIdDeployKeysRequest)

Add new deploy key to currently authenticated user

Add new deploy key to currently authenticated user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of the project
    PostV3ProjectsIdDeployKeysRequest postV3ProjectsIdDeployKeysRequest = new PostV3ProjectsIdDeployKeysRequest(); // PostV3ProjectsIdDeployKeysRequest | 
    try {
      SSHKey result = apiInstance.postV3ProjectsIdDeployKeys(id, postV3ProjectsIdDeployKeysRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#postV3ProjectsIdDeployKeys");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of the project | |
| **postV3ProjectsIdDeployKeysRequest** | [**PostV3ProjectsIdDeployKeysRequest**](PostV3ProjectsIdDeployKeysRequest.md)|  | |

### Return type

[**SSHKey**](SSHKey.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Add new deploy key to currently authenticated user |  -  |

<a id="postV3ProjectsIdDeployKeysKeyIdEnable"></a>
# **postV3ProjectsIdDeployKeysKeyIdEnable**
> SSHKey postV3ProjectsIdDeployKeysKeyIdEnable(id, keyId)

Enable a deploy key for a project

This feature was added in GitLab 8.11

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of the project
    Integer keyId = 56; // Integer | The ID of the deploy key
    try {
      SSHKey result = apiInstance.postV3ProjectsIdDeployKeysKeyIdEnable(id, keyId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#postV3ProjectsIdDeployKeysKeyIdEnable");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of the project | |
| **keyId** | **Integer**| The ID of the deploy key | |

### Return type

[**SSHKey**](SSHKey.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Enable a deploy key for a project |  -  |

<a id="postV3ProjectsIdEnvironments"></a>
# **postV3ProjectsIdEnvironments**
> Environment postV3ProjectsIdEnvironments(id, postV3ProjectsIdEnvironmentsRequest)

Creates a new environment

This feature was introduced in GitLab 8.11.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The project ID
    PostV3ProjectsIdEnvironmentsRequest postV3ProjectsIdEnvironmentsRequest = new PostV3ProjectsIdEnvironmentsRequest(); // PostV3ProjectsIdEnvironmentsRequest | 
    try {
      Environment result = apiInstance.postV3ProjectsIdEnvironments(id, postV3ProjectsIdEnvironmentsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#postV3ProjectsIdEnvironments");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The project ID | |
| **postV3ProjectsIdEnvironmentsRequest** | [**PostV3ProjectsIdEnvironmentsRequest**](PostV3ProjectsIdEnvironmentsRequest.md)|  | |

### Return type

[**Environment**](Environment.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Creates a new environment |  -  |

<a id="postV3ProjectsIdForkForkedFromId"></a>
# **postV3ProjectsIdForkForkedFromId**
> postV3ProjectsIdForkForkedFromId(id, forkedFromId)

Mark this project as forked from another

Mark this project as forked from another

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    String forkedFromId = "forkedFromId_example"; // String | The ID of the project it was forked from
    try {
      apiInstance.postV3ProjectsIdForkForkedFromId(id, forkedFromId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#postV3ProjectsIdForkForkedFromId");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **forkedFromId** | **String**| The ID of the project it was forked from | |

### Return type

null (empty response body)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Mark this project as forked from another |  -  |

<a id="postV3ProjectsIdHooks"></a>
# **postV3ProjectsIdHooks**
> ProjectHook postV3ProjectsIdHooks(id, postV3ProjectsIdHooksRequest)

Add hook to project

Add hook to project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    PostV3ProjectsIdHooksRequest postV3ProjectsIdHooksRequest = new PostV3ProjectsIdHooksRequest(); // PostV3ProjectsIdHooksRequest | 
    try {
      ProjectHook result = apiInstance.postV3ProjectsIdHooks(id, postV3ProjectsIdHooksRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#postV3ProjectsIdHooks");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **postV3ProjectsIdHooksRequest** | [**PostV3ProjectsIdHooksRequest**](PostV3ProjectsIdHooksRequest.md)|  | |

### Return type

[**ProjectHook**](ProjectHook.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Add hook to project |  -  |

<a id="postV3ProjectsIdIssues"></a>
# **postV3ProjectsIdIssues**
> Issue postV3ProjectsIdIssues(id, postV3ProjectsIdIssuesRequest)

Create a new project issue

Create a new project issue

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    PostV3ProjectsIdIssuesRequest postV3ProjectsIdIssuesRequest = new PostV3ProjectsIdIssuesRequest(); // PostV3ProjectsIdIssuesRequest | 
    try {
      Issue result = apiInstance.postV3ProjectsIdIssues(id, postV3ProjectsIdIssuesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#postV3ProjectsIdIssues");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **postV3ProjectsIdIssuesRequest** | [**PostV3ProjectsIdIssuesRequest**](PostV3ProjectsIdIssuesRequest.md)|  | |

### Return type

[**Issue**](Issue.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Create a new project issue |  -  |

<a id="postV3ProjectsIdIssuesIssueIdAddSpentTime"></a>
# **postV3ProjectsIdIssuesIssueIdAddSpentTime**
> postV3ProjectsIdIssuesIssueIdAddSpentTime(id, issueId, postV3ProjectsIdIssuesIssueIdAddSpentTimeRequest)

Add spent time for a project issue

Add spent time for a project issue

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    Integer issueId = 56; // Integer | The ID of a project issue
    PostV3ProjectsIdIssuesIssueIdAddSpentTimeRequest postV3ProjectsIdIssuesIssueIdAddSpentTimeRequest = new PostV3ProjectsIdIssuesIssueIdAddSpentTimeRequest(); // PostV3ProjectsIdIssuesIssueIdAddSpentTimeRequest | 
    try {
      apiInstance.postV3ProjectsIdIssuesIssueIdAddSpentTime(id, issueId, postV3ProjectsIdIssuesIssueIdAddSpentTimeRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#postV3ProjectsIdIssuesIssueIdAddSpentTime");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **issueId** | **Integer**| The ID of a project issue | |
| **postV3ProjectsIdIssuesIssueIdAddSpentTimeRequest** | [**PostV3ProjectsIdIssuesIssueIdAddSpentTimeRequest**](PostV3ProjectsIdIssuesIssueIdAddSpentTimeRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Add spent time for a project issue |  -  |

<a id="postV3ProjectsIdIssuesIssueIdAwardEmoji"></a>
# **postV3ProjectsIdIssuesIssueIdAwardEmoji**
> AwardEmoji postV3ProjectsIdIssuesIssueIdAwardEmoji(id, issueId, postV3ProjectsIdIssuesIssueIdAwardEmojiRequest)

Award a new Emoji

This feature was introduced in 8.9

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    Integer id = 56; // Integer | 
    Integer issueId = 56; // Integer | 
    PostV3ProjectsIdIssuesIssueIdAwardEmojiRequest postV3ProjectsIdIssuesIssueIdAwardEmojiRequest = new PostV3ProjectsIdIssuesIssueIdAwardEmojiRequest(); // PostV3ProjectsIdIssuesIssueIdAwardEmojiRequest | 
    try {
      AwardEmoji result = apiInstance.postV3ProjectsIdIssuesIssueIdAwardEmoji(id, issueId, postV3ProjectsIdIssuesIssueIdAwardEmojiRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#postV3ProjectsIdIssuesIssueIdAwardEmoji");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**|  | |
| **issueId** | **Integer**|  | |
| **postV3ProjectsIdIssuesIssueIdAwardEmojiRequest** | [**PostV3ProjectsIdIssuesIssueIdAwardEmojiRequest**](PostV3ProjectsIdIssuesIssueIdAwardEmojiRequest.md)|  | |

### Return type

[**AwardEmoji**](AwardEmoji.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Award a new Emoji |  -  |

<a id="postV3ProjectsIdIssuesIssueIdMove"></a>
# **postV3ProjectsIdIssuesIssueIdMove**
> Issue postV3ProjectsIdIssuesIssueIdMove(id, issueId, postV3ProjectsIdIssuesIssueIdMoveRequest)

Move an existing issue

Move an existing issue

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    Integer issueId = 56; // Integer | The ID of a project issue
    PostV3ProjectsIdIssuesIssueIdMoveRequest postV3ProjectsIdIssuesIssueIdMoveRequest = new PostV3ProjectsIdIssuesIssueIdMoveRequest(); // PostV3ProjectsIdIssuesIssueIdMoveRequest | 
    try {
      Issue result = apiInstance.postV3ProjectsIdIssuesIssueIdMove(id, issueId, postV3ProjectsIdIssuesIssueIdMoveRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#postV3ProjectsIdIssuesIssueIdMove");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **issueId** | **Integer**| The ID of a project issue | |
| **postV3ProjectsIdIssuesIssueIdMoveRequest** | [**PostV3ProjectsIdIssuesIssueIdMoveRequest**](PostV3ProjectsIdIssuesIssueIdMoveRequest.md)|  | |

### Return type

[**Issue**](Issue.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Move an existing issue |  -  |

<a id="postV3ProjectsIdIssuesIssueIdNotesNoteIdAwardEmoji"></a>
# **postV3ProjectsIdIssuesIssueIdNotesNoteIdAwardEmoji**
> AwardEmoji postV3ProjectsIdIssuesIssueIdNotesNoteIdAwardEmoji(id, issueId, noteId, postV3ProjectsIdIssuesIssueIdAwardEmojiRequest)

Award a new Emoji

This feature was introduced in 8.9

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    Integer id = 56; // Integer | 
    Integer issueId = 56; // Integer | 
    Integer noteId = 56; // Integer | 
    PostV3ProjectsIdIssuesIssueIdAwardEmojiRequest postV3ProjectsIdIssuesIssueIdAwardEmojiRequest = new PostV3ProjectsIdIssuesIssueIdAwardEmojiRequest(); // PostV3ProjectsIdIssuesIssueIdAwardEmojiRequest | 
    try {
      AwardEmoji result = apiInstance.postV3ProjectsIdIssuesIssueIdNotesNoteIdAwardEmoji(id, issueId, noteId, postV3ProjectsIdIssuesIssueIdAwardEmojiRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#postV3ProjectsIdIssuesIssueIdNotesNoteIdAwardEmoji");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**|  | |
| **issueId** | **Integer**|  | |
| **noteId** | **Integer**|  | |
| **postV3ProjectsIdIssuesIssueIdAwardEmojiRequest** | [**PostV3ProjectsIdIssuesIssueIdAwardEmojiRequest**](PostV3ProjectsIdIssuesIssueIdAwardEmojiRequest.md)|  | |

### Return type

[**AwardEmoji**](AwardEmoji.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Award a new Emoji |  -  |

<a id="postV3ProjectsIdIssuesIssueIdResetSpentTime"></a>
# **postV3ProjectsIdIssuesIssueIdResetSpentTime**
> postV3ProjectsIdIssuesIssueIdResetSpentTime(id, issueId)

Reset spent time for a project issue

Reset spent time for a project issue

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    Integer issueId = 56; // Integer | The ID of a project issue
    try {
      apiInstance.postV3ProjectsIdIssuesIssueIdResetSpentTime(id, issueId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#postV3ProjectsIdIssuesIssueIdResetSpentTime");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **issueId** | **Integer**| The ID of a project issue | |

### Return type

null (empty response body)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Reset spent time for a project issue |  -  |

<a id="postV3ProjectsIdIssuesIssueIdResetTimeEstimate"></a>
# **postV3ProjectsIdIssuesIssueIdResetTimeEstimate**
> postV3ProjectsIdIssuesIssueIdResetTimeEstimate(id, issueId)

Reset the time estimate for a project issue

Reset the time estimate for a project issue

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    Integer issueId = 56; // Integer | The ID of a project issue
    try {
      apiInstance.postV3ProjectsIdIssuesIssueIdResetTimeEstimate(id, issueId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#postV3ProjectsIdIssuesIssueIdResetTimeEstimate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **issueId** | **Integer**| The ID of a project issue | |

### Return type

null (empty response body)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Reset the time estimate for a project issue |  -  |

<a id="postV3ProjectsIdIssuesIssueIdTimeEstimate"></a>
# **postV3ProjectsIdIssuesIssueIdTimeEstimate**
> postV3ProjectsIdIssuesIssueIdTimeEstimate(id, issueId, postV3ProjectsIdIssuesIssueIdAddSpentTimeRequest)

Set a time estimate for a project issue

Set a time estimate for a project issue

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    Integer issueId = 56; // Integer | The ID of a project issue
    PostV3ProjectsIdIssuesIssueIdAddSpentTimeRequest postV3ProjectsIdIssuesIssueIdAddSpentTimeRequest = new PostV3ProjectsIdIssuesIssueIdAddSpentTimeRequest(); // PostV3ProjectsIdIssuesIssueIdAddSpentTimeRequest | 
    try {
      apiInstance.postV3ProjectsIdIssuesIssueIdTimeEstimate(id, issueId, postV3ProjectsIdIssuesIssueIdAddSpentTimeRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#postV3ProjectsIdIssuesIssueIdTimeEstimate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **issueId** | **Integer**| The ID of a project issue | |
| **postV3ProjectsIdIssuesIssueIdAddSpentTimeRequest** | [**PostV3ProjectsIdIssuesIssueIdAddSpentTimeRequest**](PostV3ProjectsIdIssuesIssueIdAddSpentTimeRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Set a time estimate for a project issue |  -  |

<a id="postV3ProjectsIdIssuesIssueIdTodo"></a>
# **postV3ProjectsIdIssuesIssueIdTodo**
> Todo postV3ProjectsIdIssuesIssueIdTodo(id, issueId)

Create a todo on an issuable

Create a todo on an issuable

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    Integer issueId = 56; // Integer | The ID of an issuable
    try {
      Todo result = apiInstance.postV3ProjectsIdIssuesIssueIdTodo(id, issueId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#postV3ProjectsIdIssuesIssueIdTodo");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **issueId** | **Integer**| The ID of an issuable | |

### Return type

[**Todo**](Todo.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Create a todo on an issuable |  -  |

<a id="postV3ProjectsIdIssuesNoteableIdNotes"></a>
# **postV3ProjectsIdIssuesNoteableIdNotes**
> Note postV3ProjectsIdIssuesNoteableIdNotes(id, noteableId, postV3ProjectsIdIssuesNoteableIdNotesRequest)

Create a new +noteable+ note

Create a new +noteable+ note

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    Integer noteableId = 56; // Integer | The ID of the noteable
    PostV3ProjectsIdIssuesNoteableIdNotesRequest postV3ProjectsIdIssuesNoteableIdNotesRequest = new PostV3ProjectsIdIssuesNoteableIdNotesRequest(); // PostV3ProjectsIdIssuesNoteableIdNotesRequest | 
    try {
      Note result = apiInstance.postV3ProjectsIdIssuesNoteableIdNotes(id, noteableId, postV3ProjectsIdIssuesNoteableIdNotesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#postV3ProjectsIdIssuesNoteableIdNotes");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **noteableId** | **Integer**| The ID of the noteable | |
| **postV3ProjectsIdIssuesNoteableIdNotesRequest** | [**PostV3ProjectsIdIssuesNoteableIdNotesRequest**](PostV3ProjectsIdIssuesNoteableIdNotesRequest.md)|  | |

### Return type

[**Note**](Note.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Create a new +noteable+ note |  -  |

<a id="postV3ProjectsIdIssuesSubscribableIdSubscription"></a>
# **postV3ProjectsIdIssuesSubscribableIdSubscription**
> Issue postV3ProjectsIdIssuesSubscribableIdSubscription(id, subscribableId)

Subscribe to a resource

Subscribe to a resource

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    String subscribableId = "subscribableId_example"; // String | The ID of a resource
    try {
      Issue result = apiInstance.postV3ProjectsIdIssuesSubscribableIdSubscription(id, subscribableId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#postV3ProjectsIdIssuesSubscribableIdSubscription");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **subscribableId** | **String**| The ID of a resource | |

### Return type

[**Issue**](Issue.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Subscribe to a resource |  -  |

<a id="postV3ProjectsIdKeys"></a>
# **postV3ProjectsIdKeys**
> SSHKey postV3ProjectsIdKeys(id, postV3ProjectsIdDeployKeysRequest)

Add new deploy key to currently authenticated user

Add new deploy key to currently authenticated user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of the project
    PostV3ProjectsIdDeployKeysRequest postV3ProjectsIdDeployKeysRequest = new PostV3ProjectsIdDeployKeysRequest(); // PostV3ProjectsIdDeployKeysRequest | 
    try {
      SSHKey result = apiInstance.postV3ProjectsIdKeys(id, postV3ProjectsIdDeployKeysRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#postV3ProjectsIdKeys");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of the project | |
| **postV3ProjectsIdDeployKeysRequest** | [**PostV3ProjectsIdDeployKeysRequest**](PostV3ProjectsIdDeployKeysRequest.md)|  | |

### Return type

[**SSHKey**](SSHKey.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Add new deploy key to currently authenticated user |  -  |

<a id="postV3ProjectsIdKeysKeyIdEnable"></a>
# **postV3ProjectsIdKeysKeyIdEnable**
> SSHKey postV3ProjectsIdKeysKeyIdEnable(id, keyId)

Enable a deploy key for a project

This feature was added in GitLab 8.11

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of the project
    Integer keyId = 56; // Integer | The ID of the deploy key
    try {
      SSHKey result = apiInstance.postV3ProjectsIdKeysKeyIdEnable(id, keyId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#postV3ProjectsIdKeysKeyIdEnable");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of the project | |
| **keyId** | **Integer**| The ID of the deploy key | |

### Return type

[**SSHKey**](SSHKey.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Enable a deploy key for a project |  -  |

<a id="postV3ProjectsIdLabels"></a>
# **postV3ProjectsIdLabels**
> Label postV3ProjectsIdLabels(id, postV3ProjectsIdLabelsRequest)

Create a new label

Create a new label

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    PostV3ProjectsIdLabelsRequest postV3ProjectsIdLabelsRequest = new PostV3ProjectsIdLabelsRequest(); // PostV3ProjectsIdLabelsRequest | 
    try {
      Label result = apiInstance.postV3ProjectsIdLabels(id, postV3ProjectsIdLabelsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#postV3ProjectsIdLabels");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **postV3ProjectsIdLabelsRequest** | [**PostV3ProjectsIdLabelsRequest**](PostV3ProjectsIdLabelsRequest.md)|  | |

### Return type

[**Label**](Label.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Create a new label |  -  |

<a id="postV3ProjectsIdLabelsSubscribableIdSubscription"></a>
# **postV3ProjectsIdLabelsSubscribableIdSubscription**
> Label postV3ProjectsIdLabelsSubscribableIdSubscription(id, subscribableId)

Subscribe to a resource

Subscribe to a resource

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    String subscribableId = "subscribableId_example"; // String | The ID of a resource
    try {
      Label result = apiInstance.postV3ProjectsIdLabelsSubscribableIdSubscription(id, subscribableId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#postV3ProjectsIdLabelsSubscribableIdSubscription");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **subscribableId** | **String**| The ID of a resource | |

### Return type

[**Label**](Label.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Subscribe to a resource |  -  |

<a id="postV3ProjectsIdMembers"></a>
# **postV3ProjectsIdMembers**
> Member postV3ProjectsIdMembers(id, postV3GroupsIdMembersRequest)

Adds a member to a group or project.

Adds a member to a group or project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The project ID
    PostV3GroupsIdMembersRequest postV3GroupsIdMembersRequest = new PostV3GroupsIdMembersRequest(); // PostV3GroupsIdMembersRequest | 
    try {
      Member result = apiInstance.postV3ProjectsIdMembers(id, postV3GroupsIdMembersRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#postV3ProjectsIdMembers");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The project ID | |
| **postV3GroupsIdMembersRequest** | [**PostV3GroupsIdMembersRequest**](PostV3GroupsIdMembersRequest.md)|  | |

### Return type

[**Member**](Member.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Adds a member to a group or project. |  -  |

<a id="postV3ProjectsIdMergeRequestMergeRequestIdCancelMergeWhenBuildSucceeds"></a>
# **postV3ProjectsIdMergeRequestMergeRequestIdCancelMergeWhenBuildSucceeds**
> MergeRequest postV3ProjectsIdMergeRequestMergeRequestIdCancelMergeWhenBuildSucceeds(id, mergeRequestId)

Cancel merge if \&quot;Merge When Pipeline Succeeds\&quot; is enabled

Cancel merge if \&quot;Merge When Pipeline Succeeds\&quot; is enabled

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    Integer mergeRequestId = 56; // Integer | 
    try {
      MergeRequest result = apiInstance.postV3ProjectsIdMergeRequestMergeRequestIdCancelMergeWhenBuildSucceeds(id, mergeRequestId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#postV3ProjectsIdMergeRequestMergeRequestIdCancelMergeWhenBuildSucceeds");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **mergeRequestId** | **Integer**|  | |

### Return type

[**MergeRequest**](MergeRequest.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Cancel merge if \&quot;Merge When Pipeline Succeeds\&quot; is enabled |  -  |

<a id="postV3ProjectsIdMergeRequestMergeRequestIdComments"></a>
# **postV3ProjectsIdMergeRequestMergeRequestIdComments**
> MRNote postV3ProjectsIdMergeRequestMergeRequestIdComments(id, mergeRequestId, postV3ProjectsIdMergeRequestMergeRequestIdCommentsRequest)

Post a comment to a merge request

Duplicate. DEPRECATED and WILL BE REMOVED in 9.0

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    Integer mergeRequestId = 56; // Integer | 
    PostV3ProjectsIdMergeRequestMergeRequestIdCommentsRequest postV3ProjectsIdMergeRequestMergeRequestIdCommentsRequest = new PostV3ProjectsIdMergeRequestMergeRequestIdCommentsRequest(); // PostV3ProjectsIdMergeRequestMergeRequestIdCommentsRequest | 
    try {
      MRNote result = apiInstance.postV3ProjectsIdMergeRequestMergeRequestIdComments(id, mergeRequestId, postV3ProjectsIdMergeRequestMergeRequestIdCommentsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#postV3ProjectsIdMergeRequestMergeRequestIdComments");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **mergeRequestId** | **Integer**|  | |
| **postV3ProjectsIdMergeRequestMergeRequestIdCommentsRequest** | [**PostV3ProjectsIdMergeRequestMergeRequestIdCommentsRequest**](PostV3ProjectsIdMergeRequestMergeRequestIdCommentsRequest.md)|  | |

### Return type

[**MRNote**](MRNote.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Post a comment to a merge request |  -  |

<a id="postV3ProjectsIdMergeRequestSubscribableIdSubscription"></a>
# **postV3ProjectsIdMergeRequestSubscribableIdSubscription**
> MergeRequest postV3ProjectsIdMergeRequestSubscribableIdSubscription(id, subscribableId)

Subscribe to a resource

Subscribe to a resource

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    String subscribableId = "subscribableId_example"; // String | The ID of a resource
    try {
      MergeRequest result = apiInstance.postV3ProjectsIdMergeRequestSubscribableIdSubscription(id, subscribableId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#postV3ProjectsIdMergeRequestSubscribableIdSubscription");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **subscribableId** | **String**| The ID of a resource | |

### Return type

[**MergeRequest**](MergeRequest.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Subscribe to a resource |  -  |

<a id="postV3ProjectsIdMergeRequests"></a>
# **postV3ProjectsIdMergeRequests**
> MergeRequest postV3ProjectsIdMergeRequests(id, postV3ProjectsIdMergeRequestsRequest)

Create a merge request

Create a merge request

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    PostV3ProjectsIdMergeRequestsRequest postV3ProjectsIdMergeRequestsRequest = new PostV3ProjectsIdMergeRequestsRequest(); // PostV3ProjectsIdMergeRequestsRequest | 
    try {
      MergeRequest result = apiInstance.postV3ProjectsIdMergeRequests(id, postV3ProjectsIdMergeRequestsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#postV3ProjectsIdMergeRequests");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **postV3ProjectsIdMergeRequestsRequest** | [**PostV3ProjectsIdMergeRequestsRequest**](PostV3ProjectsIdMergeRequestsRequest.md)|  | |

### Return type

[**MergeRequest**](MergeRequest.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Create a merge request |  -  |

<a id="postV3ProjectsIdMergeRequestsMergeRequestIdAddSpentTime"></a>
# **postV3ProjectsIdMergeRequestsMergeRequestIdAddSpentTime**
> postV3ProjectsIdMergeRequestsMergeRequestIdAddSpentTime(id, mergeRequestId, postV3ProjectsIdIssuesIssueIdAddSpentTimeRequest)

Add spent time for a project merge_request

Add spent time for a project merge_request

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    Integer mergeRequestId = 56; // Integer | The ID of a project merge_request
    PostV3ProjectsIdIssuesIssueIdAddSpentTimeRequest postV3ProjectsIdIssuesIssueIdAddSpentTimeRequest = new PostV3ProjectsIdIssuesIssueIdAddSpentTimeRequest(); // PostV3ProjectsIdIssuesIssueIdAddSpentTimeRequest | 
    try {
      apiInstance.postV3ProjectsIdMergeRequestsMergeRequestIdAddSpentTime(id, mergeRequestId, postV3ProjectsIdIssuesIssueIdAddSpentTimeRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#postV3ProjectsIdMergeRequestsMergeRequestIdAddSpentTime");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **mergeRequestId** | **Integer**| The ID of a project merge_request | |
| **postV3ProjectsIdIssuesIssueIdAddSpentTimeRequest** | [**PostV3ProjectsIdIssuesIssueIdAddSpentTimeRequest**](PostV3ProjectsIdIssuesIssueIdAddSpentTimeRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Add spent time for a project merge_request |  -  |

<a id="postV3ProjectsIdMergeRequestsMergeRequestIdAwardEmoji"></a>
# **postV3ProjectsIdMergeRequestsMergeRequestIdAwardEmoji**
> AwardEmoji postV3ProjectsIdMergeRequestsMergeRequestIdAwardEmoji(id, mergeRequestId, postV3ProjectsIdIssuesIssueIdAwardEmojiRequest)

Award a new Emoji

This feature was introduced in 8.9

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    Integer id = 56; // Integer | 
    Integer mergeRequestId = 56; // Integer | 
    PostV3ProjectsIdIssuesIssueIdAwardEmojiRequest postV3ProjectsIdIssuesIssueIdAwardEmojiRequest = new PostV3ProjectsIdIssuesIssueIdAwardEmojiRequest(); // PostV3ProjectsIdIssuesIssueIdAwardEmojiRequest | 
    try {
      AwardEmoji result = apiInstance.postV3ProjectsIdMergeRequestsMergeRequestIdAwardEmoji(id, mergeRequestId, postV3ProjectsIdIssuesIssueIdAwardEmojiRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#postV3ProjectsIdMergeRequestsMergeRequestIdAwardEmoji");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**|  | |
| **mergeRequestId** | **Integer**|  | |
| **postV3ProjectsIdIssuesIssueIdAwardEmojiRequest** | [**PostV3ProjectsIdIssuesIssueIdAwardEmojiRequest**](PostV3ProjectsIdIssuesIssueIdAwardEmojiRequest.md)|  | |

### Return type

[**AwardEmoji**](AwardEmoji.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Award a new Emoji |  -  |

<a id="postV3ProjectsIdMergeRequestsMergeRequestIdCancelMergeWhenBuildSucceeds"></a>
# **postV3ProjectsIdMergeRequestsMergeRequestIdCancelMergeWhenBuildSucceeds**
> MergeRequest postV3ProjectsIdMergeRequestsMergeRequestIdCancelMergeWhenBuildSucceeds(id, mergeRequestId)

Cancel merge if \&quot;Merge When Pipeline Succeeds\&quot; is enabled

Cancel merge if \&quot;Merge When Pipeline Succeeds\&quot; is enabled

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    Integer mergeRequestId = 56; // Integer | 
    try {
      MergeRequest result = apiInstance.postV3ProjectsIdMergeRequestsMergeRequestIdCancelMergeWhenBuildSucceeds(id, mergeRequestId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#postV3ProjectsIdMergeRequestsMergeRequestIdCancelMergeWhenBuildSucceeds");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **mergeRequestId** | **Integer**|  | |

### Return type

[**MergeRequest**](MergeRequest.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Cancel merge if \&quot;Merge When Pipeline Succeeds\&quot; is enabled |  -  |

<a id="postV3ProjectsIdMergeRequestsMergeRequestIdComments"></a>
# **postV3ProjectsIdMergeRequestsMergeRequestIdComments**
> MRNote postV3ProjectsIdMergeRequestsMergeRequestIdComments(id, mergeRequestId, postV3ProjectsIdMergeRequestMergeRequestIdCommentsRequest)

Post a comment to a merge request

Duplicate. DEPRECATED and WILL BE REMOVED in 9.0

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    Integer mergeRequestId = 56; // Integer | 
    PostV3ProjectsIdMergeRequestMergeRequestIdCommentsRequest postV3ProjectsIdMergeRequestMergeRequestIdCommentsRequest = new PostV3ProjectsIdMergeRequestMergeRequestIdCommentsRequest(); // PostV3ProjectsIdMergeRequestMergeRequestIdCommentsRequest | 
    try {
      MRNote result = apiInstance.postV3ProjectsIdMergeRequestsMergeRequestIdComments(id, mergeRequestId, postV3ProjectsIdMergeRequestMergeRequestIdCommentsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#postV3ProjectsIdMergeRequestsMergeRequestIdComments");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **mergeRequestId** | **Integer**|  | |
| **postV3ProjectsIdMergeRequestMergeRequestIdCommentsRequest** | [**PostV3ProjectsIdMergeRequestMergeRequestIdCommentsRequest**](PostV3ProjectsIdMergeRequestMergeRequestIdCommentsRequest.md)|  | |

### Return type

[**MRNote**](MRNote.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Post a comment to a merge request |  -  |

<a id="postV3ProjectsIdMergeRequestsMergeRequestIdNotesNoteIdAwardEmoji"></a>
# **postV3ProjectsIdMergeRequestsMergeRequestIdNotesNoteIdAwardEmoji**
> AwardEmoji postV3ProjectsIdMergeRequestsMergeRequestIdNotesNoteIdAwardEmoji(id, mergeRequestId, noteId, postV3ProjectsIdIssuesIssueIdAwardEmojiRequest)

Award a new Emoji

This feature was introduced in 8.9

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    Integer id = 56; // Integer | 
    Integer mergeRequestId = 56; // Integer | 
    Integer noteId = 56; // Integer | 
    PostV3ProjectsIdIssuesIssueIdAwardEmojiRequest postV3ProjectsIdIssuesIssueIdAwardEmojiRequest = new PostV3ProjectsIdIssuesIssueIdAwardEmojiRequest(); // PostV3ProjectsIdIssuesIssueIdAwardEmojiRequest | 
    try {
      AwardEmoji result = apiInstance.postV3ProjectsIdMergeRequestsMergeRequestIdNotesNoteIdAwardEmoji(id, mergeRequestId, noteId, postV3ProjectsIdIssuesIssueIdAwardEmojiRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#postV3ProjectsIdMergeRequestsMergeRequestIdNotesNoteIdAwardEmoji");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**|  | |
| **mergeRequestId** | **Integer**|  | |
| **noteId** | **Integer**|  | |
| **postV3ProjectsIdIssuesIssueIdAwardEmojiRequest** | [**PostV3ProjectsIdIssuesIssueIdAwardEmojiRequest**](PostV3ProjectsIdIssuesIssueIdAwardEmojiRequest.md)|  | |

### Return type

[**AwardEmoji**](AwardEmoji.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Award a new Emoji |  -  |

<a id="postV3ProjectsIdMergeRequestsMergeRequestIdResetSpentTime"></a>
# **postV3ProjectsIdMergeRequestsMergeRequestIdResetSpentTime**
> postV3ProjectsIdMergeRequestsMergeRequestIdResetSpentTime(id, mergeRequestId)

Reset spent time for a project merge_request

Reset spent time for a project merge_request

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    Integer mergeRequestId = 56; // Integer | The ID of a project merge_request
    try {
      apiInstance.postV3ProjectsIdMergeRequestsMergeRequestIdResetSpentTime(id, mergeRequestId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#postV3ProjectsIdMergeRequestsMergeRequestIdResetSpentTime");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **mergeRequestId** | **Integer**| The ID of a project merge_request | |

### Return type

null (empty response body)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Reset spent time for a project merge_request |  -  |

<a id="postV3ProjectsIdMergeRequestsMergeRequestIdResetTimeEstimate"></a>
# **postV3ProjectsIdMergeRequestsMergeRequestIdResetTimeEstimate**
> postV3ProjectsIdMergeRequestsMergeRequestIdResetTimeEstimate(id, mergeRequestId)

Reset the time estimate for a project merge_request

Reset the time estimate for a project merge_request

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    Integer mergeRequestId = 56; // Integer | The ID of a project merge_request
    try {
      apiInstance.postV3ProjectsIdMergeRequestsMergeRequestIdResetTimeEstimate(id, mergeRequestId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#postV3ProjectsIdMergeRequestsMergeRequestIdResetTimeEstimate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **mergeRequestId** | **Integer**| The ID of a project merge_request | |

### Return type

null (empty response body)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Reset the time estimate for a project merge_request |  -  |

<a id="postV3ProjectsIdMergeRequestsMergeRequestIdTimeEstimate"></a>
# **postV3ProjectsIdMergeRequestsMergeRequestIdTimeEstimate**
> postV3ProjectsIdMergeRequestsMergeRequestIdTimeEstimate(id, mergeRequestId, postV3ProjectsIdIssuesIssueIdAddSpentTimeRequest)

Set a time estimate for a project merge_request

Set a time estimate for a project merge_request

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    Integer mergeRequestId = 56; // Integer | The ID of a project merge_request
    PostV3ProjectsIdIssuesIssueIdAddSpentTimeRequest postV3ProjectsIdIssuesIssueIdAddSpentTimeRequest = new PostV3ProjectsIdIssuesIssueIdAddSpentTimeRequest(); // PostV3ProjectsIdIssuesIssueIdAddSpentTimeRequest | 
    try {
      apiInstance.postV3ProjectsIdMergeRequestsMergeRequestIdTimeEstimate(id, mergeRequestId, postV3ProjectsIdIssuesIssueIdAddSpentTimeRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#postV3ProjectsIdMergeRequestsMergeRequestIdTimeEstimate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **mergeRequestId** | **Integer**| The ID of a project merge_request | |
| **postV3ProjectsIdIssuesIssueIdAddSpentTimeRequest** | [**PostV3ProjectsIdIssuesIssueIdAddSpentTimeRequest**](PostV3ProjectsIdIssuesIssueIdAddSpentTimeRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Set a time estimate for a project merge_request |  -  |

<a id="postV3ProjectsIdMergeRequestsMergeRequestIdTodo"></a>
# **postV3ProjectsIdMergeRequestsMergeRequestIdTodo**
> Todo postV3ProjectsIdMergeRequestsMergeRequestIdTodo(id, mergeRequestId)

Create a todo on an issuable

Create a todo on an issuable

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    Integer mergeRequestId = 56; // Integer | The ID of an issuable
    try {
      Todo result = apiInstance.postV3ProjectsIdMergeRequestsMergeRequestIdTodo(id, mergeRequestId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#postV3ProjectsIdMergeRequestsMergeRequestIdTodo");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **mergeRequestId** | **Integer**| The ID of an issuable | |

### Return type

[**Todo**](Todo.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Create a todo on an issuable |  -  |

<a id="postV3ProjectsIdMergeRequestsNoteableIdNotes"></a>
# **postV3ProjectsIdMergeRequestsNoteableIdNotes**
> Note postV3ProjectsIdMergeRequestsNoteableIdNotes(id, noteableId, postV3ProjectsIdIssuesNoteableIdNotesRequest)

Create a new +noteable+ note

Create a new +noteable+ note

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    Integer noteableId = 56; // Integer | The ID of the noteable
    PostV3ProjectsIdIssuesNoteableIdNotesRequest postV3ProjectsIdIssuesNoteableIdNotesRequest = new PostV3ProjectsIdIssuesNoteableIdNotesRequest(); // PostV3ProjectsIdIssuesNoteableIdNotesRequest | 
    try {
      Note result = apiInstance.postV3ProjectsIdMergeRequestsNoteableIdNotes(id, noteableId, postV3ProjectsIdIssuesNoteableIdNotesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#postV3ProjectsIdMergeRequestsNoteableIdNotes");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **noteableId** | **Integer**| The ID of the noteable | |
| **postV3ProjectsIdIssuesNoteableIdNotesRequest** | [**PostV3ProjectsIdIssuesNoteableIdNotesRequest**](PostV3ProjectsIdIssuesNoteableIdNotesRequest.md)|  | |

### Return type

[**Note**](Note.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Create a new +noteable+ note |  -  |

<a id="postV3ProjectsIdMergeRequestsSubscribableIdSubscription"></a>
# **postV3ProjectsIdMergeRequestsSubscribableIdSubscription**
> MergeRequest postV3ProjectsIdMergeRequestsSubscribableIdSubscription(id, subscribableId)

Subscribe to a resource

Subscribe to a resource

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    String subscribableId = "subscribableId_example"; // String | The ID of a resource
    try {
      MergeRequest result = apiInstance.postV3ProjectsIdMergeRequestsSubscribableIdSubscription(id, subscribableId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#postV3ProjectsIdMergeRequestsSubscribableIdSubscription");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **subscribableId** | **String**| The ID of a resource | |

### Return type

[**MergeRequest**](MergeRequest.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Subscribe to a resource |  -  |

<a id="postV3ProjectsIdMilestones"></a>
# **postV3ProjectsIdMilestones**
> Milestone postV3ProjectsIdMilestones(id, postV3ProjectsIdMilestonesRequest)

Create a new project milestone

Create a new project milestone

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    PostV3ProjectsIdMilestonesRequest postV3ProjectsIdMilestonesRequest = new PostV3ProjectsIdMilestonesRequest(); // PostV3ProjectsIdMilestonesRequest | 
    try {
      Milestone result = apiInstance.postV3ProjectsIdMilestones(id, postV3ProjectsIdMilestonesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#postV3ProjectsIdMilestones");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **postV3ProjectsIdMilestonesRequest** | [**PostV3ProjectsIdMilestonesRequest**](PostV3ProjectsIdMilestonesRequest.md)|  | |

### Return type

[**Milestone**](Milestone.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Create a new project milestone |  -  |

<a id="postV3ProjectsIdPipeline"></a>
# **postV3ProjectsIdPipeline**
> Pipeline postV3ProjectsIdPipeline(id, postV3ProjectsIdPipelineRequest)

Create a new pipeline

This feature was introduced in GitLab 8.14

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The project ID
    PostV3ProjectsIdPipelineRequest postV3ProjectsIdPipelineRequest = new PostV3ProjectsIdPipelineRequest(); // PostV3ProjectsIdPipelineRequest | 
    try {
      Pipeline result = apiInstance.postV3ProjectsIdPipeline(id, postV3ProjectsIdPipelineRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#postV3ProjectsIdPipeline");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The project ID | |
| **postV3ProjectsIdPipelineRequest** | [**PostV3ProjectsIdPipelineRequest**](PostV3ProjectsIdPipelineRequest.md)|  | |

### Return type

[**Pipeline**](Pipeline.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Create a new pipeline |  -  |

<a id="postV3ProjectsIdPipelinesPipelineIdCancel"></a>
# **postV3ProjectsIdPipelinesPipelineIdCancel**
> Pipeline postV3ProjectsIdPipelinesPipelineIdCancel(id, pipelineId)

Cancel all builds in the pipeline

This feature was introduced in GitLab 8.11.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The project ID
    Integer pipelineId = 56; // Integer | The pipeline ID
    try {
      Pipeline result = apiInstance.postV3ProjectsIdPipelinesPipelineIdCancel(id, pipelineId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#postV3ProjectsIdPipelinesPipelineIdCancel");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The project ID | |
| **pipelineId** | **Integer**| The pipeline ID | |

### Return type

[**Pipeline**](Pipeline.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Cancel all builds in the pipeline |  -  |

<a id="postV3ProjectsIdPipelinesPipelineIdRetry"></a>
# **postV3ProjectsIdPipelinesPipelineIdRetry**
> Pipeline postV3ProjectsIdPipelinesPipelineIdRetry(id, pipelineId)

Retry failed builds in the pipeline

This feature was introduced in GitLab 8.11.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The project ID
    Integer pipelineId = 56; // Integer | The pipeline ID
    try {
      Pipeline result = apiInstance.postV3ProjectsIdPipelinesPipelineIdRetry(id, pipelineId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#postV3ProjectsIdPipelinesPipelineIdRetry");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The project ID | |
| **pipelineId** | **Integer**| The pipeline ID | |

### Return type

[**Pipeline**](Pipeline.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Retry failed builds in the pipeline |  -  |

<a id="postV3ProjectsIdRefReftriggerBuilds"></a>
# **postV3ProjectsIdRefReftriggerBuilds**
> TriggerRequest postV3ProjectsIdRefReftriggerBuilds(id, ref, postV3ProjectsIdRefRefTriggerBuildsRequest)

Trigger a GitLab project build

Trigger a GitLab project build

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    String ref = "ref_example"; // String | The commit sha or name of a branch or tag
    PostV3ProjectsIdRefRefTriggerBuildsRequest postV3ProjectsIdRefRefTriggerBuildsRequest = new PostV3ProjectsIdRefRefTriggerBuildsRequest(); // PostV3ProjectsIdRefRefTriggerBuildsRequest | 
    try {
      TriggerRequest result = apiInstance.postV3ProjectsIdRefReftriggerBuilds(id, ref, postV3ProjectsIdRefRefTriggerBuildsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#postV3ProjectsIdRefReftriggerBuilds");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **ref** | **String**| The commit sha or name of a branch or tag | |
| **postV3ProjectsIdRefRefTriggerBuildsRequest** | [**PostV3ProjectsIdRefRefTriggerBuildsRequest**](PostV3ProjectsIdRefRefTriggerBuildsRequest.md)|  | |

### Return type

[**TriggerRequest**](TriggerRequest.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Trigger a GitLab project build |  -  |

<a id="postV3ProjectsIdRepositoryBranches"></a>
# **postV3ProjectsIdRepositoryBranches**
> RepoBranch postV3ProjectsIdRepositoryBranches(id, postV3ProjectsIdRepositoryBranchesRequest)

Create branch

Create branch

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    PostV3ProjectsIdRepositoryBranchesRequest postV3ProjectsIdRepositoryBranchesRequest = new PostV3ProjectsIdRepositoryBranchesRequest(); // PostV3ProjectsIdRepositoryBranchesRequest | 
    try {
      RepoBranch result = apiInstance.postV3ProjectsIdRepositoryBranches(id, postV3ProjectsIdRepositoryBranchesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#postV3ProjectsIdRepositoryBranches");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **postV3ProjectsIdRepositoryBranchesRequest** | [**PostV3ProjectsIdRepositoryBranchesRequest**](PostV3ProjectsIdRepositoryBranchesRequest.md)|  | |

### Return type

[**RepoBranch**](RepoBranch.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Create branch |  -  |

<a id="postV3ProjectsIdRepositoryCommits"></a>
# **postV3ProjectsIdRepositoryCommits**
> RepoCommitDetail postV3ProjectsIdRepositoryCommits(id, postV3ProjectsIdRepositoryCommitsRequest)

Commit multiple file changes as one commit

This feature was introduced in GitLab 8.13

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    PostV3ProjectsIdRepositoryCommitsRequest postV3ProjectsIdRepositoryCommitsRequest = new PostV3ProjectsIdRepositoryCommitsRequest(); // PostV3ProjectsIdRepositoryCommitsRequest | 
    try {
      RepoCommitDetail result = apiInstance.postV3ProjectsIdRepositoryCommits(id, postV3ProjectsIdRepositoryCommitsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#postV3ProjectsIdRepositoryCommits");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **postV3ProjectsIdRepositoryCommitsRequest** | [**PostV3ProjectsIdRepositoryCommitsRequest**](PostV3ProjectsIdRepositoryCommitsRequest.md)|  | |

### Return type

[**RepoCommitDetail**](RepoCommitDetail.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Commit multiple file changes as one commit |  -  |

<a id="postV3ProjectsIdRepositoryCommitsShaCherryPick"></a>
# **postV3ProjectsIdRepositoryCommitsShaCherryPick**
> RepoCommit postV3ProjectsIdRepositoryCommitsShaCherryPick(id, sha, postV3ProjectsIdRepositoryCommitsShaCherryPickRequest)

Cherry pick commit into a branch

This feature was introduced in GitLab 8.15

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    String sha = "sha_example"; // String | A commit sha to be cherry picked
    PostV3ProjectsIdRepositoryCommitsShaCherryPickRequest postV3ProjectsIdRepositoryCommitsShaCherryPickRequest = new PostV3ProjectsIdRepositoryCommitsShaCherryPickRequest(); // PostV3ProjectsIdRepositoryCommitsShaCherryPickRequest | 
    try {
      RepoCommit result = apiInstance.postV3ProjectsIdRepositoryCommitsShaCherryPick(id, sha, postV3ProjectsIdRepositoryCommitsShaCherryPickRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#postV3ProjectsIdRepositoryCommitsShaCherryPick");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **sha** | **String**| A commit sha to be cherry picked | |
| **postV3ProjectsIdRepositoryCommitsShaCherryPickRequest** | [**PostV3ProjectsIdRepositoryCommitsShaCherryPickRequest**](PostV3ProjectsIdRepositoryCommitsShaCherryPickRequest.md)|  | |

### Return type

[**RepoCommit**](RepoCommit.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Cherry pick commit into a branch |  -  |

<a id="postV3ProjectsIdRepositoryCommitsShaComments"></a>
# **postV3ProjectsIdRepositoryCommitsShaComments**
> CommitNote postV3ProjectsIdRepositoryCommitsShaComments(id, sha, postV3ProjectsIdRepositoryCommitsShaCommentsRequest)

Post comment to commit

Post comment to commit

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    String sha = "sha_example"; // String | The commit's SHA
    PostV3ProjectsIdRepositoryCommitsShaCommentsRequest postV3ProjectsIdRepositoryCommitsShaCommentsRequest = new PostV3ProjectsIdRepositoryCommitsShaCommentsRequest(); // PostV3ProjectsIdRepositoryCommitsShaCommentsRequest | 
    try {
      CommitNote result = apiInstance.postV3ProjectsIdRepositoryCommitsShaComments(id, sha, postV3ProjectsIdRepositoryCommitsShaCommentsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#postV3ProjectsIdRepositoryCommitsShaComments");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **sha** | **String**| The commit&#39;s SHA | |
| **postV3ProjectsIdRepositoryCommitsShaCommentsRequest** | [**PostV3ProjectsIdRepositoryCommitsShaCommentsRequest**](PostV3ProjectsIdRepositoryCommitsShaCommentsRequest.md)|  | |

### Return type

[**CommitNote**](CommitNote.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Post comment to commit |  -  |

<a id="postV3ProjectsIdRepositoryFiles"></a>
# **postV3ProjectsIdRepositoryFiles**
> postV3ProjectsIdRepositoryFiles(id, putV3ProjectsIdRepositoryFilesRequest)

Create new file in repository

Create new file in repository

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The project ID
    PutV3ProjectsIdRepositoryFilesRequest putV3ProjectsIdRepositoryFilesRequest = new PutV3ProjectsIdRepositoryFilesRequest(); // PutV3ProjectsIdRepositoryFilesRequest | 
    try {
      apiInstance.postV3ProjectsIdRepositoryFiles(id, putV3ProjectsIdRepositoryFilesRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#postV3ProjectsIdRepositoryFiles");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The project ID | |
| **putV3ProjectsIdRepositoryFilesRequest** | [**PutV3ProjectsIdRepositoryFilesRequest**](PutV3ProjectsIdRepositoryFilesRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Create new file in repository |  -  |

<a id="postV3ProjectsIdRepositoryTags"></a>
# **postV3ProjectsIdRepositoryTags**
> RepoTag postV3ProjectsIdRepositoryTags(id, postV3ProjectsIdRepositoryTagsRequest)

Create a new repository tag

Create a new repository tag

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    PostV3ProjectsIdRepositoryTagsRequest postV3ProjectsIdRepositoryTagsRequest = new PostV3ProjectsIdRepositoryTagsRequest(); // PostV3ProjectsIdRepositoryTagsRequest | 
    try {
      RepoTag result = apiInstance.postV3ProjectsIdRepositoryTags(id, postV3ProjectsIdRepositoryTagsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#postV3ProjectsIdRepositoryTags");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **postV3ProjectsIdRepositoryTagsRequest** | [**PostV3ProjectsIdRepositoryTagsRequest**](PostV3ProjectsIdRepositoryTagsRequest.md)|  | |

### Return type

[**RepoTag**](RepoTag.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Create a new repository tag |  -  |

<a id="postV3ProjectsIdRepositoryTagsTagNameRelease"></a>
# **postV3ProjectsIdRepositoryTagsTagNameRelease**
> Release postV3ProjectsIdRepositoryTagsTagNameRelease(id, tagName, putV3ProjectsIdRepositoryTagsTagNameReleaseRequest)

Add a release note to a tag

Add a release note to a tag

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    String tagName = "tagName_example"; // String | The name of the tag
    PutV3ProjectsIdRepositoryTagsTagNameReleaseRequest putV3ProjectsIdRepositoryTagsTagNameReleaseRequest = new PutV3ProjectsIdRepositoryTagsTagNameReleaseRequest(); // PutV3ProjectsIdRepositoryTagsTagNameReleaseRequest | 
    try {
      Release result = apiInstance.postV3ProjectsIdRepositoryTagsTagNameRelease(id, tagName, putV3ProjectsIdRepositoryTagsTagNameReleaseRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#postV3ProjectsIdRepositoryTagsTagNameRelease");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **tagName** | **String**| The name of the tag | |
| **putV3ProjectsIdRepositoryTagsTagNameReleaseRequest** | [**PutV3ProjectsIdRepositoryTagsTagNameReleaseRequest**](PutV3ProjectsIdRepositoryTagsTagNameReleaseRequest.md)|  | |

### Return type

[**Release**](Release.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Add a release note to a tag |  -  |

<a id="postV3ProjectsIdRunners"></a>
# **postV3ProjectsIdRunners**
> Runner postV3ProjectsIdRunners(id, postV3ProjectsIdRunnersRequest)

Enable a runner for a project

Enable a runner for a project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    PostV3ProjectsIdRunnersRequest postV3ProjectsIdRunnersRequest = new PostV3ProjectsIdRunnersRequest(); // PostV3ProjectsIdRunnersRequest | 
    try {
      Runner result = apiInstance.postV3ProjectsIdRunners(id, postV3ProjectsIdRunnersRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#postV3ProjectsIdRunners");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **postV3ProjectsIdRunnersRequest** | [**PostV3ProjectsIdRunnersRequest**](PostV3ProjectsIdRunnersRequest.md)|  | |

### Return type

[**Runner**](Runner.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Enable a runner for a project |  -  |

<a id="postV3ProjectsIdServicesMattermostSlashCommandsTrigger"></a>
# **postV3ProjectsIdServicesMattermostSlashCommandsTrigger**
> postV3ProjectsIdServicesMattermostSlashCommandsTrigger(id, putV3ProjectsIdServicesMattermostSlashCommandsRequest)

Trigger a slash command for mattermost-slash-commands

Added in GitLab 8.13

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    PutV3ProjectsIdServicesMattermostSlashCommandsRequest putV3ProjectsIdServicesMattermostSlashCommandsRequest = new PutV3ProjectsIdServicesMattermostSlashCommandsRequest(); // PutV3ProjectsIdServicesMattermostSlashCommandsRequest | 
    try {
      apiInstance.postV3ProjectsIdServicesMattermostSlashCommandsTrigger(id, putV3ProjectsIdServicesMattermostSlashCommandsRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#postV3ProjectsIdServicesMattermostSlashCommandsTrigger");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **putV3ProjectsIdServicesMattermostSlashCommandsRequest** | [**PutV3ProjectsIdServicesMattermostSlashCommandsRequest**](PutV3ProjectsIdServicesMattermostSlashCommandsRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Trigger a slash command for mattermost-slash-commands |  -  |

<a id="postV3ProjectsIdServicesSlackSlashCommandsTrigger"></a>
# **postV3ProjectsIdServicesSlackSlashCommandsTrigger**
> postV3ProjectsIdServicesSlackSlashCommandsTrigger(id, putV3ProjectsIdServicesSlackSlashCommandsRequest)

Trigger a slash command for slack-slash-commands

Added in GitLab 8.13

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    PutV3ProjectsIdServicesSlackSlashCommandsRequest putV3ProjectsIdServicesSlackSlashCommandsRequest = new PutV3ProjectsIdServicesSlackSlashCommandsRequest(); // PutV3ProjectsIdServicesSlackSlashCommandsRequest | 
    try {
      apiInstance.postV3ProjectsIdServicesSlackSlashCommandsTrigger(id, putV3ProjectsIdServicesSlackSlashCommandsRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#postV3ProjectsIdServicesSlackSlashCommandsTrigger");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **putV3ProjectsIdServicesSlackSlashCommandsRequest** | [**PutV3ProjectsIdServicesSlackSlashCommandsRequest**](PutV3ProjectsIdServicesSlackSlashCommandsRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Trigger a slash command for slack-slash-commands |  -  |

<a id="postV3ProjectsIdShare"></a>
# **postV3ProjectsIdShare**
> ProjectGroupLink postV3ProjectsIdShare(id, postV3ProjectsIdShareRequest)

Share the project with a group

Share the project with a group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    PostV3ProjectsIdShareRequest postV3ProjectsIdShareRequest = new PostV3ProjectsIdShareRequest(); // PostV3ProjectsIdShareRequest | 
    try {
      ProjectGroupLink result = apiInstance.postV3ProjectsIdShare(id, postV3ProjectsIdShareRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#postV3ProjectsIdShare");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **postV3ProjectsIdShareRequest** | [**PostV3ProjectsIdShareRequest**](PostV3ProjectsIdShareRequest.md)|  | |

### Return type

[**ProjectGroupLink**](ProjectGroupLink.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Share the project with a group |  -  |

<a id="postV3ProjectsIdSnippets"></a>
# **postV3ProjectsIdSnippets**
> ProjectSnippet postV3ProjectsIdSnippets(id, postV3ProjectsIdSnippetsRequest)

Create a new project snippet

Create a new project snippet

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    PostV3ProjectsIdSnippetsRequest postV3ProjectsIdSnippetsRequest = new PostV3ProjectsIdSnippetsRequest(); // PostV3ProjectsIdSnippetsRequest | 
    try {
      ProjectSnippet result = apiInstance.postV3ProjectsIdSnippets(id, postV3ProjectsIdSnippetsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#postV3ProjectsIdSnippets");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **postV3ProjectsIdSnippetsRequest** | [**PostV3ProjectsIdSnippetsRequest**](PostV3ProjectsIdSnippetsRequest.md)|  | |

### Return type

[**ProjectSnippet**](ProjectSnippet.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Create a new project snippet |  -  |

<a id="postV3ProjectsIdSnippetsNoteableIdNotes"></a>
# **postV3ProjectsIdSnippetsNoteableIdNotes**
> Note postV3ProjectsIdSnippetsNoteableIdNotes(id, noteableId, postV3ProjectsIdIssuesNoteableIdNotesRequest)

Create a new +noteable+ note

Create a new +noteable+ note

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    Integer noteableId = 56; // Integer | The ID of the noteable
    PostV3ProjectsIdIssuesNoteableIdNotesRequest postV3ProjectsIdIssuesNoteableIdNotesRequest = new PostV3ProjectsIdIssuesNoteableIdNotesRequest(); // PostV3ProjectsIdIssuesNoteableIdNotesRequest | 
    try {
      Note result = apiInstance.postV3ProjectsIdSnippetsNoteableIdNotes(id, noteableId, postV3ProjectsIdIssuesNoteableIdNotesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#postV3ProjectsIdSnippetsNoteableIdNotes");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **noteableId** | **Integer**| The ID of the noteable | |
| **postV3ProjectsIdIssuesNoteableIdNotesRequest** | [**PostV3ProjectsIdIssuesNoteableIdNotesRequest**](PostV3ProjectsIdIssuesNoteableIdNotesRequest.md)|  | |

### Return type

[**Note**](Note.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Create a new +noteable+ note |  -  |

<a id="postV3ProjectsIdSnippetsSnippetIdAwardEmoji"></a>
# **postV3ProjectsIdSnippetsSnippetIdAwardEmoji**
> AwardEmoji postV3ProjectsIdSnippetsSnippetIdAwardEmoji(id, snippetId, postV3ProjectsIdIssuesIssueIdAwardEmojiRequest)

Award a new Emoji

This feature was introduced in 8.9

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    Integer id = 56; // Integer | 
    Integer snippetId = 56; // Integer | 
    PostV3ProjectsIdIssuesIssueIdAwardEmojiRequest postV3ProjectsIdIssuesIssueIdAwardEmojiRequest = new PostV3ProjectsIdIssuesIssueIdAwardEmojiRequest(); // PostV3ProjectsIdIssuesIssueIdAwardEmojiRequest | 
    try {
      AwardEmoji result = apiInstance.postV3ProjectsIdSnippetsSnippetIdAwardEmoji(id, snippetId, postV3ProjectsIdIssuesIssueIdAwardEmojiRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#postV3ProjectsIdSnippetsSnippetIdAwardEmoji");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**|  | |
| **snippetId** | **Integer**|  | |
| **postV3ProjectsIdIssuesIssueIdAwardEmojiRequest** | [**PostV3ProjectsIdIssuesIssueIdAwardEmojiRequest**](PostV3ProjectsIdIssuesIssueIdAwardEmojiRequest.md)|  | |

### Return type

[**AwardEmoji**](AwardEmoji.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Award a new Emoji |  -  |

<a id="postV3ProjectsIdSnippetsSnippetIdNotesNoteIdAwardEmoji"></a>
# **postV3ProjectsIdSnippetsSnippetIdNotesNoteIdAwardEmoji**
> AwardEmoji postV3ProjectsIdSnippetsSnippetIdNotesNoteIdAwardEmoji(id, snippetId, noteId, postV3ProjectsIdIssuesIssueIdAwardEmojiRequest)

Award a new Emoji

This feature was introduced in 8.9

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    Integer id = 56; // Integer | 
    Integer snippetId = 56; // Integer | 
    Integer noteId = 56; // Integer | 
    PostV3ProjectsIdIssuesIssueIdAwardEmojiRequest postV3ProjectsIdIssuesIssueIdAwardEmojiRequest = new PostV3ProjectsIdIssuesIssueIdAwardEmojiRequest(); // PostV3ProjectsIdIssuesIssueIdAwardEmojiRequest | 
    try {
      AwardEmoji result = apiInstance.postV3ProjectsIdSnippetsSnippetIdNotesNoteIdAwardEmoji(id, snippetId, noteId, postV3ProjectsIdIssuesIssueIdAwardEmojiRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#postV3ProjectsIdSnippetsSnippetIdNotesNoteIdAwardEmoji");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**|  | |
| **snippetId** | **Integer**|  | |
| **noteId** | **Integer**|  | |
| **postV3ProjectsIdIssuesIssueIdAwardEmojiRequest** | [**PostV3ProjectsIdIssuesIssueIdAwardEmojiRequest**](PostV3ProjectsIdIssuesIssueIdAwardEmojiRequest.md)|  | |

### Return type

[**AwardEmoji**](AwardEmoji.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Award a new Emoji |  -  |

<a id="postV3ProjectsIdStar"></a>
# **postV3ProjectsIdStar**
> Project postV3ProjectsIdStar(id)

Star a project

Star a project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    try {
      Project result = apiInstance.postV3ProjectsIdStar(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#postV3ProjectsIdStar");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |

### Return type

[**Project**](Project.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Star a project |  -  |

<a id="postV3ProjectsIdStatusesSha"></a>
# **postV3ProjectsIdStatusesSha**
> CommitStatus postV3ProjectsIdStatusesSha(id, sha, postV3ProjectsIdStatusesShaRequest)

Post status to a commit

Post status to a commit

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    String sha = "sha_example"; // String | The commit hash
    PostV3ProjectsIdStatusesShaRequest postV3ProjectsIdStatusesShaRequest = new PostV3ProjectsIdStatusesShaRequest(); // PostV3ProjectsIdStatusesShaRequest | 
    try {
      CommitStatus result = apiInstance.postV3ProjectsIdStatusesSha(id, sha, postV3ProjectsIdStatusesShaRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#postV3ProjectsIdStatusesSha");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **sha** | **String**| The commit hash | |
| **postV3ProjectsIdStatusesShaRequest** | [**PostV3ProjectsIdStatusesShaRequest**](PostV3ProjectsIdStatusesShaRequest.md)|  | |

### Return type

[**CommitStatus**](CommitStatus.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Post status to a commit |  -  |

<a id="postV3ProjectsIdTriggers"></a>
# **postV3ProjectsIdTriggers**
> Trigger postV3ProjectsIdTriggers(id)

Create a trigger

Create a trigger

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    try {
      Trigger result = apiInstance.postV3ProjectsIdTriggers(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#postV3ProjectsIdTriggers");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |

### Return type

[**Trigger**](Trigger.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Create a trigger |  -  |

<a id="postV3ProjectsIdUnarchive"></a>
# **postV3ProjectsIdUnarchive**
> Project postV3ProjectsIdUnarchive(id)

Unarchive a project

Unarchive a project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    try {
      Project result = apiInstance.postV3ProjectsIdUnarchive(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#postV3ProjectsIdUnarchive");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |

### Return type

[**Project**](Project.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Unarchive a project |  -  |

<a id="postV3ProjectsIdUploads"></a>
# **postV3ProjectsIdUploads**
> postV3ProjectsIdUploads(id, postV3ProjectsIdUploadsRequest)

Upload a file

Upload a file

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    PostV3ProjectsIdUploadsRequest postV3ProjectsIdUploadsRequest = new PostV3ProjectsIdUploadsRequest(); // PostV3ProjectsIdUploadsRequest | 
    try {
      apiInstance.postV3ProjectsIdUploads(id, postV3ProjectsIdUploadsRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#postV3ProjectsIdUploads");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **postV3ProjectsIdUploadsRequest** | [**PostV3ProjectsIdUploadsRequest**](PostV3ProjectsIdUploadsRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Upload a file |  -  |

<a id="postV3ProjectsIdVariables"></a>
# **postV3ProjectsIdVariables**
> Variable postV3ProjectsIdVariables(id, postV3ProjectsIdVariablesRequest)

Create a new variable in a project

Create a new variable in a project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    PostV3ProjectsIdVariablesRequest postV3ProjectsIdVariablesRequest = new PostV3ProjectsIdVariablesRequest(); // PostV3ProjectsIdVariablesRequest | 
    try {
      Variable result = apiInstance.postV3ProjectsIdVariables(id, postV3ProjectsIdVariablesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#postV3ProjectsIdVariables");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **postV3ProjectsIdVariablesRequest** | [**PostV3ProjectsIdVariablesRequest**](PostV3ProjectsIdVariablesRequest.md)|  | |

### Return type

[**Variable**](Variable.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Create a new variable in a project |  -  |

<a id="postV3ProjectsUserUserId"></a>
# **postV3ProjectsUserUserId**
> Project postV3ProjectsUserUserId(userId, postV3ProjectsUserUserIdRequest)

Create new project for a specified user. Only available to admin users.

Create new project for a specified user. Only available to admin users.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    Integer userId = 56; // Integer | The ID of a user
    PostV3ProjectsUserUserIdRequest postV3ProjectsUserUserIdRequest = new PostV3ProjectsUserUserIdRequest(); // PostV3ProjectsUserUserIdRequest | 
    try {
      Project result = apiInstance.postV3ProjectsUserUserId(userId, postV3ProjectsUserUserIdRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#postV3ProjectsUserUserId");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **userId** | **Integer**| The ID of a user | |
| **postV3ProjectsUserUserIdRequest** | [**PostV3ProjectsUserUserIdRequest**](PostV3ProjectsUserUserIdRequest.md)|  | |

### Return type

[**Project**](Project.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Create new project for a specified user. Only available to admin users. |  -  |

<a id="putV3ProjectsId"></a>
# **putV3ProjectsId**
> Project putV3ProjectsId(id, putV3ProjectsIdRequest)

Update an existing project

Update an existing project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    PutV3ProjectsIdRequest putV3ProjectsIdRequest = new PutV3ProjectsIdRequest(); // PutV3ProjectsIdRequest | 
    try {
      Project result = apiInstance.putV3ProjectsId(id, putV3ProjectsIdRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#putV3ProjectsId");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **putV3ProjectsIdRequest** | [**PutV3ProjectsIdRequest**](PutV3ProjectsIdRequest.md)|  | [optional] |

### Return type

[**Project**](Project.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Update an existing project |  -  |

<a id="putV3ProjectsIdAccessRequestsUserIdApprove"></a>
# **putV3ProjectsIdAccessRequestsUserIdApprove**
> Member putV3ProjectsIdAccessRequestsUserIdApprove(id, userId, putV3GroupsIdAccessRequestsUserIdApproveRequest)

Approves an access request for the given user.

This feature was introduced in GitLab 8.11.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The project ID
    Integer userId = 56; // Integer | The user ID of the access requester
    PutV3GroupsIdAccessRequestsUserIdApproveRequest putV3GroupsIdAccessRequestsUserIdApproveRequest = new PutV3GroupsIdAccessRequestsUserIdApproveRequest(); // PutV3GroupsIdAccessRequestsUserIdApproveRequest | 
    try {
      Member result = apiInstance.putV3ProjectsIdAccessRequestsUserIdApprove(id, userId, putV3GroupsIdAccessRequestsUserIdApproveRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#putV3ProjectsIdAccessRequestsUserIdApprove");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The project ID | |
| **userId** | **Integer**| The user ID of the access requester | |
| **putV3GroupsIdAccessRequestsUserIdApproveRequest** | [**PutV3GroupsIdAccessRequestsUserIdApproveRequest**](PutV3GroupsIdAccessRequestsUserIdApproveRequest.md)|  | [optional] |

### Return type

[**Member**](Member.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Approves an access request for the given user. |  -  |

<a id="putV3ProjectsIdBoardsBoardIdListsListId"></a>
# **putV3ProjectsIdBoardsBoardIdListsListId**
> ModelList putV3ProjectsIdBoardsBoardIdListsListId(id, boardId, listId, putV3ProjectsIdBoardsBoardIdListsListIdRequest)

Moves a board list to a new position

This feature was introduced in 8.13

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    Integer boardId = 56; // Integer | The ID of a board
    Integer listId = 56; // Integer | The ID of a list
    PutV3ProjectsIdBoardsBoardIdListsListIdRequest putV3ProjectsIdBoardsBoardIdListsListIdRequest = new PutV3ProjectsIdBoardsBoardIdListsListIdRequest(); // PutV3ProjectsIdBoardsBoardIdListsListIdRequest | 
    try {
      ModelList result = apiInstance.putV3ProjectsIdBoardsBoardIdListsListId(id, boardId, listId, putV3ProjectsIdBoardsBoardIdListsListIdRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#putV3ProjectsIdBoardsBoardIdListsListId");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **boardId** | **Integer**| The ID of a board | |
| **listId** | **Integer**| The ID of a list | |
| **putV3ProjectsIdBoardsBoardIdListsListIdRequest** | [**PutV3ProjectsIdBoardsBoardIdListsListIdRequest**](PutV3ProjectsIdBoardsBoardIdListsListIdRequest.md)|  | |

### Return type

[**ModelList**](ModelList.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Moves a board list to a new position |  -  |

<a id="putV3ProjectsIdEnvironmentsEnvironmentId"></a>
# **putV3ProjectsIdEnvironmentsEnvironmentId**
> Environment putV3ProjectsIdEnvironmentsEnvironmentId(id, environmentId, putV3ProjectsIdEnvironmentsEnvironmentIdRequest)

Updates an existing environment

This feature was introduced in GitLab 8.11.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The project ID
    Integer environmentId = 56; // Integer | The environment ID
    PutV3ProjectsIdEnvironmentsEnvironmentIdRequest putV3ProjectsIdEnvironmentsEnvironmentIdRequest = new PutV3ProjectsIdEnvironmentsEnvironmentIdRequest(); // PutV3ProjectsIdEnvironmentsEnvironmentIdRequest | 
    try {
      Environment result = apiInstance.putV3ProjectsIdEnvironmentsEnvironmentId(id, environmentId, putV3ProjectsIdEnvironmentsEnvironmentIdRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#putV3ProjectsIdEnvironmentsEnvironmentId");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The project ID | |
| **environmentId** | **Integer**| The environment ID | |
| **putV3ProjectsIdEnvironmentsEnvironmentIdRequest** | [**PutV3ProjectsIdEnvironmentsEnvironmentIdRequest**](PutV3ProjectsIdEnvironmentsEnvironmentIdRequest.md)|  | [optional] |

### Return type

[**Environment**](Environment.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Updates an existing environment |  -  |

<a id="putV3ProjectsIdHooksHookId"></a>
# **putV3ProjectsIdHooksHookId**
> ProjectHook putV3ProjectsIdHooksHookId(id, hookId, postV3ProjectsIdHooksRequest)

Update an existing project hook

Update an existing project hook

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    Integer hookId = 56; // Integer | The ID of the hook to update
    PostV3ProjectsIdHooksRequest postV3ProjectsIdHooksRequest = new PostV3ProjectsIdHooksRequest(); // PostV3ProjectsIdHooksRequest | 
    try {
      ProjectHook result = apiInstance.putV3ProjectsIdHooksHookId(id, hookId, postV3ProjectsIdHooksRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#putV3ProjectsIdHooksHookId");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **hookId** | **Integer**| The ID of the hook to update | |
| **postV3ProjectsIdHooksRequest** | [**PostV3ProjectsIdHooksRequest**](PostV3ProjectsIdHooksRequest.md)|  | |

### Return type

[**ProjectHook**](ProjectHook.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Update an existing project hook |  -  |

<a id="putV3ProjectsIdIssuesIssueId"></a>
# **putV3ProjectsIdIssuesIssueId**
> Issue putV3ProjectsIdIssuesIssueId(id, issueId, putV3ProjectsIdIssuesIssueIdRequest)

Update an existing issue

Update an existing issue

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    Integer issueId = 56; // Integer | The ID of a project issue
    PutV3ProjectsIdIssuesIssueIdRequest putV3ProjectsIdIssuesIssueIdRequest = new PutV3ProjectsIdIssuesIssueIdRequest(); // PutV3ProjectsIdIssuesIssueIdRequest | 
    try {
      Issue result = apiInstance.putV3ProjectsIdIssuesIssueId(id, issueId, putV3ProjectsIdIssuesIssueIdRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#putV3ProjectsIdIssuesIssueId");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **issueId** | **Integer**| The ID of a project issue | |
| **putV3ProjectsIdIssuesIssueIdRequest** | [**PutV3ProjectsIdIssuesIssueIdRequest**](PutV3ProjectsIdIssuesIssueIdRequest.md)|  | [optional] |

### Return type

[**Issue**](Issue.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Update an existing issue |  -  |

<a id="putV3ProjectsIdIssuesNoteableIdNotesNoteId"></a>
# **putV3ProjectsIdIssuesNoteableIdNotesNoteId**
> Note putV3ProjectsIdIssuesNoteableIdNotesNoteId(id, noteableId, noteId, putV3ProjectsIdIssuesNoteableIdNotesNoteIdRequest)

Update an existing +noteable+ note

Update an existing +noteable+ note

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    Integer noteableId = 56; // Integer | The ID of the noteable
    Integer noteId = 56; // Integer | The ID of a note
    PutV3ProjectsIdIssuesNoteableIdNotesNoteIdRequest putV3ProjectsIdIssuesNoteableIdNotesNoteIdRequest = new PutV3ProjectsIdIssuesNoteableIdNotesNoteIdRequest(); // PutV3ProjectsIdIssuesNoteableIdNotesNoteIdRequest | 
    try {
      Note result = apiInstance.putV3ProjectsIdIssuesNoteableIdNotesNoteId(id, noteableId, noteId, putV3ProjectsIdIssuesNoteableIdNotesNoteIdRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#putV3ProjectsIdIssuesNoteableIdNotesNoteId");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **noteableId** | **Integer**| The ID of the noteable | |
| **noteId** | **Integer**| The ID of a note | |
| **putV3ProjectsIdIssuesNoteableIdNotesNoteIdRequest** | [**PutV3ProjectsIdIssuesNoteableIdNotesNoteIdRequest**](PutV3ProjectsIdIssuesNoteableIdNotesNoteIdRequest.md)|  | |

### Return type

[**Note**](Note.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Update an existing +noteable+ note |  -  |

<a id="putV3ProjectsIdLabels"></a>
# **putV3ProjectsIdLabels**
> Label putV3ProjectsIdLabels(id, putV3ProjectsIdLabelsRequest)

Update an existing label. At least one optional parameter is required.

Update an existing label. At least one optional parameter is required.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    PutV3ProjectsIdLabelsRequest putV3ProjectsIdLabelsRequest = new PutV3ProjectsIdLabelsRequest(); // PutV3ProjectsIdLabelsRequest | 
    try {
      Label result = apiInstance.putV3ProjectsIdLabels(id, putV3ProjectsIdLabelsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#putV3ProjectsIdLabels");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **putV3ProjectsIdLabelsRequest** | [**PutV3ProjectsIdLabelsRequest**](PutV3ProjectsIdLabelsRequest.md)|  | |

### Return type

[**Label**](Label.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Update an existing label. At least one optional parameter is required. |  -  |

<a id="putV3ProjectsIdMembersUserId"></a>
# **putV3ProjectsIdMembersUserId**
> Member putV3ProjectsIdMembersUserId(id, userId, putV3GroupsIdMembersUserIdRequest)

Updates a member of a group or project.

Updates a member of a group or project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The project ID
    Integer userId = 56; // Integer | The user ID of the new member
    PutV3GroupsIdMembersUserIdRequest putV3GroupsIdMembersUserIdRequest = new PutV3GroupsIdMembersUserIdRequest(); // PutV3GroupsIdMembersUserIdRequest | 
    try {
      Member result = apiInstance.putV3ProjectsIdMembersUserId(id, userId, putV3GroupsIdMembersUserIdRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#putV3ProjectsIdMembersUserId");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The project ID | |
| **userId** | **Integer**| The user ID of the new member | |
| **putV3GroupsIdMembersUserIdRequest** | [**PutV3GroupsIdMembersUserIdRequest**](PutV3GroupsIdMembersUserIdRequest.md)|  | |

### Return type

[**Member**](Member.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Updates a member of a group or project. |  -  |

<a id="putV3ProjectsIdMergeRequestMergeRequestId"></a>
# **putV3ProjectsIdMergeRequestMergeRequestId**
> MergeRequest putV3ProjectsIdMergeRequestMergeRequestId(id, mergeRequestId, putV3ProjectsIdMergeRequestMergeRequestIdRequest)

Update a merge request

Update a merge request

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    Integer mergeRequestId = 56; // Integer | 
    PutV3ProjectsIdMergeRequestMergeRequestIdRequest putV3ProjectsIdMergeRequestMergeRequestIdRequest = new PutV3ProjectsIdMergeRequestMergeRequestIdRequest(); // PutV3ProjectsIdMergeRequestMergeRequestIdRequest | 
    try {
      MergeRequest result = apiInstance.putV3ProjectsIdMergeRequestMergeRequestId(id, mergeRequestId, putV3ProjectsIdMergeRequestMergeRequestIdRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#putV3ProjectsIdMergeRequestMergeRequestId");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **mergeRequestId** | **Integer**|  | |
| **putV3ProjectsIdMergeRequestMergeRequestIdRequest** | [**PutV3ProjectsIdMergeRequestMergeRequestIdRequest**](PutV3ProjectsIdMergeRequestMergeRequestIdRequest.md)|  | [optional] |

### Return type

[**MergeRequest**](MergeRequest.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Update a merge request |  -  |

<a id="putV3ProjectsIdMergeRequestMergeRequestIdMerge"></a>
# **putV3ProjectsIdMergeRequestMergeRequestIdMerge**
> MergeRequest putV3ProjectsIdMergeRequestMergeRequestIdMerge(id, mergeRequestId, putV3ProjectsIdMergeRequestMergeRequestIdMergeRequest)

Merge a merge request

Merge a merge request

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    Integer mergeRequestId = 56; // Integer | 
    PutV3ProjectsIdMergeRequestMergeRequestIdMergeRequest putV3ProjectsIdMergeRequestMergeRequestIdMergeRequest = new PutV3ProjectsIdMergeRequestMergeRequestIdMergeRequest(); // PutV3ProjectsIdMergeRequestMergeRequestIdMergeRequest | 
    try {
      MergeRequest result = apiInstance.putV3ProjectsIdMergeRequestMergeRequestIdMerge(id, mergeRequestId, putV3ProjectsIdMergeRequestMergeRequestIdMergeRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#putV3ProjectsIdMergeRequestMergeRequestIdMerge");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **mergeRequestId** | **Integer**|  | |
| **putV3ProjectsIdMergeRequestMergeRequestIdMergeRequest** | [**PutV3ProjectsIdMergeRequestMergeRequestIdMergeRequest**](PutV3ProjectsIdMergeRequestMergeRequestIdMergeRequest.md)|  | [optional] |

### Return type

[**MergeRequest**](MergeRequest.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Merge a merge request |  -  |

<a id="putV3ProjectsIdMergeRequestsMergeRequestId"></a>
# **putV3ProjectsIdMergeRequestsMergeRequestId**
> MergeRequest putV3ProjectsIdMergeRequestsMergeRequestId(id, mergeRequestId, putV3ProjectsIdMergeRequestMergeRequestIdRequest)

Update a merge request

Update a merge request

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    Integer mergeRequestId = 56; // Integer | 
    PutV3ProjectsIdMergeRequestMergeRequestIdRequest putV3ProjectsIdMergeRequestMergeRequestIdRequest = new PutV3ProjectsIdMergeRequestMergeRequestIdRequest(); // PutV3ProjectsIdMergeRequestMergeRequestIdRequest | 
    try {
      MergeRequest result = apiInstance.putV3ProjectsIdMergeRequestsMergeRequestId(id, mergeRequestId, putV3ProjectsIdMergeRequestMergeRequestIdRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#putV3ProjectsIdMergeRequestsMergeRequestId");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **mergeRequestId** | **Integer**|  | |
| **putV3ProjectsIdMergeRequestMergeRequestIdRequest** | [**PutV3ProjectsIdMergeRequestMergeRequestIdRequest**](PutV3ProjectsIdMergeRequestMergeRequestIdRequest.md)|  | [optional] |

### Return type

[**MergeRequest**](MergeRequest.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Update a merge request |  -  |

<a id="putV3ProjectsIdMergeRequestsMergeRequestIdMerge"></a>
# **putV3ProjectsIdMergeRequestsMergeRequestIdMerge**
> MergeRequest putV3ProjectsIdMergeRequestsMergeRequestIdMerge(id, mergeRequestId, putV3ProjectsIdMergeRequestMergeRequestIdMergeRequest)

Merge a merge request

Merge a merge request

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    Integer mergeRequestId = 56; // Integer | 
    PutV3ProjectsIdMergeRequestMergeRequestIdMergeRequest putV3ProjectsIdMergeRequestMergeRequestIdMergeRequest = new PutV3ProjectsIdMergeRequestMergeRequestIdMergeRequest(); // PutV3ProjectsIdMergeRequestMergeRequestIdMergeRequest | 
    try {
      MergeRequest result = apiInstance.putV3ProjectsIdMergeRequestsMergeRequestIdMerge(id, mergeRequestId, putV3ProjectsIdMergeRequestMergeRequestIdMergeRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#putV3ProjectsIdMergeRequestsMergeRequestIdMerge");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **mergeRequestId** | **Integer**|  | |
| **putV3ProjectsIdMergeRequestMergeRequestIdMergeRequest** | [**PutV3ProjectsIdMergeRequestMergeRequestIdMergeRequest**](PutV3ProjectsIdMergeRequestMergeRequestIdMergeRequest.md)|  | [optional] |

### Return type

[**MergeRequest**](MergeRequest.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Merge a merge request |  -  |

<a id="putV3ProjectsIdMergeRequestsNoteableIdNotesNoteId"></a>
# **putV3ProjectsIdMergeRequestsNoteableIdNotesNoteId**
> Note putV3ProjectsIdMergeRequestsNoteableIdNotesNoteId(id, noteableId, noteId, putV3ProjectsIdIssuesNoteableIdNotesNoteIdRequest)

Update an existing +noteable+ note

Update an existing +noteable+ note

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    Integer noteableId = 56; // Integer | The ID of the noteable
    Integer noteId = 56; // Integer | The ID of a note
    PutV3ProjectsIdIssuesNoteableIdNotesNoteIdRequest putV3ProjectsIdIssuesNoteableIdNotesNoteIdRequest = new PutV3ProjectsIdIssuesNoteableIdNotesNoteIdRequest(); // PutV3ProjectsIdIssuesNoteableIdNotesNoteIdRequest | 
    try {
      Note result = apiInstance.putV3ProjectsIdMergeRequestsNoteableIdNotesNoteId(id, noteableId, noteId, putV3ProjectsIdIssuesNoteableIdNotesNoteIdRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#putV3ProjectsIdMergeRequestsNoteableIdNotesNoteId");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **noteableId** | **Integer**| The ID of the noteable | |
| **noteId** | **Integer**| The ID of a note | |
| **putV3ProjectsIdIssuesNoteableIdNotesNoteIdRequest** | [**PutV3ProjectsIdIssuesNoteableIdNotesNoteIdRequest**](PutV3ProjectsIdIssuesNoteableIdNotesNoteIdRequest.md)|  | |

### Return type

[**Note**](Note.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Update an existing +noteable+ note |  -  |

<a id="putV3ProjectsIdMilestonesMilestoneId"></a>
# **putV3ProjectsIdMilestonesMilestoneId**
> Milestone putV3ProjectsIdMilestonesMilestoneId(id, milestoneId, putV3ProjectsIdMilestonesMilestoneIdRequest)

Update an existing project milestone

Update an existing project milestone

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    Integer milestoneId = 56; // Integer | The ID of a project milestone
    PutV3ProjectsIdMilestonesMilestoneIdRequest putV3ProjectsIdMilestonesMilestoneIdRequest = new PutV3ProjectsIdMilestonesMilestoneIdRequest(); // PutV3ProjectsIdMilestonesMilestoneIdRequest | 
    try {
      Milestone result = apiInstance.putV3ProjectsIdMilestonesMilestoneId(id, milestoneId, putV3ProjectsIdMilestonesMilestoneIdRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#putV3ProjectsIdMilestonesMilestoneId");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **milestoneId** | **Integer**| The ID of a project milestone | |
| **putV3ProjectsIdMilestonesMilestoneIdRequest** | [**PutV3ProjectsIdMilestonesMilestoneIdRequest**](PutV3ProjectsIdMilestonesMilestoneIdRequest.md)|  | [optional] |

### Return type

[**Milestone**](Milestone.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Update an existing project milestone |  -  |

<a id="putV3ProjectsIdNotificationSettings"></a>
# **putV3ProjectsIdNotificationSettings**
> NotificationSetting putV3ProjectsIdNotificationSettings(id, putV3ProjectsIdNotificationSettingsRequest)

Update project level notification level settings, defaults to Global

This feature was introduced in GitLab 8.12

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The group ID or project ID or project NAMESPACE/PROJECT_NAME
    PutV3ProjectsIdNotificationSettingsRequest putV3ProjectsIdNotificationSettingsRequest = new PutV3ProjectsIdNotificationSettingsRequest(); // PutV3ProjectsIdNotificationSettingsRequest | 
    try {
      NotificationSetting result = apiInstance.putV3ProjectsIdNotificationSettings(id, putV3ProjectsIdNotificationSettingsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#putV3ProjectsIdNotificationSettings");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The group ID or project ID or project NAMESPACE/PROJECT_NAME | |
| **putV3ProjectsIdNotificationSettingsRequest** | [**PutV3ProjectsIdNotificationSettingsRequest**](PutV3ProjectsIdNotificationSettingsRequest.md)|  | [optional] |

### Return type

[**NotificationSetting**](NotificationSetting.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Update project level notification level settings, defaults to Global |  -  |

<a id="putV3ProjectsIdRepositoryBranchesBranchProtect"></a>
# **putV3ProjectsIdRepositoryBranchesBranchProtect**
> RepoBranch putV3ProjectsIdRepositoryBranchesBranchProtect(id, branch, putV3ProjectsIdRepositoryBranchesBranchProtectRequest)

Protect a single branch

Protect a single branch

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    String branch = "branch_example"; // String | The name of the branch
    PutV3ProjectsIdRepositoryBranchesBranchProtectRequest putV3ProjectsIdRepositoryBranchesBranchProtectRequest = new PutV3ProjectsIdRepositoryBranchesBranchProtectRequest(); // PutV3ProjectsIdRepositoryBranchesBranchProtectRequest | 
    try {
      RepoBranch result = apiInstance.putV3ProjectsIdRepositoryBranchesBranchProtect(id, branch, putV3ProjectsIdRepositoryBranchesBranchProtectRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#putV3ProjectsIdRepositoryBranchesBranchProtect");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **branch** | **String**| The name of the branch | |
| **putV3ProjectsIdRepositoryBranchesBranchProtectRequest** | [**PutV3ProjectsIdRepositoryBranchesBranchProtectRequest**](PutV3ProjectsIdRepositoryBranchesBranchProtectRequest.md)|  | [optional] |

### Return type

[**RepoBranch**](RepoBranch.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Protect a single branch |  -  |

<a id="putV3ProjectsIdRepositoryBranchesBranchUnprotect"></a>
# **putV3ProjectsIdRepositoryBranchesBranchUnprotect**
> RepoBranch putV3ProjectsIdRepositoryBranchesBranchUnprotect(id, branch)

Unprotect a single branch

Unprotect a single branch

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    String branch = "branch_example"; // String | The name of the branch
    try {
      RepoBranch result = apiInstance.putV3ProjectsIdRepositoryBranchesBranchUnprotect(id, branch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#putV3ProjectsIdRepositoryBranchesBranchUnprotect");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **branch** | **String**| The name of the branch | |

### Return type

[**RepoBranch**](RepoBranch.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Unprotect a single branch |  -  |

<a id="putV3ProjectsIdRepositoryFiles"></a>
# **putV3ProjectsIdRepositoryFiles**
> putV3ProjectsIdRepositoryFiles(id, putV3ProjectsIdRepositoryFilesRequest)

Update existing file in repository

Update existing file in repository

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The project ID
    PutV3ProjectsIdRepositoryFilesRequest putV3ProjectsIdRepositoryFilesRequest = new PutV3ProjectsIdRepositoryFilesRequest(); // PutV3ProjectsIdRepositoryFilesRequest | 
    try {
      apiInstance.putV3ProjectsIdRepositoryFiles(id, putV3ProjectsIdRepositoryFilesRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#putV3ProjectsIdRepositoryFiles");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The project ID | |
| **putV3ProjectsIdRepositoryFilesRequest** | [**PutV3ProjectsIdRepositoryFilesRequest**](PutV3ProjectsIdRepositoryFilesRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Update existing file in repository |  -  |

<a id="putV3ProjectsIdRepositoryTagsTagNameRelease"></a>
# **putV3ProjectsIdRepositoryTagsTagNameRelease**
> Release putV3ProjectsIdRepositoryTagsTagNameRelease(id, tagName, putV3ProjectsIdRepositoryTagsTagNameReleaseRequest)

Update a tag&#39;s release note

Update a tag&#39;s release note

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    String tagName = "tagName_example"; // String | The name of the tag
    PutV3ProjectsIdRepositoryTagsTagNameReleaseRequest putV3ProjectsIdRepositoryTagsTagNameReleaseRequest = new PutV3ProjectsIdRepositoryTagsTagNameReleaseRequest(); // PutV3ProjectsIdRepositoryTagsTagNameReleaseRequest | 
    try {
      Release result = apiInstance.putV3ProjectsIdRepositoryTagsTagNameRelease(id, tagName, putV3ProjectsIdRepositoryTagsTagNameReleaseRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#putV3ProjectsIdRepositoryTagsTagNameRelease");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **tagName** | **String**| The name of the tag | |
| **putV3ProjectsIdRepositoryTagsTagNameReleaseRequest** | [**PutV3ProjectsIdRepositoryTagsTagNameReleaseRequest**](PutV3ProjectsIdRepositoryTagsTagNameReleaseRequest.md)|  | |

### Return type

[**Release**](Release.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Update a tag&#39;s release note |  -  |

<a id="putV3ProjectsIdServicesAsana"></a>
# **putV3ProjectsIdServicesAsana**
> putV3ProjectsIdServicesAsana(id, putV3ProjectsIdServicesAsanaRequest)

Set asana service for project

Set asana service for project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    Integer id = 56; // Integer | 
    PutV3ProjectsIdServicesAsanaRequest putV3ProjectsIdServicesAsanaRequest = new PutV3ProjectsIdServicesAsanaRequest(); // PutV3ProjectsIdServicesAsanaRequest | 
    try {
      apiInstance.putV3ProjectsIdServicesAsana(id, putV3ProjectsIdServicesAsanaRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#putV3ProjectsIdServicesAsana");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**|  | |
| **putV3ProjectsIdServicesAsanaRequest** | [**PutV3ProjectsIdServicesAsanaRequest**](PutV3ProjectsIdServicesAsanaRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Set asana service for project |  -  |

<a id="putV3ProjectsIdServicesAssembla"></a>
# **putV3ProjectsIdServicesAssembla**
> putV3ProjectsIdServicesAssembla(id, putV3ProjectsIdServicesAssemblaRequest)

Set assembla service for project

Set assembla service for project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    Integer id = 56; // Integer | 
    PutV3ProjectsIdServicesAssemblaRequest putV3ProjectsIdServicesAssemblaRequest = new PutV3ProjectsIdServicesAssemblaRequest(); // PutV3ProjectsIdServicesAssemblaRequest | 
    try {
      apiInstance.putV3ProjectsIdServicesAssembla(id, putV3ProjectsIdServicesAssemblaRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#putV3ProjectsIdServicesAssembla");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**|  | |
| **putV3ProjectsIdServicesAssemblaRequest** | [**PutV3ProjectsIdServicesAssemblaRequest**](PutV3ProjectsIdServicesAssemblaRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Set assembla service for project |  -  |

<a id="putV3ProjectsIdServicesBamboo"></a>
# **putV3ProjectsIdServicesBamboo**
> putV3ProjectsIdServicesBamboo(id, putV3ProjectsIdServicesBambooRequest)

Set bamboo service for project

Set bamboo service for project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    Integer id = 56; // Integer | 
    PutV3ProjectsIdServicesBambooRequest putV3ProjectsIdServicesBambooRequest = new PutV3ProjectsIdServicesBambooRequest(); // PutV3ProjectsIdServicesBambooRequest | 
    try {
      apiInstance.putV3ProjectsIdServicesBamboo(id, putV3ProjectsIdServicesBambooRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#putV3ProjectsIdServicesBamboo");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**|  | |
| **putV3ProjectsIdServicesBambooRequest** | [**PutV3ProjectsIdServicesBambooRequest**](PutV3ProjectsIdServicesBambooRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Set bamboo service for project |  -  |

<a id="putV3ProjectsIdServicesBugzilla"></a>
# **putV3ProjectsIdServicesBugzilla**
> putV3ProjectsIdServicesBugzilla(id, putV3ProjectsIdServicesBugzillaRequest)

Set bugzilla service for project

Set bugzilla service for project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    Integer id = 56; // Integer | 
    PutV3ProjectsIdServicesBugzillaRequest putV3ProjectsIdServicesBugzillaRequest = new PutV3ProjectsIdServicesBugzillaRequest(); // PutV3ProjectsIdServicesBugzillaRequest | 
    try {
      apiInstance.putV3ProjectsIdServicesBugzilla(id, putV3ProjectsIdServicesBugzillaRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#putV3ProjectsIdServicesBugzilla");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**|  | |
| **putV3ProjectsIdServicesBugzillaRequest** | [**PutV3ProjectsIdServicesBugzillaRequest**](PutV3ProjectsIdServicesBugzillaRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Set bugzilla service for project |  -  |

<a id="putV3ProjectsIdServicesBuildkite"></a>
# **putV3ProjectsIdServicesBuildkite**
> putV3ProjectsIdServicesBuildkite(id, putV3ProjectsIdServicesBuildkiteRequest)

Set buildkite service for project

Set buildkite service for project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    Integer id = 56; // Integer | 
    PutV3ProjectsIdServicesBuildkiteRequest putV3ProjectsIdServicesBuildkiteRequest = new PutV3ProjectsIdServicesBuildkiteRequest(); // PutV3ProjectsIdServicesBuildkiteRequest | 
    try {
      apiInstance.putV3ProjectsIdServicesBuildkite(id, putV3ProjectsIdServicesBuildkiteRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#putV3ProjectsIdServicesBuildkite");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**|  | |
| **putV3ProjectsIdServicesBuildkiteRequest** | [**PutV3ProjectsIdServicesBuildkiteRequest**](PutV3ProjectsIdServicesBuildkiteRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Set buildkite service for project |  -  |

<a id="putV3ProjectsIdServicesBuildsEmail"></a>
# **putV3ProjectsIdServicesBuildsEmail**
> putV3ProjectsIdServicesBuildsEmail(id, putV3ProjectsIdServicesBuildsEmailRequest)

Set builds-email service for project

Set builds-email service for project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    Integer id = 56; // Integer | 
    PutV3ProjectsIdServicesBuildsEmailRequest putV3ProjectsIdServicesBuildsEmailRequest = new PutV3ProjectsIdServicesBuildsEmailRequest(); // PutV3ProjectsIdServicesBuildsEmailRequest | 
    try {
      apiInstance.putV3ProjectsIdServicesBuildsEmail(id, putV3ProjectsIdServicesBuildsEmailRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#putV3ProjectsIdServicesBuildsEmail");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**|  | |
| **putV3ProjectsIdServicesBuildsEmailRequest** | [**PutV3ProjectsIdServicesBuildsEmailRequest**](PutV3ProjectsIdServicesBuildsEmailRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Set builds-email service for project |  -  |

<a id="putV3ProjectsIdServicesCampfire"></a>
# **putV3ProjectsIdServicesCampfire**
> putV3ProjectsIdServicesCampfire(id, putV3ProjectsIdServicesCampfireRequest)

Set campfire service for project

Set campfire service for project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    Integer id = 56; // Integer | 
    PutV3ProjectsIdServicesCampfireRequest putV3ProjectsIdServicesCampfireRequest = new PutV3ProjectsIdServicesCampfireRequest(); // PutV3ProjectsIdServicesCampfireRequest | 
    try {
      apiInstance.putV3ProjectsIdServicesCampfire(id, putV3ProjectsIdServicesCampfireRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#putV3ProjectsIdServicesCampfire");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**|  | |
| **putV3ProjectsIdServicesCampfireRequest** | [**PutV3ProjectsIdServicesCampfireRequest**](PutV3ProjectsIdServicesCampfireRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Set campfire service for project |  -  |

<a id="putV3ProjectsIdServicesCustomIssueTracker"></a>
# **putV3ProjectsIdServicesCustomIssueTracker**
> putV3ProjectsIdServicesCustomIssueTracker(id, putV3ProjectsIdServicesBugzillaRequest)

Set custom-issue-tracker service for project

Set custom-issue-tracker service for project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    Integer id = 56; // Integer | 
    PutV3ProjectsIdServicesBugzillaRequest putV3ProjectsIdServicesBugzillaRequest = new PutV3ProjectsIdServicesBugzillaRequest(); // PutV3ProjectsIdServicesBugzillaRequest | 
    try {
      apiInstance.putV3ProjectsIdServicesCustomIssueTracker(id, putV3ProjectsIdServicesBugzillaRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#putV3ProjectsIdServicesCustomIssueTracker");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**|  | |
| **putV3ProjectsIdServicesBugzillaRequest** | [**PutV3ProjectsIdServicesBugzillaRequest**](PutV3ProjectsIdServicesBugzillaRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Set custom-issue-tracker service for project |  -  |

<a id="putV3ProjectsIdServicesDroneCi"></a>
# **putV3ProjectsIdServicesDroneCi**
> putV3ProjectsIdServicesDroneCi(id, putV3ProjectsIdServicesDroneCiRequest)

Set drone-ci service for project

Set drone-ci service for project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    Integer id = 56; // Integer | 
    PutV3ProjectsIdServicesDroneCiRequest putV3ProjectsIdServicesDroneCiRequest = new PutV3ProjectsIdServicesDroneCiRequest(); // PutV3ProjectsIdServicesDroneCiRequest | 
    try {
      apiInstance.putV3ProjectsIdServicesDroneCi(id, putV3ProjectsIdServicesDroneCiRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#putV3ProjectsIdServicesDroneCi");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**|  | |
| **putV3ProjectsIdServicesDroneCiRequest** | [**PutV3ProjectsIdServicesDroneCiRequest**](PutV3ProjectsIdServicesDroneCiRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Set drone-ci service for project |  -  |

<a id="putV3ProjectsIdServicesEmailsOnPush"></a>
# **putV3ProjectsIdServicesEmailsOnPush**
> putV3ProjectsIdServicesEmailsOnPush(id, putV3ProjectsIdServicesEmailsOnPushRequest)

Set emails-on-push service for project

Set emails-on-push service for project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    Integer id = 56; // Integer | 
    PutV3ProjectsIdServicesEmailsOnPushRequest putV3ProjectsIdServicesEmailsOnPushRequest = new PutV3ProjectsIdServicesEmailsOnPushRequest(); // PutV3ProjectsIdServicesEmailsOnPushRequest | 
    try {
      apiInstance.putV3ProjectsIdServicesEmailsOnPush(id, putV3ProjectsIdServicesEmailsOnPushRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#putV3ProjectsIdServicesEmailsOnPush");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**|  | |
| **putV3ProjectsIdServicesEmailsOnPushRequest** | [**PutV3ProjectsIdServicesEmailsOnPushRequest**](PutV3ProjectsIdServicesEmailsOnPushRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Set emails-on-push service for project |  -  |

<a id="putV3ProjectsIdServicesExternalWiki"></a>
# **putV3ProjectsIdServicesExternalWiki**
> putV3ProjectsIdServicesExternalWiki(id, putV3ProjectsIdServicesExternalWikiRequest)

Set external-wiki service for project

Set external-wiki service for project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    Integer id = 56; // Integer | 
    PutV3ProjectsIdServicesExternalWikiRequest putV3ProjectsIdServicesExternalWikiRequest = new PutV3ProjectsIdServicesExternalWikiRequest(); // PutV3ProjectsIdServicesExternalWikiRequest | 
    try {
      apiInstance.putV3ProjectsIdServicesExternalWiki(id, putV3ProjectsIdServicesExternalWikiRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#putV3ProjectsIdServicesExternalWiki");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**|  | |
| **putV3ProjectsIdServicesExternalWikiRequest** | [**PutV3ProjectsIdServicesExternalWikiRequest**](PutV3ProjectsIdServicesExternalWikiRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Set external-wiki service for project |  -  |

<a id="putV3ProjectsIdServicesFlowdock"></a>
# **putV3ProjectsIdServicesFlowdock**
> putV3ProjectsIdServicesFlowdock(id, putV3ProjectsIdServicesFlowdockRequest)

Set flowdock service for project

Set flowdock service for project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    Integer id = 56; // Integer | 
    PutV3ProjectsIdServicesFlowdockRequest putV3ProjectsIdServicesFlowdockRequest = new PutV3ProjectsIdServicesFlowdockRequest(); // PutV3ProjectsIdServicesFlowdockRequest | 
    try {
      apiInstance.putV3ProjectsIdServicesFlowdock(id, putV3ProjectsIdServicesFlowdockRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#putV3ProjectsIdServicesFlowdock");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**|  | |
| **putV3ProjectsIdServicesFlowdockRequest** | [**PutV3ProjectsIdServicesFlowdockRequest**](PutV3ProjectsIdServicesFlowdockRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Set flowdock service for project |  -  |

<a id="putV3ProjectsIdServicesGemnasium"></a>
# **putV3ProjectsIdServicesGemnasium**
> putV3ProjectsIdServicesGemnasium(id, putV3ProjectsIdServicesGemnasiumRequest)

Set gemnasium service for project

Set gemnasium service for project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    Integer id = 56; // Integer | 
    PutV3ProjectsIdServicesGemnasiumRequest putV3ProjectsIdServicesGemnasiumRequest = new PutV3ProjectsIdServicesGemnasiumRequest(); // PutV3ProjectsIdServicesGemnasiumRequest | 
    try {
      apiInstance.putV3ProjectsIdServicesGemnasium(id, putV3ProjectsIdServicesGemnasiumRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#putV3ProjectsIdServicesGemnasium");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**|  | |
| **putV3ProjectsIdServicesGemnasiumRequest** | [**PutV3ProjectsIdServicesGemnasiumRequest**](PutV3ProjectsIdServicesGemnasiumRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Set gemnasium service for project |  -  |

<a id="putV3ProjectsIdServicesHipchat"></a>
# **putV3ProjectsIdServicesHipchat**
> putV3ProjectsIdServicesHipchat(id, putV3ProjectsIdServicesHipchatRequest)

Set hipchat service for project

Set hipchat service for project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    Integer id = 56; // Integer | 
    PutV3ProjectsIdServicesHipchatRequest putV3ProjectsIdServicesHipchatRequest = new PutV3ProjectsIdServicesHipchatRequest(); // PutV3ProjectsIdServicesHipchatRequest | 
    try {
      apiInstance.putV3ProjectsIdServicesHipchat(id, putV3ProjectsIdServicesHipchatRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#putV3ProjectsIdServicesHipchat");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**|  | |
| **putV3ProjectsIdServicesHipchatRequest** | [**PutV3ProjectsIdServicesHipchatRequest**](PutV3ProjectsIdServicesHipchatRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Set hipchat service for project |  -  |

<a id="putV3ProjectsIdServicesIrker"></a>
# **putV3ProjectsIdServicesIrker**
> putV3ProjectsIdServicesIrker(id, putV3ProjectsIdServicesIrkerRequest)

Set irker service for project

Set irker service for project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    Integer id = 56; // Integer | 
    PutV3ProjectsIdServicesIrkerRequest putV3ProjectsIdServicesIrkerRequest = new PutV3ProjectsIdServicesIrkerRequest(); // PutV3ProjectsIdServicesIrkerRequest | 
    try {
      apiInstance.putV3ProjectsIdServicesIrker(id, putV3ProjectsIdServicesIrkerRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#putV3ProjectsIdServicesIrker");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**|  | |
| **putV3ProjectsIdServicesIrkerRequest** | [**PutV3ProjectsIdServicesIrkerRequest**](PutV3ProjectsIdServicesIrkerRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Set irker service for project |  -  |

<a id="putV3ProjectsIdServicesJira"></a>
# **putV3ProjectsIdServicesJira**
> putV3ProjectsIdServicesJira(id, putV3ProjectsIdServicesJiraRequest)

Set jira service for project

Set jira service for project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    Integer id = 56; // Integer | 
    PutV3ProjectsIdServicesJiraRequest putV3ProjectsIdServicesJiraRequest = new PutV3ProjectsIdServicesJiraRequest(); // PutV3ProjectsIdServicesJiraRequest | 
    try {
      apiInstance.putV3ProjectsIdServicesJira(id, putV3ProjectsIdServicesJiraRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#putV3ProjectsIdServicesJira");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**|  | |
| **putV3ProjectsIdServicesJiraRequest** | [**PutV3ProjectsIdServicesJiraRequest**](PutV3ProjectsIdServicesJiraRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Set jira service for project |  -  |

<a id="putV3ProjectsIdServicesKubernetes"></a>
# **putV3ProjectsIdServicesKubernetes**
> putV3ProjectsIdServicesKubernetes(id, putV3ProjectsIdServicesKubernetesRequest)

Set kubernetes service for project

Set kubernetes service for project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    Integer id = 56; // Integer | 
    PutV3ProjectsIdServicesKubernetesRequest putV3ProjectsIdServicesKubernetesRequest = new PutV3ProjectsIdServicesKubernetesRequest(); // PutV3ProjectsIdServicesKubernetesRequest | 
    try {
      apiInstance.putV3ProjectsIdServicesKubernetes(id, putV3ProjectsIdServicesKubernetesRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#putV3ProjectsIdServicesKubernetes");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**|  | |
| **putV3ProjectsIdServicesKubernetesRequest** | [**PutV3ProjectsIdServicesKubernetesRequest**](PutV3ProjectsIdServicesKubernetesRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Set kubernetes service for project |  -  |

<a id="putV3ProjectsIdServicesMattermost"></a>
# **putV3ProjectsIdServicesMattermost**
> putV3ProjectsIdServicesMattermost(id, putV3ProjectsIdServicesMattermostRequest)

Set mattermost service for project

Set mattermost service for project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    Integer id = 56; // Integer | 
    PutV3ProjectsIdServicesMattermostRequest putV3ProjectsIdServicesMattermostRequest = new PutV3ProjectsIdServicesMattermostRequest(); // PutV3ProjectsIdServicesMattermostRequest | 
    try {
      apiInstance.putV3ProjectsIdServicesMattermost(id, putV3ProjectsIdServicesMattermostRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#putV3ProjectsIdServicesMattermost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**|  | |
| **putV3ProjectsIdServicesMattermostRequest** | [**PutV3ProjectsIdServicesMattermostRequest**](PutV3ProjectsIdServicesMattermostRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Set mattermost service for project |  -  |

<a id="putV3ProjectsIdServicesMattermostSlashCommands"></a>
# **putV3ProjectsIdServicesMattermostSlashCommands**
> putV3ProjectsIdServicesMattermostSlashCommands(id, putV3ProjectsIdServicesMattermostSlashCommandsRequest)

Set mattermost-slash-commands service for project

Set mattermost-slash-commands service for project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    Integer id = 56; // Integer | 
    PutV3ProjectsIdServicesMattermostSlashCommandsRequest putV3ProjectsIdServicesMattermostSlashCommandsRequest = new PutV3ProjectsIdServicesMattermostSlashCommandsRequest(); // PutV3ProjectsIdServicesMattermostSlashCommandsRequest | 
    try {
      apiInstance.putV3ProjectsIdServicesMattermostSlashCommands(id, putV3ProjectsIdServicesMattermostSlashCommandsRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#putV3ProjectsIdServicesMattermostSlashCommands");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**|  | |
| **putV3ProjectsIdServicesMattermostSlashCommandsRequest** | [**PutV3ProjectsIdServicesMattermostSlashCommandsRequest**](PutV3ProjectsIdServicesMattermostSlashCommandsRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Set mattermost-slash-commands service for project |  -  |

<a id="putV3ProjectsIdServicesPipelinesEmail"></a>
# **putV3ProjectsIdServicesPipelinesEmail**
> putV3ProjectsIdServicesPipelinesEmail(id, putV3ProjectsIdServicesPipelinesEmailRequest)

Set pipelines-email service for project

Set pipelines-email service for project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    Integer id = 56; // Integer | 
    PutV3ProjectsIdServicesPipelinesEmailRequest putV3ProjectsIdServicesPipelinesEmailRequest = new PutV3ProjectsIdServicesPipelinesEmailRequest(); // PutV3ProjectsIdServicesPipelinesEmailRequest | 
    try {
      apiInstance.putV3ProjectsIdServicesPipelinesEmail(id, putV3ProjectsIdServicesPipelinesEmailRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#putV3ProjectsIdServicesPipelinesEmail");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**|  | |
| **putV3ProjectsIdServicesPipelinesEmailRequest** | [**PutV3ProjectsIdServicesPipelinesEmailRequest**](PutV3ProjectsIdServicesPipelinesEmailRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Set pipelines-email service for project |  -  |

<a id="putV3ProjectsIdServicesPivotaltracker"></a>
# **putV3ProjectsIdServicesPivotaltracker**
> putV3ProjectsIdServicesPivotaltracker(id, putV3ProjectsIdServicesPivotaltrackerRequest)

Set pivotaltracker service for project

Set pivotaltracker service for project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    Integer id = 56; // Integer | 
    PutV3ProjectsIdServicesPivotaltrackerRequest putV3ProjectsIdServicesPivotaltrackerRequest = new PutV3ProjectsIdServicesPivotaltrackerRequest(); // PutV3ProjectsIdServicesPivotaltrackerRequest | 
    try {
      apiInstance.putV3ProjectsIdServicesPivotaltracker(id, putV3ProjectsIdServicesPivotaltrackerRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#putV3ProjectsIdServicesPivotaltracker");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**|  | |
| **putV3ProjectsIdServicesPivotaltrackerRequest** | [**PutV3ProjectsIdServicesPivotaltrackerRequest**](PutV3ProjectsIdServicesPivotaltrackerRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Set pivotaltracker service for project |  -  |

<a id="putV3ProjectsIdServicesPushover"></a>
# **putV3ProjectsIdServicesPushover**
> putV3ProjectsIdServicesPushover(id, putV3ProjectsIdServicesPushoverRequest)

Set pushover service for project

Set pushover service for project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    Integer id = 56; // Integer | 
    PutV3ProjectsIdServicesPushoverRequest putV3ProjectsIdServicesPushoverRequest = new PutV3ProjectsIdServicesPushoverRequest(); // PutV3ProjectsIdServicesPushoverRequest | 
    try {
      apiInstance.putV3ProjectsIdServicesPushover(id, putV3ProjectsIdServicesPushoverRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#putV3ProjectsIdServicesPushover");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**|  | |
| **putV3ProjectsIdServicesPushoverRequest** | [**PutV3ProjectsIdServicesPushoverRequest**](PutV3ProjectsIdServicesPushoverRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Set pushover service for project |  -  |

<a id="putV3ProjectsIdServicesRedmine"></a>
# **putV3ProjectsIdServicesRedmine**
> putV3ProjectsIdServicesRedmine(id, putV3ProjectsIdServicesRedmineRequest)

Set redmine service for project

Set redmine service for project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    Integer id = 56; // Integer | 
    PutV3ProjectsIdServicesRedmineRequest putV3ProjectsIdServicesRedmineRequest = new PutV3ProjectsIdServicesRedmineRequest(); // PutV3ProjectsIdServicesRedmineRequest | 
    try {
      apiInstance.putV3ProjectsIdServicesRedmine(id, putV3ProjectsIdServicesRedmineRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#putV3ProjectsIdServicesRedmine");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**|  | |
| **putV3ProjectsIdServicesRedmineRequest** | [**PutV3ProjectsIdServicesRedmineRequest**](PutV3ProjectsIdServicesRedmineRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Set redmine service for project |  -  |

<a id="putV3ProjectsIdServicesSlack"></a>
# **putV3ProjectsIdServicesSlack**
> putV3ProjectsIdServicesSlack(id, putV3ProjectsIdServicesSlackRequest)

Set slack service for project

Set slack service for project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    Integer id = 56; // Integer | 
    PutV3ProjectsIdServicesSlackRequest putV3ProjectsIdServicesSlackRequest = new PutV3ProjectsIdServicesSlackRequest(); // PutV3ProjectsIdServicesSlackRequest | 
    try {
      apiInstance.putV3ProjectsIdServicesSlack(id, putV3ProjectsIdServicesSlackRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#putV3ProjectsIdServicesSlack");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**|  | |
| **putV3ProjectsIdServicesSlackRequest** | [**PutV3ProjectsIdServicesSlackRequest**](PutV3ProjectsIdServicesSlackRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Set slack service for project |  -  |

<a id="putV3ProjectsIdServicesSlackSlashCommands"></a>
# **putV3ProjectsIdServicesSlackSlashCommands**
> putV3ProjectsIdServicesSlackSlashCommands(id, putV3ProjectsIdServicesSlackSlashCommandsRequest)

Set slack-slash-commands service for project

Set slack-slash-commands service for project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    Integer id = 56; // Integer | 
    PutV3ProjectsIdServicesSlackSlashCommandsRequest putV3ProjectsIdServicesSlackSlashCommandsRequest = new PutV3ProjectsIdServicesSlackSlashCommandsRequest(); // PutV3ProjectsIdServicesSlackSlashCommandsRequest | 
    try {
      apiInstance.putV3ProjectsIdServicesSlackSlashCommands(id, putV3ProjectsIdServicesSlackSlashCommandsRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#putV3ProjectsIdServicesSlackSlashCommands");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**|  | |
| **putV3ProjectsIdServicesSlackSlashCommandsRequest** | [**PutV3ProjectsIdServicesSlackSlashCommandsRequest**](PutV3ProjectsIdServicesSlackSlashCommandsRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Set slack-slash-commands service for project |  -  |

<a id="putV3ProjectsIdServicesTeamcity"></a>
# **putV3ProjectsIdServicesTeamcity**
> putV3ProjectsIdServicesTeamcity(id, putV3ProjectsIdServicesTeamcityRequest)

Set teamcity service for project

Set teamcity service for project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    Integer id = 56; // Integer | 
    PutV3ProjectsIdServicesTeamcityRequest putV3ProjectsIdServicesTeamcityRequest = new PutV3ProjectsIdServicesTeamcityRequest(); // PutV3ProjectsIdServicesTeamcityRequest | 
    try {
      apiInstance.putV3ProjectsIdServicesTeamcity(id, putV3ProjectsIdServicesTeamcityRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#putV3ProjectsIdServicesTeamcity");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**|  | |
| **putV3ProjectsIdServicesTeamcityRequest** | [**PutV3ProjectsIdServicesTeamcityRequest**](PutV3ProjectsIdServicesTeamcityRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Set teamcity service for project |  -  |

<a id="putV3ProjectsIdSnippetsNoteableIdNotesNoteId"></a>
# **putV3ProjectsIdSnippetsNoteableIdNotesNoteId**
> Note putV3ProjectsIdSnippetsNoteableIdNotesNoteId(id, noteableId, noteId, putV3ProjectsIdIssuesNoteableIdNotesNoteIdRequest)

Update an existing +noteable+ note

Update an existing +noteable+ note

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    Integer noteableId = 56; // Integer | The ID of the noteable
    Integer noteId = 56; // Integer | The ID of a note
    PutV3ProjectsIdIssuesNoteableIdNotesNoteIdRequest putV3ProjectsIdIssuesNoteableIdNotesNoteIdRequest = new PutV3ProjectsIdIssuesNoteableIdNotesNoteIdRequest(); // PutV3ProjectsIdIssuesNoteableIdNotesNoteIdRequest | 
    try {
      Note result = apiInstance.putV3ProjectsIdSnippetsNoteableIdNotesNoteId(id, noteableId, noteId, putV3ProjectsIdIssuesNoteableIdNotesNoteIdRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#putV3ProjectsIdSnippetsNoteableIdNotesNoteId");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **noteableId** | **Integer**| The ID of the noteable | |
| **noteId** | **Integer**| The ID of a note | |
| **putV3ProjectsIdIssuesNoteableIdNotesNoteIdRequest** | [**PutV3ProjectsIdIssuesNoteableIdNotesNoteIdRequest**](PutV3ProjectsIdIssuesNoteableIdNotesNoteIdRequest.md)|  | |

### Return type

[**Note**](Note.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Update an existing +noteable+ note |  -  |

<a id="putV3ProjectsIdSnippetsSnippetId"></a>
# **putV3ProjectsIdSnippetsSnippetId**
> ProjectSnippet putV3ProjectsIdSnippetsSnippetId(id, snippetId, putV3ProjectsIdSnippetsSnippetIdRequest)

Update an existing project snippet

Update an existing project snippet

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    Integer snippetId = 56; // Integer | The ID of a project snippet
    PutV3ProjectsIdSnippetsSnippetIdRequest putV3ProjectsIdSnippetsSnippetIdRequest = new PutV3ProjectsIdSnippetsSnippetIdRequest(); // PutV3ProjectsIdSnippetsSnippetIdRequest | 
    try {
      ProjectSnippet result = apiInstance.putV3ProjectsIdSnippetsSnippetId(id, snippetId, putV3ProjectsIdSnippetsSnippetIdRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#putV3ProjectsIdSnippetsSnippetId");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **snippetId** | **Integer**| The ID of a project snippet | |
| **putV3ProjectsIdSnippetsSnippetIdRequest** | [**PutV3ProjectsIdSnippetsSnippetIdRequest**](PutV3ProjectsIdSnippetsSnippetIdRequest.md)|  | [optional] |

### Return type

[**ProjectSnippet**](ProjectSnippet.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Update an existing project snippet |  -  |

<a id="putV3ProjectsIdVariablesKey"></a>
# **putV3ProjectsIdVariablesKey**
> Variable putV3ProjectsIdVariablesKey(id, key, putV3ProjectsIdVariablesKeyRequest)

Update an existing variable from a project

Update an existing variable from a project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String id = "id_example"; // String | The ID of a project
    String key = "key_example"; // String | The key of the variable
    PutV3ProjectsIdVariablesKeyRequest putV3ProjectsIdVariablesKeyRequest = new PutV3ProjectsIdVariablesKeyRequest(); // PutV3ProjectsIdVariablesKeyRequest | 
    try {
      Variable result = apiInstance.putV3ProjectsIdVariablesKey(id, key, putV3ProjectsIdVariablesKeyRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#putV3ProjectsIdVariablesKey");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of a project | |
| **key** | **String**| The key of the variable | |
| **putV3ProjectsIdVariablesKeyRequest** | [**PutV3ProjectsIdVariablesKeyRequest**](PutV3ProjectsIdVariablesKeyRequest.md)|  | [optional] |

### Return type

[**Variable**](Variable.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Update an existing variable from a project |  -  |

