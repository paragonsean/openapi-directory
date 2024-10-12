

# UpdateFlowSourceRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**decryption** | [**UpdateFlowOutputRequestEncryption**](UpdateFlowOutputRequestEncryption.md) |  |  [optional] |
|**description** | **String** | A description for the source. This value is not used or seen outside of the current AWS Elemental MediaConnect account. |  [optional] |
|**entitlementArn** | **String** | The ARN of the entitlement that allows you to subscribe to this flow. The entitlement is set by the flow originator, and the ARN is generated as part of the originator&#39;s flow. |  [optional] |
|**ingestPort** | **Integer** | The port that the flow will be listening on for incoming content. |  [optional] |
|**maxBitrate** | **Integer** | The smoothing max bitrate (in bps) for RIST, RTP, and RTP-FEC streams. |  [optional] |
|**maxLatency** | **Integer** | The maximum latency in milliseconds. This parameter applies only to RIST-based, Zixi-based, and Fujitsu-based streams. |  [optional] |
|**maxSyncBuffer** | **Integer** | The size of the buffer (in milliseconds) to use to sync incoming source data. |  [optional] |
|**mediaStreamSourceConfigurations** | [**List&lt;MediaStreamSourceConfigurationRequest&gt;**](MediaStreamSourceConfigurationRequest.md) | The media streams that are associated with the source, and the parameters for those associations. |  [optional] |
|**minLatency** | **Integer** | The minimum latency in milliseconds for SRT-based streams. In streams that use the SRT protocol, this value that you set on your MediaConnect source or output represents the minimal potential latency of that connection. The latency of the stream is set to the highest number between the sender’s minimum latency and the receiver’s minimum latency. |  [optional] |
|**protocol** | [**ProtocolEnum**](#ProtocolEnum) | The protocol that is used by the source. |  [optional] |
|**senderControlPort** | **Integer** | The port that the flow uses to send outbound requests to initiate connection with the sender. |  [optional] |
|**senderIpAddress** | **String** | The IP address that the flow communicates with to initiate connection with the sender. |  [optional] |
|**sourceListenerAddress** | **String** | Source IP or domain name for SRT-caller protocol. |  [optional] |
|**sourceListenerPort** | **Integer** | Source port for SRT-caller protocol. |  [optional] |
|**streamId** | **String** | The stream ID that you want to use for this transport. This parameter applies only to Zixi and SRT caller-based streams. |  [optional] |
|**vpcInterfaceName** | **String** | The name of the VPC interface to use for this source. |  [optional] |
|**whitelistCidr** | **String** | The range of IP addresses that should be allowed to contribute content to your source. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16. |  [optional] |
|**gatewayBridgeSource** | [**UpdateFlowSourceRequestGatewayBridgeSource**](UpdateFlowSourceRequestGatewayBridgeSource.md) |  |  [optional] |



## Enum: ProtocolEnum

| Name | Value |
|---- | -----|
| ZIXI_PUSH | &quot;zixi-push&quot; |
| RTP_FEC | &quot;rtp-fec&quot; |
| RTP | &quot;rtp&quot; |
| ZIXI_PULL | &quot;zixi-pull&quot; |
| RIST | &quot;rist&quot; |
| ST2110_JPEGXS | &quot;st2110-jpegxs&quot; |
| CDI | &quot;cdi&quot; |
| SRT_LISTENER | &quot;srt-listener&quot; |
| SRT_CALLER | &quot;srt-caller&quot; |
| FUJITSU_QOS | &quot;fujitsu-qos&quot; |
| UDP | &quot;udp&quot; |



