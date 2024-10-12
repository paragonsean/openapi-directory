# AwsMediaConnect.UpdateFlowSourceRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**decryption** | [**UpdateFlowOutputRequestEncryption**](UpdateFlowOutputRequestEncryption.md) |  | [optional] 
**description** | **String** | A description for the source. This value is not used or seen outside of the current AWS Elemental MediaConnect account. | [optional] 
**entitlementArn** | **String** | The ARN of the entitlement that allows you to subscribe to this flow. The entitlement is set by the flow originator, and the ARN is generated as part of the originator&#39;s flow. | [optional] 
**ingestPort** | **Number** | The port that the flow will be listening on for incoming content. | [optional] 
**maxBitrate** | **Number** | The smoothing max bitrate (in bps) for RIST, RTP, and RTP-FEC streams. | [optional] 
**maxLatency** | **Number** | The maximum latency in milliseconds. This parameter applies only to RIST-based, Zixi-based, and Fujitsu-based streams. | [optional] 
**maxSyncBuffer** | **Number** | The size of the buffer (in milliseconds) to use to sync incoming source data. | [optional] 
**mediaStreamSourceConfigurations** | [**[MediaStreamSourceConfigurationRequest]**](MediaStreamSourceConfigurationRequest.md) | The media streams that are associated with the source, and the parameters for those associations. | [optional] 
**minLatency** | **Number** | The minimum latency in milliseconds for SRT-based streams. In streams that use the SRT protocol, this value that you set on your MediaConnect source or output represents the minimal potential latency of that connection. The latency of the stream is set to the highest number between the sender’s minimum latency and the receiver’s minimum latency. | [optional] 
**protocol** | **String** | The protocol that is used by the source. | [optional] 
**senderControlPort** | **Number** | The port that the flow uses to send outbound requests to initiate connection with the sender. | [optional] 
**senderIpAddress** | **String** | The IP address that the flow communicates with to initiate connection with the sender. | [optional] 
**sourceListenerAddress** | **String** | Source IP or domain name for SRT-caller protocol. | [optional] 
**sourceListenerPort** | **Number** | Source port for SRT-caller protocol. | [optional] 
**streamId** | **String** | The stream ID that you want to use for this transport. This parameter applies only to Zixi and SRT caller-based streams. | [optional] 
**vpcInterfaceName** | **String** | The name of the VPC interface to use for this source. | [optional] 
**whitelistCidr** | **String** | The range of IP addresses that should be allowed to contribute content to your source. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16. | [optional] 
**gatewayBridgeSource** | [**UpdateFlowSourceRequestGatewayBridgeSource**](UpdateFlowSourceRequestGatewayBridgeSource.md) |  | [optional] 



## Enum: ProtocolEnum


* `zixi-push` (value: `"zixi-push"`)

* `rtp-fec` (value: `"rtp-fec"`)

* `rtp` (value: `"rtp"`)

* `zixi-pull` (value: `"zixi-pull"`)

* `rist` (value: `"rist"`)

* `st2110-jpegxs` (value: `"st2110-jpegxs"`)

* `cdi` (value: `"cdi"`)

* `srt-listener` (value: `"srt-listener"`)

* `srt-caller` (value: `"srt-caller"`)

* `fujitsu-qos` (value: `"fujitsu-qos"`)

* `udp` (value: `"udp"`)




