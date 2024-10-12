

# CheckBase


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | **OffsetDateTime** |  |  [optional] [readonly] |
|**description** | **String** | An optional description of the check. |  [optional] |
|**id** | **String** |  |  [optional] [readonly] |
|**labels** | [**List&lt;Label&gt;**](Label.md) |  |  [optional] |
|**lastRunError** | **String** |  |  [optional] [readonly] |
|**lastRunStatus** | [**LastRunStatusEnum**](#LastRunStatusEnum) |  |  [optional] [readonly] |
|**latestCompleted** | **OffsetDateTime** | Timestamp of latest scheduled, completed run, RFC3339. |  [optional] [readonly] |
|**links** | [**CheckBaseLinks**](CheckBaseLinks.md) |  |  [optional] |
|**name** | **String** |  |  |
|**orgID** | **String** | The ID of the organization that owns this check. |  |
|**ownerID** | **String** | The ID of creator used to create this check. |  [optional] [readonly] |
|**query** | [**DashboardQuery**](DashboardQuery.md) |  |  |
|**status** | **TaskStatusType** |  |  [optional] |
|**taskID** | **String** | The ID of the task associated with this check. |  [optional] |
|**updatedAt** | **OffsetDateTime** |  |  [optional] [readonly] |



## Enum: LastRunStatusEnum

| Name | Value |
|---- | -----|
| FAILED | &quot;failed&quot; |
| SUCCESS | &quot;success&quot; |
| CANCELED | &quot;canceled&quot; |



