# AwsElementalMediaLive.UpdateChannelRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cdiInputSpecification** | [**CreateChannelRequestCdiInputSpecification**](CreateChannelRequestCdiInputSpecification.md) |  | [optional] 
**destinations** | [**[OutputDestination]**](OutputDestination.md) | Placeholder documentation for __listOfOutputDestination | [optional] 
**encoderSettings** | [**CreateChannelRequestEncoderSettings**](CreateChannelRequestEncoderSettings.md) |  | [optional] 
**inputAttachments** | [**[InputAttachment]**](InputAttachment.md) | Placeholder documentation for __listOfInputAttachment | [optional] 
**inputSpecification** | [**CreateChannelRequestInputSpecification**](CreateChannelRequestInputSpecification.md) |  | [optional] 
**logLevel** | **String** | The log level the user wants for their channel. | [optional] 
**maintenance** | [**UpdateChannelRequestMaintenance**](UpdateChannelRequestMaintenance.md) |  | [optional] 
**name** | **String** | Placeholder documentation for __string | [optional] 
**roleArn** | **String** | Placeholder documentation for __string | [optional] 



## Enum: LogLevelEnum


* `ERROR` (value: `"ERROR"`)

* `WARNING` (value: `"WARNING"`)

* `INFO` (value: `"INFO"`)

* `DEBUG` (value: `"DEBUG"`)

* `DISABLED` (value: `"DISABLED"`)




