# VirtualWanasAServiceManagementClient.VpnSiteProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addressSpace** | [**P2SVpnGatewayPropertiesCustomRoutes**](P2SVpnGatewayPropertiesCustomRoutes.md) |  | [optional] 
**bgpProperties** | [**VpnGatewayPropertiesBgpSettings**](VpnGatewayPropertiesBgpSettings.md) |  | [optional] 
**deviceProperties** | [**DeviceProperties**](DeviceProperties.md) |  | [optional] 
**ipAddress** | **String** | The ip-address for the vpn-site. | [optional] 
**isSecuritySite** | **Boolean** | IsSecuritySite flag. | [optional] 
**provisioningState** | **String** | The current provisioning state. | [optional] [readonly] 
**siteKey** | **String** | The key for vpn-site that can be used for connections. | [optional] 
**virtualWan** | [**HubVirtualNetworkConnectionPropertiesRemoteVirtualNetwork**](HubVirtualNetworkConnectionPropertiesRemoteVirtualNetwork.md) |  | [optional] 
**vpnSiteLinks** | [**[VpnSiteLink]**](VpnSiteLink.md) | List of all vpn site links | [optional] 



## Enum: ProvisioningStateEnum


* `Succeeded` (value: `"Succeeded"`)

* `Updating` (value: `"Updating"`)

* `Deleting` (value: `"Deleting"`)

* `Failed` (value: `"Failed"`)




