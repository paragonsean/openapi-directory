

# VpnGatewayProperties

Parameters for VpnGateway.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bgpSettings** | [**VpnGatewayPropertiesBgpSettings**](VpnGatewayPropertiesBgpSettings.md) |  |  [optional] |
|**connections** | [**List&lt;VpnConnection&gt;**](VpnConnection.md) | List of all vpn connections to the gateway. |  [optional] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The current provisioning state. |  [optional] [readonly] |
|**virtualHub** | [**HubVirtualNetworkConnectionPropertiesRemoteVirtualNetwork**](HubVirtualNetworkConnectionPropertiesRemoteVirtualNetwork.md) |  |  [optional] |
|**vpnGatewayScaleUnit** | **Integer** | The scale unit for this vpn gateway. |  [optional] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| SUCCEEDED | &quot;Succeeded&quot; |
| UPDATING | &quot;Updating&quot; |
| DELETING | &quot;Deleting&quot; |
| FAILED | &quot;Failed&quot; |



