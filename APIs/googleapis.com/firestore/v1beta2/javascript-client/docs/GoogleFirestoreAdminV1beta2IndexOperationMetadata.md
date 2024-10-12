# CloudFirestoreApi.GoogleFirestoreAdminV1beta2IndexOperationMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endTime** | **String** | The time this operation completed. Will be unset if operation still in progress. | [optional] 
**index** | **String** | The index resource that this operation is acting on. For example: &#x60;projects/{project_id}/databases/{database_id}/collectionGroups/{collection_id}/indexes/{index_id}&#x60; | [optional] 
**progressBytes** | [**GoogleFirestoreAdminV1beta2Progress**](GoogleFirestoreAdminV1beta2Progress.md) |  | [optional] 
**progressDocuments** | [**GoogleFirestoreAdminV1beta2Progress**](GoogleFirestoreAdminV1beta2Progress.md) |  | [optional] 
**startTime** | **String** | The time this operation started. | [optional] 
**state** | **String** | The state of the operation. | [optional] 



## Enum: StateEnum


* `OPERATION_STATE_UNSPECIFIED` (value: `"OPERATION_STATE_UNSPECIFIED"`)

* `INITIALIZING` (value: `"INITIALIZING"`)

* `PROCESSING` (value: `"PROCESSING"`)

* `CANCELLING` (value: `"CANCELLING"`)

* `FINALIZING` (value: `"FINALIZING"`)

* `SUCCESSFUL` (value: `"SUCCESSFUL"`)

* `FAILED` (value: `"FAILED"`)

* `CANCELLED` (value: `"CANCELLED"`)




