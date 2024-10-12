# ExpressRouteCrossConnectionRestApis.ExpressRouteCrossConnectionProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bandwidthInMbps** | **Number** | The circuit bandwidth In Mbps. | [optional] 
**expressRouteCircuit** | [**ExpressRouteCircuitReference**](ExpressRouteCircuitReference.md) |  | [optional] 
**peeringLocation** | **String** | The peering location of the ExpressRoute circuit. | [optional] 
**peerings** | [**[ExpressRouteCrossConnectionPeering]**](ExpressRouteCrossConnectionPeering.md) | The list of peerings. | [optional] 
**primaryAzurePort** | **String** | The name of the primary port. | [optional] [readonly] 
**provisioningState** | **String** | The current provisioning state. | [optional] [readonly] 
**sTag** | **Number** | The identifier of the circuit traffic. | [optional] [readonly] 
**secondaryAzurePort** | **String** | The name of the secondary port. | [optional] [readonly] 
**serviceProviderNotes** | **String** | Additional read only notes set by the connectivity provider. | [optional] 
**serviceProviderProvisioningState** | **String** | The ServiceProviderProvisioningState state of the resource. | [optional] 



## Enum: ProvisioningStateEnum


* `Succeeded` (value: `"Succeeded"`)

* `Updating` (value: `"Updating"`)

* `Deleting` (value: `"Deleting"`)

* `Failed` (value: `"Failed"`)





## Enum: ServiceProviderProvisioningStateEnum


* `NotProvisioned` (value: `"NotProvisioned"`)

* `Provisioning` (value: `"Provisioning"`)

* `Provisioned` (value: `"Provisioned"`)

* `Deprovisioning` (value: `"Deprovisioning"`)




