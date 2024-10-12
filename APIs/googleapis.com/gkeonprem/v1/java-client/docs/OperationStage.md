

# OperationStage

Information about a particular stage of an operation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endTime** | **String** | Time the stage ended. |  [optional] |
|**metrics** | [**List&lt;Metric&gt;**](Metric.md) | Progress metric bundle. |  [optional] |
|**stage** | [**StageEnum**](#StageEnum) | The high-level stage of the operation. |  [optional] |
|**startTime** | **String** | Time the stage started. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Output only. State of the stage. |  [optional] [readonly] |



## Enum: StageEnum

| Name | Value |
|---- | -----|
| STAGE_UNSPECIFIED | &quot;STAGE_UNSPECIFIED&quot; |
| PREFLIGHT_CHECK | &quot;PREFLIGHT_CHECK&quot; |
| CONFIGURE | &quot;CONFIGURE&quot; |
| DEPLOY | &quot;DEPLOY&quot; |
| HEALTH_CHECK | &quot;HEALTH_CHECK&quot; |
| UPDATE | &quot;UPDATE&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| PENDING | &quot;PENDING&quot; |
| RUNNING | &quot;RUNNING&quot; |
| SUCCEEDED | &quot;SUCCEEDED&quot; |
| FAILED | &quot;FAILED&quot; |



