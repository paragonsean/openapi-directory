

# ServicesListSkus200ResponseValueInnerCapacity

A description of the scaling capacities of the SKU

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**_default** | **Integer** | The default capacity |  [optional] |
|**maximum** | **Integer** | The maximum capacity |  [optional] |
|**minimum** | **Integer** | The minimum capacity, usually 0 or 1. |  [optional] |
|**scaleType** | [**ScaleTypeEnum**](#ScaleTypeEnum) | The scalability approach |  [optional] |



## Enum: ScaleTypeEnum

| Name | Value |
|---- | -----|
| NONE | &quot;none&quot; |
| MANUAL | &quot;manual&quot; |
| AUTOMATIC | &quot;automatic&quot; |



