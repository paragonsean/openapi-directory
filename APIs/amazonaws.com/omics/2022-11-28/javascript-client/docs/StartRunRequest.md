# AmazonOmics.StartRunRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflowId** | **String** | The run&#39;s workflow ID. | [optional] 
**workflowType** | **String** | The run&#39;s workflows type. | [optional] 
**runId** | **String** | The run&#39;s ID. | [optional] 
**roleArn** | **String** | A service role for the run. | 
**name** | **String** | A name for the run. | [optional] 
**runGroupId** | **String** | The run&#39;s group ID. | [optional] 
**priority** | **Number** | A priority for the run. | [optional] 
**parameters** | **Object** | Parameters for the run. | [optional] 
**storageCapacity** | **Number** | A storage capacity for the run in gigabytes. | [optional] 
**outputUri** | **String** | An output URI for the run. | [optional] 
**logLevel** | **String** | A log level for the run. | [optional] 
**tags** | **{String: String}** | Tags for the run. | [optional] 
**requestId** | **String** | To ensure that requests don&#39;t run multiple times, specify a unique ID for each request. | 



## Enum: WorkflowTypeEnum


* `PRIVATE` (value: `"PRIVATE"`)

* `READY2RUN` (value: `"READY2RUN"`)





## Enum: LogLevelEnum


* `OFF` (value: `"OFF"`)

* `FATAL` (value: `"FATAL"`)

* `ERROR` (value: `"ERROR"`)

* `ALL` (value: `"ALL"`)




