# ServiceManagementApi.MetricRule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metricCosts** | **{String: String}** | Metrics to update when the selected methods are called, and the associated cost applied to each metric. The key of the map is the metric name, and the values are the amount increased for the metric against which the quota limits are defined. The value must not be negative. | [optional] 
**selector** | **String** | Selects the methods to which this rule applies. Refer to selector for syntax details. | [optional] 


