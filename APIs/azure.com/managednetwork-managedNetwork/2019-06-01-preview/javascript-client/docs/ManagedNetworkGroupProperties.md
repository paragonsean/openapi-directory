# ManagedNetworkManagementClient.ManagedNetworkGroupProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**managementGroups** | [**[ResourceId]**](ResourceId.md) | The collection of management groups covered by the Managed Network | [optional] 
**subnets** | [**[ResourceId]**](ResourceId.md) | The collection of  subnets covered by the Managed Network | [optional] 
**subscriptions** | [**[ResourceId]**](ResourceId.md) | The collection of subscriptions covered by the Managed Network | [optional] 
**virtualNetworks** | [**[ResourceId]**](ResourceId.md) | The collection of virtual nets covered by the Managed Network | [optional] 
**etag** | **String** | A unique read-only string that changes whenever the resource is updated. | [optional] [readonly] 
**provisioningState** | **String** | Provisioning state of the ManagedNetwork resource. | [optional] [readonly] 



## Enum: ProvisioningStateEnum


* `Updating` (value: `"Updating"`)

* `Deleting` (value: `"Deleting"`)

* `Failed` (value: `"Failed"`)

* `Succeeded` (value: `"Succeeded"`)




