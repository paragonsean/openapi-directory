

# GoogleCloudDatapipelinesV1Job

Definition of the job information maintained by the pipeline. Fields in this entity are retrieved from the executor API (e.g. Dataflow API).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Output only. The time of job creation. |  [optional] [readonly] |
|**dataflowJobDetails** | [**GoogleCloudDatapipelinesV1DataflowJobDetails**](GoogleCloudDatapipelinesV1DataflowJobDetails.md) |  |  [optional] |
|**endTime** | **String** | Output only. The time of job termination. This is absent if the job is still running. |  [optional] [readonly] |
|**id** | **String** | Output only. The internal ID for the job. |  [optional] [readonly] |
|**name** | **String** | Required. The fully qualified resource name for the job. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | The current state of the job. |  [optional] |
|**status** | [**GoogleRpcStatus**](GoogleRpcStatus.md) |  |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| PENDING | &quot;STATE_PENDING&quot; |
| RUNNING | &quot;STATE_RUNNING&quot; |
| DONE | &quot;STATE_DONE&quot; |
| FAILED | &quot;STATE_FAILED&quot; |
| CANCELLED | &quot;STATE_CANCELLED&quot; |



