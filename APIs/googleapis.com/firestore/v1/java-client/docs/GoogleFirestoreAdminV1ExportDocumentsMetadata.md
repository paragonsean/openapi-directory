

# GoogleFirestoreAdminV1ExportDocumentsMetadata

Metadata for google.longrunning.Operation results from FirestoreAdmin.ExportDocuments.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**collectionIds** | **List&lt;String&gt;** | Which collection ids are being exported. |  [optional] |
|**endTime** | **String** | The time this operation completed. Will be unset if operation still in progress. |  [optional] |
|**namespaceIds** | **List&lt;String&gt;** | Which namespace ids are being exported. |  [optional] |
|**operationState** | [**OperationStateEnum**](#OperationStateEnum) | The state of the export operation. |  [optional] |
|**outputUriPrefix** | **String** | Where the documents are being exported to. |  [optional] |
|**progressBytes** | [**GoogleFirestoreAdminV1Progress**](GoogleFirestoreAdminV1Progress.md) |  |  [optional] |
|**progressDocuments** | [**GoogleFirestoreAdminV1Progress**](GoogleFirestoreAdminV1Progress.md) |  |  [optional] |
|**snapshotTime** | **String** | The timestamp that corresponds to the version of the database that is being exported. If unspecified, there are no guarantees about the consistency of the documents being exported. |  [optional] |
|**startTime** | **String** | The time this operation started. |  [optional] |



## Enum: OperationStateEnum

| Name | Value |
|---- | -----|
| OPERATION_STATE_UNSPECIFIED | &quot;OPERATION_STATE_UNSPECIFIED&quot; |
| INITIALIZING | &quot;INITIALIZING&quot; |
| PROCESSING | &quot;PROCESSING&quot; |
| CANCELLING | &quot;CANCELLING&quot; |
| FINALIZING | &quot;FINALIZING&quot; |
| SUCCESSFUL | &quot;SUCCESSFUL&quot; |
| FAILED | &quot;FAILED&quot; |
| CANCELLED | &quot;CANCELLED&quot; |



