

# VirtualTariffConsumptionData

Container class for the virtual tariff consumption

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**consumption** | **Double** | The consumption (e.g. kWh) of this tariff |  [optional] |
|**currency** | **String** | The currency of the price |  [optional] |
|**name** | **String** | The Name of this virtual tariff |  [optional] |
|**price** | **Double** | The price of the energy in this timerange |  [optional] |
|**tariffType** | [**TariffTypeEnum**](#TariffTypeEnum) | The type of the virtual tariff (e.g. solar) |  [optional] |



## Enum: TariffTypeEnum

| Name | Value |
|---- | -----|
| BATTERY | &quot;Battery&quot; |
| SOLAR | &quot;Solar&quot; |
| NORMAL | &quot;Normal&quot; |



