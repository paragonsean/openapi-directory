

# ListNotificationChannelDescriptorsResponse

The ListNotificationChannelDescriptors response.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**channelDescriptors** | [**List&lt;NotificationChannelDescriptor&gt;**](NotificationChannelDescriptor.md) | The monitored resource descriptors supported for the specified project, optionally filtered. |  [optional] |
|**nextPageToken** | **String** | If not empty, indicates that there may be more results that match the request. Use the value in the page_token field in a subsequent request to fetch the next set of results. If empty, all results have been returned. |  [optional] |



