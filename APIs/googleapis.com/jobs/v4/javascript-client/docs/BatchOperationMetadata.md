# CloudTalentSolutionApi.BatchOperationMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | The time when the batch operation is created. | [optional] 
**endTime** | **String** | The time when the batch operation is finished and google.longrunning.Operation.done is set to &#x60;true&#x60;. | [optional] 
**failureCount** | **Number** | Count of failed item(s) inside an operation. | [optional] 
**state** | **String** | The state of a long running operation. | [optional] 
**stateDescription** | **String** | More detailed information about operation state. | [optional] 
**successCount** | **Number** | Count of successful item(s) inside an operation. | [optional] 
**totalCount** | **Number** | Count of total item(s) inside an operation. | [optional] 
**updateTime** | **String** | The time when the batch operation status is updated. The metadata and the update_time is refreshed every minute otherwise cached data is returned. | [optional] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `INITIALIZING` (value: `"INITIALIZING"`)

* `PROCESSING` (value: `"PROCESSING"`)

* `SUCCEEDED` (value: `"SUCCEEDED"`)

* `FAILED` (value: `"FAILED"`)

* `CANCELLING` (value: `"CANCELLING"`)

* `CANCELLED` (value: `"CANCELLED"`)




