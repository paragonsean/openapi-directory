# Superset.ChartDataBoxplotOptionsSchema

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**groupby** | **[String]** |  | [optional] 
**metrics** | **[Object]** | Aggregate expressions. Metrics can be passed as both references to datasource metrics (strings), or ad-hoc metricswhich are defined only within the query object. See &#x60;ChartDataAdhocMetricSchema&#x60; for the structure of ad-hoc metrics. | [optional] 
**percentiles** | **Object** | Upper and lower percentiles for percentile whisker type. | [optional] 
**whiskerType** | **String** | Whisker type. Any numpy function will work. | 



## Enum: WhiskerTypeEnum


* `tukey` (value: `"tukey"`)

* `min/max` (value: `"min/max"`)

* `percentile` (value: `"percentile"`)




