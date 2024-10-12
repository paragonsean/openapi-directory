

# Method

Method represents a method of an API interface.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | The simple name of this method. |  [optional] |
|**options** | [**List&lt;Option&gt;**](Option.md) | Any metadata attached to the method. |  [optional] |
|**requestStreaming** | **Boolean** | If true, the request is streamed. |  [optional] |
|**requestTypeUrl** | **String** | A URL of the input message type. |  [optional] |
|**responseStreaming** | **Boolean** | If true, the response is streamed. |  [optional] |
|**responseTypeUrl** | **String** | The URL of the output message type. |  [optional] |
|**syntax** | [**SyntaxEnum**](#SyntaxEnum) | The source syntax of this method. |  [optional] |



## Enum: SyntaxEnum

| Name | Value |
|---- | -----|
| PROTO2 | &quot;SYNTAX_PROTO2&quot; |
| PROTO3 | &quot;SYNTAX_PROTO3&quot; |
| EDITIONS | &quot;SYNTAX_EDITIONS&quot; |



