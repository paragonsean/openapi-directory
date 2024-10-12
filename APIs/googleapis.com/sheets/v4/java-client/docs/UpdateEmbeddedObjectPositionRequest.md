

# UpdateEmbeddedObjectPositionRequest

Update an embedded object's position (such as a moving or resizing a chart or image).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fields** | **String** | The fields of OverlayPosition that should be updated when setting a new position. Used only if newPosition.overlayPosition is set, in which case at least one field must be specified. The root &#x60;newPosition.overlayPosition&#x60; is implied and should not be specified. A single &#x60;\&quot;*\&quot;&#x60; can be used as short-hand for listing every field. |  [optional] |
|**newPosition** | [**EmbeddedObjectPosition**](EmbeddedObjectPosition.md) |  |  [optional] |
|**objectId** | **Integer** | The ID of the object to moved. |  [optional] |



