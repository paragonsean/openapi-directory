

# CreateChannelRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cdiInputSpecification** | [**CreateChannelRequestCdiInputSpecification**](CreateChannelRequestCdiInputSpecification.md) |  |  [optional] |
|**channelClass** | [**ChannelClassEnum**](#ChannelClassEnum) | A standard channel has two encoding pipelines and a single pipeline channel only has one. |  [optional] |
|**destinations** | [**List&lt;OutputDestination&gt;**](OutputDestination.md) | Placeholder documentation for __listOfOutputDestination |  [optional] |
|**encoderSettings** | [**CreateChannelRequestEncoderSettings**](CreateChannelRequestEncoderSettings.md) |  |  [optional] |
|**inputAttachments** | [**List&lt;InputAttachment&gt;**](InputAttachment.md) | Placeholder documentation for __listOfInputAttachment |  [optional] |
|**inputSpecification** | [**CreateChannelRequestInputSpecification**](CreateChannelRequestInputSpecification.md) |  |  [optional] |
|**logLevel** | [**LogLevelEnum**](#LogLevelEnum) | The log level the user wants for their channel. |  [optional] |
|**maintenance** | [**CreateChannelRequestMaintenance**](CreateChannelRequestMaintenance.md) |  |  [optional] |
|**name** | **String** | Placeholder documentation for __string |  [optional] |
|**requestId** | **String** | Placeholder documentation for __string |  [optional] |
|**reserved** | **String** | Placeholder documentation for __string |  [optional] |
|**roleArn** | **String** | Placeholder documentation for __string |  [optional] |
|**tags** | **Map&lt;String, String&gt;** | Placeholder documentation for Tags |  [optional] |
|**vpc** | [**CreateChannelRequestVpc**](CreateChannelRequestVpc.md) |  |  [optional] |



## Enum: ChannelClassEnum

| Name | Value |
|---- | -----|
| STANDARD | &quot;STANDARD&quot; |
| SINGLE_PIPELINE | &quot;SINGLE_PIPELINE&quot; |



## Enum: LogLevelEnum

| Name | Value |
|---- | -----|
| ERROR | &quot;ERROR&quot; |
| WARNING | &quot;WARNING&quot; |
| INFO | &quot;INFO&quot; |
| DEBUG | &quot;DEBUG&quot; |
| DISABLED | &quot;DISABLED&quot; |



