

# BatchUpdatePresentationResponse

Response message from a batch update.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**presentationId** | **String** | The presentation the updates were applied to. |  [optional] |
|**replies** | [**List&lt;Response&gt;**](Response.md) | The reply of the updates. This maps 1:1 with the updates, although replies to some requests may be empty. |  [optional] |
|**writeControl** | [**WriteControl**](WriteControl.md) |  |  [optional] |



