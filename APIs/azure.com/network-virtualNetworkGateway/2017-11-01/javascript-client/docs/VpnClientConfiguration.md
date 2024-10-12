# NetworkManagementClient.VpnClientConfiguration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**radiusServerAddress** | **String** | The radius server address property of the VirtualNetworkGateway resource for vpn client connection. | [optional] 
**radiusServerSecret** | **String** | The radius secret property of the VirtualNetworkGateway resource for vpn client connection. | [optional] 
**vpnClientAddressPool** | [**LocalNetworkGatewayPropertiesFormatLocalNetworkAddressSpace**](LocalNetworkGatewayPropertiesFormatLocalNetworkAddressSpace.md) |  | [optional] 
**vpnClientProtocols** | **[String]** | VpnClientProtocols for Virtual network gateway. | [optional] 
**vpnClientRevokedCertificates** | [**[VpnClientRevokedCertificate]**](VpnClientRevokedCertificate.md) | VpnClientRevokedCertificate for Virtual network gateway. | [optional] 
**vpnClientRootCertificates** | [**[VpnClientRootCertificate]**](VpnClientRootCertificate.md) | VpnClientRootCertificate for virtual network gateway. | [optional] 



## Enum: [VpnClientProtocolsEnum]


* `IkeV2` (value: `"IkeV2"`)

* `SSTP` (value: `"SSTP"`)




