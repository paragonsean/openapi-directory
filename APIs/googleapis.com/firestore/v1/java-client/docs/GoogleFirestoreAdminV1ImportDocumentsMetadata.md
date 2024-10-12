

# GoogleFirestoreAdminV1ImportDocumentsMetadata

Metadata for google.longrunning.Operation results from FirestoreAdmin.ImportDocuments.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**collectionIds** | **List&lt;String&gt;** | Which collection ids are being imported. |  [optional] |
|**endTime** | **String** | The time this operation completed. Will be unset if operation still in progress. |  [optional] |
|**inputUriPrefix** | **String** | The location of the documents being imported. |  [optional] |
|**namespaceIds** | **List&lt;String&gt;** | Which namespace ids are being imported. |  [optional] |
|**operationState** | [**OperationStateEnum**](#OperationStateEnum) | The state of the import operation. |  [optional] |
|**progressBytes** | [**GoogleFirestoreAdminV1Progress**](GoogleFirestoreAdminV1Progress.md) |  |  [optional] |
|**progressDocuments** | [**GoogleFirestoreAdminV1Progress**](GoogleFirestoreAdminV1Progress.md) |  |  [optional] |
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



