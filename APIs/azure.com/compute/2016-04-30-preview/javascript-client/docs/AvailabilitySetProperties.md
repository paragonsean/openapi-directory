# ComputeManagementClient.AvailabilitySetProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**managed** | **Boolean** | If the availability set supports managed disks. | [optional] 
**platformFaultDomainCount** | **Number** | Fault Domain count. | [optional] 
**platformUpdateDomainCount** | **Number** | Update Domain count. | [optional] 
**statuses** | [**[InstanceViewStatus]**](InstanceViewStatus.md) | The resource status information. | [optional] [readonly] 
**virtualMachines** | [**[SubResource]**](SubResource.md) | A list of references to all virtual machines in the availability set. | [optional] 


