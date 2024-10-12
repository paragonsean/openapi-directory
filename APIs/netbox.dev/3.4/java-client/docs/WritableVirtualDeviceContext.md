

# WritableVirtualDeviceContext


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**comments** | **String** |  |  [optional] |
|**created** | **OffsetDateTime** |  |  [optional] [readonly] |
|**customFields** | **Object** |  |  [optional] |
|**description** | **String** |  |  [optional] |
|**device** | **Integer** |  |  [optional] |
|**display** | **String** |  |  [optional] [readonly] |
|**id** | **Integer** |  |  [optional] [readonly] |
|**identifier** | **Integer** | Numeric identifier unique to the parent device |  [optional] |
|**interfaceCount** | **Integer** |  |  [optional] [readonly] |
|**lastUpdated** | **OffsetDateTime** |  |  [optional] [readonly] |
|**name** | **String** |  |  |
|**primaryIp** | **String** |  |  [optional] [readonly] |
|**primaryIp4** | **Integer** |  |  [optional] |
|**primaryIp6** | **Integer** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  |
|**tags** | [**List&lt;NestedTag&gt;**](NestedTag.md) |  |  [optional] |
|**tenant** | **Integer** |  |  [optional] |
|**url** | **URI** |  |  [optional] [readonly] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| PLANNED | &quot;planned&quot; |
| OFFLINE | &quot;offline&quot; |



