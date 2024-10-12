# NetworkManagementClient.VpnClientConfiguration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aadAudience** | **String** | The AADAudience property of the VirtualNetworkGateway resource for vpn client connection used for AAD authentication. | [optional] 
**aadIssuer** | **String** | The AADIssuer property of the VirtualNetworkGateway resource for vpn client connection used for AAD authentication. | [optional] 
**aadTenant** | **String** | The AADTenant property of the VirtualNetworkGateway resource for vpn client connection used for AAD authentication. | [optional] 
**radiusServerAddress** | **String** | The radius server address property of the VirtualNetworkGateway resource for vpn client connection. | [optional] 
**radiusServerSecret** | **String** | The radius secret property of the VirtualNetworkGateway resource for vpn client connection. | [optional] 
**vpnClientAddressPool** | [**LocalNetworkGatewayPropertiesFormatLocalNetworkAddressSpace**](LocalNetworkGatewayPropertiesFormatLocalNetworkAddressSpace.md) |  | [optional] 
**vpnClientIpsecPolicies** | [**[IpsecPolicy]**](IpsecPolicy.md) | VpnClientIpsecPolicies for virtual network gateway P2S client. | [optional] 
**vpnClientProtocols** | **[String]** | VpnClientProtocols for Virtual network gateway. | [optional] 
**vpnClientRevokedCertificates** | [**[VpnClientRevokedCertificate]**](VpnClientRevokedCertificate.md) | VpnClientRevokedCertificate for Virtual network gateway. | [optional] 
**vpnClientRootCertificates** | [**[VpnClientRootCertificate]**](VpnClientRootCertificate.md) | VpnClientRootCertificate for virtual network gateway. | [optional] 



## Enum: [VpnClientProtocolsEnum]


* `IkeV2` (value: `"IkeV2"`)

* `SSTP` (value: `"SSTP"`)

* `OpenVPN` (value: `"OpenVPN"`)




