# GitHubV3RestApi.ReposCreateForAuthenticatedUserRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowMergeCommit** | **Boolean** | Whether to allow merge commits for pull requests. | [optional] [default to true]
**allowRebaseMerge** | **Boolean** | Whether to allow rebase merges for pull requests. | [optional] [default to true]
**allowSquashMerge** | **Boolean** | Whether to allow squash merges for pull requests. | [optional] [default to true]
**autoInit** | **Boolean** | Whether the repository is initialized with a minimal README. | [optional] [default to false]
**deleteBranchOnMerge** | **Boolean** | Whether to delete head branches when pull requests are merged | [optional] [default to false]
**description** | **String** | A short description of the repository. | [optional] 
**gitignoreTemplate** | **String** | The desired language or platform to apply to the .gitignore. | [optional] 
**hasDownloads** | **Boolean** | Whether downloads are enabled. | [optional] [default to true]
**hasIssues** | **Boolean** | Whether issues are enabled. | [optional] [default to true]
**hasProjects** | **Boolean** | Whether projects are enabled. | [optional] [default to true]
**hasWiki** | **Boolean** | Whether the wiki is enabled. | [optional] [default to true]
**homepage** | **String** | A URL with more information about the repository. | [optional] 
**isTemplate** | **Boolean** | Whether this repository acts as a template that can be used to generate new repositories. | [optional] [default to false]
**licenseTemplate** | **String** | The license keyword of the open source license for this repository. | [optional] 
**name** | **String** | The name of the repository. | 
**_private** | **Boolean** | Whether the repository is private. | [optional] [default to false]
**teamId** | **Number** | The id of the team that will be granted access to this repository. This is only valid when creating a repository in an organization. | [optional] 


