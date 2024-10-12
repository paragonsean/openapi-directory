

# GoogleFirestoreAdminV1beta1IndexOperationMetadata

Metadata for index operations. This metadata populates the metadata field of google.longrunning.Operation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cancelled** | **Boolean** | True if the [google.longrunning.Operation] was cancelled. If the cancellation is in progress, cancelled will be true but google.longrunning.Operation.done will be false. |  [optional] |
|**documentProgress** | [**GoogleFirestoreAdminV1beta1Progress**](GoogleFirestoreAdminV1beta1Progress.md) |  |  [optional] |
|**endTime** | **String** | The time the operation ended, either successfully or otherwise. Unset if the operation is still active. |  [optional] |
|**index** | **String** | The index resource that this operation is acting on. For example: &#x60;projects/{project_id}/databases/{database_id}/indexes/{index_id}&#x60; |  [optional] |
|**operationType** | [**OperationTypeEnum**](#OperationTypeEnum) | The type of index operation. |  [optional] |
|**startTime** | **String** | The time that work began on the operation. |  [optional] |



## Enum: OperationTypeEnum

| Name | Value |
|---- | -----|
| OPERATION_TYPE_UNSPECIFIED | &quot;OPERATION_TYPE_UNSPECIFIED&quot; |
| CREATING_INDEX | &quot;CREATING_INDEX&quot; |



