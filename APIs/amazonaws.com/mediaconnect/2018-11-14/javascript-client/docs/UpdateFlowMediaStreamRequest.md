# AwsMediaConnect.UpdateFlowMediaStreamRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**UpdateFlowMediaStreamRequestAttributes**](UpdateFlowMediaStreamRequestAttributes.md) |  | [optional] 
**clockRate** | **Number** | The sample rate (in Hz) for the stream. If the media stream type is video or ancillary data, set this value to 90000. If the media stream type is audio, set this value to either 48000 or 96000. | [optional] 
**description** | **String** | Description | [optional] 
**mediaStreamType** | **String** | The type of media stream. | [optional] 
**videoFormat** | **String** | The resolution of the video. | [optional] 



## Enum: MediaStreamTypeEnum


* `video` (value: `"video"`)

* `audio` (value: `"audio"`)

* `ancillary-data` (value: `"ancillary-data"`)




