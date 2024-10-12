

# LocationDrivingDirectionMetrics

A location indexed with the regions that people usually come from. This is captured by counting how many driving-direction requests to this location are from each region.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**locationName** | **String** | The location resource name this metric value belongs to. |  [optional] |
|**timeZone** | **String** | Time zone (IANA timezone IDs, for example, &#39;Europe/London&#39;) of the location. |  [optional] |
|**topDirectionSources** | [**List&lt;TopDirectionSources&gt;**](TopDirectionSources.md) | Driving-direction requests by source region. By convention, these are sorted by count with at most 10 results. |  [optional] |



