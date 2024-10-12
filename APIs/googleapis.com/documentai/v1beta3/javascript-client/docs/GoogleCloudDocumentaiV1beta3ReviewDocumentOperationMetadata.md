# CloudDocumentAiApi.GoogleCloudDocumentaiV1beta3ReviewDocumentOperationMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commonMetadata** | [**GoogleCloudDocumentaiV1beta3CommonOperationMetadata**](GoogleCloudDocumentaiV1beta3CommonOperationMetadata.md) |  | [optional] 
**createTime** | **String** | The creation time of the operation. | [optional] 
**questionId** | **String** | The Crowd Compute question ID. | [optional] 
**state** | **String** | Used only when Operation.done is false. | [optional] 
**stateMessage** | **String** | A message providing more details about the current state of processing. For example, the error message if the operation is failed. | [optional] 
**updateTime** | **String** | The last update time of the operation. | [optional] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `RUNNING` (value: `"RUNNING"`)

* `CANCELLING` (value: `"CANCELLING"`)

* `SUCCEEDED` (value: `"SUCCEEDED"`)

* `FAILED` (value: `"FAILED"`)

* `CANCELLED` (value: `"CANCELLED"`)




