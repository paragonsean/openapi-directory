

# ResourceSkuCapacity

Describes scaling information of a SKU.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**_default** | **Integer** | The default capacity. |  [optional] [readonly] |
|**maximum** | **Integer** | The maximum capacity that can be set. |  [optional] [readonly] |
|**minimum** | **Integer** | The minimum capacity. |  [optional] [readonly] |
|**scaleType** | [**ScaleTypeEnum**](#ScaleTypeEnum) | The scale type applicable to the sku. |  [optional] [readonly] |



## Enum: ScaleTypeEnum

| Name | Value |
|---- | -----|
| AUTOMATIC | &quot;automatic&quot; |
| MANUAL | &quot;manual&quot; |
| NONE | &quot;none&quot; |



