# PrivateDnsManagementClient.VirtualNetworkLinkProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provisioningState** | **String** | The provisioning state of the resource. This is a read-only property and any attempt to set this value will be ignored. | [optional] [readonly] 
**registrationEnabled** | **Boolean** | Is auto-registration of virtual machine records in the virtual network in the Private DNS zone enabled? | [optional] 
**virtualNetwork** | [**SubResource**](SubResource.md) |  | [optional] 
**virtualNetworkLinkState** | **String** | The status of the virtual network link to the Private DNS zone. Possible values are &#39;InProgress&#39; and &#39;Done&#39;. This is a read-only property and any attempt to set this value will be ignored. | [optional] [readonly] 



## Enum: ProvisioningStateEnum


* `Creating` (value: `"Creating"`)

* `Updating` (value: `"Updating"`)

* `Deleting` (value: `"Deleting"`)

* `Succeeded` (value: `"Succeeded"`)

* `Failed` (value: `"Failed"`)

* `Canceled` (value: `"Canceled"`)





## Enum: VirtualNetworkLinkStateEnum


* `InProgress` (value: `"InProgress"`)

* `Completed` (value: `"Completed"`)




