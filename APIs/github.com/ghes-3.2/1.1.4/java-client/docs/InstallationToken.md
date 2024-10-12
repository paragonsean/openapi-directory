

# InstallationToken

Authentication token for a GitHub App installed on a user or org.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**expiresAt** | **String** |  |  |
|**hasMultipleSingleFiles** | **Boolean** |  |  [optional] |
|**permissions** | [**AppPermissions**](AppPermissions.md) |  |  [optional] |
|**repositories** | [**List&lt;Repository&gt;**](Repository.md) |  |  [optional] |
|**repositorySelection** | [**RepositorySelectionEnum**](#RepositorySelectionEnum) |  |  [optional] |
|**singleFile** | **String** |  |  [optional] |
|**singleFilePaths** | **List&lt;String&gt;** |  |  [optional] |
|**token** | **String** |  |  |



## Enum: RepositorySelectionEnum

| Name | Value |
|---- | -----|
| ALL | &quot;all&quot; |
| SELECTED | &quot;selected&quot; |



