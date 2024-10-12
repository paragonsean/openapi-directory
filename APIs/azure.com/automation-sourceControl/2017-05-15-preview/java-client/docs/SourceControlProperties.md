

# SourceControlProperties

Definition of the source control properties

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**autoSync** | **Boolean** | The auto sync of the source control. Default is false. |  [optional] |
|**branch** | **String** | The repo branch of the source control. Include branch as empty string for VsoTfvc. |  [optional] |
|**creationTime** | **OffsetDateTime** | The creation time. |  [optional] |
|**description** | **String** | The description. |  [optional] |
|**folderPath** | **String** | The folder path of the source control. |  [optional] |
|**lastModifiedTime** | **OffsetDateTime** | The last modified time. |  [optional] |
|**publishRunbook** | **Boolean** | The auto publish of the source control. Default is true. |  [optional] |
|**repoUrl** | **String** | The repo url of the source control. |  [optional] |
|**sourceType** | [**SourceTypeEnum**](#SourceTypeEnum) | The source type. Must be one of VsoGit, VsoTfvc, GitHub. |  [optional] |



## Enum: SourceTypeEnum

| Name | Value |
|---- | -----|
| VSO_GIT | &quot;VsoGit&quot; |
| VSO_TFVC | &quot;VsoTfvc&quot; |
| GIT_HUB | &quot;GitHub&quot; |



