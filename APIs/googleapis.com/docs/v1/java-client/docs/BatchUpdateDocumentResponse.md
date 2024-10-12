

# BatchUpdateDocumentResponse

Response message from a BatchUpdateDocument request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**documentId** | **String** | The ID of the document to which the updates were applied to. |  [optional] |
|**replies** | [**List&lt;Response&gt;**](Response.md) | The reply of the updates. This maps 1:1 with the updates, although replies to some requests may be empty. |  [optional] |
|**writeControl** | [**WriteControl**](WriteControl.md) |  |  [optional] |



