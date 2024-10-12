

# ExpressRoutePortPropertiesFormat

Properties specific to ExpressRoutePort resources.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allocationDate** | **String** | Date of the physical port allocation to be used in Letter of Authorization. |  [optional] [readonly] |
|**bandwidthInGbps** | **Integer** | Bandwidth of procured ports in Gbps. |  [optional] |
|**circuits** | [**List&lt;ExpressRoutePortPropertiesFormatCircuitsInner&gt;**](ExpressRoutePortPropertiesFormatCircuitsInner.md) | Reference the ExpressRoute circuit(s) that are provisioned on this ExpressRoutePort resource. |  [optional] [readonly] |
|**encapsulation** | [**EncapsulationEnum**](#EncapsulationEnum) | Encapsulation method on physical ports. |  [optional] |
|**etherType** | **String** | Ether type of the physical port. |  [optional] [readonly] |
|**links** | [**List&lt;ExpressRouteLink&gt;**](ExpressRouteLink.md) | The set of physical links of the ExpressRoutePort resource. |  [optional] |
|**mtu** | **String** | Maximum transmission unit of the physical port pair(s). |  [optional] [readonly] |
|**peeringLocation** | **String** | The name of the peering location that the ExpressRoutePort is mapped to physically. |  [optional] |
|**provisionedBandwidthInGbps** | **BigDecimal** | Aggregate Gbps of associated circuit bandwidths. |  [optional] [readonly] |
|**provisioningState** | **String** | The provisioning state of the ExpressRoutePort resource. Possible values are: &#39;Succeeded&#39;, &#39;Updating&#39;, &#39;Deleting&#39;, and &#39;Failed&#39;. |  [optional] [readonly] |
|**resourceGuid** | **String** | The resource GUID property of the ExpressRoutePort resource. |  [optional] |



## Enum: EncapsulationEnum

| Name | Value |
|---- | -----|
| DOT1_Q | &quot;Dot1Q&quot; |
| QIN_Q | &quot;QinQ&quot; |



