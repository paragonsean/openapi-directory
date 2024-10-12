

# TimeseriesProperties

Defines the properties of a timeseries

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**aggregationInterval** | [**AggregationIntervalEnum**](#AggregationIntervalEnum) | The aggregation interval of the Timeseries |  [optional] |
|**country** | **String** | The country associated with the Timeseries. Values are country ISO codes as specified here- https://www.iso.org/iso-3166-country-codes.html |  [optional] |
|**endDateTimeUTC** | **String** | The end DateTime of the Timeseries in UTC |  [optional] |
|**endpoint** | **String** | The endpoint associated with the Timeseries data point |  [optional] |
|**startDateTimeUTC** | **String** | The start DateTime of the Timeseries in UTC |  [optional] |
|**timeseriesData** | [**List&lt;TimeseriesDataPoint&gt;**](TimeseriesDataPoint.md) | The set of data points for the timeseries |  [optional] |
|**timeseriesType** | [**TimeseriesTypeEnum**](#TimeseriesTypeEnum) | The type of Timeseries |  [optional] |



## Enum: AggregationIntervalEnum

| Name | Value |
|---- | -----|
| HOURLY | &quot;Hourly&quot; |
| DAILY | &quot;Daily&quot; |



## Enum: TimeseriesTypeEnum

| Name | Value |
|---- | -----|
| MEASUREMENT_COUNTS | &quot;MeasurementCounts&quot; |
| LATENCY_P50 | &quot;LatencyP50&quot; |
| LATENCY_P75 | &quot;LatencyP75&quot; |
| LATENCY_P95 | &quot;LatencyP95&quot; |



