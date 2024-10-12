

# EnterpriseAdminCreateSelfHostedRunnerGroupForEnterpriseRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | Name of the runner group. |  |
|**runners** | **List&lt;Integer&gt;** | List of runner IDs to add to the runner group. |  [optional] |
|**selectedOrganizationIds** | **List&lt;Integer&gt;** | List of organization IDs that can access the runner group. |  [optional] |
|**visibility** | [**VisibilityEnum**](#VisibilityEnum) | Visibility of a runner group. You can select all organizations or select individual organization. Can be one of: &#x60;all&#x60; or &#x60;selected&#x60; |  [optional] |



## Enum: VisibilityEnum

| Name | Value |
|---- | -----|
| SELECTED | &quot;selected&quot; |
| ALL | &quot;all&quot; |



