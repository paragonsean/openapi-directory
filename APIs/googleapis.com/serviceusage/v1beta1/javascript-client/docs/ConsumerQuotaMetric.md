# ServiceUsageApi.ConsumerQuotaMetric

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consumerQuotaLimits** | [**[ConsumerQuotaLimit]**](ConsumerQuotaLimit.md) | The consumer quota for each quota limit defined on the metric. | [optional] 
**descendantConsumerQuotaLimits** | [**[ConsumerQuotaLimit]**](ConsumerQuotaLimit.md) | The quota limits targeting the descendant containers of the consumer in request. If the consumer in request is of type &#x60;organizations&#x60; or &#x60;folders&#x60;, the field will list per-project limits in the metric; if the consumer in request is of type &#x60;project&#x60;, the field will be empty. The &#x60;quota_buckets&#x60; field of each descendant consumer quota limit will not be populated. | [optional] 
**displayName** | **String** | The display name of the metric. An example name would be: &#x60;CPUs&#x60; | [optional] 
**metric** | **String** | The name of the metric. An example name would be: &#x60;compute.googleapis.com/cpus&#x60; | [optional] 
**name** | **String** | The resource name of the quota settings on this metric for this consumer. An example name would be: &#x60;projects/123/services/compute.googleapis.com/consumerQuotaMetrics/compute.googleapis.com%2Fcpus&#x60; The resource name is intended to be opaque and should not be parsed for its component strings, since its representation could change in the future. | [optional] 
**unit** | **String** | The units in which the metric value is reported. | [optional] 


