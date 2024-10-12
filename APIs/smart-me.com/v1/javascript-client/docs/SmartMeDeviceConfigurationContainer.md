# SmartMe.SmartMeDeviceConfigurationContainer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deviceEncryptionKey** | **String** | The encryption key used to decrypt messages received from an external meter (used only for the smart-me modules) | [optional] 
**devicePinCode** | **String** | PIN code to enter on a external meter (e.g. for the FNN meters) | [optional] 
**dnsUpdateState** | **String** | Configuration of the dynamic DNS service. More information: http://wiki.smart-me.com/index.php/Dynamisches_DNS | [optional] 
**enableModbusTcp** | **Boolean** | Enables or disables Modbus TCP (if the meter supports it). | [optional] 
**id** | **String** | The ID of the device | [optional] 
**inputConfiguration** | [**[InputConfigurationContainer]**](InputConfigurationContainer.md) | The configuration for the intput outputs | [optional] 
**outputConfiguration** | [**[OutputConfigurationContainer]**](OutputConfigurationContainer.md) | The configuration for the external outputs | [optional] 
**showReactiveEnergy** | **Boolean** | Shows the reactive energy values (if the meter supports it). | [optional] 
**switchConfiguration** | [**[SwitchConfigurationContainer]**](SwitchConfigurationContainer.md) | The configuration for the phase switches | [optional] 
**uploadInterval** | **String** | Number of seconds the device will upload the data. For smaller values maybe a professional license is needed. | [optional] 



## Enum: DnsUpdateStateEnum


* `NoUpdate` (value: `"NoUpdate"`)

* `DnsUpdatePublicIp` (value: `"DnsUpdatePublicIp"`)

* `DnsUpdateInternalIp` (value: `"DnsUpdateInternalIp"`)





## Enum: UploadIntervalEnum


* `1s` (value: `"UploadInterval_1s"`)

* `5s` (value: `"UploadInterval_5s"`)

* `10s` (value: `"UploadInterval_10s"`)

* `30s` (value: `"UploadInterval_30s"`)

* `60s` (value: `"UploadInterval_60s"`)

* `5min` (value: `"UploadInterval_5min"`)

* `15min` (value: `"UploadInterval_15min"`)

* `30min` (value: `"UploadInterval_30min"`)

* `60min` (value: `"UploadInterval_60min"`)

* `6h` (value: `"UploadInterval_6h"`)

* `12h` (value: `"UploadInterval_12h"`)

* `24h` (value: `"UploadInterval_24h"`)




