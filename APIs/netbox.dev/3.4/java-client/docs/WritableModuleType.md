

# WritableModuleType


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**comments** | **String** |  |  [optional] |
|**created** | **OffsetDateTime** |  |  [optional] [readonly] |
|**customFields** | **Object** |  |  [optional] |
|**description** | **String** |  |  [optional] |
|**display** | **String** |  |  [optional] [readonly] |
|**id** | **Integer** |  |  [optional] [readonly] |
|**lastUpdated** | **OffsetDateTime** |  |  [optional] [readonly] |
|**manufacturer** | **Integer** |  |  |
|**model** | **String** |  |  |
|**partNumber** | **String** | Discrete part number (optional) |  [optional] |
|**tags** | [**List&lt;NestedTag&gt;**](NestedTag.md) |  |  [optional] |
|**url** | **URI** |  |  [optional] [readonly] |
|**weight** | **BigDecimal** |  |  [optional] |
|**weightUnit** | [**WeightUnitEnum**](#WeightUnitEnum) |  |  [optional] |



## Enum: WeightUnitEnum

| Name | Value |
|---- | -----|
| KG | &quot;kg&quot; |
| G | &quot;g&quot; |
| LB | &quot;lb&quot; |
| OZ | &quot;oz&quot; |



