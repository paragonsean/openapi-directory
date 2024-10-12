

# ModelEnum

Enum type definition.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**edition** | **String** | The source edition string, only valid when syntax is SYNTAX_EDITIONS. |  [optional] |
|**enumvalue** | [**List&lt;EnumValue&gt;**](EnumValue.md) | Enum value definitions. |  [optional] |
|**name** | **String** | Enum type name. |  [optional] |
|**options** | [**List&lt;Option&gt;**](Option.md) | Protocol buffer options. |  [optional] |
|**sourceContext** | [**SourceContext**](SourceContext.md) |  |  [optional] |
|**syntax** | [**SyntaxEnum**](#SyntaxEnum) | The source syntax. |  [optional] |



## Enum: SyntaxEnum

| Name | Value |
|---- | -----|
| PROTO2 | &quot;SYNTAX_PROTO2&quot; |
| PROTO3 | &quot;SYNTAX_PROTO3&quot; |
| EDITIONS | &quot;SYNTAX_EDITIONS&quot; |



