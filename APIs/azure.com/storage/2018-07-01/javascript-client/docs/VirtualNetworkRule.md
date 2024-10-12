# StorageManagementClient.VirtualNetworkRule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **String** | The action of virtual network rule. | [optional] [default to &#39;Allow&#39;]
**id** | **String** | Resource ID of a subnet, for example: /subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.Network/virtualNetworks/{vnetName}/subnets/{subnetName}. | 
**state** | **String** | Gets the state of virtual network rule. | [optional] 



## Enum: ActionEnum


* `Allow` (value: `"Allow"`)





## Enum: StateEnum


* `provisioning` (value: `"provisioning"`)

* `deprovisioning` (value: `"deprovisioning"`)

* `succeeded` (value: `"succeeded"`)

* `failed` (value: `"failed"`)

* `networkSourceDeleted` (value: `"networkSourceDeleted"`)




