

# WritableCluster


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**comments** | **String** |  |  [optional] |
|**created** | **OffsetDateTime** |  |  [optional] [readonly] |
|**customFields** | **Object** |  |  [optional] |
|**description** | **String** |  |  [optional] |
|**deviceCount** | **Integer** |  |  [optional] [readonly] |
|**display** | **String** |  |  [optional] [readonly] |
|**group** | **Integer** |  |  [optional] |
|**id** | **Integer** |  |  [optional] [readonly] |
|**lastUpdated** | **OffsetDateTime** |  |  [optional] [readonly] |
|**name** | **String** |  |  |
|**site** | **Integer** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**tags** | [**List&lt;NestedTag&gt;**](NestedTag.md) |  |  [optional] |
|**tenant** | **Integer** |  |  [optional] |
|**type** | **Integer** |  |  |
|**url** | **URI** |  |  [optional] [readonly] |
|**virtualmachineCount** | **Integer** |  |  [optional] [readonly] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PLANNED | &quot;planned&quot; |
| STAGING | &quot;staging&quot; |
| ACTIVE | &quot;active&quot; |
| DECOMMISSIONING | &quot;decommissioning&quot; |
| OFFLINE | &quot;offline&quot; |



