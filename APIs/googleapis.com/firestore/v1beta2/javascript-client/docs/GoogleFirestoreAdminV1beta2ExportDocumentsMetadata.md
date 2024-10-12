# CloudFirestoreApi.GoogleFirestoreAdminV1beta2ExportDocumentsMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collectionIds** | **[String]** | Which collection ids are being exported. | [optional] 
**endTime** | **String** | The time this operation completed. Will be unset if operation still in progress. | [optional] 
**operationState** | **String** | The state of the export operation. | [optional] 
**outputUriPrefix** | **String** | Where the entities are being exported to. | [optional] 
**progressBytes** | [**GoogleFirestoreAdminV1beta2Progress**](GoogleFirestoreAdminV1beta2Progress.md) |  | [optional] 
**progressDocuments** | [**GoogleFirestoreAdminV1beta2Progress**](GoogleFirestoreAdminV1beta2Progress.md) |  | [optional] 
**startTime** | **String** | The time this operation started. | [optional] 



## Enum: OperationStateEnum


* `OPERATION_STATE_UNSPECIFIED` (value: `"OPERATION_STATE_UNSPECIFIED"`)

* `INITIALIZING` (value: `"INITIALIZING"`)

* `PROCESSING` (value: `"PROCESSING"`)

* `CANCELLING` (value: `"CANCELLING"`)

* `FINALIZING` (value: `"FINALIZING"`)

* `SUCCESSFUL` (value: `"SUCCESSFUL"`)

* `FAILED` (value: `"FAILED"`)

* `CANCELLED` (value: `"CANCELLED"`)




