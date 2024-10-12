

# Type

A protocol buffer message type.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**edition** | **String** | The source edition string, only valid when syntax is SYNTAX_EDITIONS. |  [optional] |
|**fields** | [**List&lt;Field&gt;**](Field.md) | The list of fields. |  [optional] |
|**name** | **String** | The fully qualified message name. |  [optional] |
|**oneofs** | **List&lt;String&gt;** | The list of types appearing in oneof definitions in this type. |  [optional] |
|**options** | [**List&lt;Option&gt;**](Option.md) | The protocol buffer options. |  [optional] |
|**sourceContext** | [**SourceContext**](SourceContext.md) |  |  [optional] |
|**syntax** | [**SyntaxEnum**](#SyntaxEnum) | The source syntax. |  [optional] |



## Enum: SyntaxEnum

| Name | Value |
|---- | -----|
| PROTO2 | &quot;SYNTAX_PROTO2&quot; |
| PROTO3 | &quot;SYNTAX_PROTO3&quot; |
| EDITIONS | &quot;SYNTAX_EDITIONS&quot; |



