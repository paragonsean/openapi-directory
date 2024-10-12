

# WritableVirtualMachineWithConfigContext


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cluster** | **Integer** |  |  [optional] |
|**comments** | **String** |  |  [optional] |
|**configContext** | **Object** |  |  [optional] [readonly] |
|**created** | **OffsetDateTime** |  |  [optional] [readonly] |
|**customFields** | **Object** |  |  [optional] |
|**description** | **String** |  |  [optional] |
|**device** | **Integer** |  |  [optional] |
|**disk** | **Integer** |  |  [optional] |
|**display** | **String** |  |  [optional] [readonly] |
|**id** | **Integer** |  |  [optional] [readonly] |
|**lastUpdated** | **OffsetDateTime** |  |  [optional] [readonly] |
|**localContextData** | **Object** |  |  [optional] |
|**memory** | **Integer** |  |  [optional] |
|**name** | **String** |  |  |
|**platform** | **Integer** |  |  [optional] |
|**primaryIp** | **String** |  |  [optional] [readonly] |
|**primaryIp4** | **Integer** |  |  [optional] |
|**primaryIp6** | **Integer** |  |  [optional] |
|**role** | **Integer** |  |  [optional] |
|**site** | **Integer** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**tags** | [**List&lt;NestedTag&gt;**](NestedTag.md) |  |  [optional] |
|**tenant** | **Integer** |  |  [optional] |
|**url** | **URI** |  |  [optional] [readonly] |
|**vcpus** | **BigDecimal** |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| OFFLINE | &quot;offline&quot; |
| ACTIVE | &quot;active&quot; |
| PLANNED | &quot;planned&quot; |
| STAGED | &quot;staged&quot; |
| FAILED | &quot;failed&quot; |
| DECOMMISSIONING | &quot;decommissioning&quot; |



