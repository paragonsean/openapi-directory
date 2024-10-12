# ApigeeApi.GoogleCloudApigeeV1StatsEnvironmentStats

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dimensions** | [**[GoogleCloudApigeeV1DimensionMetric]**](GoogleCloudApigeeV1DimensionMetric.md) | List of metrics grouped under dimensions. | [optional] 
**metrics** | [**[GoogleCloudApigeeV1Metric]**](GoogleCloudApigeeV1Metric.md) | In the final response, only one of the following fields will be present based on the dimensions provided. If no dimensions are provided, then only top-level metrics is provided. If dimensions are included, then there will be a top-level dimensions field under environments which will contain metrics values and the dimension name. Example: &#x60;&#x60;&#x60; \&quot;environments\&quot;: [ { \&quot;dimensions\&quot;: [ { \&quot;metrics\&quot;: [ { \&quot;name\&quot;: \&quot;sum(message_count)\&quot;, \&quot;values\&quot;: [ \&quot;2.14049521E8\&quot; ] } ], \&quot;name\&quot;: \&quot;nit_proxy\&quot; } ], \&quot;name\&quot;: \&quot;prod\&quot; } ]&#x60;&#x60;&#x60; or &#x60;&#x60;&#x60;\&quot;environments\&quot;: [ { \&quot;metrics\&quot;: [ { \&quot;name\&quot;: \&quot;sum(message_count)\&quot;, \&quot;values\&quot;: [ \&quot;2.19026331E8\&quot; ] } ], \&quot;name\&quot;: \&quot;prod\&quot; } ]&#x60;&#x60;&#x60; List of metric values. | [optional] 
**name** | **String** | Name of the environment. | [optional] 


