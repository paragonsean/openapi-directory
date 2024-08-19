

# Installation

Installation

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accessTokensUrl** | **URI** |  |  |
|**account** | [**InstallationAccount**](InstallationAccount.md) |  |  |
|**appId** | **Integer** |  |  |
|**appSlug** | **String** |  |  |
|**contactEmail** | **String** |  |  [optional] |
|**createdAt** | **OffsetDateTime** |  |  |
|**events** | **List&lt;String&gt;** |  |  |
|**hasMultipleSingleFiles** | **Boolean** |  |  [optional] |
|**htmlUrl** | **URI** |  |  |
|**id** | **Integer** | The ID of the installation. |  |
|**permissions** | [**AppPermissions**](AppPermissions.md) |  |  |
|**repositoriesUrl** | **URI** |  |  |
|**repositorySelection** | [**RepositorySelectionEnum**](#RepositorySelectionEnum) | Describe whether all repositories have been selected or there&#39;s a selection involved |  |
|**singleFileName** | **String** |  |  |
|**singleFilePaths** | **List&lt;String&gt;** |  |  [optional] |
|**suspendedAt** | **OffsetDateTime** |  |  |
|**suspendedBy** | [**NullableSimpleUser**](NullableSimpleUser.md) |  |  |
|**targetId** | **Integer** | The ID of the user or organization this token is being scoped to. |  |
|**targetType** | **String** |  |  |
|**updatedAt** | **OffsetDateTime** |  |  |



## Enum: RepositorySelectionEnum

| Name | Value |
|---- | -----|
| ALL | &quot;all&quot; |
| SELECTED | &quot;selected&quot; |



