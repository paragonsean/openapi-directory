# YouTubeDataApiV3.LiveBroadcastSnippet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actualEndTime** | **Date** | The date and time that the broadcast actually ended. This information is only available once the broadcast&#39;s state is complete. | [optional] 
**actualStartTime** | **Date** | The date and time that the broadcast actually started. This information is only available once the broadcast&#39;s state is live. | [optional] 
**channelId** | **String** | The ID that YouTube uses to uniquely identify the channel that is publishing the broadcast. | [optional] 
**description** | **String** | The broadcast&#39;s description. As with the title, you can set this field by modifying the broadcast resource or by setting the description field of the corresponding video resource. | [optional] 
**isDefaultBroadcast** | **Boolean** | Indicates whether this broadcast is the default broadcast. Internal only. | [optional] 
**liveChatId** | **String** | The id of the live chat for this broadcast. | [optional] 
**publishedAt** | **Date** | The date and time that the broadcast was added to YouTube&#39;s live broadcast schedule. | [optional] 
**scheduledEndTime** | **Date** | The date and time that the broadcast is scheduled to end. | [optional] 
**scheduledStartTime** | **Date** | The date and time that the broadcast is scheduled to start. | [optional] 
**thumbnails** | [**ThumbnailDetails**](ThumbnailDetails.md) |  | [optional] 
**title** | **String** | The broadcast&#39;s title. Note that the broadcast represents exactly one YouTube video. You can set this field by modifying the broadcast resource or by setting the title field of the corresponding video resource. | [optional] 


