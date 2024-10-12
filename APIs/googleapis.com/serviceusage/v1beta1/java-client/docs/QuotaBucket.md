

# QuotaBucket

A quota bucket is a quota provisioning unit for a specific set of dimensions.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adminOverride** | [**QuotaOverride**](QuotaOverride.md) |  |  [optional] |
|**consumerOverride** | [**QuotaOverride**](QuotaOverride.md) |  |  [optional] |
|**defaultLimit** | **String** | The default limit of this quota bucket, as specified by the service configuration. |  [optional] |
|**dimensions** | **Map&lt;String, String&gt;** | The dimensions of this quota bucket. If this map is empty, this is the global bucket, which is the default quota value applied to all requests that do not have a more specific override. If this map is nonempty, the default limit, effective limit, and quota overrides apply only to requests that have the dimensions given in the map. For example, if the map has key &#x60;region&#x60; and value &#x60;us-east-1&#x60;, then the specified effective limit is only effective in that region, and the specified overrides apply only in that region. |  [optional] |
|**effectiveLimit** | **String** | The effective limit of this quota bucket. Equal to default_limit if there are no overrides. |  [optional] |
|**producerOverride** | [**QuotaOverride**](QuotaOverride.md) |  |  [optional] |
|**producerQuotaPolicy** | [**ProducerQuotaPolicy**](ProducerQuotaPolicy.md) |  |  [optional] |



