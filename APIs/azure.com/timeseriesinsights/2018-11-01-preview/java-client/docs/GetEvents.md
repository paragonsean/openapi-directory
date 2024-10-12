

# GetEvents

Get Events query. Allows to retrieve raw events for a given Time Series ID and search span.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**filter** | [**Tsx**](Tsx.md) |  |  [optional] |
|**projectedProperties** | [**List&lt;EventProperty&gt;**](EventProperty.md) | Projected properties is an array of properties which you want to project. These properties must appear in the events; otherwise, they are not returned. |  [optional] |
|**searchSpan** | [**DateTimeRange**](DateTimeRange.md) |  |  |
|**take** | **Integer** | Maximum number of property values in the whole response set, not the maximum number of property values per page. Defaults to 10,000 when not set. Maximum value of take can be 250,000. |  [optional] |
|**timeSeriesId** | **List&lt;Object&gt;** | A single Time Series ID value that is an array of primitive values that uniquely identifies a time series instance (e.g. a single device). Note that a single Time Series ID can be composite if multiple properties are specified as Time Series ID at environment creation time. The position and type of values must match Time Series ID properties specified on the environment and returned by Get Model Setting API. Cannot be empty. |  |



