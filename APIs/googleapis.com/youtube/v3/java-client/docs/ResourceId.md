

# ResourceId

A resource id is a generic reference that points to another YouTube resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**channelId** | **String** | The ID that YouTube uses to uniquely identify the referred resource, if that resource is a channel. This property is only present if the resourceId.kind value is youtube#channel. |  [optional] |
|**kind** | **String** | The type of the API resource. |  [optional] |
|**playlistId** | **String** | The ID that YouTube uses to uniquely identify the referred resource, if that resource is a playlist. This property is only present if the resourceId.kind value is youtube#playlist. |  [optional] |
|**videoId** | **String** | The ID that YouTube uses to uniquely identify the referred resource, if that resource is a video. This property is only present if the resourceId.kind value is youtube#video. |  [optional] |



