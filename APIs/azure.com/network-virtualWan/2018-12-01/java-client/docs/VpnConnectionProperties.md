

# VpnConnectionProperties

Parameters for VpnConnection

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**connectionBandwidth** | **Integer** | Expected bandwidth in MBPS. |  [optional] |
|**connectionStatus** | **VpnConnectionStatus** |  |  [optional] |
|**egressBytesTransferred** | **Long** | Egress bytes transferred. |  [optional] [readonly] |
|**enableBgp** | **Boolean** | EnableBgp flag |  [optional] |
|**enableInternetSecurity** | **Boolean** | Enable internet security |  [optional] |
|**enableRateLimiting** | **Boolean** | EnableBgp flag |  [optional] |
|**ingressBytesTransferred** | **Long** | Ingress bytes transferred. |  [optional] [readonly] |
|**ipsecPolicies** | [**List&lt;P2SVpnServerConfigurationPropertiesVpnClientIpsecPoliciesInner&gt;**](P2SVpnServerConfigurationPropertiesVpnClientIpsecPoliciesInner.md) | The IPSec Policies to be considered by this connection. |  [optional] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The current provisioning state. |  [optional] [readonly] |
|**remoteVpnSite** | [**HubVirtualNetworkConnectionPropertiesRemoteVirtualNetwork**](HubVirtualNetworkConnectionPropertiesRemoteVirtualNetwork.md) |  |  [optional] |
|**routingWeight** | **Integer** | Routing weight for vpn connection. |  [optional] |
|**sharedKey** | **String** | SharedKey for the vpn connection. |  [optional] |
|**vpnConnectionProtocolType** | [**VpnConnectionProtocolTypeEnum**](#VpnConnectionProtocolTypeEnum) | Gateway connection protocol. Possible values are: &#39;IKEv2&#39;, &#39;IKEv1&#39;. |  [optional] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| SUCCEEDED | &quot;Succeeded&quot; |
| UPDATING | &quot;Updating&quot; |
| DELETING | &quot;Deleting&quot; |
| FAILED | &quot;Failed&quot; |



## Enum: VpnConnectionProtocolTypeEnum

| Name | Value |
|---- | -----|
| IKEV2 | &quot;IKEv2&quot; |
| IKEV1 | &quot;IKEv1&quot; |



