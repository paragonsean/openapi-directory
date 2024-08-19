# VisualStudioResourceProviderClient.CodeRepository

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorizationReference** | **String** | Reference to the authorization info used to access the code repository. This value is used as a key into the global authorization details dictionary. | [optional] 
**defaultBranch** | **String** | Default branch for which continuous integration should be configured in the VSTS pipeline. | 
**id** | **String** | Unique identifier of the code repository. | 
**properties** | **{String: String}** | Repository-specific properties. | [optional] 
**repositoryType** | **String** | Type of code repository. | 



## Enum: RepositoryTypeEnum


* `gitHub` (value: `"gitHub"`)

* `vstsGit` (value: `"vstsGit"`)




