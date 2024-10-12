

# ReportCrossDimensionReachCriteria

The report criteria for a report of type \"CROSS_DIMENSION_REACH\".

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**breakdown** | [**List&lt;SortedDimension&gt;**](SortedDimension.md) | The list of dimensions the report should include. |  [optional] |
|**dateRange** | [**DateRange**](DateRange.md) |  |  [optional] |
|**dimension** | [**DimensionEnum**](#DimensionEnum) | The dimension option. |  [optional] |
|**dimensionFilters** | [**List&lt;DimensionValue&gt;**](DimensionValue.md) | The list of filters on which dimensions are filtered. |  [optional] |
|**metricNames** | **List&lt;String&gt;** | The list of names of metrics the report should include. |  [optional] |
|**overlapMetricNames** | **List&lt;String&gt;** | The list of names of overlap metrics the report should include. |  [optional] |
|**pivoted** | **Boolean** | Whether the report is pivoted or not. Defaults to true. |  [optional] |



## Enum: DimensionEnum

| Name | Value |
|---- | -----|
| ADVERTISER | &quot;ADVERTISER&quot; |
| CAMPAIGN | &quot;CAMPAIGN&quot; |
| SITE_BY_ADVERTISER | &quot;SITE_BY_ADVERTISER&quot; |
| SITE_BY_CAMPAIGN | &quot;SITE_BY_CAMPAIGN&quot; |



