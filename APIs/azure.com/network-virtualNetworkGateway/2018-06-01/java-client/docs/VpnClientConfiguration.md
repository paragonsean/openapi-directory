

# VpnClientConfiguration

VpnClientConfiguration for P2S client.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**radiusServerAddress** | **String** | The radius server address property of the VirtualNetworkGateway resource for vpn client connection. |  [optional] |
|**radiusServerSecret** | **String** | The radius secret property of the VirtualNetworkGateway resource for vpn client connection. |  [optional] |
|**vpnClientAddressPool** | [**LocalNetworkGatewayPropertiesFormatLocalNetworkAddressSpace**](LocalNetworkGatewayPropertiesFormatLocalNetworkAddressSpace.md) |  |  [optional] |
|**vpnClientIpsecPolicies** | [**List&lt;IpsecPolicy&gt;**](IpsecPolicy.md) | VpnClientIpsecPolicies for virtual network gateway P2S client. |  [optional] |
|**vpnClientProtocols** | [**List&lt;VpnClientProtocolsEnum&gt;**](#List&lt;VpnClientProtocolsEnum&gt;) | VpnClientProtocols for Virtual network gateway. |  [optional] |
|**vpnClientRevokedCertificates** | [**List&lt;VpnClientRevokedCertificate&gt;**](VpnClientRevokedCertificate.md) | VpnClientRevokedCertificate for Virtual network gateway. |  [optional] |
|**vpnClientRootCertificates** | [**List&lt;VpnClientRootCertificate&gt;**](VpnClientRootCertificate.md) | VpnClientRootCertificate for virtual network gateway. |  [optional] |



## Enum: List&lt;VpnClientProtocolsEnum&gt;

| Name | Value |
|---- | -----|
| IKE_V2 | &quot;IkeV2&quot; |
| SSTP | &quot;SSTP&quot; |
| OPEN_VPN | &quot;OpenVPN&quot; |



