

# VirtualTariff


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**factor** | **Double** | Says how many of the active power is used in this tariff. This is calculated from the last meter values. |  [optional] |
|**id** | **String** |  |  [optional] |
|**name** | **String** |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  [optional] |
|**unit** | **String** |  |  [optional] |
|**value** | **Double** | The Counter Value of this tariff |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| BATTERY | &quot;Battery&quot; |
| SOLAR | &quot;Solar&quot; |
| NORMAL | &quot;Normal&quot; |



