

# CreateInputRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**destinations** | [**List&lt;InputDestinationRequest&gt;**](InputDestinationRequest.md) | Placeholder documentation for __listOfInputDestinationRequest |  [optional] |
|**inputDevices** | [**List&lt;InputDeviceSettings&gt;**](InputDeviceSettings.md) | Placeholder documentation for __listOfInputDeviceSettings |  [optional] |
|**inputSecurityGroups** | **List&lt;String&gt;** | Placeholder documentation for __listOf__string |  [optional] |
|**mediaConnectFlows** | [**List&lt;MediaConnectFlowRequest&gt;**](MediaConnectFlowRequest.md) | Placeholder documentation for __listOfMediaConnectFlowRequest |  [optional] |
|**name** | **String** | Placeholder documentation for __string |  [optional] |
|**requestId** | **String** | Placeholder documentation for __string |  [optional] |
|**roleArn** | **String** | Placeholder documentation for __string |  [optional] |
|**sources** | [**List&lt;InputSourceRequest&gt;**](InputSourceRequest.md) | Placeholder documentation for __listOfInputSourceRequest |  [optional] |
|**tags** | **Map&lt;String, String&gt;** | Placeholder documentation for Tags |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The different types of inputs that AWS Elemental MediaLive supports. |  [optional] |
|**vpc** | [**CreateInputRequestVpc**](CreateInputRequestVpc.md) |  |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| UDP_PUSH | &quot;UDP_PUSH&quot; |
| RTP_PUSH | &quot;RTP_PUSH&quot; |
| RTMP_PUSH | &quot;RTMP_PUSH&quot; |
| RTMP_PULL | &quot;RTMP_PULL&quot; |
| URL_PULL | &quot;URL_PULL&quot; |
| MP4_FILE | &quot;MP4_FILE&quot; |
| MEDIACONNECT | &quot;MEDIACONNECT&quot; |
| INPUT_DEVICE | &quot;INPUT_DEVICE&quot; |
| AWS_CDI | &quot;AWS_CDI&quot; |
| TS_FILE | &quot;TS_FILE&quot; |



