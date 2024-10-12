# LgtmApiSpecification.Operation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **Number** | The identifier for the operation. | [optional] 
**status** | **String** | Status of the operation. | [optional] 
**taskResult** | [**OperationTaskResult**](OperationTaskResult.md) |  | [optional] 
**taskResultUrl** | **String** | The URL for the result of the task. For some operations, included only on completion. | [optional] 
**taskType** | **String** |  | 
**uploads** | [**{String: UploadSession}**](UploadSession.md) |  | [optional] 



## Enum: StatusEnum


* `pending` (value: `"pending"`)

* `done` (value: `"done"`)





## Enum: TaskTypeEnum


* `analysis` (value: `"analysis"`)

* `codereview` (value: `"codereview"`)

* `queryjob` (value: `"queryjob"`)




