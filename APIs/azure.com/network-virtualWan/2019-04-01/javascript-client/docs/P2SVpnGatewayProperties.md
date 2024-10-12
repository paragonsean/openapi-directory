# VirtualWanasAServiceManagementClient.P2SVpnGatewayProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customRoutes** | [**P2SVpnGatewayPropertiesCustomRoutes**](P2SVpnGatewayPropertiesCustomRoutes.md) |  | [optional] 
**p2SVpnServerConfiguration** | [**HubVirtualNetworkConnectionPropertiesRemoteVirtualNetwork**](HubVirtualNetworkConnectionPropertiesRemoteVirtualNetwork.md) |  | [optional] 
**provisioningState** | **String** | The current provisioning state. | [optional] [readonly] 
**virtualHub** | [**HubVirtualNetworkConnectionPropertiesRemoteVirtualNetwork**](HubVirtualNetworkConnectionPropertiesRemoteVirtualNetwork.md) |  | [optional] 
**vpnClientAddressPool** | [**P2SVpnGatewayPropertiesCustomRoutes**](P2SVpnGatewayPropertiesCustomRoutes.md) |  | [optional] 
**vpnClientConnectionHealth** | [**VpnClientConnectionHealth**](VpnClientConnectionHealth.md) |  | [optional] 
**vpnGatewayScaleUnit** | **Number** | The scale unit for this p2s vpn gateway. | [optional] 



## Enum: ProvisioningStateEnum


* `Succeeded` (value: `"Succeeded"`)

* `Updating` (value: `"Updating"`)

* `Deleting` (value: `"Deleting"`)

* `Failed` (value: `"Failed"`)




