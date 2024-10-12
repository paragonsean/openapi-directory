

# ListWorkflowsRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**workflowType** | [**WorkflowTypeEnum**](#WorkflowTypeEnum) | The type of workflow. The only supported value is APPFLOW_INTEGRATION. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Status of workflow execution. |  [optional] |
|**queryStartDate** | **OffsetDateTime** | Retrieve workflows started after timestamp. |  [optional] |
|**queryEndDate** | **OffsetDateTime** | Retrieve workflows ended after timestamp. |  [optional] |



## Enum: WorkflowTypeEnum

| Name | Value |
|---- | -----|
| APPFLOW_INTEGRATION | &quot;APPFLOW_INTEGRATION&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| NOT_STARTED | &quot;NOT_STARTED&quot; |
| IN_PROGRESS | &quot;IN_PROGRESS&quot; |
| COMPLETE | &quot;COMPLETE&quot; |
| FAILED | &quot;FAILED&quot; |
| SPLIT | &quot;SPLIT&quot; |
| RETRY | &quot;RETRY&quot; |
| CANCELLED | &quot;CANCELLED&quot; |



