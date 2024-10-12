# YouTubeDataApiV3.VideoProcessingDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**editorSuggestionsAvailability** | **String** | This value indicates whether video editing suggestions, which might improve video quality or the playback experience, are available for the video. You can retrieve these suggestions by requesting the suggestions part in your videos.list() request. | [optional] 
**fileDetailsAvailability** | **String** | This value indicates whether file details are available for the uploaded video. You can retrieve a video&#39;s file details by requesting the fileDetails part in your videos.list() request. | [optional] 
**processingFailureReason** | **String** | The reason that YouTube failed to process the video. This property will only have a value if the processingStatus property&#39;s value is failed. | [optional] 
**processingIssuesAvailability** | **String** | This value indicates whether the video processing engine has generated suggestions that might improve YouTube&#39;s ability to process the the video, warnings that explain video processing problems, or errors that cause video processing problems. You can retrieve these suggestions by requesting the suggestions part in your videos.list() request. | [optional] 
**processingProgress** | [**VideoProcessingDetailsProcessingProgress**](VideoProcessingDetailsProcessingProgress.md) |  | [optional] 
**processingStatus** | **String** | The video&#39;s processing status. This value indicates whether YouTube was able to process the video or if the video is still being processed. | [optional] 
**tagSuggestionsAvailability** | **String** | This value indicates whether keyword (tag) suggestions are available for the video. Tags can be added to a video&#39;s metadata to make it easier for other users to find the video. You can retrieve these suggestions by requesting the suggestions part in your videos.list() request. | [optional] 
**thumbnailsAvailability** | **String** | This value indicates whether thumbnail images have been generated for the video. | [optional] 



## Enum: ProcessingFailureReasonEnum


* `uploadFailed` (value: `"uploadFailed"`)

* `transcodeFailed` (value: `"transcodeFailed"`)

* `streamingFailed` (value: `"streamingFailed"`)

* `other` (value: `"other"`)





## Enum: ProcessingStatusEnum


* `processing` (value: `"processing"`)

* `succeeded` (value: `"succeeded"`)

* `failed` (value: `"failed"`)

* `terminated` (value: `"terminated"`)




