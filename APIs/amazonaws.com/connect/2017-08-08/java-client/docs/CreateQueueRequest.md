

# CreateQueueRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | The name of the queue. |  |
|**description** | **String** | The description of the queue. |  [optional] |
|**outboundCallerConfig** | [**CreateQueueRequestOutboundCallerConfig**](CreateQueueRequestOutboundCallerConfig.md) |  |  [optional] |
|**hoursOfOperationId** | **String** | The identifier for the hours of operation. |  |
|**maxContacts** | **Integer** | The maximum number of contacts that can be in the queue before it is considered full. |  [optional] |
|**quickConnectIds** | **List&lt;String&gt;** | The quick connects available to agents who are working the queue. |  [optional] |
|**tags** | **Map&lt;String, String&gt;** | The tags used to organize, track, or control access for this resource. For example, { \&quot;tags\&quot;: {\&quot;key1\&quot;:\&quot;value1\&quot;, \&quot;key2\&quot;:\&quot;value2\&quot;} }. |  [optional] |



