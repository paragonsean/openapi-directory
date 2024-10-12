# DataPipelinesApi.GoogleCloudDatapipelinesV1Job

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. The time of job creation. | [optional] [readonly] 
**dataflowJobDetails** | [**GoogleCloudDatapipelinesV1DataflowJobDetails**](GoogleCloudDatapipelinesV1DataflowJobDetails.md) |  | [optional] 
**endTime** | **String** | Output only. The time of job termination. This is absent if the job is still running. | [optional] [readonly] 
**id** | **String** | Output only. The internal ID for the job. | [optional] [readonly] 
**name** | **String** | Required. The fully qualified resource name for the job. | [optional] 
**state** | **String** | The current state of the job. | [optional] 
**status** | [**GoogleRpcStatus**](GoogleRpcStatus.md) |  | [optional] 



## Enum: StateEnum


* `UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `PENDING` (value: `"STATE_PENDING"`)

* `RUNNING` (value: `"STATE_RUNNING"`)

* `DONE` (value: `"STATE_DONE"`)

* `FAILED` (value: `"STATE_FAILED"`)

* `CANCELLED` (value: `"STATE_CANCELLED"`)




