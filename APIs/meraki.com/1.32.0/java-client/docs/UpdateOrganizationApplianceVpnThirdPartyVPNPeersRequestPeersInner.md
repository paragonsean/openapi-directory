

# UpdateOrganizationApplianceVpnThirdPartyVPNPeersRequestPeersInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ikeVersion** | [**IkeVersionEnum**](#IkeVersionEnum) | [optional] The IKE version to be used for the IPsec VPN peer configuration. Defaults to &#39;1&#39; when omitted. |  [optional] |
|**ipsecPolicies** | [**GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInnerIpsecPolicies**](GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInnerIpsecPolicies.md) |  |  [optional] |
|**ipsecPoliciesPreset** | **String** | One of the following available presets: &#39;default&#39;, &#39;aws&#39;, &#39;azure&#39;. If this is provided, the &#39;ipsecPolicies&#39; parameter is ignored. |  [optional] |
|**localId** | **String** | [optional] The local ID is used to identify the MX to the peer. This will apply to all MXs this peer applies to. |  [optional] |
|**name** | **String** | The name of the VPN peer |  |
|**networkTags** | **List&lt;String&gt;** | A list of network tags that will connect with this peer. Use [&#39;all&#39;] for all networks. Use [&#39;none&#39;] for no networks. If not included, the default is [&#39;all&#39;]. |  [optional] |
|**privateSubnets** | **List&lt;String&gt;** | The list of the private subnets of the VPN peer |  |
|**publicIp** | **String** | [optional] The public IP of the VPN peer |  [optional] |
|**remoteId** | **String** | [optional] The remote ID is used to identify the connecting VPN peer. This can either be a valid IPv4 Address, FQDN or User FQDN. |  [optional] |
|**secret** | **String** | The shared secret with the VPN peer |  |



## Enum: IkeVersionEnum

| Name | Value |
|---- | -----|
| _1 | &quot;1&quot; |
| _2 | &quot;2&quot; |



