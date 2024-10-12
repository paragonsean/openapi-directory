# ListenApiPodcastSearchDirectoryAndInsightsApi.PlaylistItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addedAtMs** | **Number** | Timestamp (in milliseconds) when this item is added. | [optional] 
**data** | [**PlaylistItemData**](PlaylistItemData.md) |  | [optional] 
**id** | **Number** | Playlist item id. | [optional] 
**notes** | **String** | Notes for this item. | [optional] 
**type** | **String** | The type of this playlist item. If a playlist is **episode_list**, then an item could be either **episode** or **custom_audio**. If it&#39;s **podcast_list**, then an item can only be **podcast**.  | [optional] 



## Enum: TypeEnum


* `episode` (value: `"episode"`)

* `custom_audio` (value: `"custom_audio"`)

* `podcast` (value: `"podcast"`)




