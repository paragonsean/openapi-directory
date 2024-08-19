# YouTubeDataApiV3.CdnSettings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format** | **String** | The format of the video stream that you are sending to Youtube.  | [optional] 
**frameRate** | **String** | The frame rate of the inbound video data. | [optional] 
**ingestionInfo** | [**IngestionInfo**](IngestionInfo.md) |  | [optional] 
**ingestionType** | **String** |  The method or protocol used to transmit the video stream. | [optional] 
**resolution** | **String** | The resolution of the inbound video data. | [optional] 



## Enum: FrameRateEnum


* `30fps` (value: `"30fps"`)

* `60fps` (value: `"60fps"`)

* `variable` (value: `"variable"`)





## Enum: IngestionTypeEnum


* `rtmp` (value: `"rtmp"`)

* `dash` (value: `"dash"`)

* `webrtc` (value: `"webrtc"`)

* `hls` (value: `"hls"`)





## Enum: ResolutionEnum


* `240p` (value: `"240p"`)

* `360p` (value: `"360p"`)

* `480p` (value: `"480p"`)

* `720p` (value: `"720p"`)

* `1080p` (value: `"1080p"`)

* `1440p` (value: `"1440p"`)

* `2160p` (value: `"2160p"`)

* `variable` (value: `"variable"`)




