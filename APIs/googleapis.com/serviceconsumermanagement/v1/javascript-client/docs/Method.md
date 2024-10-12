# ServiceConsumerManagementApi.Method

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** | The simple name of this method. | [optional] 
**options** | [**[Option]**](Option.md) | Any metadata attached to the method. | [optional] 
**requestStreaming** | **Boolean** | If true, the request is streamed. | [optional] 
**requestTypeUrl** | **String** | A URL of the input message type. | [optional] 
**responseStreaming** | **Boolean** | If true, the response is streamed. | [optional] 
**responseTypeUrl** | **String** | The URL of the output message type. | [optional] 
**syntax** | **String** | The source syntax of this method. | [optional] 



## Enum: SyntaxEnum


* `PROTO2` (value: `"SYNTAX_PROTO2"`)

* `PROTO3` (value: `"SYNTAX_PROTO3"`)

* `EDITIONS` (value: `"SYNTAX_EDITIONS"`)




