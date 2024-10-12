

# ChartDataBoxplotOptionsSchema


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**groupby** | **List&lt;String&gt;** |  |  [optional] |
|**metrics** | **List&lt;Object&gt;** | Aggregate expressions. Metrics can be passed as both references to datasource metrics (strings), or ad-hoc metricswhich are defined only within the query object. See &#x60;ChartDataAdhocMetricSchema&#x60; for the structure of ad-hoc metrics. |  [optional] |
|**percentiles** | **Object** | Upper and lower percentiles for percentile whisker type. |  [optional] |
|**whiskerType** | [**WhiskerTypeEnum**](#WhiskerTypeEnum) | Whisker type. Any numpy function will work. |  |



## Enum: WhiskerTypeEnum

| Name | Value |
|---- | -----|
| TUKEY | &quot;tukey&quot; |
| MIN_MAX | &quot;min/max&quot; |
| PERCENTILE | &quot;percentile&quot; |



