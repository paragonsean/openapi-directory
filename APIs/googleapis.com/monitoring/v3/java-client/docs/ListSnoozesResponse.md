

# ListSnoozesResponse

The results of a successful ListSnoozes call, containing the matching Snoozes.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextPageToken** | **String** | Page token for repeated calls to ListSnoozes, to fetch additional pages of results. If this is empty or missing, there are no more pages. |  [optional] |
|**snoozes** | [**List&lt;Snooze&gt;**](Snooze.md) | Snoozes matching this list call. |  [optional] |



