# VirtualWanasAServiceManagementClient.VpnConnectionProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connectionBandwidth** | **Number** | Expected bandwidth in MBPS. | [optional] 
**connectionStatus** | [**VpnConnectionStatus**](VpnConnectionStatus.md) |  | [optional] 
**egressBytesTransferred** | **Number** | Egress bytes transferred. | [optional] [readonly] 
**enableBgp** | **Boolean** | EnableBgp flag | [optional] 
**enableInternetSecurity** | **Boolean** | Enable internet security | [optional] 
**enableRateLimiting** | **Boolean** | EnableBgp flag | [optional] 
**ingressBytesTransferred** | **Number** | Ingress bytes transferred. | [optional] [readonly] 
**ipsecPolicies** | [**[P2SVpnServerConfigurationPropertiesVpnClientIpsecPoliciesInner]**](P2SVpnServerConfigurationPropertiesVpnClientIpsecPoliciesInner.md) | The IPSec Policies to be considered by this connection. | [optional] 
**provisioningState** | [**ProvisioningState**](ProvisioningState.md) |  | [optional] 
**remoteVpnSite** | [**HubVirtualNetworkConnectionPropertiesRemoteVirtualNetwork**](HubVirtualNetworkConnectionPropertiesRemoteVirtualNetwork.md) |  | [optional] 
**routingWeight** | **Number** | routing weight for vpn connection. | [optional] 
**sharedKey** | **String** | SharedKey for the vpn connection. | [optional] 
**vpnConnectionProtocolType** | **String** | Gateway connection protocol. Possible values are: &#39;IKEv2&#39;, &#39;IKEv1&#39;. | [optional] 



## Enum: VpnConnectionProtocolTypeEnum


* `IKEv2` (value: `"IKEv2"`)

* `IKEv1` (value: `"IKEv1"`)




