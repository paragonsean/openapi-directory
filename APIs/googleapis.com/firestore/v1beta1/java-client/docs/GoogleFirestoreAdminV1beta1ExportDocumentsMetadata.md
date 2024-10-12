

# GoogleFirestoreAdminV1beta1ExportDocumentsMetadata

Metadata for ExportDocuments operations.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**collectionIds** | **List&lt;String&gt;** | Which collection ids are being exported. |  [optional] |
|**endTime** | **String** | The time the operation ended, either successfully or otherwise. Unset if the operation is still active. |  [optional] |
|**operationState** | [**OperationStateEnum**](#OperationStateEnum) | The state of the export operation. |  [optional] |
|**outputUriPrefix** | **String** | Where the entities are being exported to. |  [optional] |
|**progressBytes** | [**GoogleFirestoreAdminV1beta1Progress**](GoogleFirestoreAdminV1beta1Progress.md) |  |  [optional] |
|**progressDocuments** | [**GoogleFirestoreAdminV1beta1Progress**](GoogleFirestoreAdminV1beta1Progress.md) |  |  [optional] |
|**startTime** | **String** | The time that work began on the operation. |  [optional] |



## Enum: OperationStateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| INITIALIZING | &quot;INITIALIZING&quot; |
| PROCESSING | &quot;PROCESSING&quot; |
| CANCELLING | &quot;CANCELLING&quot; |
| FINALIZING | &quot;FINALIZING&quot; |
| SUCCESSFUL | &quot;SUCCESSFUL&quot; |
| FAILED | &quot;FAILED&quot; |
| CANCELLED | &quot;CANCELLED&quot; |



