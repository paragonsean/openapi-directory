# ListenApiPodcastSearchDirectoryAndInsightsApi.PlaylistResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | Playlist description. | [optional] 
**id** | **String** | A 11-character playlist id, which can be used to further fetch detailed playlist metadata via &#x60;GET /playlists/{id}&#x60;. | [optional] 
**image** | **String** | High resolution image url of the playlist. | [optional] 
**items** | [**[PlaylistItem]**](PlaylistItem.md) | A list of playlist items. | [optional] 
**lastTimestampMs** | **Number** | Passed to the **last_timestamp_ms** parameter of &#x60;GET /playlists/{id}&#x60; to paginate through items of that playlist.  | [optional] 
**listennotesUrl** | **String** | The url of this playlist on ListenNotes.com. | [optional] 
**name** | **String** | Playlist name. | [optional] 
**thumbnail** | **String** | Low resolution image url of the playlist. | [optional] 
**total** | **Number** | Total number of items in this playlist. | [optional] 
**totalAudioLengthSec** | **Number** | Total audio length of all episodes in this playlist, in seconds. It will have a valid value only when type is **episode_list**. In other words, it will be 0 if type is **podcast_list**. | [optional] 
**type** | **String** | The type of this playlist, which should be either **episode_list** or **podcast_list**.  | [optional] 
**visibility** | [**PlaylistVisibilityField**](PlaylistVisibilityField.md) |  | [optional] 



## Enum: TypeEnum


* `episode_list` (value: `"episode_list"`)

* `podcast_list` (value: `"podcast_list"`)




