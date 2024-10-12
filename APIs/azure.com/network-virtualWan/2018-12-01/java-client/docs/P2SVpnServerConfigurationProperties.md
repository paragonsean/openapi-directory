

# P2SVpnServerConfigurationProperties

Parameters for P2SVpnServerConfiguration

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**etag** | **String** | A unique read-only string that changes whenever the resource is updated. |  [optional] |
|**name** | **String** | The name of the P2SVpnServerConfiguration that is unique within a VirtualWan in a resource group. This name can be used to access the resource along with Paren VirtualWan resource name. |  [optional] |
|**p2SVpnGateways** | [**List&lt;HubVirtualNetworkConnectionPropertiesRemoteVirtualNetwork&gt;**](HubVirtualNetworkConnectionPropertiesRemoteVirtualNetwork.md) |  |  [optional] [readonly] |
|**p2SVpnServerConfigRadiusClientRootCertificates** | [**List&lt;P2SVpnServerConfigRadiusClientRootCertificate&gt;**](P2SVpnServerConfigRadiusClientRootCertificate.md) | Radius client root certificate of P2SVpnServerConfiguration. |  [optional] |
|**p2SVpnServerConfigRadiusServerRootCertificates** | [**List&lt;P2SVpnServerConfigRadiusServerRootCertificate&gt;**](P2SVpnServerConfigRadiusServerRootCertificate.md) | Radius Server root certificate of P2SVpnServerConfiguration. |  [optional] |
|**p2SVpnServerConfigVpnClientRevokedCertificates** | [**List&lt;P2SVpnServerConfigVpnClientRevokedCertificate&gt;**](P2SVpnServerConfigVpnClientRevokedCertificate.md) | VPN client revoked certificate of P2SVpnServerConfiguration. |  [optional] |
|**p2SVpnServerConfigVpnClientRootCertificates** | [**List&lt;P2SVpnServerConfigVpnClientRootCertificate&gt;**](P2SVpnServerConfigVpnClientRootCertificate.md) | VPN client root certificate of P2SVpnServerConfiguration. |  [optional] |
|**provisioningState** | **String** | The provisioning state of the P2SVpnServerConfiguration resource. Possible values are: &#39;Updating&#39;, &#39;Deleting&#39;, and &#39;Failed&#39;. |  [optional] [readonly] |
|**radiusServerAddress** | **String** | The radius server address property of the P2SVpnServerConfiguration resource for point to site client connection. |  [optional] |
|**radiusServerSecret** | **String** | The radius secret property of the P2SVpnServerConfiguration resource for point to site client connection. |  [optional] |
|**vpnClientIpsecPolicies** | [**List&lt;P2SVpnServerConfigurationPropertiesVpnClientIpsecPoliciesInner&gt;**](P2SVpnServerConfigurationPropertiesVpnClientIpsecPoliciesInner.md) | VpnClientIpsecPolicies for P2SVpnServerConfiguration. |  [optional] |
|**vpnProtocols** | [**List&lt;VpnProtocolsEnum&gt;**](#List&lt;VpnProtocolsEnum&gt;) | VPN protocols for the P2SVpnServerConfiguration. |  [optional] |



## Enum: List&lt;VpnProtocolsEnum&gt;

| Name | Value |
|---- | -----|
| IKE_V2 | &quot;IkeV2&quot; |
| OPEN_VPN | &quot;OpenVPN&quot; |



