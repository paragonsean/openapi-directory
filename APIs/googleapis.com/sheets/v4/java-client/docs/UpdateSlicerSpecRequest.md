

# UpdateSlicerSpecRequest

Updates a slicer's specifications. (This does not move or resize a slicer. To move or resize a slicer use UpdateEmbeddedObjectPositionRequest.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fields** | **String** | The fields that should be updated. At least one field must be specified. The root &#x60;SlicerSpec&#x60; is implied and should not be specified. A single \&quot;*\&quot;&#x60; can be used as short-hand for listing every field. |  [optional] |
|**slicerId** | **Integer** | The id of the slicer to update. |  [optional] |
|**spec** | [**SlicerSpec**](SlicerSpec.md) |  |  [optional] |



