# GoogleMyBusinessApi.ListCustomerMediaItemsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mediaItems** | [**[MediaItem]**](MediaItem.md) | The returned list of media items. | [optional] 
**nextPageToken** | **String** | If there are more media items than the requested page size, then this field is populated with a token to fetch the next page of media items on a subsequent call to ListCustomerMediaItems. | [optional] 
**totalMediaItemCount** | **Number** | The total number of media items for this location, irrespective of pagination. This number is approximate, particularly when there are multiple pages of results. | [optional] 


