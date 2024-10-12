

# SourceRepositoryProperties

The properties of the source code repository.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**isCommitTriggerEnabled** | **Boolean** | The value of this property indicates whether the source control commit trigger is enabled or not. |  [optional] |
|**repositoryUrl** | **String** | The full URL to the source code repository |  |
|**sourceControlAuthProperties** | [**SourceControlAuthInfo**](SourceControlAuthInfo.md) |  |  [optional] |
|**sourceControlType** | [**SourceControlTypeEnum**](#SourceControlTypeEnum) | The type of source control service. |  |



## Enum: SourceControlTypeEnum

| Name | Value |
|---- | -----|
| GITHUB | &quot;Github&quot; |
| VISUAL_STUDIO_TEAM_SERVICE | &quot;VisualStudioTeamService&quot; |



