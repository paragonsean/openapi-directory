# AwsElementalMediaLive.CreateChannelRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cdiInputSpecification** | [**CreateChannelRequestCdiInputSpecification**](CreateChannelRequestCdiInputSpecification.md) |  | [optional] 
**channelClass** | **String** | A standard channel has two encoding pipelines and a single pipeline channel only has one. | [optional] 
**destinations** | [**[OutputDestination]**](OutputDestination.md) | Placeholder documentation for __listOfOutputDestination | [optional] 
**encoderSettings** | [**CreateChannelRequestEncoderSettings**](CreateChannelRequestEncoderSettings.md) |  | [optional] 
**inputAttachments** | [**[InputAttachment]**](InputAttachment.md) | Placeholder documentation for __listOfInputAttachment | [optional] 
**inputSpecification** | [**CreateChannelRequestInputSpecification**](CreateChannelRequestInputSpecification.md) |  | [optional] 
**logLevel** | **String** | The log level the user wants for their channel. | [optional] 
**maintenance** | [**CreateChannelRequestMaintenance**](CreateChannelRequestMaintenance.md) |  | [optional] 
**name** | **String** | Placeholder documentation for __string | [optional] 
**requestId** | **String** | Placeholder documentation for __string | [optional] 
**reserved** | **String** | Placeholder documentation for __string | [optional] 
**roleArn** | **String** | Placeholder documentation for __string | [optional] 
**tags** | **{String: String}** | Placeholder documentation for Tags | [optional] 
**vpc** | [**CreateChannelRequestVpc**](CreateChannelRequestVpc.md) |  | [optional] 



## Enum: ChannelClassEnum


* `STANDARD` (value: `"STANDARD"`)

* `SINGLE_PIPELINE` (value: `"SINGLE_PIPELINE"`)





## Enum: LogLevelEnum


* `ERROR` (value: `"ERROR"`)

* `WARNING` (value: `"WARNING"`)

* `INFO` (value: `"INFO"`)

* `DEBUG` (value: `"DEBUG"`)

* `DISABLED` (value: `"DISABLED"`)




