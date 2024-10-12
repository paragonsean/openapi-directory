

# ConsumerQuotaLimit

Consumer quota settings for a quota limit.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowsAdminOverrides** | **Boolean** | Whether admin overrides are allowed on this limit |  [optional] |
|**isPrecise** | **Boolean** | Whether this limit is precise or imprecise. |  [optional] |
|**metric** | **String** | The name of the parent metric of this limit. An example name would be: &#x60;compute.googleapis.com/cpus&#x60; |  [optional] |
|**name** | **String** | The resource name of the quota limit. An example name would be: &#x60;projects/123/services/compute.googleapis.com/consumerQuotaMetrics/compute.googleapis.com%2Fcpus/limits/%2Fproject%2Fregion&#x60; The resource name is intended to be opaque and should not be parsed for its component strings, since its representation could change in the future. |  [optional] |
|**quotaBuckets** | [**List&lt;QuotaBucket&gt;**](QuotaBucket.md) | Summary of the enforced quota buckets, organized by quota dimension, ordered from least specific to most specific (for example, the global default bucket, with no quota dimensions, will always appear first). |  [optional] |
|**supportedLocations** | **List&lt;String&gt;** | List of all supported locations. This field is present only if the limit has a {region} or {zone} dimension. |  [optional] |
|**unit** | **String** | The limit unit. An example unit would be &#x60;1/{project}/{region}&#x60; Note that &#x60;{project}&#x60; and &#x60;{region}&#x60; are not placeholders in this example; the literal characters &#x60;{&#x60; and &#x60;}&#x60; occur in the string. |  [optional] |



