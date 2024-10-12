

# MetricValue

A value for a single Metric from a starting time.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dimensionalValues** | [**List&lt;DimensionalMetricValue&gt;**](DimensionalMetricValue.md) | Dimensional values for this metric. |  [optional] |
|**metric** | [**MetricEnum**](#MetricEnum) | The metric for which the value applies. |  [optional] |
|**totalValue** | [**DimensionalMetricValue**](DimensionalMetricValue.md) |  |  [optional] |



## Enum: MetricEnum

| Name | Value |
|---- | -----|
| METRIC_UNSPECIFIED | &quot;METRIC_UNSPECIFIED&quot; |
| ALL | &quot;ALL&quot; |
| QUERIES_DIRECT | &quot;QUERIES_DIRECT&quot; |
| QUERIES_INDIRECT | &quot;QUERIES_INDIRECT&quot; |
| QUERIES_CHAIN | &quot;QUERIES_CHAIN&quot; |
| VIEWS_MAPS | &quot;VIEWS_MAPS&quot; |
| VIEWS_SEARCH | &quot;VIEWS_SEARCH&quot; |
| ACTIONS_WEBSITE | &quot;ACTIONS_WEBSITE&quot; |
| ACTIONS_PHONE | &quot;ACTIONS_PHONE&quot; |
| ACTIONS_DRIVING_DIRECTIONS | &quot;ACTIONS_DRIVING_DIRECTIONS&quot; |
| PHOTOS_VIEWS_MERCHANT | &quot;PHOTOS_VIEWS_MERCHANT&quot; |
| PHOTOS_VIEWS_CUSTOMERS | &quot;PHOTOS_VIEWS_CUSTOMERS&quot; |
| PHOTOS_COUNT_MERCHANT | &quot;PHOTOS_COUNT_MERCHANT&quot; |
| PHOTOS_COUNT_CUSTOMERS | &quot;PHOTOS_COUNT_CUSTOMERS&quot; |
| LOCAL_POST_VIEWS_SEARCH | &quot;LOCAL_POST_VIEWS_SEARCH&quot; |
| LOCAL_POST_ACTIONS_CALL_TO_ACTION | &quot;LOCAL_POST_ACTIONS_CALL_TO_ACTION&quot; |



