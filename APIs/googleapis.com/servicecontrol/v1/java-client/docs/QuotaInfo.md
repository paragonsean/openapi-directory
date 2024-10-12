

# QuotaInfo

Contains the quota information for a quota check response.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**limitExceeded** | **List&lt;String&gt;** | Quota Metrics that have exceeded quota limits. For QuotaGroup-based quota, this is QuotaGroup.name For QuotaLimit-based quota, this is QuotaLimit.name See: google.api.Quota Deprecated: Use quota_metrics to get per quota group limit exceeded status. |  [optional] |
|**quotaConsumed** | **Map&lt;String, Integer&gt;** | Map of quota group name to the actual number of tokens consumed. If the quota check was not successful, then this will not be populated due to no quota consumption. We are not merging this field with &#39;quota_metrics&#39; field because of the complexity of scaling in Chemist client code base. For simplicity, we will keep this field for Castor (that scales quota usage) and &#39;quota_metrics&#39; for SuperQuota (that doesn&#39;t scale quota usage).  |  [optional] |
|**quotaMetrics** | [**List&lt;MetricValueSet&gt;**](MetricValueSet.md) | Quota metrics to indicate the usage. Depending on the check request, one or more of the following metrics will be included: 1. For rate quota, per quota group or per quota metric incremental usage will be specified using the following delta metric: \&quot;serviceruntime.googleapis.com/api/consumer/quota_used_count\&quot; 2. For allocation quota, per quota metric total usage will be specified using the following gauge metric: \&quot;serviceruntime.googleapis.com/allocation/consumer/quota_used_count\&quot; 3. For both rate quota and allocation quota, the quota limit reached condition will be specified using the following boolean metric: \&quot;serviceruntime.googleapis.com/quota/exceeded\&quot; |  [optional] |



