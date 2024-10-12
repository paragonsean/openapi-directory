# GitHubV3RestApi.ReposCreateForAuthenticatedUserRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowAutoMerge** | **Boolean** | Whether to allow Auto-merge to be used on pull requests. | [optional] [default to false]
**allowMergeCommit** | **Boolean** | Whether to allow merge commits for pull requests. | [optional] [default to true]
**allowRebaseMerge** | **Boolean** | Whether to allow rebase merges for pull requests. | [optional] [default to true]
**allowSquashMerge** | **Boolean** | Whether to allow squash merges for pull requests. | [optional] [default to true]
**autoInit** | **Boolean** | Whether the repository is initialized with a minimal README. | [optional] [default to false]
**deleteBranchOnMerge** | **Boolean** | Whether to delete head branches when pull requests are merged | [optional] [default to false]
**description** | **String** | A short description of the repository. | [optional] 
**gitignoreTemplate** | **String** | The desired language or platform to apply to the .gitignore. | [optional] 
**hasDiscussions** | **Boolean** | Whether discussions are enabled. | [optional] [default to false]
**hasDownloads** | **Boolean** | Whether downloads are enabled. | [optional] [default to true]
**hasIssues** | **Boolean** | Whether issues are enabled. | [optional] [default to true]
**hasProjects** | **Boolean** | Whether projects are enabled. | [optional] [default to true]
**hasWiki** | **Boolean** | Whether the wiki is enabled. | [optional] [default to true]
**homepage** | **String** | A URL with more information about the repository. | [optional] 
**isTemplate** | **Boolean** | Whether this repository acts as a template that can be used to generate new repositories. | [optional] [default to false]
**licenseTemplate** | **String** | The license keyword of the open source license for this repository. | [optional] 
**mergeCommitMessage** | **String** | The default value for a merge commit message.  - &#x60;PR_TITLE&#x60; - default to the pull request&#39;s title. - &#x60;PR_BODY&#x60; - default to the pull request&#39;s body. - &#x60;BLANK&#x60; - default to a blank commit message. | [optional] 
**mergeCommitTitle** | **String** | The default value for a merge commit title.  - &#x60;PR_TITLE&#x60; - default to the pull request&#39;s title. - &#x60;MERGE_MESSAGE&#x60; - default to the classic title for a merge message (e.g., Merge pull request #123 from branch-name). | [optional] 
**name** | **String** | The name of the repository. | 
**_private** | **Boolean** | Whether the repository is private. | [optional] [default to false]
**squashMergeCommitMessage** | **String** | The default value for a squash merge commit message:  - &#x60;PR_BODY&#x60; - default to the pull request&#39;s body. - &#x60;COMMIT_MESSAGES&#x60; - default to the branch&#39;s commit messages. - &#x60;BLANK&#x60; - default to a blank commit message. | [optional] 
**squashMergeCommitTitle** | **String** | The default value for a squash merge commit title:  - &#x60;PR_TITLE&#x60; - default to the pull request&#39;s title. - &#x60;COMMIT_OR_PR_TITLE&#x60; - default to the commit&#39;s title (if only one commit) or the pull request&#39;s title (when more than one commit). | [optional] 
**teamId** | **Number** | The id of the team that will be granted access to this repository. This is only valid when creating a repository in an organization. | [optional] 



## Enum: MergeCommitMessageEnum


* `PR_BODY` (value: `"PR_BODY"`)

* `PR_TITLE` (value: `"PR_TITLE"`)

* `BLANK` (value: `"BLANK"`)





## Enum: MergeCommitTitleEnum


* `PR_TITLE` (value: `"PR_TITLE"`)

* `MERGE_MESSAGE` (value: `"MERGE_MESSAGE"`)





## Enum: SquashMergeCommitMessageEnum


* `PR_BODY` (value: `"PR_BODY"`)

* `COMMIT_MESSAGES` (value: `"COMMIT_MESSAGES"`)

* `BLANK` (value: `"BLANK"`)





## Enum: SquashMergeCommitTitleEnum


* `PR_TITLE` (value: `"PR_TITLE"`)

* `COMMIT_OR_PR_TITLE` (value: `"COMMIT_OR_PR_TITLE"`)




