

# NetworkReportSpecSortCondition

Sorting direction to be applied on a dimension or a metric.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dimension** | [**DimensionEnum**](#DimensionEnum) | Sort by the specified dimension. |  [optional] |
|**metric** | [**MetricEnum**](#MetricEnum) | Sort by the specified metric. |  [optional] |
|**order** | [**OrderEnum**](#OrderEnum) | Sorting order of the dimension or metric. |  [optional] |



## Enum: DimensionEnum

| Name | Value |
|---- | -----|
| DIMENSION_UNSPECIFIED | &quot;DIMENSION_UNSPECIFIED&quot; |
| DATE | &quot;DATE&quot; |
| MONTH | &quot;MONTH&quot; |
| WEEK | &quot;WEEK&quot; |
| AD_UNIT | &quot;AD_UNIT&quot; |
| APP | &quot;APP&quot; |
| AD_TYPE | &quot;AD_TYPE&quot; |
| COUNTRY | &quot;COUNTRY&quot; |
| FORMAT | &quot;FORMAT&quot; |
| PLATFORM | &quot;PLATFORM&quot; |
| MOBILE_OS_VERSION | &quot;MOBILE_OS_VERSION&quot; |
| GMA_SDK_VERSION | &quot;GMA_SDK_VERSION&quot; |
| APP_VERSION_NAME | &quot;APP_VERSION_NAME&quot; |
| SERVING_RESTRICTION | &quot;SERVING_RESTRICTION&quot; |



## Enum: MetricEnum

| Name | Value |
|---- | -----|
| METRIC_UNSPECIFIED | &quot;METRIC_UNSPECIFIED&quot; |
| AD_REQUESTS | &quot;AD_REQUESTS&quot; |
| CLICKS | &quot;CLICKS&quot; |
| ESTIMATED_EARNINGS | &quot;ESTIMATED_EARNINGS&quot; |
| IMPRESSIONS | &quot;IMPRESSIONS&quot; |
| IMPRESSION_CTR | &quot;IMPRESSION_CTR&quot; |
| IMPRESSION_RPM | &quot;IMPRESSION_RPM&quot; |
| MATCHED_REQUESTS | &quot;MATCHED_REQUESTS&quot; |
| MATCH_RATE | &quot;MATCH_RATE&quot; |
| SHOW_RATE | &quot;SHOW_RATE&quot; |



## Enum: OrderEnum

| Name | Value |
|---- | -----|
| SORT_ORDER_UNSPECIFIED | &quot;SORT_ORDER_UNSPECIFIED&quot; |
| ASCENDING | &quot;ASCENDING&quot; |
| DESCENDING | &quot;DESCENDING&quot; |



