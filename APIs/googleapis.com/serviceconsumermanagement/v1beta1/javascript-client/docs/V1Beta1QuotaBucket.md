# ServiceConsumerManagementApi.V1Beta1QuotaBucket

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adminOverride** | [**V1Beta1QuotaOverride**](V1Beta1QuotaOverride.md) |  | [optional] 
**consumerOverride** | [**V1Beta1QuotaOverride**](V1Beta1QuotaOverride.md) |  | [optional] 
**defaultLimit** | **String** | The default limit of this quota bucket, as specified by the service configuration. | [optional] 
**dimensions** | **{String: String}** | The dimensions of this quota bucket. If this map is empty, this is the global bucket, which is the default quota value applied to all requests that do not have a more specific override. If this map is nonempty, the default limit, effective limit, and quota overrides apply only to requests that have the dimensions given in the map. For example, if the map has key \&quot;region\&quot; and value \&quot;us-east-1\&quot;, then the specified effective limit is only effective in that region, and the specified overrides apply only in that region. | [optional] 
**effectiveLimit** | **String** | The effective limit of this quota bucket. Equal to default_limit if there are no overrides. | [optional] 
**producerOverride** | [**V1Beta1QuotaOverride**](V1Beta1QuotaOverride.md) |  | [optional] 
**producerQuotaPolicy** | [**V1Beta1ProducerQuotaPolicy**](V1Beta1ProducerQuotaPolicy.md) |  | [optional] 


