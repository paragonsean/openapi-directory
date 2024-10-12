# YouTubeDataApiV3.LiveStreamConfigurationIssue

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | The long-form description of the issue and how to resolve it. | [optional] 
**reason** | **String** | The short-form reason for this issue. | [optional] 
**severity** | **String** | How severe this issue is to the stream. | [optional] 
**type** | **String** | The kind of error happening. | [optional] 



## Enum: SeverityEnum


* `info` (value: `"info"`)

* `warning` (value: `"warning"`)

* `error` (value: `"error"`)





## Enum: TypeEnum


* `gopSizeOver` (value: `"gopSizeOver"`)

* `gopSizeLong` (value: `"gopSizeLong"`)

* `gopSizeShort` (value: `"gopSizeShort"`)

* `openGop` (value: `"openGop"`)

* `badContainer` (value: `"badContainer"`)

* `audioBitrateHigh` (value: `"audioBitrateHigh"`)

* `audioBitrateLow` (value: `"audioBitrateLow"`)

* `audioSampleRate` (value: `"audioSampleRate"`)

* `bitrateHigh` (value: `"bitrateHigh"`)

* `bitrateLow` (value: `"bitrateLow"`)

* `audioCodec` (value: `"audioCodec"`)

* `videoCodec` (value: `"videoCodec"`)

* `noAudioStream` (value: `"noAudioStream"`)

* `noVideoStream` (value: `"noVideoStream"`)

* `multipleVideoStreams` (value: `"multipleVideoStreams"`)

* `multipleAudioStreams` (value: `"multipleAudioStreams"`)

* `audioTooManyChannels` (value: `"audioTooManyChannels"`)

* `interlacedVideo` (value: `"interlacedVideo"`)

* `frameRateHigh` (value: `"frameRateHigh"`)

* `resolutionMismatch` (value: `"resolutionMismatch"`)

* `videoCodecMismatch` (value: `"videoCodecMismatch"`)

* `videoInterlaceMismatch` (value: `"videoInterlaceMismatch"`)

* `videoProfileMismatch` (value: `"videoProfileMismatch"`)

* `videoBitrateMismatch` (value: `"videoBitrateMismatch"`)

* `framerateMismatch` (value: `"framerateMismatch"`)

* `gopMismatch` (value: `"gopMismatch"`)

* `audioSampleRateMismatch` (value: `"audioSampleRateMismatch"`)

* `audioStereoMismatch` (value: `"audioStereoMismatch"`)

* `audioCodecMismatch` (value: `"audioCodecMismatch"`)

* `audioBitrateMismatch` (value: `"audioBitrateMismatch"`)

* `videoResolutionSuboptimal` (value: `"videoResolutionSuboptimal"`)

* `videoResolutionUnsupported` (value: `"videoResolutionUnsupported"`)

* `videoIngestionStarved` (value: `"videoIngestionStarved"`)

* `videoIngestionFasterThanRealtime` (value: `"videoIngestionFasterThanRealtime"`)




