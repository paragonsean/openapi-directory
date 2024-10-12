# GitHubV3RestApi.Installation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessTokensUrl** | **String** |  | 
**account** | [**InstallationAccount**](InstallationAccount.md) |  | 
**appId** | **Number** |  | 
**appSlug** | **String** |  | 
**contactEmail** | **String** |  | [optional] 
**createdAt** | **Date** |  | 
**events** | **[String]** |  | 
**hasMultipleSingleFiles** | **Boolean** |  | [optional] 
**htmlUrl** | **String** |  | 
**id** | **Number** | The ID of the installation. | 
**permissions** | [**AppPermissions**](AppPermissions.md) |  | 
**repositoriesUrl** | **String** |  | 
**repositorySelection** | **String** | Describe whether all repositories have been selected or there&#39;s a selection involved | 
**singleFileName** | **String** |  | 
**singleFilePaths** | **[String]** |  | [optional] 
**suspendedAt** | **Date** |  | 
**suspendedBy** | [**NullableSimpleUser**](NullableSimpleUser.md) |  | 
**targetId** | **Number** | The ID of the user or organization this token is being scoped to. | 
**targetType** | **String** |  | 
**updatedAt** | **Date** |  | 



## Enum: RepositorySelectionEnum


* `all` (value: `"all"`)

* `selected` (value: `"selected"`)




