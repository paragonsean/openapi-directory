# CloudMonitoringApi.Type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**edition** | **String** | The source edition string, only valid when syntax is SYNTAX_EDITIONS. | [optional] 
**fields** | [**[Field]**](Field.md) | The list of fields. | [optional] 
**name** | **String** | The fully qualified message name. | [optional] 
**oneofs** | **[String]** | The list of types appearing in oneof definitions in this type. | [optional] 
**options** | [**[Option]**](Option.md) | The protocol buffer options. | [optional] 
**sourceContext** | [**SourceContext**](SourceContext.md) |  | [optional] 
**syntax** | **String** | The source syntax. | [optional] 



## Enum: SyntaxEnum


* `PROTO2` (value: `"SYNTAX_PROTO2"`)

* `PROTO3` (value: `"SYNTAX_PROTO3"`)

* `EDITIONS` (value: `"SYNTAX_EDITIONS"`)




