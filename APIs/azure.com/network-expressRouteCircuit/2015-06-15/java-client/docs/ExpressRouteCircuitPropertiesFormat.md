

# ExpressRouteCircuitPropertiesFormat

Properties of ExpressRouteCircuit.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authorizations** | [**List&lt;ExpressRouteCircuitAuthorization&gt;**](ExpressRouteCircuitAuthorization.md) | The list of authorizations. |  [optional] |
|**circuitProvisioningState** | **String** | The CircuitProvisioningState state of the resource. |  [optional] |
|**peerings** | [**List&lt;ExpressRouteCircuitPeering&gt;**](ExpressRouteCircuitPeering.md) | The list of peerings. |  [optional] |
|**provisioningState** | **String** | Gets the provisioning state of the public IP resource. Possible values are: &#39;Updating&#39;, &#39;Deleting&#39;, and &#39;Failed&#39;. |  [optional] |
|**serviceKey** | **String** | The ServiceKey. |  [optional] |
|**serviceProviderNotes** | **String** | The ServiceProviderNotes. |  [optional] |
|**serviceProviderProperties** | [**ExpressRouteCircuitServiceProviderProperties**](ExpressRouteCircuitServiceProviderProperties.md) |  |  [optional] |
|**serviceProviderProvisioningState** | [**ServiceProviderProvisioningStateEnum**](#ServiceProviderProvisioningStateEnum) | The ServiceProviderProvisioningState state of the resource. Possible values are &#39;NotProvisioned&#39;, &#39;Provisioning&#39;, &#39;Provisioned&#39;, and &#39;Deprovisioning&#39;. |  [optional] |



## Enum: ServiceProviderProvisioningStateEnum

| Name | Value |
|---- | -----|
| NOT_PROVISIONED | &quot;NotProvisioned&quot; |
| PROVISIONING | &quot;Provisioning&quot; |
| PROVISIONED | &quot;Provisioned&quot; |
| DEPROVISIONING | &quot;Deprovisioning&quot; |



