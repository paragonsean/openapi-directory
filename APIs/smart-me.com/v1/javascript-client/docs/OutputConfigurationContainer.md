# SmartMe.OutputConfigurationContainer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**digitalOutputNoConnectionAction** | **String** | The Action when the device has lost the connection | [optional] 
**name** | **String** | The Name of the Output | [optional] 
**number** | **Number** | The number of the Output. (1 for Output 1, 2 for Output 2) | [optional] 
**s0PulseValue** | **String** | The S0 Pulse Value | [optional] 
**type** | **String** | The Type of the output | [optional] 



## Enum: DigitalOutputNoConnectionActionEnum


* `Nothing` (value: `"Nothing"`)

* `TurnOff` (value: `"TurnOff"`)

* `TurnOn` (value: `"TurnOn"`)

* `SetPwmValue` (value: `"SetPwmValue"`)





## Enum: S0PulseValueEnum


* `PulseValue1000Kwh` (value: `"PulseValue1000Kwh"`)

* `PulseValue10000Kwh` (value: `"PulseValue10000Kwh"`)





## Enum: TypeEnum


* `ImpulseOutputActiveEnergy` (value: `"ImpulseOutputActiveEnergy"`)

* `ImpulseOutputActiveEnergyImport` (value: `"ImpulseOutputActiveEnergyImport"`)

* `ImpulseOutputActiveEnergyExport` (value: `"ImpulseOutputActiveEnergyExport"`)

* `ImpulseOutputReactiveEnergy` (value: `"ImpulseOutputReactiveEnergy"`)

* `DigitalOutput` (value: `"DigitalOutput"`)

* `AnalogPwmSignalOutput` (value: `"AnalogPwmSignalOutput"`)

* `Disabled` (value: `"Disabled"`)




