

# ArtifactSourceProperties

Properties of an artifact source.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**branchRef** | **String** | The branch reference of the artifact source. |  [optional] |
|**displayName** | **String** | The display name of the artifact source. |  [optional] |
|**folderPath** | **String** | The folder path of the artifact source. |  [optional] |
|**provisioningState** | **String** | The provisioning status of the resource. |  [optional] |
|**securityToken** | **String** | The security token of the artifact source. |  [optional] |
|**sourceType** | [**SourceTypeEnum**](#SourceTypeEnum) | The type of the artifact source. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the artifact source. |  [optional] |
|**uri** | **String** | The URI of the artifact source. |  [optional] |



## Enum: SourceTypeEnum

| Name | Value |
|---- | -----|
| VSO_GIT | &quot;VsoGit&quot; |
| GIT_HUB | &quot;GitHub&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;Enabled&quot; |
| DISABLED | &quot;Disabled&quot; |



