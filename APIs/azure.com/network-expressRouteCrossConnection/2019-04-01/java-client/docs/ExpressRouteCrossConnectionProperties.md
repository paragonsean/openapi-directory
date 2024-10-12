

# ExpressRouteCrossConnectionProperties

Properties of ExpressRouteCrossConnection.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bandwidthInMbps** | **Integer** | The circuit bandwidth In Mbps. |  [optional] |
|**expressRouteCircuit** | [**ExpressRouteCircuitReference**](ExpressRouteCircuitReference.md) |  |  [optional] |
|**peeringLocation** | **String** | The peering location of the ExpressRoute circuit. |  [optional] |
|**peerings** | [**List&lt;ExpressRouteCrossConnectionPeering&gt;**](ExpressRouteCrossConnectionPeering.md) | The list of peerings. |  [optional] |
|**primaryAzurePort** | **String** | The name of the primary port. |  [optional] [readonly] |
|**provisioningState** | **String** | Gets the provisioning state of the public IP resource. Possible values are: &#39;Updating&#39;, &#39;Deleting&#39;, and &#39;Failed&#39;. |  [optional] [readonly] |
|**sTag** | **Integer** | The identifier of the circuit traffic. |  [optional] [readonly] |
|**secondaryAzurePort** | **String** | The name of the secondary port. |  [optional] [readonly] |
|**serviceProviderNotes** | **String** | Additional read only notes set by the connectivity provider. |  [optional] |
|**serviceProviderProvisioningState** | [**ServiceProviderProvisioningStateEnum**](#ServiceProviderProvisioningStateEnum) | The ServiceProviderProvisioningState state of the resource. |  [optional] |



## Enum: ServiceProviderProvisioningStateEnum

| Name | Value |
|---- | -----|
| NOT_PROVISIONED | &quot;NotProvisioned&quot; |
| PROVISIONING | &quot;Provisioning&quot; |
| PROVISIONED | &quot;Provisioned&quot; |
| DEPROVISIONING | &quot;Deprovisioning&quot; |



