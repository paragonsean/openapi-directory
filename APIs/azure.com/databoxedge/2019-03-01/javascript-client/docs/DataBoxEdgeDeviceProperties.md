# DataBoxEdgeManagementClient.DataBoxEdgeDeviceProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuredRoleTypes** | **[String]** | Type of compute roles configured. | [optional] [readonly] 
**culture** | **String** | The Data Box Edge/Gateway device culture. | [optional] [readonly] 
**dataBoxEdgeDeviceStatus** | **String** | The status of the Data Box Edge/Gateway device. | [optional] 
**description** | **String** | The Description of the Data Box Edge/Gateway device. | [optional] 
**deviceHcsVersion** | **String** | The device software version number of the device (eg: 1.2.18105.6). | [optional] [readonly] 
**deviceLocalCapacity** | **Number** | The Data Box Edge/Gateway device local capacity in MB. | [optional] [readonly] 
**deviceModel** | **String** | The Data Box Edge/Gateway device model. | [optional] [readonly] 
**deviceSoftwareVersion** | **String** | The Data Box Edge/Gateway device software version. | [optional] [readonly] 
**deviceType** | **String** | The type of the Data Box Edge/Gateway device. | [optional] [readonly] 
**friendlyName** | **String** | The Data Box Edge/Gateway device name. | [optional] 
**modelDescription** | **String** | The description of the Data Box Edge/Gateway device model. | [optional] 
**serialNumber** | **String** | The Serial Number of Data Box Edge/Gateway device. | [optional] [readonly] 
**timeZone** | **String** | The Data Box Edge/Gateway device timezone. | [optional] [readonly] 



## Enum: [ConfiguredRoleTypesEnum]


* `IOT` (value: `"IOT"`)

* `ASA` (value: `"ASA"`)

* `Functions` (value: `"Functions"`)

* `Cognitive` (value: `"Cognitive"`)





## Enum: DataBoxEdgeDeviceStatusEnum


* `ReadyToSetup` (value: `"ReadyToSetup"`)

* `Online` (value: `"Online"`)

* `Offline` (value: `"Offline"`)

* `NeedsAttention` (value: `"NeedsAttention"`)

* `Disconnected` (value: `"Disconnected"`)

* `PartiallyDisconnected` (value: `"PartiallyDisconnected"`)





## Enum: DeviceTypeEnum


* `DataBoxEdgeDevice` (value: `"DataBoxEdgeDevice"`)




