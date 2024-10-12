

# LiveChatMessageListResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**etag** | **String** | Etag of this resource. |  [optional] |
|**eventId** | **String** | Serialized EventId of the request which produced this response. |  [optional] |
|**items** | [**List&lt;LiveChatMessage&gt;**](LiveChatMessage.md) |  |  [optional] |
|**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string \&quot;youtube#liveChatMessageListResponse\&quot;. |  [optional] |
|**nextPageToken** | **String** |  |  [optional] |
|**offlineAt** | **OffsetDateTime** | The date and time when the underlying stream went offline. |  [optional] |
|**pageInfo** | [**PageInfo**](PageInfo.md) |  |  [optional] |
|**pollingIntervalMillis** | **Integer** | The amount of time the client should wait before polling again. |  [optional] |
|**tokenPagination** | **Object** | Stub token pagination template to suppress results. |  [optional] |
|**visitorId** | **String** | The visitorId identifies the visitor. |  [optional] |



