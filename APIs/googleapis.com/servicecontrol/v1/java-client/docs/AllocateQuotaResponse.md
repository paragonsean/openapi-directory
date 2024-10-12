

# AllocateQuotaResponse

Response message for the AllocateQuota method.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allocateErrors** | [**List&lt;QuotaError&gt;**](QuotaError.md) | Indicates the decision of the allocate. |  [optional] |
|**allocateInfo** | [**AllocateInfo**](AllocateInfo.md) |  |  [optional] |
|**operationId** | **String** | The same operation_id value used in the AllocateQuotaRequest. Used for logging and diagnostics purposes. |  [optional] |
|**quotaMetrics** | [**List&lt;MetricValueSet&gt;**](MetricValueSet.md) | Quota metrics to indicate the result of allocation. Depending on the request, one or more of the following metrics will be included: 1. Per quota group or per quota metric incremental usage will be specified using the following delta metric : \&quot;serviceruntime.googleapis.com/api/consumer/quota_used_count\&quot; 2. The quota limit reached condition will be specified using the following boolean metric : \&quot;serviceruntime.googleapis.com/quota/exceeded\&quot; |  [optional] |
|**serviceConfigId** | **String** | ID of the actual config used to process the request. |  [optional] |



