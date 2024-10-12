# CloudDocumentAiApi.GoogleCloudDocumentaiV1beta3BatchProcessMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | The creation time of the operation. | [optional] 
**individualProcessStatuses** | [**[GoogleCloudDocumentaiV1beta3BatchProcessMetadataIndividualProcessStatus]**](GoogleCloudDocumentaiV1beta3BatchProcessMetadataIndividualProcessStatus.md) | The list of response details of each document. | [optional] 
**state** | **String** | The state of the current batch processing. | [optional] 
**stateMessage** | **String** | A message providing more details about the current state of processing. For example, the error message if the operation is failed. | [optional] 
**updateTime** | **String** | The last update time of the operation. | [optional] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `WAITING` (value: `"WAITING"`)

* `RUNNING` (value: `"RUNNING"`)

* `SUCCEEDED` (value: `"SUCCEEDED"`)

* `CANCELLING` (value: `"CANCELLING"`)

* `CANCELLED` (value: `"CANCELLED"`)

* `FAILED` (value: `"FAILED"`)




