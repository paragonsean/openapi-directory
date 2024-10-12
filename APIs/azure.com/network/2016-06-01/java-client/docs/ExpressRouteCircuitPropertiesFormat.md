

# ExpressRouteCircuitPropertiesFormat

Properties of ExpressRouteCircuit

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowClassicOperations** | **Boolean** | allow classic operations |  [optional] |
|**authorizations** | [**List&lt;ExpressRouteCircuitAuthorization&gt;**](ExpressRouteCircuitAuthorization.md) | Gets or sets list of authorizations |  [optional] |
|**circuitProvisioningState** | **String** | Gets or sets CircuitProvisioningState state of the resource  |  [optional] |
|**gatewayManagerEtag** | **String** | Gets or sets the GatewayManager Etag |  [optional] |
|**peerings** | [**List&lt;ExpressRouteCircuitPeering&gt;**](ExpressRouteCircuitPeering.md) | Gets or sets list of peerings |  [optional] |
|**provisioningState** | **String** | Gets provisioning state of the PublicIP resource Updating/Deleting/Failed |  [optional] |
|**serviceKey** | **String** | Gets or sets ServiceKey |  [optional] |
|**serviceProviderNotes** | **String** | Gets or sets ServiceProviderNotes |  [optional] |
|**serviceProviderProperties** | [**ExpressRouteCircuitServiceProviderProperties**](ExpressRouteCircuitServiceProviderProperties.md) |  |  [optional] |
|**serviceProviderProvisioningState** | [**ServiceProviderProvisioningStateEnum**](#ServiceProviderProvisioningStateEnum) | Gets or sets ServiceProviderProvisioningState state of the resource  |  [optional] |



## Enum: ServiceProviderProvisioningStateEnum

| Name | Value |
|---- | -----|
| NOT_PROVISIONED | &quot;NotProvisioned&quot; |
| PROVISIONING | &quot;Provisioning&quot; |
| PROVISIONED | &quot;Provisioned&quot; |
| DEPROVISIONING | &quot;Deprovisioning&quot; |



