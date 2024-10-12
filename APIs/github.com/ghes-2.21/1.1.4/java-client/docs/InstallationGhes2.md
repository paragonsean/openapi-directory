

# InstallationGhes2

Installation

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accessTokensUrl** | **URI** |  |  |
|**account** | [**InstallationGhes2Account**](InstallationGhes2Account.md) |  |  |
|**appId** | **Integer** |  |  |
|**appSlug** | **String** |  |  |
|**contactEmail** | **String** |  |  [optional] |
|**createdAt** | **OffsetDateTime** |  |  |
|**events** | **List&lt;String&gt;** |  |  |
|**htmlUrl** | **URI** |  |  |
|**id** | **Integer** | The ID of the installation. |  |
|**permissions** | [**InstallationGhes2Permissions**](InstallationGhes2Permissions.md) |  |  |
|**repositoriesUrl** | **URI** |  |  |
|**repositorySelection** | [**RepositorySelectionEnum**](#RepositorySelectionEnum) | Describe whether all repositories have been selected or there&#39;s a selection involved |  |
|**singleFileName** | **String** |  |  |
|**suspendedAt** | **OffsetDateTime** |  |  [optional] |
|**suspendedBy** | [**NullableSimpleUser**](NullableSimpleUser.md) |  |  [optional] |
|**targetId** | **Integer** | The ID of the user or organization this token is being scoped to. |  |
|**targetType** | **String** |  |  |
|**updatedAt** | **OffsetDateTime** |  |  |



## Enum: RepositorySelectionEnum

| Name | Value |
|---- | -----|
| ALL | &quot;all&quot; |
| SELECTED | &quot;selected&quot; |



