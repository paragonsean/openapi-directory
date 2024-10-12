# CloudFirestoreApi.GoogleFirestoreAdminV1beta1ImportDocumentsMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collectionIds** | **[String]** | Which collection ids are being imported. | [optional] 
**endTime** | **String** | The time the operation ended, either successfully or otherwise. Unset if the operation is still active. | [optional] 
**inputUriPrefix** | **String** | The location of the documents being imported. | [optional] 
**operationState** | **String** | The state of the import operation. | [optional] 
**progressBytes** | [**GoogleFirestoreAdminV1beta1Progress**](GoogleFirestoreAdminV1beta1Progress.md) |  | [optional] 
**progressDocuments** | [**GoogleFirestoreAdminV1beta1Progress**](GoogleFirestoreAdminV1beta1Progress.md) |  | [optional] 
**startTime** | **String** | The time that work began on the operation. | [optional] 



## Enum: OperationStateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `INITIALIZING` (value: `"INITIALIZING"`)

* `PROCESSING` (value: `"PROCESSING"`)

* `CANCELLING` (value: `"CANCELLING"`)

* `FINALIZING` (value: `"FINALIZING"`)

* `SUCCESSFUL` (value: `"SUCCESSFUL"`)

* `FAILED` (value: `"FAILED"`)

* `CANCELLED` (value: `"CANCELLED"`)




