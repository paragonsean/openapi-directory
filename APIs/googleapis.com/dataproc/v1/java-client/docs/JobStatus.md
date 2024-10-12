

# JobStatus

Dataproc job status.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**details** | **String** | Optional. Output only. Job state details, such as an error description if the state is ERROR. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Output only. A state message specifying the overall job state. |  [optional] [readonly] |
|**stateStartTime** | **String** | Output only. The time when this state was entered. |  [optional] [readonly] |
|**substate** | [**SubstateEnum**](#SubstateEnum) | Output only. Additional state information, which includes status reported by the agent. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| PENDING | &quot;PENDING&quot; |
| SETUP_DONE | &quot;SETUP_DONE&quot; |
| RUNNING | &quot;RUNNING&quot; |
| CANCEL_PENDING | &quot;CANCEL_PENDING&quot; |
| CANCEL_STARTED | &quot;CANCEL_STARTED&quot; |
| CANCELLED | &quot;CANCELLED&quot; |
| DONE | &quot;DONE&quot; |
| ERROR | &quot;ERROR&quot; |
| ATTEMPT_FAILURE | &quot;ATTEMPT_FAILURE&quot; |



## Enum: SubstateEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;UNSPECIFIED&quot; |
| SUBMITTED | &quot;SUBMITTED&quot; |
| QUEUED | &quot;QUEUED&quot; |
| STALE_STATUS | &quot;STALE_STATUS&quot; |



