

# DomainMapping

Resource to hold the state and status of a user's domain mapping. NOTE: This resource is currently in Beta.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**apiVersion** | **String** | The API version for this call such as \&quot;domains.cloudrun.com/v1\&quot;. |  [optional] |
|**kind** | **String** | The kind of resource, in this case \&quot;DomainMapping\&quot;. |  [optional] |
|**metadata** | [**ObjectMeta**](ObjectMeta.md) |  |  [optional] |
|**spec** | [**DomainMappingSpec**](DomainMappingSpec.md) |  |  [optional] |
|**status** | [**DomainMappingStatus**](DomainMappingStatus.md) |  |  [optional] |



