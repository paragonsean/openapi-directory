

# Type

A type definition for some HL7v2 type (incl. Segments and Datatypes).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fields** | [**List&lt;Field&gt;**](Field.md) | The (sub) fields this type has (if not primitive). |  [optional] |
|**name** | **String** | The name of this type. This would be the segment or datatype name. For example, \&quot;PID\&quot; or \&quot;XPN\&quot;. |  [optional] |
|**primitive** | [**PrimitiveEnum**](#PrimitiveEnum) | If this is a primitive type then this field is the type of the primitive For example, STRING. Leave unspecified for composite types. |  [optional] |



## Enum: PrimitiveEnum

| Name | Value |
|---- | -----|
| PRIMITIVE_UNSPECIFIED | &quot;PRIMITIVE_UNSPECIFIED&quot; |
| STRING | &quot;STRING&quot; |
| VARIES | &quot;VARIES&quot; |
| UNESCAPED_STRING | &quot;UNESCAPED_STRING&quot; |



