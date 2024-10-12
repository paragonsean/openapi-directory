

# GoogleCloudApigeeV1StatsHostStats

Encapsulates the hostname wrapper: ``` \"hosts\": [ { \"metrics\": [ { \"name\": \"sum(message_count)\", \"values\": [ \"2.52056245E8\" ] } ], \"name\": \"example.com\" } ]```

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dimensions** | [**List&lt;GoogleCloudApigeeV1DimensionMetric&gt;**](GoogleCloudApigeeV1DimensionMetric.md) | List of metrics grouped under dimensions. |  [optional] |
|**metrics** | [**List&lt;GoogleCloudApigeeV1Metric&gt;**](GoogleCloudApigeeV1Metric.md) | In the final response, only one of the following fields will be present based on the dimensions provided. If no dimensions are provided, then only the top-level metrics are provided. If dimensions are included, then there will be a top-level dimensions field under hostnames which will contain metrics values and the dimension name. Example: &#x60;&#x60;&#x60; \&quot;hosts\&quot;: [ { \&quot;dimensions\&quot;: [ { \&quot;metrics\&quot;: [ { \&quot;name\&quot;: \&quot;sum(message_count)\&quot;, \&quot;values\&quot;: [ \&quot;2.14049521E8\&quot; ] } ], \&quot;name\&quot;: \&quot;nit_proxy\&quot; } ], \&quot;name\&quot;: \&quot;example.com\&quot; } ]&#x60;&#x60;&#x60; OR &#x60;&#x60;&#x60;\&quot;hosts\&quot;: [ { \&quot;metrics\&quot;: [ { \&quot;name\&quot;: \&quot;sum(message_count)\&quot;, \&quot;values\&quot;: [ \&quot;2.19026331E8\&quot; ] } ], \&quot;name\&quot;: \&quot;example.com\&quot; } ]&#x60;&#x60;&#x60; List of metric values. |  [optional] |
|**name** | **String** | Hostname used in query. |  [optional] |



