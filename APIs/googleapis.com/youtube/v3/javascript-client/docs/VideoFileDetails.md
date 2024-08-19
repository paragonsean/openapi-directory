# YouTubeDataApiV3.VideoFileDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audioStreams** | [**[VideoFileDetailsAudioStream]**](VideoFileDetailsAudioStream.md) | A list of audio streams contained in the uploaded video file. Each item in the list contains detailed metadata about an audio stream. | [optional] 
**bitrateBps** | **String** | The uploaded video file&#39;s combined (video and audio) bitrate in bits per second. | [optional] 
**container** | **String** | The uploaded video file&#39;s container format. | [optional] 
**creationTime** | **String** | The date and time when the uploaded video file was created. The value is specified in ISO 8601 format. Currently, the following ISO 8601 formats are supported: - Date only: YYYY-MM-DD - Naive time: YYYY-MM-DDTHH:MM:SS - Time with timezone: YYYY-MM-DDTHH:MM:SS+HH:MM  | [optional] 
**durationMs** | **String** | The length of the uploaded video in milliseconds. | [optional] 
**fileName** | **String** | The uploaded file&#39;s name. This field is present whether a video file or another type of file was uploaded. | [optional] 
**fileSize** | **String** | The uploaded file&#39;s size in bytes. This field is present whether a video file or another type of file was uploaded. | [optional] 
**fileType** | **String** | The uploaded file&#39;s type as detected by YouTube&#39;s video processing engine. Currently, YouTube only processes video files, but this field is present whether a video file or another type of file was uploaded. | [optional] 
**videoStreams** | [**[VideoFileDetailsVideoStream]**](VideoFileDetailsVideoStream.md) | A list of video streams contained in the uploaded video file. Each item in the list contains detailed metadata about a video stream. | [optional] 



## Enum: FileTypeEnum


* `video` (value: `"video"`)

* `audio` (value: `"audio"`)

* `image` (value: `"image"`)

* `archive` (value: `"archive"`)

* `document` (value: `"document"`)

* `project` (value: `"project"`)

* `other` (value: `"other"`)




