

# Overlay

Base type for all overlays - image, audio or video.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**atOdataType** | **String** | The discriminator for derived types. |  |
|**audioGainLevel** | **Double** | The gain level of audio in the overlay. The value should be in the range [0, 1.0]. The default is 1.0. |  [optional] |
|**end** | **String** | The position in the input video at which the overlay ends. The value should be in ISO 8601 duration format. For example, PT30S to end the overlay at 30 seconds in to the input video. If not specified the overlay will be applied until the end of the input video if inputLoop is true. Else, if inputLoop is false, then overlay will last as long as the duration of the overlay media. |  [optional] |
|**fadeInDuration** | **String** | The duration over which the overlay fades in onto the input video. The value should be in ISO 8601 duration format. If not specified the default behavior is to have no fade in (same as PT0S). |  [optional] |
|**fadeOutDuration** | **String** | The duration over which the overlay fades out of the input video. The value should be in ISO 8601 duration format. If not specified the default behavior is to have no fade out (same as PT0S). |  [optional] |
|**inputLabel** | **String** | The label of the job input which is to be used as an overlay. The Input must specify exactly one file. You can specify an image file in JPG or PNG formats, or an audio file (such as a WAV, MP3, WMA or M4A file), or a video file. See https://aka.ms/mesformats for the complete list of supported audio and video file formats. |  |
|**start** | **String** | The start position, with reference to the input video, at which the overlay starts. The value should be in ISO 8601 format. For example, PT05S to start the overlay at 5 seconds in to the input video. If not specified the overlay starts from the beginning of the input video. |  [optional] |



