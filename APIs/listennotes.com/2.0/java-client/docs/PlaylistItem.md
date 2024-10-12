

# PlaylistItem

An item in a playlist

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**addedAtMs** | **Integer** | Timestamp (in milliseconds) when this item is added. |  [optional] |
|**data** | [**PlaylistItemData**](PlaylistItemData.md) |  |  [optional] |
|**id** | **Integer** | Playlist item id. |  [optional] |
|**notes** | **String** | Notes for this item. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of this playlist item. If a playlist is **episode_list**, then an item could be either **episode** or **custom_audio**. If it&#39;s **podcast_list**, then an item can only be **podcast**.  |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| EPISODE | &quot;episode&quot; |
| CUSTOM_AUDIO | &quot;custom_audio&quot; |
| PODCAST | &quot;podcast&quot; |



