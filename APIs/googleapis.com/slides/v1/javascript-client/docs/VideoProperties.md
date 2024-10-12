# GoogleSlidesApi.VideoProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**autoPlay** | **Boolean** | Whether to enable video autoplay when the page is displayed in present mode. Defaults to false. | [optional] 
**end** | **Number** | The time at which to end playback, measured in seconds from the beginning of the video. If set, the end time should be after the start time. If not set or if you set this to a value that exceeds the video&#39;s length, the video will be played until its end. | [optional] 
**mute** | **Boolean** | Whether to mute the audio during video playback. Defaults to false. | [optional] 
**outline** | [**Outline**](Outline.md) |  | [optional] 
**start** | **Number** | The time at which to start playback, measured in seconds from the beginning of the video. If set, the start time should be before the end time. If you set this to a value that exceeds the video&#39;s length in seconds, the video will be played from the last second. If not set, the video will be played from the beginning. | [optional] 


