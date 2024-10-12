

# SourceUpdateParameters

The properties for updating the source code repository.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**branch** | **String** | The branch name of the source code. |  [optional] |
|**repositoryUrl** | **String** | The full URL to the source code repository |  [optional] |
|**sourceControlAuthProperties** | [**AuthInfoUpdateParameters**](AuthInfoUpdateParameters.md) |  |  [optional] |
|**sourceControlType** | [**SourceControlTypeEnum**](#SourceControlTypeEnum) | The type of source control service. |  [optional] |



## Enum: SourceControlTypeEnum

| Name | Value |
|---- | -----|
| GITHUB | &quot;Github&quot; |
| VISUAL_STUDIO_TEAM_SERVICE | &quot;VisualStudioTeamService&quot; |



