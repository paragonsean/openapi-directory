# NetworkExperiments.TimeseriesProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregationInterval** | **String** | The aggregation interval of the Timeseries | [optional] 
**country** | **String** | The country associated with the Timeseries. Values are country ISO codes as specified here- https://www.iso.org/iso-3166-country-codes.html | [optional] 
**endDateTimeUTC** | **String** | The end DateTime of the Timeseries in UTC | [optional] 
**endpoint** | **String** | The endpoint associated with the Timeseries data point | [optional] 
**startDateTimeUTC** | **String** | The start DateTime of the Timeseries in UTC | [optional] 
**timeseriesData** | [**[TimeseriesDataPoint]**](TimeseriesDataPoint.md) | The set of data points for the timeseries | [optional] 
**timeseriesType** | **String** | The type of Timeseries | [optional] 



## Enum: AggregationIntervalEnum


* `Hourly` (value: `"Hourly"`)

* `Daily` (value: `"Daily"`)





## Enum: TimeseriesTypeEnum


* `MeasurementCounts` (value: `"MeasurementCounts"`)

* `LatencyP50` (value: `"LatencyP50"`)

* `LatencyP75` (value: `"LatencyP75"`)

* `LatencyP95` (value: `"LatencyP95"`)




