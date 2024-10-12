# ManagedNetworkManagementClient.HubAndSpokePeeringPolicyProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hub** | [**ResourceId**](ResourceId.md) |  | [optional] 
**spokes** | [**[ResourceId]**](ResourceId.md) | Gets or sets the spokes group IDs | [optional] 
**mesh** | [**[ResourceId]**](ResourceId.md) | Gets or sets the mesh group IDs | [optional] 
**type** | **String** | Gets or sets the connectivity type of a network structure policy | 
**etag** | **String** | A unique read-only string that changes whenever the resource is updated. | [optional] [readonly] 
**provisioningState** | **String** | Provisioning state of the ManagedNetwork resource. | [optional] [readonly] 



## Enum: TypeEnum


* `HubAndSpokeTopology` (value: `"HubAndSpokeTopology"`)

* `MeshTopology` (value: `"MeshTopology"`)





## Enum: ProvisioningStateEnum


* `Updating` (value: `"Updating"`)

* `Deleting` (value: `"Deleting"`)

* `Failed` (value: `"Failed"`)

* `Succeeded` (value: `"Succeeded"`)




