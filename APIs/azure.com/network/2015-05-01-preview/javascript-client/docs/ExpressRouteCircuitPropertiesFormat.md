# NetworkResourceProviderClient.ExpressRouteCircuitPropertiesFormat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorizations** | [**[ExpressRouteCircuitAuthorization]**](ExpressRouteCircuitAuthorization.md) | Gets or sets list of authorizations | [optional] 
**circuitProvisioningState** | **String** | Gets or sets CircuitProvisioningState state of the resource  | [optional] 
**peerings** | [**[ExpressRouteCircuitPeering]**](ExpressRouteCircuitPeering.md) | Gets or sets list of peerings | [optional] 
**provisioningState** | **String** | Gets or sets Provisioning state of the PublicIP resource Updating/Deleting/Failed | [optional] 
**serviceKey** | **String** | Gets or sets ServiceKey | [optional] 
**serviceProviderNotes** | **String** | Gets or sets ServiceProviderNotes | [optional] 
**serviceProviderProperties** | [**ExpressRouteCircuitServiceProviderProperties**](ExpressRouteCircuitServiceProviderProperties.md) |  | [optional] 
**serviceProviderProvisioningState** | **String** | Gets or sets ServiceProviderProvisioningState state of the resource  | [optional] 



## Enum: ServiceProviderProvisioningStateEnum


* `NotProvisioned` (value: `"NotProvisioned"`)

* `Provisioning` (value: `"Provisioning"`)

* `Provisioned` (value: `"Provisioned"`)

* `Deprovisioning` (value: `"Deprovisioning"`)




