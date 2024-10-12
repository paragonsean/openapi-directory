

# GetSeries

Get Series query. Allows to retrieve time series of calculated variable values from events for a given Time Series ID and search span.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**filter** | [**Tsx**](Tsx.md) |  |  [optional] |
|**inlineVariables** | [**Map&lt;String, Variable&gt;**](Variable.md) | Optional inline variables apart from the ones already defined in the time series type in the model. When the inline variable name is the same name as in the model, the inline variable definition takes precedence. Can be null. |  [optional] |
|**projectedVariables** | **List&lt;String&gt;** | Selected variables that needs to be projected in the query result. When it is null or not set, all the variables from inlineVariables and time series type in the model are returned. Can be null. |  [optional] |
|**searchSpan** | [**DateTimeRange**](DateTimeRange.md) |  |  |
|**take** | **Integer** | Maximum number of property values in the whole response set, not the maximum number of property values per page. Defaults to 10,000 when not set. Maximum value of take can be 250,000. |  [optional] |
|**timeSeriesId** | **List&lt;Object&gt;** | A single Time Series ID value that is an array of primitive values that uniquely identifies a time series instance (e.g. a single device). Note that a single Time Series ID can be composite if multiple properties are specified as Time Series ID at environment creation time. The position and type of values must match Time Series ID properties specified on the environment and returned by Get Model Setting API. Cannot be empty. |  |



