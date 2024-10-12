

# WritableModule


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**assetTag** | **String** | A unique tag used to identify this device |  [optional] |
|**comments** | **String** |  |  [optional] |
|**created** | **OffsetDateTime** |  |  [optional] [readonly] |
|**customFields** | **Object** |  |  [optional] |
|**description** | **String** |  |  [optional] |
|**device** | **Integer** |  |  |
|**display** | **String** |  |  [optional] [readonly] |
|**id** | **Integer** |  |  [optional] [readonly] |
|**lastUpdated** | **OffsetDateTime** |  |  [optional] [readonly] |
|**moduleBay** | **Integer** |  |  |
|**moduleType** | **Integer** |  |  |
|**serial** | **String** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**tags** | [**List&lt;NestedTag&gt;**](NestedTag.md) |  |  [optional] |
|**url** | **URI** |  |  [optional] [readonly] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| OFFLINE | &quot;offline&quot; |
| ACTIVE | &quot;active&quot; |
| PLANNED | &quot;planned&quot; |
| STAGED | &quot;staged&quot; |
| FAILED | &quot;failed&quot; |
| DECOMMISSIONING | &quot;decommissioning&quot; |



