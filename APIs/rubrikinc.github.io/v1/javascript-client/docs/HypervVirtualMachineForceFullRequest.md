# RubrikRestApi.HypervVirtualMachineForceFullRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**virtualDiskInfos** | [**[HypervVirtualDiskForceFullInfo]**](HypervVirtualDiskForceFullInfo.md) | Configuration to force a full snapshot for the virtual disks listed in the request. The configuration specifies which virtual disks in HyperV VM receive forced full snapshots, and whether to perform deduplication. If the configuration is missing, a forced full snapshot is not requested. If the configuration contains an empty array, a forced full snapshot is requested for all virtual disks in the HyperV virtual machine, and deduplication is performed by default. If the configuration array contains specific virtual disks, a forced full snapshot is requested only for these disks. The shouldDedupe flag determines if deduplication is performed. If a forced full snapshot is requested, the next backup job checks the configuration and takes the full snapshot according to the configuration. After the full snapshot is taken, the backup job clears the configuration to prevent additional full snapshots from being taken. | [optional] 


