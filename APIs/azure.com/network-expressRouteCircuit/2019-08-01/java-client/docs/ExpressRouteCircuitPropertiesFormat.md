

# ExpressRouteCircuitPropertiesFormat

Properties of ExpressRouteCircuit.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowClassicOperations** | **Boolean** | Allow classic operations. |  [optional] |
|**authorizations** | [**List&lt;ExpressRouteCircuitAuthorization&gt;**](ExpressRouteCircuitAuthorization.md) | The list of authorizations. |  [optional] |
|**bandwidthInGbps** | **BigDecimal** | The bandwidth of the circuit when the circuit is provisioned on an ExpressRoutePort resource. |  [optional] |
|**circuitProvisioningState** | **String** | The CircuitProvisioningState state of the resource. |  [optional] |
|**expressRoutePort** | [**ExpressRouteCircuitConnectionPropertiesFormatExpressRouteCircuitPeering**](ExpressRouteCircuitConnectionPropertiesFormatExpressRouteCircuitPeering.md) |  |  [optional] |
|**gatewayManagerEtag** | **String** | The GatewayManager Etag. |  [optional] |
|**globalReachEnabled** | **Boolean** | Flag denoting Global reach status. |  [optional] |
|**peerings** | [**List&lt;ExpressRouteCircuitPeering&gt;**](ExpressRouteCircuitPeering.md) | The list of peerings. |  [optional] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The current provisioning state. |  [optional] [readonly] |
|**serviceKey** | **String** | The ServiceKey. |  [optional] |
|**serviceProviderNotes** | **String** | The ServiceProviderNotes. |  [optional] |
|**serviceProviderProperties** | [**ExpressRouteCircuitServiceProviderProperties**](ExpressRouteCircuitServiceProviderProperties.md) |  |  [optional] |
|**serviceProviderProvisioningState** | **ServiceProviderProvisioningState** |  |  [optional] |
|**stag** | **Integer** | The identifier of the circuit traffic. Outer tag for QinQ encapsulation. |  [optional] [readonly] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| SUCCEEDED | &quot;Succeeded&quot; |
| UPDATING | &quot;Updating&quot; |
| DELETING | &quot;Deleting&quot; |
| FAILED | &quot;Failed&quot; |



