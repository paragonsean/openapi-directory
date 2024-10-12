

# ExpressRouteConnectionProperties

Properties of the ExpressRouteConnection subresource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authorizationKey** | **String** | Authorization key to establish the connection. |  [optional] |
|**expressRouteCircuitPeering** | [**ExpressRouteCircuitPeeringId**](ExpressRouteCircuitPeeringId.md) |  |  |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The provisioning state of the resource. |  [optional] [readonly] |
|**routingWeight** | **Integer** | The routing weight associated to the connection. |  [optional] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| SUCCEEDED | &quot;Succeeded&quot; |
| UPDATING | &quot;Updating&quot; |
| DELETING | &quot;Deleting&quot; |
| FAILED | &quot;Failed&quot; |



