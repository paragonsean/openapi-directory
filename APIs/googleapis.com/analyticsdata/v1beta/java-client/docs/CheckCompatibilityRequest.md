

# CheckCompatibilityRequest

The request for compatibility information for a report's dimensions and metrics. Check compatibility provides a preview of the compatibility of a report; fields shared with the `runReport` request should be the same values as in your `runReport` request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**compatibilityFilter** | [**CompatibilityFilterEnum**](#CompatibilityFilterEnum) | Filters the dimensions and metrics in the response to just this compatibility. Commonly used as &#x60;”compatibilityFilter”: “COMPATIBLE”&#x60; to only return compatible dimensions &amp; metrics. |  [optional] |
|**dimensionFilter** | [**FilterExpression**](FilterExpression.md) |  |  [optional] |
|**dimensions** | [**List&lt;Dimension&gt;**](Dimension.md) | The dimensions in this report. &#x60;dimensions&#x60; should be the same value as in your &#x60;runReport&#x60; request. |  [optional] |
|**metricFilter** | [**FilterExpression**](FilterExpression.md) |  |  [optional] |
|**metrics** | [**List&lt;Metric&gt;**](Metric.md) | The metrics in this report. &#x60;metrics&#x60; should be the same value as in your &#x60;runReport&#x60; request. |  [optional] |



## Enum: CompatibilityFilterEnum

| Name | Value |
|---- | -----|
| COMPATIBILITY_UNSPECIFIED | &quot;COMPATIBILITY_UNSPECIFIED&quot; |
| COMPATIBLE | &quot;COMPATIBLE&quot; |
| INCOMPATIBLE | &quot;INCOMPATIBLE&quot; |



