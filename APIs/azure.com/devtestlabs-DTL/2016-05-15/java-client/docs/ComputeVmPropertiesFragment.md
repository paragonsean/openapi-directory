

# ComputeVmPropertiesFragment

Properties of a virtual machine returned by the Microsoft.Compute API.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataDiskIds** | **List&lt;String&gt;** | Gets data disks blob uri for the virtual machine. |  [optional] |
|**dataDisks** | [**List&lt;ComputeDataDiskFragment&gt;**](ComputeDataDiskFragment.md) | Gets all data disks attached to the virtual machine. |  [optional] |
|**networkInterfaceId** | **String** | Gets the network interface ID of the virtual machine. |  [optional] |
|**osDiskId** | **String** | Gets OS disk blob uri for the virtual machine. |  [optional] |
|**osType** | **String** | Gets the OS type of the virtual machine. |  [optional] |
|**statuses** | [**List&lt;ComputeVmInstanceViewStatusFragment&gt;**](ComputeVmInstanceViewStatusFragment.md) | Gets the statuses of the virtual machine. |  [optional] |
|**vmSize** | **String** | Gets the size of the virtual machine. |  [optional] |



