# NetworkManagementClient.ExpressRoutePortPropertiesFormat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocationDate** | **String** | Date of the physical port allocation to be used in Letter of Authorization. | [optional] [readonly] 
**bandwidthInGbps** | **Number** | Bandwidth of procured ports in Gbps. | [optional] 
**circuits** | [**[ExpressRoutePortPropertiesFormatCircuitsInner]**](ExpressRoutePortPropertiesFormatCircuitsInner.md) | Reference the ExpressRoute circuit(s) that are provisioned on this ExpressRoutePort resource. | [optional] [readonly] 
**encapsulation** | **String** | Encapsulation method on physical ports. | [optional] 
**etherType** | **String** | Ether type of the physical port. | [optional] [readonly] 
**links** | [**[ExpressRouteLink]**](ExpressRouteLink.md) | The set of physical links of the ExpressRoutePort resource. | [optional] 
**mtu** | **String** | Maximum transmission unit of the physical port pair(s). | [optional] [readonly] 
**peeringLocation** | **String** | The name of the peering location that the ExpressRoutePort is mapped to physically. | [optional] 
**provisionedBandwidthInGbps** | **Number** | Aggregate Gbps of associated circuit bandwidths. | [optional] [readonly] 
**provisioningState** | **String** | The current provisioning state. | [optional] [readonly] 
**resourceGuid** | **String** | The resource GUID property of the express route port resource. | [optional] 



## Enum: EncapsulationEnum


* `Dot1Q` (value: `"Dot1Q"`)

* `QinQ` (value: `"QinQ"`)





## Enum: ProvisioningStateEnum


* `Succeeded` (value: `"Succeeded"`)

* `Updating` (value: `"Updating"`)

* `Deleting` (value: `"Deleting"`)

* `Failed` (value: `"Failed"`)




