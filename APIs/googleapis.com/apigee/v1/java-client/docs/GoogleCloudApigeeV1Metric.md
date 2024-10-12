

# GoogleCloudApigeeV1Metric

Encapsulates the metric data point. For example: ```{ \"name\": \"sum(message_count)\", \"values\" : [ { \"timestamp\": 1549004400000, \"value\": \"39.0\" }, { \"timestamp\" : 1548997200000, \"value\" : \"0.0\" } ] }``` or ```{ \"name\": \"sum(message_count)\", \"values\" : [\"39.0\"] }```

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | Metric name. |  [optional] |
|**values** | **List&lt;Object&gt;** | List of metric values. Possible value formats include: &#x60;\&quot;values\&quot;:[\&quot;39.0\&quot;]&#x60; or &#x60;\&quot;values\&quot;:[ { \&quot;value\&quot;: \&quot;39.0\&quot;, \&quot;timestamp\&quot;: 1232434354} ]&#x60; |  [optional] |



