# StorSimple8000SeriesManagementClient.DeviceProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activationTime** | **Date** | The UTC time at which the device was activated | 
**activeController** | **String** | The identifier of the active controller of the device. | 
**agentGroupVersion** | **Number** | The device agent group version. | [optional] 
**availableLocalStorageInBytes** | **Number** | The storage in bytes that is available locally on the device. | [optional] 
**availableTieredStorageInBytes** | **Number** | The storage in bytes that is available on the device for tiered volumes. | [optional] 
**culture** | **String** | The language culture setting on the device. For eg: \&quot;en-US\&quot; | 
**details** | [**DeviceDetails**](DeviceDetails.md) |  | [optional] 
**deviceConfigurationStatus** | **String** | The current configuration status of the device. | 
**deviceDescription** | **String** | The device description. | 
**deviceLocation** | **String** | The location of the virtual appliance. | [optional] 
**deviceSoftwareVersion** | **String** | The version number of the software running on the device. | 
**deviceType** | **String** | The type of the device. | 
**friendlyName** | **String** | The friendly name of the device. | 
**friendlySoftwareName** | **String** | The friendly name of the software running on the device. | [optional] 
**friendlySoftwareVersion** | **String** | The device friendly software version. | 
**modelDescription** | **String** | The device model. | 
**networkInterfaceCardCount** | **Number** | The number of network interface cards | [optional] 
**provisionedLocalStorageInBytes** | **Number** | The storage in bytes used for locally pinned volumes on the device (including additional local reservation). | [optional] 
**provisionedTieredStorageInBytes** | **Number** | The storage in bytes that has been provisioned on the device for tiered volumes. | [optional] 
**provisionedVolumeSizeInBytes** | **Number** | Total capacity in bytes of tiered and locally pinned volumes on the device | [optional] 
**rolloverDetails** | [**DeviceRolloverDetails**](DeviceRolloverDetails.md) |  | [optional] 
**serialNumber** | **String** | The serial number. | 
**status** | **String** | The current status of the device. | 
**targetIqn** | **String** | The target IQN. | 
**totalTieredStorageInBytes** | **Number** | The total tiered storage available on the device in bytes. | [optional] 
**usingStorageInBytes** | **Number** | The storage in bytes that is currently being used on the device, including both local and cloud. | [optional] 
**virtualMachineApiType** | **String** | The virtual machine API type. | [optional] [readonly] 



## Enum: ActiveControllerEnum


* `Unknown` (value: `"Unknown"`)

* `None` (value: `"None"`)

* `Controller0` (value: `"Controller0"`)

* `Controller1` (value: `"Controller1"`)





## Enum: DeviceConfigurationStatusEnum


* `Complete` (value: `"Complete"`)

* `Pending` (value: `"Pending"`)





## Enum: DeviceTypeEnum


* `Invalid` (value: `"Invalid"`)

* `Series8000VirtualAppliance` (value: `"Series8000VirtualAppliance"`)

* `Series8000PhysicalAppliance` (value: `"Series8000PhysicalAppliance"`)





## Enum: StatusEnum


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





## Enum: VirtualMachineApiTypeEnum


* `Classic` (value: `"Classic"`)

* `Arm` (value: `"Arm"`)




