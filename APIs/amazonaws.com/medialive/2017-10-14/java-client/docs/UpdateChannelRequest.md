

# UpdateChannelRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cdiInputSpecification** | [**CreateChannelRequestCdiInputSpecification**](CreateChannelRequestCdiInputSpecification.md) |  |  [optional] |
|**destinations** | [**List&lt;OutputDestination&gt;**](OutputDestination.md) | Placeholder documentation for __listOfOutputDestination |  [optional] |
|**encoderSettings** | [**CreateChannelRequestEncoderSettings**](CreateChannelRequestEncoderSettings.md) |  |  [optional] |
|**inputAttachments** | [**List&lt;InputAttachment&gt;**](InputAttachment.md) | Placeholder documentation for __listOfInputAttachment |  [optional] |
|**inputSpecification** | [**CreateChannelRequestInputSpecification**](CreateChannelRequestInputSpecification.md) |  |  [optional] |
|**logLevel** | [**LogLevelEnum**](#LogLevelEnum) | The log level the user wants for their channel. |  [optional] |
|**maintenance** | [**UpdateChannelRequestMaintenance**](UpdateChannelRequestMaintenance.md) |  |  [optional] |
|**name** | **String** | Placeholder documentation for __string |  [optional] |
|**roleArn** | **String** | Placeholder documentation for __string |  [optional] |



## Enum: LogLevelEnum

| Name | Value |
|---- | -----|
| ERROR | &quot;ERROR&quot; |
| WARNING | &quot;WARNING&quot; |
| INFO | &quot;INFO&quot; |
| DEBUG | &quot;DEBUG&quot; |
| DISABLED | &quot;DISABLED&quot; |



