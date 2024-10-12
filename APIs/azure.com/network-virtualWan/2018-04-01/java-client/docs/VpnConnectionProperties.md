

# VpnConnectionProperties

Parameters for VpnConnection

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**connectionBandwidth** | **Integer** | Expected bandwidth in MBPS. |  [optional] [readonly] |
|**connectionStatus** | **VpnConnectionStatus** |  |  [optional] |
|**egressBytesTransferred** | **Long** | Egress bytes transferred. |  [optional] [readonly] |
|**enableBgp** | **Boolean** | EnableBgp flag |  [optional] |
|**ingressBytesTransferred** | **Long** | Ingress bytes transferred. |  [optional] [readonly] |
|**ipsecPolicies** | [**List&lt;VpnConnectionPropertiesIpsecPoliciesInner&gt;**](VpnConnectionPropertiesIpsecPoliciesInner.md) | The IPSec Policies to be considered by this connection. |  [optional] |
|**provisioningState** | **ProvisioningState** |  |  [optional] |
|**remoteVpnSite** | [**GetVpnSitesConfigurationRequestVpnSitesInner**](GetVpnSitesConfigurationRequestVpnSitesInner.md) |  |  [optional] |
|**routingWeight** | **Integer** | routing weight for vpn connection. |  [optional] |
|**sharedKey** | **String** | SharedKey for the vpn connection. |  [optional] |



