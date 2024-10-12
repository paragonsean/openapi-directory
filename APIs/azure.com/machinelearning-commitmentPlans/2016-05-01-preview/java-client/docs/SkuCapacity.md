

# SkuCapacity

Describes scaling information of a SKU.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**_default** | **Long** | The default capacity. |  [optional] [readonly] |
|**maximum** | **Long** | The maximum capacity that can be set. |  [optional] [readonly] |
|**minimum** | **Long** | The minimum capacity. |  [optional] [readonly] |
|**scaleType** | [**ScaleTypeEnum**](#ScaleTypeEnum) | The scale type applicable to the sku. |  [optional] [readonly] |



## Enum: ScaleTypeEnum

| Name | Value |
|---- | -----|
| AUTOMATIC | &quot;Automatic&quot; |
| MANUAL | &quot;Manual&quot; |
| NONE | &quot;None&quot; |



