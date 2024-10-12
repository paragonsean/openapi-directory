

# WritablePrefix


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**depth** | **Integer** |  |  [optional] [readonly] |
|**children** | **Integer** |  |  [optional] [readonly] |
|**comments** | **String** |  |  [optional] |
|**created** | **OffsetDateTime** |  |  [optional] [readonly] |
|**customFields** | **Object** |  |  [optional] |
|**description** | **String** |  |  [optional] |
|**display** | **String** |  |  [optional] [readonly] |
|**family** | **String** |  |  [optional] [readonly] |
|**id** | **Integer** |  |  [optional] [readonly] |
|**isPool** | **Boolean** | All IP addresses within this prefix are considered usable |  [optional] |
|**lastUpdated** | **OffsetDateTime** |  |  [optional] [readonly] |
|**markUtilized** | **Boolean** | Treat as 100% utilized |  [optional] |
|**prefix** | **String** | IPv4 or IPv6 network with mask |  |
|**role** | **Integer** | The primary function of this prefix |  [optional] |
|**site** | **Integer** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Operational status of this prefix |  [optional] |
|**tags** | [**List&lt;NestedTag&gt;**](NestedTag.md) |  |  [optional] |
|**tenant** | **Integer** |  |  [optional] |
|**url** | **URI** |  |  [optional] [readonly] |
|**vlan** | **Integer** |  |  [optional] |
|**vrf** | **Integer** |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| CONTAINER | &quot;container&quot; |
| ACTIVE | &quot;active&quot; |
| RESERVED | &quot;reserved&quot; |
| DEPRECATED | &quot;deprecated&quot; |



