# NetworkManagementClient.ExpressRouteGatewayProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**autoScaleConfiguration** | [**ExpressRouteGatewayPropertiesAutoScaleConfiguration**](ExpressRouteGatewayPropertiesAutoScaleConfiguration.md) |  | [optional] 
**expressRouteConnections** | [**[ExpressRouteConnection]**](ExpressRouteConnection.md) | List of ExpressRoute connections to the ExpressRoute gateway. | [optional] [readonly] 
**provisioningState** | **String** | The provisioning state of the resource. | [optional] [readonly] 
**virtualHub** | [**VirtualHubId**](VirtualHubId.md) |  | 



## Enum: ProvisioningStateEnum


* `Succeeded` (value: `"Succeeded"`)

* `Updating` (value: `"Updating"`)

* `Deleting` (value: `"Deleting"`)

* `Failed` (value: `"Failed"`)




