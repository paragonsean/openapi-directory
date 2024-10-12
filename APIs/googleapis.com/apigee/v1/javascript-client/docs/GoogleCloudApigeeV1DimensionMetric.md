# ApigeeApi.GoogleCloudApigeeV1DimensionMetric

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**individualNames** | **[String]** | Individual dimension names. E.g. [\&quot;dim1_name\&quot;, \&quot;dim2_name\&quot;]. | [optional] 
**metrics** | [**[GoogleCloudApigeeV1Metric]**](GoogleCloudApigeeV1Metric.md) | List of metrics. | [optional] 
**name** | **String** | Comma joined dimension names. E.g. \&quot;dim1_name,dim2_name\&quot;. Deprecated. If name already has comma before join, we may get wrong splits. Please use individual_names. | [optional] 


