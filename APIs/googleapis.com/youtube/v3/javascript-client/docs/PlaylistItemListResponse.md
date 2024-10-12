# YouTubeDataApiV3.PlaylistItemListResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**etag** | **String** |  | [optional] 
**eventId** | **String** | Serialized EventId of the request which produced this response. | [optional] 
**items** | [**[PlaylistItem]**](PlaylistItem.md) | A list of playlist items that match the request criteria. | [optional] 
**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string \&quot;youtube#playlistItemListResponse\&quot;. Etag of this resource. | [optional] [default to &#39;youtube#playlistItemListResponse&#39;]
**nextPageToken** | **String** | The token that can be used as the value of the pageToken parameter to retrieve the next page in the result set. | [optional] 
**pageInfo** | [**PageInfo**](PageInfo.md) |  | [optional] 
**prevPageToken** | **String** | The token that can be used as the value of the pageToken parameter to retrieve the previous page in the result set. | [optional] 
**tokenPagination** | **Object** | Stub token pagination template to suppress results. | [optional] 
**visitorId** | **String** | The visitorId identifies the visitor. | [optional] 


