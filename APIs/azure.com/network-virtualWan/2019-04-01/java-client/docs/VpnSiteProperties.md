

# VpnSiteProperties

Parameters for VpnSite.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**addressSpace** | [**P2SVpnGatewayPropertiesCustomRoutes**](P2SVpnGatewayPropertiesCustomRoutes.md) |  |  [optional] |
|**bgpProperties** | [**VpnGatewayPropertiesBgpSettings**](VpnGatewayPropertiesBgpSettings.md) |  |  [optional] |
|**deviceProperties** | [**DeviceProperties**](DeviceProperties.md) |  |  [optional] |
|**ipAddress** | **String** | The ip-address for the vpn-site. |  [optional] |
|**isSecuritySite** | **Boolean** | IsSecuritySite flag. |  [optional] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The current provisioning state. |  [optional] [readonly] |
|**siteKey** | **String** | The key for vpn-site that can be used for connections. |  [optional] |
|**virtualWan** | [**HubVirtualNetworkConnectionPropertiesRemoteVirtualNetwork**](HubVirtualNetworkConnectionPropertiesRemoteVirtualNetwork.md) |  |  [optional] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| SUCCEEDED | &quot;Succeeded&quot; |
| UPDATING | &quot;Updating&quot; |
| DELETING | &quot;Deleting&quot; |
| FAILED | &quot;Failed&quot; |



