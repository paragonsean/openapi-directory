# RubrikRestApi.HypervVirtualMachineForceFullResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**virtualDiskInfos** | [**[HypervVirtualDiskForceFullInfo]**](HypervVirtualDiskForceFullInfo.md) | Configuration for each virtual disk that requested a forced full snapshot. If the configuration does not exist, either a forced full snapshot was not requested for the HyperV virtual machine, or a backup job took the requested full snapshot and cleared the configuration. | [optional] 
**vmId** | **String** | ID of the Hyper-V virtual machine containing all virtual disks. | 


