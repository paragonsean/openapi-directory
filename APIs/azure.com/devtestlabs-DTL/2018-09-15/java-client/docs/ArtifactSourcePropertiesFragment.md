

# ArtifactSourcePropertiesFragment

Properties of an artifact source.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**armTemplateFolderPath** | **String** | The folder containing Azure Resource Manager templates. |  [optional] |
|**branchRef** | **String** | The artifact source&#39;s branch reference. |  [optional] |
|**displayName** | **String** | The artifact source&#39;s display name. |  [optional] |
|**folderPath** | **String** | The folder containing artifacts. |  [optional] |
|**securityToken** | **String** | The security token to authenticate to the artifact source. |  [optional] |
|**sourceType** | [**SourceTypeEnum**](#SourceTypeEnum) | The artifact source&#39;s type. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Indicates if the artifact source is enabled (values: Enabled, Disabled). |  [optional] |
|**uri** | **String** | The artifact source&#39;s URI. |  [optional] |



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



