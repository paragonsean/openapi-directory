# AwsElementalMediaLive.CreateInputRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destinations** | [**[InputDestinationRequest]**](InputDestinationRequest.md) | Placeholder documentation for __listOfInputDestinationRequest | [optional] 
**inputDevices** | [**[InputDeviceSettings]**](InputDeviceSettings.md) | Placeholder documentation for __listOfInputDeviceSettings | [optional] 
**inputSecurityGroups** | **[String]** | Placeholder documentation for __listOf__string | [optional] 
**mediaConnectFlows** | [**[MediaConnectFlowRequest]**](MediaConnectFlowRequest.md) | Placeholder documentation for __listOfMediaConnectFlowRequest | [optional] 
**name** | **String** | Placeholder documentation for __string | [optional] 
**requestId** | **String** | Placeholder documentation for __string | [optional] 
**roleArn** | **String** | Placeholder documentation for __string | [optional] 
**sources** | [**[InputSourceRequest]**](InputSourceRequest.md) | Placeholder documentation for __listOfInputSourceRequest | [optional] 
**tags** | **{String: String}** | Placeholder documentation for Tags | [optional] 
**type** | **String** | The different types of inputs that AWS Elemental MediaLive supports. | [optional] 
**vpc** | [**CreateInputRequestVpc**](CreateInputRequestVpc.md) |  | [optional] 



## Enum: TypeEnum


* `UDP_PUSH` (value: `"UDP_PUSH"`)

* `RTP_PUSH` (value: `"RTP_PUSH"`)

* `RTMP_PUSH` (value: `"RTMP_PUSH"`)

* `RTMP_PULL` (value: `"RTMP_PULL"`)

* `URL_PULL` (value: `"URL_PULL"`)

* `MP4_FILE` (value: `"MP4_FILE"`)

* `MEDIACONNECT` (value: `"MEDIACONNECT"`)

* `INPUT_DEVICE` (value: `"INPUT_DEVICE"`)

* `AWS_CDI` (value: `"AWS_CDI"`)

* `TS_FILE` (value: `"TS_FILE"`)




