# StorSimple8000SeriesManagementClient.MetricFilter

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **String** | Specifies the category of the metrics to be filtered. E.g., \&quot;CapacityUtilization\&quot;. Valid values are the ones returned as the field \&quot;category\&quot; in the ListMetricDefinitions call. Only &#39;Equality&#39; operator is supported for this property. | 
**dimensions** | [**DimensionFilter**](DimensionFilter.md) |  | [optional] 
**endTime** | **Date** | Specifies the end time of the time range to be queried. Only &#39;Less Than Or Equal To&#39; operator is supported for this property. | [optional] 
**name** | [**MetricNameFilter**](MetricNameFilter.md) |  | [optional] 
**startTime** | **Date** | Specifies the start time of the time range to be queried. Only &#39;Greater Than Or Equal To&#39; operator is supported for this property. | [optional] 
**timeGrain** | **String** | Specifies the time granularity of the metrics to be returned. E.g., \&quot;P1D\&quot;. Valid values are the ones returned as the field \&quot;timeGrain\&quot; in the ListMetricDefinitions call. Only &#39;Equality&#39; operator is supported for this property. | [optional] 


