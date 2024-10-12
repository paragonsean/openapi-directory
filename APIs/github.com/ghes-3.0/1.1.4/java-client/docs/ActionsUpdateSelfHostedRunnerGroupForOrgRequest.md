

# ActionsUpdateSelfHostedRunnerGroupForOrgRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowsPublicRepositories** | **Boolean** | Whether the runner group can be used by &#x60;public&#x60; repositories. |  [optional] |
|**name** | **String** | Name of the runner group. |  |
|**visibility** | [**VisibilityEnum**](#VisibilityEnum) | Visibility of a runner group. You can select all repositories, select individual repositories, or all private repositories. Can be one of: &#x60;all&#x60;, &#x60;selected&#x60;, or &#x60;private&#x60;. |  [optional] |



## Enum: VisibilityEnum

| Name | Value |
|---- | -----|
| SELECTED | &quot;selected&quot; |
| ALL | &quot;all&quot; |
| PRIVATE | &quot;private&quot; |



