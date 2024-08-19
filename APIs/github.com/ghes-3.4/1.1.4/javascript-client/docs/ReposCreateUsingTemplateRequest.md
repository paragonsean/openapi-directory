# GitHubV3RestApi.ReposCreateUsingTemplateRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | A short description of the new repository. | [optional] 
**includeAllBranches** | **Boolean** | Set to &#x60;true&#x60; to include the directory structure and files from all branches in the template repository, and not just the default branch. Default: &#x60;false&#x60;. | [optional] [default to false]
**name** | **String** | The name of the new repository. | 
**owner** | **String** | The organization or person who will own the new repository. To create a new repository in an organization, the authenticated user must be a member of the specified organization. | [optional] 
**_private** | **Boolean** | Either &#x60;true&#x60; to create a new private repository or &#x60;false&#x60; to create a new public one. | [optional] [default to false]


