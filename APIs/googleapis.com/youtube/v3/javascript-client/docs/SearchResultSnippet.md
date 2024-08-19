# YouTubeDataApiV3.SearchResultSnippet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channelId** | **String** | The value that YouTube uses to uniquely identify the channel that published the resource that the search result identifies. | [optional] 
**channelTitle** | **String** | The title of the channel that published the resource that the search result identifies. | [optional] 
**description** | **String** | A description of the search result. | [optional] 
**liveBroadcastContent** | **String** | It indicates if the resource (video or channel) has upcoming/active live broadcast content. Or it&#39;s \&quot;none\&quot; if there is not any upcoming/active live broadcasts. | [optional] 
**publishedAt** | **Date** | The creation date and time of the resource that the search result identifies. | [optional] 
**thumbnails** | [**ThumbnailDetails**](ThumbnailDetails.md) |  | [optional] 
**title** | **String** | The title of the search result. | [optional] 



## Enum: LiveBroadcastContentEnum


* `none` (value: `"none"`)

* `upcoming` (value: `"upcoming"`)

* `live` (value: `"live"`)

* `completed` (value: `"completed"`)




