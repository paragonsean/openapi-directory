# StorSimple8000SeriesManagementClient.FailoverTarget

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**availableLocalStorageInBytes** | **Number** | The amount of free local storage available on the device in bytes. | [optional] 
**availableTieredStorageInBytes** | **Number** | The amount of free tiered storage available for the device in bytes. | [optional] 
**dataContainersCount** | **Number** | The count of data containers on the device. | [optional] 
**deviceId** | **String** | The path ID of the device. | [optional] 
**deviceLocation** | **String** | The geo location (applicable only for cloud appliances) of the device. | [optional] 
**deviceSoftwareVersion** | **String** | The software version of the device. | [optional] 
**deviceStatus** | **String** | The status of the device. | [optional] 
**eligibilityResult** | [**TargetEligibilityResult**](TargetEligibilityResult.md) |  | [optional] 
**friendlyDeviceSoftwareVersion** | **String** | The friendly name for the current version of software on the device. | [optional] 
**modelDescription** | **String** | The model number of the device. | [optional] 
**volumesCount** | **Number** | The count of volumes on the device. | [optional] 



## Enum: DeviceStatusEnum


* `Unknown` (value: `"Unknown"`)

* `Online` (value: `"Online"`)

* `Offline` (value: `"Offline"`)

* `Deactivated` (value: `"Deactivated"`)

* `RequiresAttention` (value: `"RequiresAttention"`)

* `MaintenanceMode` (value: `"MaintenanceMode"`)

* `Creating` (value: `"Creating"`)

* `Provisioning` (value: `"Provisioning"`)

* `Deactivating` (value: `"Deactivating"`)

* `Deleted` (value: `"Deleted"`)

* `ReadyToSetup` (value: `"ReadyToSetup"`)




