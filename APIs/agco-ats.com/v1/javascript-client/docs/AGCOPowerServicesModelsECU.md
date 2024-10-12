# AgcoApi.AGCOPowerServicesModelsECU

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activationCode** | **Blob** | The code used to activate the ECU. May not be modified. Returned only on activation. | [optional] 
**damagedDescription** | **String** | A description why the ECU cannot be deactivated. | [optional] 
**engineSerialNumber** | **String** | The serial number of the ECU’s engine | 
**replacesECUSerialNumber** | **String** | The serial number of the ECU that this ECU replaces. Required if activating an ECU.. | [optional] 
**serialNumber** | **String** | The serial number of the ECU | 
**state** | **String** | The state of the ECU | 



## Enum: StateEnum


* `Active` (value: `"Active"`)

* `Inactive` (value: `"Inactive"`)

* `Damaged` (value: `"Damaged"`)




