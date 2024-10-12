

# VmwareVsphereConfig

VmwareVsphereConfig represents configuration for the VMware VCenter for node pool.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**datastore** | **String** | The name of the vCenter datastore. Inherited from the user cluster. |  [optional] |
|**hostGroups** | **List&lt;String&gt;** | Vsphere host groups to apply to all VMs in the node pool |  [optional] |
|**tags** | [**List&lt;VmwareVsphereTag&gt;**](VmwareVsphereTag.md) | Tags to apply to VMs. |  [optional] |



