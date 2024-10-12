

# ListDomainMappingsResponse

ListDomainMappingsResponse is a list of DomainMapping resources.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**apiVersion** | **String** | The API version for this call such as \&quot;domains.cloudrun.com/v1\&quot;. |  [optional] |
|**items** | [**List&lt;DomainMapping&gt;**](DomainMapping.md) | List of DomainMappings. |  [optional] |
|**kind** | **String** | The kind of this resource, in this case \&quot;DomainMappingList\&quot;. |  [optional] |
|**metadata** | [**ListMeta**](ListMeta.md) |  |  [optional] |
|**unreachable** | **List&lt;String&gt;** | Locations that could not be reached. |  [optional] |



