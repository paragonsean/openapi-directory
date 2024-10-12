

# VideoLayer

Describes the settings to be used when encoding the input video into a desired output bitrate layer.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adaptiveBFrame** | **Boolean** | Whether or not adaptive B-frames are to be used when encoding this layer. If not specified, the encoder will turn it on whenever the video profile permits its use. |  [optional] |
|**bFrames** | **Integer** | The number of B-frames to be used when encoding this layer.  If not specified, the encoder chooses an appropriate number based on the video profile and level. |  [optional] |
|**bitrate** | **Integer** | The average bitrate in bits per second at which to encode the input video when generating this layer. This is a required field. |  |
|**frameRate** | **String** | The frame rate (in frames per second) at which to encode this layer. The value can be in the form of M/N where M and N are integers (For example, 30000/1001), or in the form of a number (For example, 30, or 29.97). The encoder enforces constraints on allowed frame rates based on the profile and level. If it is not specified, the encoder will use the same frame rate as the input video. |  [optional] |
|**maxBitrate** | **Integer** | The maximum bitrate (in bits per second), at which the VBV buffer should be assumed to refill. If not specified, defaults to the same value as bitrate. |  [optional] |
|**slices** | **Integer** | The number of slices to be used when encoding this layer. If not specified, default is zero, which means that encoder will use a single slice for each frame. |  [optional] |



