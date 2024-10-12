# CloudFirestoreApi.GoogleFirestoreAdminV1FieldOperationMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endTime** | **String** | The time this operation completed. Will be unset if operation still in progress. | [optional] 
**field** | **String** | The field resource that this operation is acting on. For example: &#x60;projects/{project_id}/databases/{database_id}/collectionGroups/{collection_id}/fields/{field_path}&#x60; | [optional] 
**indexConfigDeltas** | [**[GoogleFirestoreAdminV1IndexConfigDelta]**](GoogleFirestoreAdminV1IndexConfigDelta.md) | A list of IndexConfigDelta, which describe the intent of this operation. | [optional] 
**progressBytes** | [**GoogleFirestoreAdminV1Progress**](GoogleFirestoreAdminV1Progress.md) |  | [optional] 
**progressDocuments** | [**GoogleFirestoreAdminV1Progress**](GoogleFirestoreAdminV1Progress.md) |  | [optional] 
**startTime** | **String** | The time this operation started. | [optional] 
**state** | **String** | The state of the operation. | [optional] 
**ttlConfigDelta** | [**GoogleFirestoreAdminV1TtlConfigDelta**](GoogleFirestoreAdminV1TtlConfigDelta.md) |  | [optional] 



## Enum: StateEnum


* `OPERATION_STATE_UNSPECIFIED` (value: `"OPERATION_STATE_UNSPECIFIED"`)

* `INITIALIZING` (value: `"INITIALIZING"`)

* `PROCESSING` (value: `"PROCESSING"`)

* `CANCELLING` (value: `"CANCELLING"`)

* `FINALIZING` (value: `"FINALIZING"`)

* `SUCCESSFUL` (value: `"SUCCESSFUL"`)

* `FAILED` (value: `"FAILED"`)

* `CANCELLED` (value: `"CANCELLED"`)




