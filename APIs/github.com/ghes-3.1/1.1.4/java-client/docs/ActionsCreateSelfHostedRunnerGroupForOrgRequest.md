

# ActionsCreateSelfHostedRunnerGroupForOrgRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowsPublicRepositories** | **Boolean** | Whether the runner group can be used by &#x60;public&#x60; repositories. |  [optional] |
|**name** | **String** | Name of the runner group. |  |
|**runners** | **List&lt;Integer&gt;** | List of runner IDs to add to the runner group. |  [optional] |
|**selectedRepositoryIds** | **List&lt;Integer&gt;** | List of repository IDs that can access the runner group. |  [optional] |
|**visibility** | [**VisibilityEnum**](#VisibilityEnum) | Visibility of a runner group. You can select all repositories, select individual repositories, or limit access to private repositories. |  [optional] |



## Enum: VisibilityEnum

| Name | Value |
|---- | -----|
| SELECTED | &quot;selected&quot; |
| ALL | &quot;all&quot; |
| PRIVATE | &quot;private&quot; |



