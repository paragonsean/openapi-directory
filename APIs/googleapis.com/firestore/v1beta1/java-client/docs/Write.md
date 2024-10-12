

# Write

A write on a document.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**currentDocument** | [**Precondition**](Precondition.md) |  |  [optional] |
|**delete** | **String** | A document name to delete. In the format: &#x60;projects/{project_id}/databases/{database_id}/documents/{document_path}&#x60;. |  [optional] |
|**transform** | [**DocumentTransform**](DocumentTransform.md) |  |  [optional] |
|**update** | [**Document**](Document.md) |  |  [optional] |
|**updateMask** | [**DocumentMask**](DocumentMask.md) |  |  [optional] |
|**updateTransforms** | [**List&lt;FieldTransform&gt;**](FieldTransform.md) | The transforms to perform after update. This field can be set only when the operation is &#x60;update&#x60;. If present, this write is equivalent to performing &#x60;update&#x60; and &#x60;transform&#x60; to the same document atomically and in order. |  [optional] |



