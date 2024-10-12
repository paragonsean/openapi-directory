# AzureMediaServices.Video

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keyFrameInterval** | **String** | The distance between two key frames, thereby defining a group of pictures (GOP). The value should be a non-zero integer in the range [1, 30] seconds, specified in ISO 8601 format. The default is 2 seconds (PT2S). | [optional] 
**stretchMode** | **String** | The resizing mode - how the input video will be resized to fit the desired output resolution(s). Default is AutoSize | [optional] 



## Enum: StretchModeEnum


* `None` (value: `"None"`)

* `AutoSize` (value: `"AutoSize"`)

* `AutoFit` (value: `"AutoFit"`)




