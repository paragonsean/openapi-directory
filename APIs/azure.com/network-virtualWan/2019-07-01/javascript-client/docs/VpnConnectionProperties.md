# VirtualWanasAServiceManagementClient.VpnConnectionProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connectionBandwidth** | **Number** | Expected bandwidth in MBPS. | [optional] 
**connectionStatus** | [**VpnConnectionStatus**](VpnConnectionStatus.md) |  | [optional] 
**egressBytesTransferred** | **Number** | Egress bytes transferred. | [optional] [readonly] 
**enableBgp** | **Boolean** | EnableBgp flag. | [optional] 
**enableInternetSecurity** | **Boolean** | Enable internet security. | [optional] 
**enableRateLimiting** | **Boolean** | EnableBgp flag. | [optional] 
**ingressBytesTransferred** | **Number** | Ingress bytes transferred. | [optional] [readonly] 
**ipsecPolicies** | [**[P2SVpnServerConfigurationPropertiesVpnClientIpsecPoliciesInner]**](P2SVpnServerConfigurationPropertiesVpnClientIpsecPoliciesInner.md) | The IPSec Policies to be considered by this connection. | [optional] 
**provisioningState** | **String** | The current provisioning state. | [optional] [readonly] 
**remoteVpnSite** | [**HubVirtualNetworkConnectionPropertiesRemoteVirtualNetwork**](HubVirtualNetworkConnectionPropertiesRemoteVirtualNetwork.md) |  | [optional] 
**routingWeight** | **Number** | Routing weight for vpn connection. | [optional] 
**sharedKey** | **String** | SharedKey for the vpn connection. | [optional] 
**useLocalAzureIpAddress** | **Boolean** | Use local azure ip to initiate connection. | [optional] 
**usePolicyBasedTrafficSelectors** | **Boolean** | Enable policy-based traffic selectors. | [optional] 
**vpnConnectionProtocolType** | **String** | Gateway connection protocol. | [optional] 
**vpnLinkConnections** | [**[VpnSiteLinkConnection]**](VpnSiteLinkConnection.md) | List of all vpn site link connections to the gateway. | [optional] 



## Enum: ProvisioningStateEnum


* `Succeeded` (value: `"Succeeded"`)

* `Updating` (value: `"Updating"`)

* `Deleting` (value: `"Deleting"`)

* `Failed` (value: `"Failed"`)





## Enum: VpnConnectionProtocolTypeEnum


* `IKEv2` (value: `"IKEv2"`)

* `IKEv1` (value: `"IKEv1"`)




