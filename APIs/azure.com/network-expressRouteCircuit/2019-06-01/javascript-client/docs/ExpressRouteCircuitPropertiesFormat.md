# NetworkManagementClient.ExpressRouteCircuitPropertiesFormat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowClassicOperations** | **Boolean** | Allow classic operations. | [optional] 
**authorizations** | [**[ExpressRouteCircuitAuthorization]**](ExpressRouteCircuitAuthorization.md) | The list of authorizations. | [optional] 
**bandwidthInGbps** | **Number** | The bandwidth of the circuit when the circuit is provisioned on an ExpressRoutePort resource. | [optional] 
**circuitProvisioningState** | **String** | The CircuitProvisioningState state of the resource. | [optional] 
**expressRoutePort** | [**ExpressRouteCircuitConnectionPropertiesFormatExpressRouteCircuitPeering**](ExpressRouteCircuitConnectionPropertiesFormatExpressRouteCircuitPeering.md) |  | [optional] 
**gatewayManagerEtag** | **String** | The GatewayManager Etag. | [optional] 
**globalReachEnabled** | **Boolean** | Flag denoting Global reach status. | [optional] 
**peerings** | [**[ExpressRouteCircuitPeering]**](ExpressRouteCircuitPeering.md) | The list of peerings. | [optional] 
**provisioningState** | **String** | Gets the provisioning state of the public IP resource. Possible values are: &#39;Updating&#39;, &#39;Deleting&#39;, and &#39;Failed&#39;. | [optional] 
**serviceKey** | **String** | The ServiceKey. | [optional] 
**serviceProviderNotes** | **String** | The ServiceProviderNotes. | [optional] 
**serviceProviderProperties** | [**ExpressRouteCircuitServiceProviderProperties**](ExpressRouteCircuitServiceProviderProperties.md) |  | [optional] 
**serviceProviderProvisioningState** | [**ServiceProviderProvisioningState**](ServiceProviderProvisioningState.md) |  | [optional] 
**stag** | **Number** | The identifier of the circuit traffic. Outer tag for QinQ encapsulation. | [optional] [readonly] 


