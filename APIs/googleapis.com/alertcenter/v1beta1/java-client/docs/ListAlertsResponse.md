

# ListAlertsResponse

Response message for an alert listing request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**alerts** | [**List&lt;Alert&gt;**](Alert.md) | The list of alerts. |  [optional] |
|**nextPageToken** | **String** | The token for the next page. If not empty, indicates that there may be more alerts that match the listing request; this value can be used in a subsequent ListAlertsRequest to get alerts continuing from last result of the current list call. |  [optional] |



