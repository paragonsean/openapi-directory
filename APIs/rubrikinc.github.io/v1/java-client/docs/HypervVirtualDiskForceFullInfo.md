

# HypervVirtualDiskForceFullInfo

Information required to request a force full snapshot for a Hyper-V virtual disk running in a Hyper-V virtual machine.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**shouldDedupe** | **Boolean** | Indicates if deduplication should be enabled for the forced full snapshot of the Virtual Disk. When set to true, deduplication is performed against local data on the Rubrik cluster. |  |
|**virtualDiskId** | **String** | ID of the virtual disk running in the Hyper-V virtual machine. |  |



