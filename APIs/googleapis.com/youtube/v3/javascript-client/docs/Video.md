# YouTubeDataApiV3.Video

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ageGating** | [**VideoAgeGating**](VideoAgeGating.md) |  | [optional] 
**contentDetails** | [**VideoContentDetails**](VideoContentDetails.md) |  | [optional] 
**etag** | **String** | Etag of this resource. | [optional] 
**fileDetails** | [**VideoFileDetails**](VideoFileDetails.md) |  | [optional] 
**id** | **String** | The ID that YouTube uses to uniquely identify the video. | [optional] 
**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string \&quot;youtube#video\&quot;. | [optional] [default to &#39;youtube#video&#39;]
**liveStreamingDetails** | [**VideoLiveStreamingDetails**](VideoLiveStreamingDetails.md) |  | [optional] 
**localizations** | [**{String: VideoLocalization}**](VideoLocalization.md) | The localizations object contains localized versions of the basic details about the video, such as its title and description. | [optional] 
**monetizationDetails** | [**VideoMonetizationDetails**](VideoMonetizationDetails.md) |  | [optional] 
**player** | [**VideoPlayer**](VideoPlayer.md) |  | [optional] 
**processingDetails** | [**VideoProcessingDetails**](VideoProcessingDetails.md) |  | [optional] 
**projectDetails** | **Object** | DEPRECATED. b/157517979: This part was never populated after it was added. However, it sees non-zero traffic because there is generated client code in the wild that refers to it [1]. We keep this field and do NOT remove it because otherwise V3 would return an error when this part gets requested [2]. [1] https://developers.google.com/resources/api-libraries/documentation/youtube/v3/csharp/latest/classGoogle_1_1Apis_1_1YouTube_1_1v3_1_1Data_1_1VideoProjectDetails.html [2] http://google3/video/youtube/src/python/servers/data_api/common.py?l&#x3D;1565-1569&amp;rcl&#x3D;344141677 | [optional] 
**recordingDetails** | [**VideoRecordingDetails**](VideoRecordingDetails.md) |  | [optional] 
**snippet** | [**VideoSnippet**](VideoSnippet.md) |  | [optional] 
**statistics** | [**VideoStatistics**](VideoStatistics.md) |  | [optional] 
**status** | [**VideoStatus**](VideoStatus.md) |  | [optional] 
**suggestions** | [**VideoSuggestions**](VideoSuggestions.md) |  | [optional] 
**topicDetails** | [**VideoTopicDetails**](VideoTopicDetails.md) |  | [optional] 


