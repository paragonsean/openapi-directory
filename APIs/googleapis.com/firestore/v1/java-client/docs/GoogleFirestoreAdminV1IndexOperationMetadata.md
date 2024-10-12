

# GoogleFirestoreAdminV1IndexOperationMetadata

Metadata for google.longrunning.Operation results from FirestoreAdmin.CreateIndex.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endTime** | **String** | The time this operation completed. Will be unset if operation still in progress. |  [optional] |
|**index** | **String** | The index resource that this operation is acting on. For example: &#x60;projects/{project_id}/databases/{database_id}/collectionGroups/{collection_id}/indexes/{index_id}&#x60; |  [optional] |
|**progressBytes** | [**GoogleFirestoreAdminV1Progress**](GoogleFirestoreAdminV1Progress.md) |  |  [optional] |
|**progressDocuments** | [**GoogleFirestoreAdminV1Progress**](GoogleFirestoreAdminV1Progress.md) |  |  [optional] |
|**startTime** | **String** | The time this operation started. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | The state of the operation. |  [optional] |



## Enum: StateEnum

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



