

# ReposUpdateRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowForking** | **Boolean** | Either &#x60;true&#x60; to allow private forks, or &#x60;false&#x60; to prevent private forks. |  [optional] |
|**allowMergeCommit** | **Boolean** | Either &#x60;true&#x60; to allow merging pull requests with a merge commit, or &#x60;false&#x60; to prevent merging pull requests with merge commits. |  [optional] |
|**allowRebaseMerge** | **Boolean** | Either &#x60;true&#x60; to allow rebase-merging pull requests, or &#x60;false&#x60; to prevent rebase-merging. |  [optional] |
|**allowSquashMerge** | **Boolean** | Either &#x60;true&#x60; to allow squash-merging pull requests, or &#x60;false&#x60; to prevent squash-merging. |  [optional] |
|**allowUpdateBranch** | **Boolean** | Either &#x60;true&#x60; to always allow a pull request head branch that is behind its base branch to be updated even if it is not required to be up to date before merging, or false otherwise. |  [optional] |
|**archived** | **Boolean** | &#x60;true&#x60; to archive this repository. **Note**: You cannot unarchive repositories through the API. |  [optional] |
|**defaultBranch** | **String** | Updates the default branch for this repository. |  [optional] |
|**deleteBranchOnMerge** | **Boolean** | Either &#x60;true&#x60; to allow automatically deleting head branches when pull requests are merged, or &#x60;false&#x60; to prevent automatic deletion. |  [optional] |
|**description** | **String** | A short description of the repository. |  [optional] |
|**hasIssues** | **Boolean** | Either &#x60;true&#x60; to enable issues for this repository or &#x60;false&#x60; to disable them. |  [optional] |
|**hasProjects** | **Boolean** | Either &#x60;true&#x60; to enable projects for this repository or &#x60;false&#x60; to disable them. **Note:** If you&#39;re creating a repository in an organization that has disabled repository projects, the default is &#x60;false&#x60;, and if you pass &#x60;true&#x60;, the API returns an error. |  [optional] |
|**hasWiki** | **Boolean** | Either &#x60;true&#x60; to enable the wiki for this repository or &#x60;false&#x60; to disable it. |  [optional] |
|**homepage** | **String** | A URL with more information about the repository. |  [optional] |
|**isTemplate** | **Boolean** | Either &#x60;true&#x60; to make this repo available as a template repository or &#x60;false&#x60; to prevent it. |  [optional] |
|**name** | **String** | The name of the repository. |  [optional] |
|**_private** | **Boolean** | Either &#x60;true&#x60; to make the repository private or &#x60;false&#x60; to make it public. Default: &#x60;false&#x60;.   **Note**: You will get a &#x60;422&#x60; error if the organization restricts [changing repository visibility](https://docs.github.com/articles/repository-permission-levels-for-an-organization#changing-the-visibility-of-repositories) to organization owners and a non-owner tries to change the value of private. **Note**: You will get a &#x60;422&#x60; error if the organization restricts [changing repository visibility](https://docs.github.com/articles/repository-permission-levels-for-an-organization#changing-the-visibility-of-repositories) to organization owners and a non-owner tries to change the value of private. |  [optional] |
|**useSquashPrTitleAsDefault** | **Boolean** | Either &#x60;true&#x60; to allow squash-merge commits to use pull request title, or &#x60;false&#x60; to use commit message. |  [optional] |
|**visibility** | [**VisibilityEnum**](#VisibilityEnum) | Can be &#x60;public&#x60; or &#x60;private&#x60;. If your organization is associated with an enterprise account using GitHub Enterprise Cloud or GitHub Enterprise Server 2.20+, &#x60;visibility&#x60; can also be &#x60;internal&#x60;. The &#x60;visibility&#x60; parameter overrides the &#x60;private&#x60; parameter when you use both along with the &#x60;nebula-preview&#x60; preview header. |  [optional] |



## Enum: VisibilityEnum

| Name | Value |
|---- | -----|
| PUBLIC | &quot;public&quot; |
| PRIVATE | &quot;private&quot; |
| INTERNAL | &quot;internal&quot; |



