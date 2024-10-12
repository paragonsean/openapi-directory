

# P2SVpnGatewayProperties

Parameters for P2SVpnGateway

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**p2SVpnServerConfiguration** | [**HubVirtualNetworkConnectionPropertiesRemoteVirtualNetwork**](HubVirtualNetworkConnectionPropertiesRemoteVirtualNetwork.md) |  |  [optional] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The current provisioning state. |  [optional] [readonly] |
|**virtualHub** | [**HubVirtualNetworkConnectionPropertiesRemoteVirtualNetwork**](HubVirtualNetworkConnectionPropertiesRemoteVirtualNetwork.md) |  |  [optional] |
|**vpnClientAddressPool** | [**P2SVpnGatewayPropertiesVpnClientAddressPool**](P2SVpnGatewayPropertiesVpnClientAddressPool.md) |  |  [optional] |
|**vpnClientConnectionHealth** | [**VpnClientConnectionHealth**](VpnClientConnectionHealth.md) |  |  [optional] |
|**vpnGatewayScaleUnit** | **Integer** | The scale unit for this p2s vpn gateway. |  [optional] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| SUCCEEDED | &quot;Succeeded&quot; |
| UPDATING | &quot;Updating&quot; |
| DELETING | &quot;Deleting&quot; |
| FAILED | &quot;Failed&quot; |



