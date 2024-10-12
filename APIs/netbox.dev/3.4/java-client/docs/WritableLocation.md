

# WritableLocation


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**depth** | **Integer** |  |  [optional] [readonly] |
|**created** | **OffsetDateTime** |  |  [optional] [readonly] |
|**customFields** | **Object** |  |  [optional] |
|**description** | **String** |  |  [optional] |
|**deviceCount** | **Integer** |  |  [optional] [readonly] |
|**display** | **String** |  |  [optional] [readonly] |
|**id** | **Integer** |  |  [optional] [readonly] |
|**lastUpdated** | **OffsetDateTime** |  |  [optional] [readonly] |
|**name** | **String** |  |  |
|**parent** | **Integer** |  |  [optional] |
|**rackCount** | **Integer** |  |  [optional] [readonly] |
|**site** | **Integer** |  |  |
|**slug** | **String** |  |  |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**tags** | [**List&lt;NestedTag&gt;**](NestedTag.md) |  |  [optional] |
|**tenant** | **Integer** |  |  [optional] |
|**url** | **URI** |  |  [optional] [readonly] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PLANNED | &quot;planned&quot; |
| STAGING | &quot;staging&quot; |
| ACTIVE | &quot;active&quot; |
| DECOMMISSIONING | &quot;decommissioning&quot; |
| RETIRED | &quot;retired&quot; |



