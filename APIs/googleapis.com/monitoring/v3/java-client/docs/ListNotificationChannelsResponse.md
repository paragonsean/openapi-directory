

# ListNotificationChannelsResponse

The ListNotificationChannels response.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextPageToken** | **String** | If not empty, indicates that there may be more results that match the request. Use the value in the page_token field in a subsequent request to fetch the next set of results. If empty, all results have been returned. |  [optional] |
|**notificationChannels** | [**List&lt;NotificationChannel&gt;**](NotificationChannel.md) | The notification channels defined for the specified project. |  [optional] |
|**totalSize** | **Integer** | The total number of notification channels in all pages. This number is only an estimate, and may change in subsequent pages. https://aip.dev/158 |  [optional] |



