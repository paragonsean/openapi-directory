# VirtualWanasAServiceManagementClient.P2SVpnServerConfigurationProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**etag** | **String** | A unique read-only string that changes whenever the resource is updated. | [optional] 
**name** | **String** | The name of the P2SVpnServerConfiguration that is unique within a VirtualWan in a resource group. This name can be used to access the resource along with Parent VirtualWan resource name. | [optional] 
**p2SVpnGateways** | [**[HubVirtualNetworkConnectionPropertiesRemoteVirtualNetwork]**](HubVirtualNetworkConnectionPropertiesRemoteVirtualNetwork.md) |  | [optional] [readonly] 
**p2SVpnServerConfigRadiusClientRootCertificates** | [**[P2SVpnServerConfigRadiusClientRootCertificate]**](P2SVpnServerConfigRadiusClientRootCertificate.md) | Radius client root certificate of P2SVpnServerConfiguration. | [optional] 
**p2SVpnServerConfigRadiusServerRootCertificates** | [**[P2SVpnServerConfigRadiusServerRootCertificate]**](P2SVpnServerConfigRadiusServerRootCertificate.md) | Radius Server root certificate of P2SVpnServerConfiguration. | [optional] 
**p2SVpnServerConfigVpnClientRevokedCertificates** | [**[P2SVpnServerConfigVpnClientRevokedCertificate]**](P2SVpnServerConfigVpnClientRevokedCertificate.md) | VPN client revoked certificate of P2SVpnServerConfiguration. | [optional] 
**p2SVpnServerConfigVpnClientRootCertificates** | [**[P2SVpnServerConfigVpnClientRootCertificate]**](P2SVpnServerConfigVpnClientRootCertificate.md) | VPN client root certificate of P2SVpnServerConfiguration. | [optional] 
**provisioningState** | **String** | The provisioning state of the P2SVpnServerConfiguration resource. Possible values are: &#39;Updating&#39;, &#39;Deleting&#39;, and &#39;Failed&#39;. | [optional] [readonly] 
**radiusServerAddress** | **String** | The radius server address property of the P2SVpnServerConfiguration resource for point to site client connection. | [optional] 
**radiusServerSecret** | **String** | The radius secret property of the P2SVpnServerConfiguration resource for point to site client connection. | [optional] 
**vpnClientIpsecPolicies** | [**[P2SVpnServerConfigurationPropertiesVpnClientIpsecPoliciesInner]**](P2SVpnServerConfigurationPropertiesVpnClientIpsecPoliciesInner.md) | VpnClientIpsecPolicies for P2SVpnServerConfiguration. | [optional] 
**vpnProtocols** | **[String]** | vpnProtocols for the P2SVpnServerConfiguration. | [optional] 



## Enum: [VpnProtocolsEnum]


* `IkeV2` (value: `"IkeV2"`)

* `OpenVPN` (value: `"OpenVPN"`)




