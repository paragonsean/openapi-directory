

# WritableVirtualMachineWithConfigContext


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cluster** | **Integer** |  |  |
|**comments** | **String** |  |  [optional] |
|**configContext** | **Map&lt;String, String&gt;** |  |  [optional] [readonly] |
|**created** | **LocalDate** |  |  [optional] [readonly] |
|**customFields** | **Object** |  |  [optional] |
|**disk** | **Integer** |  |  [optional] |
|**id** | **Integer** |  |  [optional] [readonly] |
|**lastUpdated** | **OffsetDateTime** |  |  [optional] [readonly] |
|**localContextData** | **String** |  |  [optional] |
|**memory** | **Integer** |  |  [optional] |
|**name** | **String** |  |  |
|**platform** | **Integer** |  |  [optional] |
|**primaryIp** | **String** |  |  [optional] [readonly] |
|**primaryIp4** | **Integer** |  |  [optional] |
|**primaryIp6** | **Integer** |  |  [optional] |
|**role** | **Integer** |  |  [optional] |
|**site** | **String** |  |  [optional] [readonly] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**tags** | **List&lt;String&gt;** |  |  [optional] |
|**tenant** | **Integer** |  |  [optional] |
|**vcpus** | **Integer** |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| OFFLINE | &quot;offline&quot; |
| ACTIVE | &quot;active&quot; |
| PLANNED | &quot;planned&quot; |
| STAGED | &quot;staged&quot; |
| FAILED | &quot;failed&quot; |
| DECOMMISSIONING | &quot;decommissioning&quot; |



