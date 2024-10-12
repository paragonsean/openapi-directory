# YouTubeDataApiV3.PlaylistItemContentDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endAt** | **String** | The time, measured in seconds from the start of the video, when the video should stop playing. (The playlist owner can specify the times when the video should start and stop playing when the video is played in the context of the playlist.) By default, assume that the video.endTime is the end of the video. | [optional] 
**note** | **String** | A user-generated note for this item. | [optional] 
**startAt** | **String** | The time, measured in seconds from the start of the video, when the video should start playing. (The playlist owner can specify the times when the video should start and stop playing when the video is played in the context of the playlist.) The default value is 0. | [optional] 
**videoId** | **String** | The ID that YouTube uses to uniquely identify a video. To retrieve the video resource, set the id query parameter to this value in your API request. | [optional] 
**videoPublishedAt** | **Date** | The date and time that the video was published to YouTube. | [optional] 


