

# ActionsUpdateSelfHostedRunnerGroupForOrgRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowsPublicRepositories** | **Boolean** | Whether the runner group can be used by &#x60;public&#x60; repositories. |  [optional] |
|**name** | **String** | Name of the runner group. |  |
|**visibility** | [**VisibilityEnum**](#VisibilityEnum) | Visibility of a runner group. You can select all repositories, select individual repositories, or all private repositories. |  [optional] |



## Enum: VisibilityEnum

| Name | Value |
|---- | -----|
| SELECTED | &quot;selected&quot; |
| ALL | &quot;all&quot; |
| PRIVATE | &quot;private&quot; |



