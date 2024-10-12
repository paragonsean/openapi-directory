# CloudFirestoreApi.GoogleFirestoreAdminV1ImportDocumentsMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collectionIds** | **[String]** | Which collection ids are being imported. | [optional] 
**endTime** | **String** | The time this operation completed. Will be unset if operation still in progress. | [optional] 
**inputUriPrefix** | **String** | The location of the documents being imported. | [optional] 
**namespaceIds** | **[String]** | Which namespace ids are being imported. | [optional] 
**operationState** | **String** | The state of the import operation. | [optional] 
**progressBytes** | [**GoogleFirestoreAdminV1Progress**](GoogleFirestoreAdminV1Progress.md) |  | [optional] 
**progressDocuments** | [**GoogleFirestoreAdminV1Progress**](GoogleFirestoreAdminV1Progress.md) |  | [optional] 
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




