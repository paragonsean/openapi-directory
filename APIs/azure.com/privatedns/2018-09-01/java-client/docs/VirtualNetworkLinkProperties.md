

# VirtualNetworkLinkProperties

Represents the properties of the Private DNS zone.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The provisioning state of the resource. This is a read-only property and any attempt to set this value will be ignored. |  [optional] [readonly] |
|**registrationEnabled** | **Boolean** | Is auto-registration of virtual machine records in the virtual network in the Private DNS zone enabled? |  [optional] |
|**virtualNetwork** | [**SubResource**](SubResource.md) |  |  [optional] |
|**virtualNetworkLinkState** | [**VirtualNetworkLinkStateEnum**](#VirtualNetworkLinkStateEnum) | The status of the virtual network link to the Private DNS zone. Possible values are &#39;InProgress&#39; and &#39;Done&#39;. This is a read-only property and any attempt to set this value will be ignored. |  [optional] [readonly] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| CREATING | &quot;Creating&quot; |
| UPDATING | &quot;Updating&quot; |
| DELETING | &quot;Deleting&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| FAILED | &quot;Failed&quot; |
| CANCELED | &quot;Canceled&quot; |



## Enum: VirtualNetworkLinkStateEnum

| Name | Value |
|---- | -----|
| IN_PROGRESS | &quot;InProgress&quot; |
| COMPLETED | &quot;Completed&quot; |



