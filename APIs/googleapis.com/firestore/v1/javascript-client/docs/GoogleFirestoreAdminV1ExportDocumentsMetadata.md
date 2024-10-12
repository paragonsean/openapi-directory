# CloudFirestoreApi.GoogleFirestoreAdminV1ExportDocumentsMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collectionIds** | **[String]** | Which collection ids are being exported. | [optional] 
**endTime** | **String** | The time this operation completed. Will be unset if operation still in progress. | [optional] 
**namespaceIds** | **[String]** | Which namespace ids are being exported. | [optional] 
**operationState** | **String** | The state of the export operation. | [optional] 
**outputUriPrefix** | **String** | Where the documents are being exported to. | [optional] 
**progressBytes** | [**GoogleFirestoreAdminV1Progress**](GoogleFirestoreAdminV1Progress.md) |  | [optional] 
**progressDocuments** | [**GoogleFirestoreAdminV1Progress**](GoogleFirestoreAdminV1Progress.md) |  | [optional] 
**snapshotTime** | **String** | The timestamp that corresponds to the version of the database that is being exported. If unspecified, there are no guarantees about the consistency of the documents being exported. | [optional] 
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




