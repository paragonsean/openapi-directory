

# Filter

Filter matches L4 traffic.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**destRange** | **String** | Optional. The destination IP range of outgoing packets that this policy-based route applies to. Default is \&quot;0.0.0.0/0\&quot; if protocol version is IPv4. |  [optional] |
|**ipProtocol** | **String** | Optional. The IP protocol that this policy-based route applies to. Valid values are &#39;TCP&#39;, &#39;UDP&#39;, and &#39;ALL&#39;. Default is &#39;ALL&#39;. |  [optional] |
|**protocolVersion** | [**ProtocolVersionEnum**](#ProtocolVersionEnum) | Required. Internet protocol versions this policy-based route applies to. For this version, only IPV4 is supported. |  [optional] |
|**srcRange** | **String** | Optional. The source IP range of outgoing packets that this policy-based route applies to. Default is \&quot;0.0.0.0/0\&quot; if protocol version is IPv4. |  [optional] |



## Enum: ProtocolVersionEnum

| Name | Value |
|---- | -----|
| PROTOCOL_VERSION_UNSPECIFIED | &quot;PROTOCOL_VERSION_UNSPECIFIED&quot; |
| IPV4 | &quot;IPV4&quot; |



