

# ReposCreateForAuthenticatedUserRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowMergeCommit** | **Boolean** | Whether to allow merge commits for pull requests. |  [optional] |
|**allowRebaseMerge** | **Boolean** | Whether to allow rebase merges for pull requests. |  [optional] |
|**allowSquashMerge** | **Boolean** | Whether to allow squash merges for pull requests. |  [optional] |
|**autoInit** | **Boolean** | Whether the repository is initialized with a minimal README. |  [optional] |
|**deleteBranchOnMerge** | **Boolean** | Whether to delete head branches when pull requests are merged |  [optional] |
|**description** | **String** | A short description of the repository. |  [optional] |
|**gitignoreTemplate** | **String** | The desired language or platform to apply to the .gitignore. |  [optional] |
|**hasDownloads** | **Boolean** | Whether downloads are enabled. |  [optional] |
|**hasIssues** | **Boolean** | Whether issues are enabled. |  [optional] |
|**hasProjects** | **Boolean** | Whether projects are enabled. |  [optional] |
|**hasWiki** | **Boolean** | Whether the wiki is enabled. |  [optional] |
|**homepage** | **String** | A URL with more information about the repository. |  [optional] |
|**isTemplate** | **Boolean** | Whether this repository acts as a template that can be used to generate new repositories. |  [optional] |
|**licenseTemplate** | **String** | The license keyword of the open source license for this repository. |  [optional] |
|**name** | **String** | The name of the repository. |  |
|**_private** | **Boolean** | Whether the repository is private. |  [optional] |
|**teamId** | **Integer** | The id of the team that will be granted access to this repository. This is only valid when creating a repository in an organization. |  [optional] |



