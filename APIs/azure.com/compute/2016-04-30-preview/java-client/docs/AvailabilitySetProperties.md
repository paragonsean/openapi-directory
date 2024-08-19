

# AvailabilitySetProperties

The instance view of a resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**managed** | **Boolean** | If the availability set supports managed disks. |  [optional] |
|**platformFaultDomainCount** | **Integer** | Fault Domain count. |  [optional] |
|**platformUpdateDomainCount** | **Integer** | Update Domain count. |  [optional] |
|**statuses** | [**List&lt;InstanceViewStatus&gt;**](InstanceViewStatus.md) | The resource status information. |  [optional] [readonly] |
|**virtualMachines** | [**List&lt;SubResource&gt;**](SubResource.md) | A list of references to all virtual machines in the availability set. |  [optional] |



