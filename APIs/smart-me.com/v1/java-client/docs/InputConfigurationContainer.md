

# InputConfigurationContainer

Configuration for the input of a meter (digital inputs)

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | The Name of the Input |  [optional] |
|**number** | **Integer** | The number of the Input. (1 for Input 1) |  [optional] |
|**offText** | **String** | The visualization text for an OFF action |  [optional] |
|**onText** | **String** | The visualization text for an ON action |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The Type of the output |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TARIFF_INPUT | &quot;TariffInput&quot; |
| DIGITAL_INPUT | &quot;DigitalInput&quot; |



