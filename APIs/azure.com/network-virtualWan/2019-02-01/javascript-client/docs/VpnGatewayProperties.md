# VirtualWanasAServiceManagementClient.VpnGatewayProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bgpSettings** | [**VpnGatewayPropertiesBgpSettings**](VpnGatewayPropertiesBgpSettings.md) |  | [optional] 
**connections** | [**[VpnConnection]**](VpnConnection.md) | List of all vpn connections to the gateway. | [optional] 
**provisioningState** | **String** | The current provisioning state. | [optional] [readonly] 
**virtualHub** | [**HubVirtualNetworkConnectionPropertiesRemoteVirtualNetwork**](HubVirtualNetworkConnectionPropertiesRemoteVirtualNetwork.md) |  | [optional] 
**vpnGatewayScaleUnit** | **Number** | The scale unit for this vpn gateway. | [optional] 



## Enum: ProvisioningStateEnum


* `Succeeded` (value: `"Succeeded"`)

* `Updating` (value: `"Updating"`)

* `Deleting` (value: `"Deleting"`)

* `Failed` (value: `"Failed"`)




