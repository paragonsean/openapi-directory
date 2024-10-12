# GitHubV3RestApi.InstallationGhes2

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessTokensUrl** | **String** |  | 
**account** | [**InstallationGhes2Account**](InstallationGhes2Account.md) |  | 
**appId** | **Number** |  | 
**appSlug** | **String** |  | 
**contactEmail** | **String** |  | [optional] 
**createdAt** | **Date** |  | 
**events** | **[String]** |  | 
**htmlUrl** | **String** |  | 
**id** | **Number** | The ID of the installation. | 
**permissions** | [**InstallationGhes2Permissions**](InstallationGhes2Permissions.md) |  | 
**repositoriesUrl** | **String** |  | 
**repositorySelection** | **String** | Describe whether all repositories have been selected or there&#39;s a selection involved | 
**singleFileName** | **String** |  | 
**suspendedAt** | **Date** |  | [optional] 
**suspendedBy** | [**NullableSimpleUser**](NullableSimpleUser.md) |  | [optional] 
**targetId** | **Number** | The ID of the user or organization this token is being scoped to. | 
**targetType** | **String** |  | 
**updatedAt** | **Date** |  | 



## Enum: RepositorySelectionEnum


* `all` (value: `"all"`)

* `selected` (value: `"selected"`)




