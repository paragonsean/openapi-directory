

# Layer

The encoder can be configured to produce video and/or images (thumbnails) at different resolutions, by specifying a layer for each desired resolution. A layer represents the properties for the video or image at a resolution.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**atOdataType** | **String** | The discriminator for derived types. |  |
|**height** | **String** | The height of the output video for this layer. The value can be absolute (in pixels) or relative (in percentage). For example 50% means the output video has half as many pixels in height as the input. |  [optional] |
|**label** | **String** | The alphanumeric label for this layer, which can be used in multiplexing different video and audio layers, or in naming the output file. |  [optional] |
|**width** | **String** | The width of the output video for this layer. The value can be absolute (in pixels) or relative (in percentage). For example 50% means the output video has half as many pixels in width as the input. |  [optional] |



