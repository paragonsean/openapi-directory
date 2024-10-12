# GitHubV3RestApi.ReposCreateInOrgRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowAutoMerge** | **Boolean** | Either &#x60;true&#x60; to allow auto-merge on pull requests, or &#x60;false&#x60; to disallow auto-merge. | [optional] [default to false]
**allowMergeCommit** | **Boolean** | Either &#x60;true&#x60; to allow merging pull requests with a merge commit, or &#x60;false&#x60; to prevent merging pull requests with merge commits. | [optional] [default to true]
**allowRebaseMerge** | **Boolean** | Either &#x60;true&#x60; to allow rebase-merging pull requests, or &#x60;false&#x60; to prevent rebase-merging. | [optional] [default to true]
**allowSquashMerge** | **Boolean** | Either &#x60;true&#x60; to allow squash-merging pull requests, or &#x60;false&#x60; to prevent squash-merging. | [optional] [default to true]
**autoInit** | **Boolean** | Pass &#x60;true&#x60; to create an initial commit with empty README. | [optional] [default to false]
**deleteBranchOnMerge** | **Boolean** | Either &#x60;true&#x60; to allow automatically deleting head branches when pull requests are merged, or &#x60;false&#x60; to prevent automatic deletion. **The authenticated user must be an organization owner to set this property to &#x60;true&#x60;.** | [optional] [default to false]
**description** | **String** | A short description of the repository. | [optional] 
**gitignoreTemplate** | **String** | Desired language or platform [.gitignore template](https://github.com/github/gitignore) to apply. Use the name of the template without the extension. For example, \&quot;Haskell\&quot;. | [optional] 
**hasDownloads** | **Boolean** | Whether downloads are enabled. | [optional] [default to true]
**hasIssues** | **Boolean** | Either &#x60;true&#x60; to enable issues for this repository or &#x60;false&#x60; to disable them. | [optional] [default to true]
**hasProjects** | **Boolean** | Either &#x60;true&#x60; to enable projects for this repository or &#x60;false&#x60; to disable them. **Note:** If you&#39;re creating a repository in an organization that has disabled repository projects, the default is &#x60;false&#x60;, and if you pass &#x60;true&#x60;, the API returns an error. | [optional] [default to true]
**hasWiki** | **Boolean** | Either &#x60;true&#x60; to enable the wiki for this repository or &#x60;false&#x60; to disable it. | [optional] [default to true]
**homepage** | **String** | A URL with more information about the repository. | [optional] 
**isTemplate** | **Boolean** | Either &#x60;true&#x60; to make this repo available as a template repository or &#x60;false&#x60; to prevent it. | [optional] [default to false]
**licenseTemplate** | **String** | Choose an [open source license template](https://choosealicense.com/) that best suits your needs, and then use the [license keyword](https://docs.github.com/enterprise-server@3.4/articles/licensing-a-repository/#searching-github-by-license-type) as the &#x60;license_template&#x60; string. For example, \&quot;mit\&quot; or \&quot;mpl-2.0\&quot;. | [optional] 
**mergeCommitMessage** | **String** | The default value for a merge commit message.  - &#x60;PR_TITLE&#x60; - default to the pull request&#39;s title. - &#x60;PR_BODY&#x60; - default to the pull request&#39;s body. - &#x60;BLANK&#x60; - default to a blank commit message. | [optional] 
**mergeCommitTitle** | **String** | The default value for a merge commit title.  - &#x60;PR_TITLE&#x60; - default to the pull request&#39;s title. - &#x60;MERGE_MESSAGE&#x60; - default to the classic title for a merge message (e.g., Merge pull request #123 from branch-name). | [optional] 
**name** | **String** | The name of the repository. | 
**_private** | **Boolean** | Whether the repository is private. | [optional] [default to false]
**squashMergeCommitMessage** | **String** | The default value for a squash merge commit message:  - &#x60;PR_BODY&#x60; - default to the pull request&#39;s body. - &#x60;COMMIT_MESSAGES&#x60; - default to the branch&#39;s commit messages. - &#x60;BLANK&#x60; - default to a blank commit message. | [optional] 
**squashMergeCommitTitle** | **String** | The default value for a squash merge commit title:  - &#x60;PR_TITLE&#x60; - default to the pull request&#39;s title. - &#x60;COMMIT_OR_PR_TITLE&#x60; - default to the commit&#39;s title (if only one commit) or the pull request&#39;s title (when more than one commit). | [optional] 
**teamId** | **Number** | The id of the team that will be granted access to this repository. This is only valid when creating a repository in an organization. | [optional] 
**useSquashPrTitleAsDefault** | **Boolean** | Either &#x60;true&#x60; to allow squash-merge commits to use pull request title, or &#x60;false&#x60; to use commit message. **This property has been deprecated. Please use &#x60;squash_merge_commit_title&#x60; instead. | [optional] [default to false]
**visibility** | **String** | The visibility of the repository. **Note**: For GitHub Enterprise Server, this endpoint will only list repositories available to all users on the enterprise. For more information, see \&quot;[Creating an internal repository](https://docs.github.com/enterprise-server@3.4/github/creating-cloning-and-archiving-repositories/about-repository-visibility#about-internal-repositories)\&quot; in the GitHub Help documentation.   The &#x60;visibility&#x60; parameter overrides the &#x60;private&#x60; parameter when you use both parameters with the &#x60;nebula-preview&#x60; preview header. | [optional] 



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





## Enum: VisibilityEnum


* `public` (value: `"public"`)

* `private` (value: `"private"`)

* `internal` (value: `"internal"`)




