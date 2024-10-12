

# WritableVLAN


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**comments** | **String** |  |  [optional] |
|**created** | **OffsetDateTime** |  |  [optional] [readonly] |
|**customFields** | **Object** |  |  [optional] |
|**description** | **String** |  |  [optional] |
|**display** | **String** |  |  [optional] [readonly] |
|**group** | **Integer** |  |  [optional] |
|**id** | **Integer** |  |  [optional] [readonly] |
|**l2vpnTermination** | **String** |  |  [optional] [readonly] |
|**lastUpdated** | **OffsetDateTime** |  |  [optional] [readonly] |
|**name** | **String** |  |  |
|**prefixCount** | **Integer** |  |  [optional] [readonly] |
|**role** | **Integer** |  |  [optional] |
|**site** | **Integer** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**tags** | [**List&lt;NestedTag&gt;**](NestedTag.md) |  |  [optional] |
|**tenant** | **Integer** |  |  [optional] |
|**url** | **URI** |  |  [optional] [readonly] |
|**vid** | **Integer** |  |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| RESERVED | &quot;reserved&quot; |
| DEPRECATED | &quot;deprecated&quot; |



