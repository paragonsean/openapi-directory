# AwsMediaConnect.UpdateFlowOutputRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cidrAllowList** | **[String]** | The range of IP addresses that should be allowed to initiate output requests to this flow. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16. | [optional] 
**description** | **String** | A description of the output. This description appears only on the AWS Elemental MediaConnect console and will not be seen by the end user. | [optional] 
**destination** | **String** | The IP address where you want to send the output. | [optional] 
**encryption** | [**UpdateFlowOutputRequestEncryption**](UpdateFlowOutputRequestEncryption.md) |  | [optional] 
**maxLatency** | **Number** | The maximum latency in milliseconds. This parameter applies only to RIST-based, Zixi-based, and Fujitsu-based streams. | [optional] 
**mediaStreamOutputConfigurations** | [**[MediaStreamOutputConfigurationRequest]**](MediaStreamOutputConfigurationRequest.md) | The media streams that are associated with the output, and the parameters for those associations. | [optional] 
**minLatency** | **Number** | The minimum latency in milliseconds for SRT-based streams. In streams that use the SRT protocol, this value that you set on your MediaConnect source or output represents the minimal potential latency of that connection. The latency of the stream is set to the highest number between the sender’s minimum latency and the receiver’s minimum latency. | [optional] 
**port** | **Number** | The port to use when content is distributed to this output. | [optional] 
**protocol** | **String** | The protocol to use for the output. | [optional] 
**remoteId** | **String** | The remote ID for the Zixi-pull stream. | [optional] 
**senderControlPort** | **Number** | The port that the flow uses to send outbound requests to initiate connection with the sender. | [optional] 
**senderIpAddress** | **String** | The IP address that the flow communicates with to initiate connection with the sender. | [optional] 
**smoothingLatency** | **Number** | The smoothing latency in milliseconds for RIST, RTP, and RTP-FEC streams. | [optional] 
**streamId** | **String** | The stream ID that you want to use for this transport. This parameter applies only to Zixi and SRT caller-based streams. | [optional] 
**vpcInterfaceAttachment** | [**UpdateFlowOutputRequestVpcInterfaceAttachment**](UpdateFlowOutputRequestVpcInterfaceAttachment.md) |  | [optional] 



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




