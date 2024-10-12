

# InstanceHit

Time series instance that is returned by instances search call. Returned instance matched the search request and contains highlighted text to be displayed to the user if it is set to 'true'.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**hierarchyIds** | **List&lt;UUID&gt;** | List of time series hierarchy IDs that time series instance which matched the search request belongs to. Cannot be used to lookup hierarchies. May be null. |  [optional] [readonly] |
|**highlights** | [**InstanceHitHighlights**](InstanceHitHighlights.md) |  |  [optional] |
|**name** | **String** | Name of the time series instance that matched the search request. May be null. |  [optional] [readonly] |
|**timeSeriesId** | **List&lt;Object&gt;** | A single Time Series ID value that is an array of primitive values that uniquely identifies a time series instance (e.g. a single device). Note that a single Time Series ID can be composite if multiple properties are specified as Time Series ID at environment creation time. The position and type of values must match Time Series ID properties specified on the environment and returned by Get Model Setting API. Cannot be empty. |  [optional] |
|**typeId** | **UUID** | Represents the type that time series instance which matched the search request belongs to. Never null. |  [optional] [readonly] |



