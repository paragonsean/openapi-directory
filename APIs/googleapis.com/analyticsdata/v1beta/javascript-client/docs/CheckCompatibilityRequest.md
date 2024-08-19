# GoogleAnalyticsDataApi.CheckCompatibilityRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compatibilityFilter** | **String** | Filters the dimensions and metrics in the response to just this compatibility. Commonly used as &#x60;”compatibilityFilter”: “COMPATIBLE”&#x60; to only return compatible dimensions &amp; metrics. | [optional] 
**dimensionFilter** | [**FilterExpression**](FilterExpression.md) |  | [optional] 
**dimensions** | [**[Dimension]**](Dimension.md) | The dimensions in this report. &#x60;dimensions&#x60; should be the same value as in your &#x60;runReport&#x60; request. | [optional] 
**metricFilter** | [**FilterExpression**](FilterExpression.md) |  | [optional] 
**metrics** | [**[Metric]**](Metric.md) | The metrics in this report. &#x60;metrics&#x60; should be the same value as in your &#x60;runReport&#x60; request. | [optional] 



## Enum: CompatibilityFilterEnum


* `COMPATIBILITY_UNSPECIFIED` (value: `"COMPATIBILITY_UNSPECIFIED"`)

* `COMPATIBLE` (value: `"COMPATIBLE"`)

* `INCOMPATIBLE` (value: `"INCOMPATIBLE"`)




