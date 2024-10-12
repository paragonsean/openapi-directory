

# WritableIPRange


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**children** | **Integer** |  |  [optional] [readonly] |
|**comments** | **String** |  |  [optional] |
|**created** | **OffsetDateTime** |  |  [optional] [readonly] |
|**customFields** | **Object** |  |  [optional] |
|**description** | **String** |  |  [optional] |
|**display** | **String** |  |  [optional] [readonly] |
|**endAddress** | **String** | IPv4 or IPv6 address (with mask) |  |
|**family** | **String** |  |  [optional] [readonly] |
|**id** | **Integer** |  |  [optional] [readonly] |
|**lastUpdated** | **OffsetDateTime** |  |  [optional] [readonly] |
|**role** | **Integer** | The primary function of this range |  [optional] |
|**size** | **Integer** |  |  [optional] [readonly] |
|**startAddress** | **String** | IPv4 or IPv6 address (with mask) |  |
|**status** | [**StatusEnum**](#StatusEnum) | Operational status of this range |  [optional] |
|**tags** | [**List&lt;NestedTag&gt;**](NestedTag.md) |  |  [optional] |
|**tenant** | **Integer** |  |  [optional] |
|**url** | **URI** |  |  [optional] [readonly] |
|**vrf** | **Integer** |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| RESERVED | &quot;reserved&quot; |
| DEPRECATED | &quot;deprecated&quot; |



