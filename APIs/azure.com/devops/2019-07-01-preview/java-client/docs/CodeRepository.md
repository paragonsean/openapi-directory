

# CodeRepository

Repository containing the source code for a pipeline.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authorization** | [**Authorization**](Authorization.md) |  |  [optional] |
|**defaultBranch** | **String** | Default branch used to configure Continuous Integration (CI) in the pipeline. |  |
|**id** | **String** | Unique immutable identifier of the code repository. |  |
|**properties** | **Map&lt;String, String&gt;** | Repository-specific properties. |  [optional] |
|**repositoryType** | [**RepositoryTypeEnum**](#RepositoryTypeEnum) | Type of code repository. |  |



## Enum: RepositoryTypeEnum

| Name | Value |
|---- | -----|
| GIT_HUB | &quot;gitHub&quot; |
| VSTS_GIT | &quot;vstsGit&quot; |



