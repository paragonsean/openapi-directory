

# OutputConfigurationContainer

Configuration for the outputs of a meter (analog/digital outputs)

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**digitalOutputNoConnectionAction** | [**DigitalOutputNoConnectionActionEnum**](#DigitalOutputNoConnectionActionEnum) | The Action when the device has lost the connection |  [optional] |
|**name** | **String** | The Name of the Output |  [optional] |
|**number** | **Integer** | The number of the Output. (1 for Output 1, 2 for Output 2) |  [optional] |
|**s0PulseValue** | [**S0PulseValueEnum**](#S0PulseValueEnum) | The S0 Pulse Value |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The Type of the output |  [optional] |



## Enum: DigitalOutputNoConnectionActionEnum

| Name | Value |
|---- | -----|
| NOTHING | &quot;Nothing&quot; |
| TURN_OFF | &quot;TurnOff&quot; |
| TURN_ON | &quot;TurnOn&quot; |
| SET_PWM_VALUE | &quot;SetPwmValue&quot; |



## Enum: S0PulseValueEnum

| Name | Value |
|---- | -----|
| PULSE_VALUE1000_KWH | &quot;PulseValue1000Kwh&quot; |
| PULSE_VALUE10000_KWH | &quot;PulseValue10000Kwh&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| IMPULSE_OUTPUT_ACTIVE_ENERGY | &quot;ImpulseOutputActiveEnergy&quot; |
| IMPULSE_OUTPUT_ACTIVE_ENERGY_IMPORT | &quot;ImpulseOutputActiveEnergyImport&quot; |
| IMPULSE_OUTPUT_ACTIVE_ENERGY_EXPORT | &quot;ImpulseOutputActiveEnergyExport&quot; |
| IMPULSE_OUTPUT_REACTIVE_ENERGY | &quot;ImpulseOutputReactiveEnergy&quot; |
| DIGITAL_OUTPUT | &quot;DigitalOutput&quot; |
| ANALOG_PWM_SIGNAL_OUTPUT | &quot;AnalogPwmSignalOutput&quot; |
| DISABLED | &quot;Disabled&quot; |



