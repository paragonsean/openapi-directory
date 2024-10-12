

# AutomationRunEntity

List Automation Runs

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**automationId** | **Integer** | ID of the associated Automation. |  [optional] |
|**completedAt** | **OffsetDateTime** | Automation run completion/failure date/time. |  [optional] |
|**createdAt** | **OffsetDateTime** | Automation run start date/time. |  [optional] |
|**id** | **Integer** | ID. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The success status of the AutomationRun. One of &#x60;running&#x60;, &#x60;success&#x60;, &#x60;partial_failure&#x60;, or &#x60;failure&#x60;. |  [optional] |
|**statusMessagesUrl** | **String** | Link to status messages log file. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| RUNNING | &quot;running&quot; |
| SUCCESS | &quot;success&quot; |
| PARTIAL_FAILURE | &quot;partial_failure&quot; |
| FAILURE | &quot;failure&quot; |
| SKIPPED | &quot;skipped&quot; |



