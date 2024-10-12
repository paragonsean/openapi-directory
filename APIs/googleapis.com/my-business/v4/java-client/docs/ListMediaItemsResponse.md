

# ListMediaItemsResponse

Response message for Media.ListMediaItems.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**mediaItems** | [**List&lt;MediaItem&gt;**](MediaItem.md) | The returned list of media items. |  [optional] |
|**nextPageToken** | **String** | If there are more media items than the requested page size, then this field is populated with a token to fetch the next page of media items on a subsequent call to ListMediaItems. |  [optional] |
|**totalMediaItemCount** | **Integer** | The total number of media items for this location, irrespective of pagination. |  [optional] |



