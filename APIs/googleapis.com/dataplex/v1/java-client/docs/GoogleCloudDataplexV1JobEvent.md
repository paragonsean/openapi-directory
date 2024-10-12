

# GoogleCloudDataplexV1JobEvent

The payload associated with Job logs that contains events describing jobs that have run within a Lake.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endTime** | **String** | The time when the job ended running. |  [optional] |
|**executionTrigger** | [**ExecutionTriggerEnum**](#ExecutionTriggerEnum) | Job execution trigger. |  [optional] |
|**jobId** | **String** | The unique id identifying the job. |  [optional] |
|**message** | **String** | The log message. |  [optional] |
|**retries** | **Integer** | The number of retries. |  [optional] |
|**service** | [**ServiceEnum**](#ServiceEnum) | The service used to execute the job. |  [optional] |
|**serviceJob** | **String** | The reference to the job within the service. |  [optional] |
|**startTime** | **String** | The time when the job started running. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | The job state on completion. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of the job. |  [optional] |



## Enum: ExecutionTriggerEnum

| Name | Value |
|---- | -----|
| EXECUTION_TRIGGER_UNSPECIFIED | &quot;EXECUTION_TRIGGER_UNSPECIFIED&quot; |
| TASK_CONFIG | &quot;TASK_CONFIG&quot; |
| RUN_REQUEST | &quot;RUN_REQUEST&quot; |



## Enum: ServiceEnum

| Name | Value |
|---- | -----|
| SERVICE_UNSPECIFIED | &quot;SERVICE_UNSPECIFIED&quot; |
| DATAPROC | &quot;DATAPROC&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| SUCCEEDED | &quot;SUCCEEDED&quot; |
| FAILED | &quot;FAILED&quot; |
| CANCELLED | &quot;CANCELLED&quot; |
| ABORTED | &quot;ABORTED&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;TYPE_UNSPECIFIED&quot; |
| SPARK | &quot;SPARK&quot; |
| NOTEBOOK | &quot;NOTEBOOK&quot; |



