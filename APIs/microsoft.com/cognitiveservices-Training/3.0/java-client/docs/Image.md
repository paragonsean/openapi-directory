

# Image

Image model to be sent as JSON.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**created** | **OffsetDateTime** | Date the image was created. |  [optional] [readonly] |
|**height** | **Integer** | Height of the image. |  [optional] [readonly] |
|**id** | **UUID** | Id of the image. |  [optional] [readonly] |
|**originalImageUri** | **String** | The URI to the original uploaded image. |  [optional] [readonly] |
|**regions** | [**List&lt;ImageRegion&gt;**](ImageRegion.md) | Regions associated with this image. |  [optional] [readonly] |
|**resizedImageUri** | **String** | The URI to the (resized) image used for training. |  [optional] [readonly] |
|**tags** | [**List&lt;ImageTag&gt;**](ImageTag.md) | Tags associated with this image. |  [optional] [readonly] |
|**thumbnailUri** | **String** | The URI to the thumbnail of the original image. |  [optional] [readonly] |
|**width** | **Integer** | Width of the image. |  [optional] [readonly] |



