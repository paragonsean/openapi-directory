# MerakiDashboardApi.UpdateOrganizationThirdPartyVPNPeersRequestPeersInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ikeVersion** | **String** | [optional] The IKE version to be used for the IPsec VPN peer configuration. Defaults to &#39;1&#39; when omitted. | [optional] [default to &#39;1&#39;]
**ipsecPolicies** | [**UpdateOrganizationThirdPartyVPNPeersRequestPeersInnerIpsecPolicies**](UpdateOrganizationThirdPartyVPNPeersRequestPeersInnerIpsecPolicies.md) |  | [optional] 
**ipsecPoliciesPreset** | **String** | One of the following available presets: &#39;default&#39;, &#39;aws&#39;, &#39;azure&#39;. If this is provided, the &#39;ipsecPolicies&#39; parameter is ignored. | [optional] 
**name** | **String** | The name of the VPN peer | 
**networkTags** | **[String]** | A list of network tags that will connect with this peer. Use [&#39;all&#39;] for all networks. Use [&#39;none&#39;] for no networks. If not included, the default is [&#39;all&#39;]. | [optional] 
**privateSubnets** | **[String]** | The list of the private subnets of the VPN peer | 
**publicIp** | **String** | The public IP of the VPN peer | 
**remoteId** | **String** | [optional] The remote ID is used to identify the connecting VPN peer. This can either be a valid IPv4 Address, FQDN or User FQDN. | [optional] 
**secret** | **String** | The shared secret with the VPN peer | 



## Enum: IkeVersionEnum


* `1` (value: `"1"`)

* `2` (value: `"2"`)




