

# V1Beta1ConsumerQuotaMetric

Consumer quota settings for a quota metric.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**consumerQuotaLimits** | [**List&lt;V1Beta1ConsumerQuotaLimit&gt;**](V1Beta1ConsumerQuotaLimit.md) | The consumer quota for each quota limit defined on the metric. |  [optional] |
|**descendantConsumerQuotaLimits** | [**List&lt;V1Beta1ConsumerQuotaLimit&gt;**](V1Beta1ConsumerQuotaLimit.md) | The quota limits targeting the descendant containers of the consumer in request. If the consumer in request is of type &#x60;organizations&#x60; or &#x60;folders&#x60;, the field will list per-project limits in the metric; if the consumer in request is of type &#x60;project&#x60;, the field will be empty. The &#x60;quota_buckets&#x60; field of each descendant consumer quota limit will not be populated. |  [optional] |
|**displayName** | **String** | The display name of the metric. An example name would be: \&quot;CPUs\&quot; |  [optional] |
|**metric** | **String** | The name of the metric. An example name would be: &#x60;compute.googleapis.com/cpus&#x60; |  [optional] |
|**name** | **String** | The resource name of the quota settings on this metric for this consumer. An example name would be: &#x60;services/serviceconsumermanagement.googleapis.com/projects/123/consumerQuotaMetrics/compute.googleapis.com%2Fcpus&#x60; The resource name is intended to be opaque and should not be parsed for its component strings, since its representation could change in the future. |  [optional] |
|**unit** | **String** | The units in which the metric value is reported. |  [optional] |



