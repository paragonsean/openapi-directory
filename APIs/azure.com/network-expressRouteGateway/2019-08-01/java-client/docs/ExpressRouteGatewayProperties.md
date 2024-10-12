

# ExpressRouteGatewayProperties

ExpressRoute gateway resource properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**autoScaleConfiguration** | [**ExpressRouteGatewayPropertiesAutoScaleConfiguration**](ExpressRouteGatewayPropertiesAutoScaleConfiguration.md) |  |  [optional] |
|**expressRouteConnections** | [**List&lt;ExpressRouteConnection&gt;**](ExpressRouteConnection.md) | List of ExpressRoute connections to the ExpressRoute gateway. |  [optional] [readonly] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The current provisioning state. |  [optional] [readonly] |
|**virtualHub** | [**VirtualHubId**](VirtualHubId.md) |  |  |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| SUCCEEDED | &quot;Succeeded&quot; |
| UPDATING | &quot;Updating&quot; |
| DELETING | &quot;Deleting&quot; |
| FAILED | &quot;Failed&quot; |



