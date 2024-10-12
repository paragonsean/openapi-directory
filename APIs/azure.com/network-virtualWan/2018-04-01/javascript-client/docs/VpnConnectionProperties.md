# VirtualWanasAServiceManagementClient.VpnConnectionProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connectionBandwidth** | **Number** | Expected bandwidth in MBPS. | [optional] [readonly] 
**connectionStatus** | [**VpnConnectionStatus**](VpnConnectionStatus.md) |  | [optional] 
**egressBytesTransferred** | **Number** | Egress bytes transferred. | [optional] [readonly] 
**enableBgp** | **Boolean** | EnableBgp flag | [optional] 
**ingressBytesTransferred** | **Number** | Ingress bytes transferred. | [optional] [readonly] 
**ipsecPolicies** | [**[VpnConnectionPropertiesIpsecPoliciesInner]**](VpnConnectionPropertiesIpsecPoliciesInner.md) | The IPSec Policies to be considered by this connection. | [optional] 
**provisioningState** | [**ProvisioningState**](ProvisioningState.md) |  | [optional] 
**remoteVpnSite** | [**GetVpnSitesConfigurationRequestVpnSitesInner**](GetVpnSitesConfigurationRequestVpnSitesInner.md) |  | [optional] 
**routingWeight** | **Number** | routing weight for vpn connection. | [optional] 
**sharedKey** | **String** | SharedKey for the vpn connection. | [optional] 


