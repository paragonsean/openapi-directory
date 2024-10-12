# NetworkManagementClient.ExpressRouteCircuitPropertiesFormat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowClassicOperations** | **Boolean** | Allow classic operations | [optional] 
**authorizations** | [**[ExpressRouteCircuitAuthorization]**](ExpressRouteCircuitAuthorization.md) | The list of authorizations. | [optional] 
**circuitProvisioningState** | **String** | The CircuitProvisioningState state of the resource. | [optional] 
**gatewayManagerEtag** | **String** | The GatewayManager Etag. | [optional] 
**peerings** | [**[ExpressRouteCircuitPeering]**](ExpressRouteCircuitPeering.md) | The list of peerings. | [optional] 
**provisioningState** | **String** | Gets the provisioning state of the public IP resource. Possible values are: &#39;Updating&#39;, &#39;Deleting&#39;, and &#39;Failed&#39;. | [optional] 
**serviceKey** | **String** | The ServiceKey. | [optional] 
**serviceProviderNotes** | **String** | The ServiceProviderNotes. | [optional] 
**serviceProviderProperties** | [**ExpressRouteCircuitServiceProviderProperties**](ExpressRouteCircuitServiceProviderProperties.md) |  | [optional] 
**serviceProviderProvisioningState** | **String** | The ServiceProviderProvisioningState state of the resource. Possible values are &#39;NotProvisioned&#39;, &#39;Provisioning&#39;, &#39;Provisioned&#39;, and &#39;Deprovisioning&#39;. | [optional] 



## Enum: ServiceProviderProvisioningStateEnum


* `NotProvisioned` (value: `"NotProvisioned"`)

* `Provisioning` (value: `"Provisioning"`)

* `Provisioned` (value: `"Provisioned"`)

* `Deprovisioning` (value: `"Deprovisioning"`)




