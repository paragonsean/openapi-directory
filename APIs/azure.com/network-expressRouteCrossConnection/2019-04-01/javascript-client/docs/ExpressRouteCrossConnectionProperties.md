# ExpressRouteCrossConnectionRestApis.ExpressRouteCrossConnectionProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bandwidthInMbps** | **Number** | The circuit bandwidth In Mbps. | [optional] 
**expressRouteCircuit** | [**ExpressRouteCircuitReference**](ExpressRouteCircuitReference.md) |  | [optional] 
**peeringLocation** | **String** | The peering location of the ExpressRoute circuit. | [optional] 
**peerings** | [**[ExpressRouteCrossConnectionPeering]**](ExpressRouteCrossConnectionPeering.md) | The list of peerings. | [optional] 
**primaryAzurePort** | **String** | The name of the primary port. | [optional] [readonly] 
**provisioningState** | **String** | Gets the provisioning state of the public IP resource. Possible values are: &#39;Updating&#39;, &#39;Deleting&#39;, and &#39;Failed&#39;. | [optional] [readonly] 
**sTag** | **Number** | The identifier of the circuit traffic. | [optional] [readonly] 
**secondaryAzurePort** | **String** | The name of the secondary port. | [optional] [readonly] 
**serviceProviderNotes** | **String** | Additional read only notes set by the connectivity provider. | [optional] 
**serviceProviderProvisioningState** | **String** | The ServiceProviderProvisioningState state of the resource. | [optional] 



## Enum: ServiceProviderProvisioningStateEnum


* `NotProvisioned` (value: `"NotProvisioned"`)

* `Provisioning` (value: `"Provisioning"`)

* `Provisioned` (value: `"Provisioned"`)

* `Deprovisioning` (value: `"Deprovisioning"`)




