

# GetNetworkSwitchDhcpV4ServersSeen200ResponseInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clientId** | **String** | Client id of the server if available. |  [optional] |
|**device** | [**GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerDevice**](GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerDevice.md) |  |  [optional] |
|**ipv4** | [**GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerIpv4**](GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerIpv4.md) |  |  [optional] |
|**isAllowed** | **Boolean** | Whether the server is allowed or blocked. Always true for configured servers. |  [optional] |
|**isConfigured** | **Boolean** | Whether the server is configured. |  [optional] |
|**lastAck** | [**GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastAck**](GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastAck.md) |  |  [optional] |
|**lastPacket** | [**GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacket**](GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacket.md) |  |  [optional] |
|**lastSeenAt** | **OffsetDateTime** | Last time the server was seen. |  [optional] |
|**mac** | **String** | Mac address of the server. |  [optional] |
|**seenBy** | [**List&lt;GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerSeenByInner&gt;**](GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerSeenByInner.md) | Devices that saw the server. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | server type. Can be a &#39;device&#39;, &#39;stack&#39;, or &#39;discovered&#39; (i.e client). |  [optional] |
|**vlan** | **Integer** | Vlan id of the server. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| DEVICE | &quot;device&quot; |
| DISCOVERED | &quot;discovered&quot; |
| STACK | &quot;stack&quot; |



