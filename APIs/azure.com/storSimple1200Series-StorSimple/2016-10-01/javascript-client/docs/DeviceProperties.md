# StorSimpleManagementClient.DeviceProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activationTime** | **Date** | The UTC time at which the device was activated | [optional] 
**allowedDeviceOperations** | **[String]** | Operations that are allowed on the device based on its current state | [optional] 
**culture** | **String** | Language culture setting on the device. For eg: \&quot;en-US\&quot; | [optional] 
**details** | [**DeviceDetails**](DeviceDetails.md) |  | [optional] 
**deviceCapabilities** | **[String]** | Device can be configured either as FileServer or IscsiServer | [optional] 
**deviceConfigurationStatus** | **String** | \&quot;Complete\&quot; if the device has been successfully registered as File/IscsiServer and the creation of share/volume is complete, \&quot;Pending\&quot; if the device is only registered but the creation of share/volume is complete is still pending | [optional] 
**deviceDescription** | **String** | Short description given for the device | [optional] 
**deviceSoftwareVersion** | **String** | Version number of the software running on the device | [optional] 
**domainName** | **String** | Fully qualified name of the domain to which the device is attached | [optional] 
**friendlySoftwareName** | **String** | Friendly name for the software version | [optional] 
**modelDescription** | **String** | Name of the device model | [optional] 
**status** | **String** | Current status of the device | [optional] 
**type** | **String** | Type of the device | [optional] 



## Enum: [AllowedDeviceOperationsEnum]


* `None` (value: `"None"`)

* `Delete` (value: `"Delete"`)

* `DeleteWithWarning` (value: `"DeleteWithWarning"`)

* `DRSource` (value: `"DRSource"`)

* `DRTarget` (value: `"DRTarget"`)

* `Browsable` (value: `"Browsable"`)

* `ReadOnlyForDR` (value: `"ReadOnlyForDR"`)

* `Deactivate` (value: `"Deactivate"`)





## Enum: [DeviceCapabilitiesEnum]


* `Invalid` (value: `"Invalid"`)

* `FileServer` (value: `"FileServer"`)

* `IscsiServer` (value: `"IscsiServer"`)





## Enum: DeviceConfigurationStatusEnum


* `Complete` (value: `"Complete"`)

* `Pending` (value: `"Pending"`)





## Enum: StatusEnum


* `Unknown` (value: `"Unknown"`)

* `Online` (value: `"Online"`)

* `Offline` (value: `"Offline"`)

* `RequiresAttention` (value: `"RequiresAttention"`)

* `MaintenanceMode` (value: `"MaintenanceMode"`)

* `Creating` (value: `"Creating"`)

* `Provisioning` (value: `"Provisioning"`)

* `Deleted` (value: `"Deleted"`)

* `ReadyToSetup` (value: `"ReadyToSetup"`)

* `Deactivated` (value: `"Deactivated"`)

* `Deactivating` (value: `"Deactivating"`)





## Enum: TypeEnum


* `Invalid` (value: `"Invalid"`)

* `Appliance` (value: `"Appliance"`)

* `VirtualAppliance` (value: `"VirtualAppliance"`)

* `Series9000OnPremVirtualAppliance` (value: `"Series9000OnPremVirtualAppliance"`)

* `Series9000VirtualAppliance` (value: `"Series9000VirtualAppliance"`)

* `Series9000PhysicalAppliance` (value: `"Series9000PhysicalAppliance"`)




