# SiteRecoveryManagementClient.HyperVVirtualMachineDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**diskDetails** | [**[DiskDetails]**](DiskDetails.md) | The Last successful failover time. | [optional] 
**generation** | **String** | The id of the object in fabric. | [optional] 
**hasFibreChannelAdapter** | **String** | A value indicating whether the VM has a fibre channel adapter attached. String value of {SrsDataContract.PresenceStatus} enum. | [optional] 
**hasPhysicalDisk** | **String** | A value indicating whether the VM has a physical disk attached. String value of {SrsDataContract.PresenceStatus} enum. | [optional] 
**hasSharedVhd** | **String** | A value indicating whether the VM has a shared VHD attached. String value of {SrsDataContract.PresenceStatus} enum. | [optional] 
**osDetails** | [**OSDetails**](OSDetails.md) |  | [optional] 
**sourceItemId** | **String** | The source id of the object. | [optional] 



## Enum: HasFibreChannelAdapterEnum


* `Unknown` (value: `"Unknown"`)

* `Present` (value: `"Present"`)

* `NotPresent` (value: `"NotPresent"`)





## Enum: HasPhysicalDiskEnum


* `Unknown` (value: `"Unknown"`)

* `Present` (value: `"Present"`)

* `NotPresent` (value: `"NotPresent"`)





## Enum: HasSharedVhdEnum


* `Unknown` (value: `"Unknown"`)

* `Present` (value: `"Present"`)

* `NotPresent` (value: `"NotPresent"`)




