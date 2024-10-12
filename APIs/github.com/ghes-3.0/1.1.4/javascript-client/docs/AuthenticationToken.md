# GitHubV3RestApi.AuthenticationToken

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expiresAt** | **Date** | The time this token expires | 
**permissions** | **Object** |  | [optional] 
**repositories** | [**[Repository]**](Repository.md) | The repositories this token has access to | [optional] 
**repositorySelection** | **String** | Describe whether all repositories have been selected or there&#39;s a selection involved | [optional] 
**singleFile** | **String** |  | [optional] 
**token** | **String** | The token used for authentication | 



## Enum: RepositorySelectionEnum


* `all` (value: `"all"`)

* `selected` (value: `"selected"`)




