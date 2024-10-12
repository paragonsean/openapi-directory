# YouTubeDataApiV3.VideoFileDetailsVideoStream

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aspectRatio** | **Number** | The video content&#39;s display aspect ratio, which specifies the aspect ratio in which the video should be displayed. | [optional] 
**bitrateBps** | **String** | The video stream&#39;s bitrate, in bits per second. | [optional] 
**codec** | **String** | The video codec that the stream uses. | [optional] 
**frameRateFps** | **Number** | The video stream&#39;s frame rate, in frames per second. | [optional] 
**heightPixels** | **Number** | The encoded video content&#39;s height in pixels. | [optional] 
**rotation** | **String** | The amount that YouTube needs to rotate the original source content to properly display the video. | [optional] 
**vendor** | **String** | A value that uniquely identifies a video vendor. Typically, the value is a four-letter vendor code. | [optional] 
**widthPixels** | **Number** | The encoded video content&#39;s width in pixels. You can calculate the video&#39;s encoding aspect ratio as width_pixels / height_pixels. | [optional] 



## Enum: RotationEnum


* `none` (value: `"none"`)

* `clockwise` (value: `"clockwise"`)

* `upsideDown` (value: `"upsideDown"`)

* `counterClockwise` (value: `"counterClockwise"`)

* `other` (value: `"other"`)




