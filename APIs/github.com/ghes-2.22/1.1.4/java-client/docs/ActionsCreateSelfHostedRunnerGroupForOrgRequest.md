

# ActionsCreateSelfHostedRunnerGroupForOrgRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | Name of the runner group. |  |
|**runners** | **List&lt;Integer&gt;** | List of runner IDs to add to the runner group. |  [optional] |
|**selectedRepositoryIds** | **List&lt;Integer&gt;** | List of repository IDs that can access the runner group. |  [optional] |
|**visibility** | [**VisibilityEnum**](#VisibilityEnum) | Visibility of a runner group. You can select all repositories, select individual repositories, or limit access to private repositories. Can be one of: &#x60;all&#x60;, &#x60;selected&#x60;, or &#x60;private&#x60;. |  [optional] |



## Enum: VisibilityEnum

| Name | Value |
|---- | -----|
| SELECTED | &quot;selected&quot; |
| ALL | &quot;all&quot; |
| PRIVATE | &quot;private&quot; |



