# CloudHealthcareApi.Type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fields** | [**[Field]**](Field.md) | The (sub) fields this type has (if not primitive). | [optional] 
**name** | **String** | The name of this type. This would be the segment or datatype name. For example, \&quot;PID\&quot; or \&quot;XPN\&quot;. | [optional] 
**primitive** | **String** | If this is a primitive type then this field is the type of the primitive For example, STRING. Leave unspecified for composite types. | [optional] 



## Enum: PrimitiveEnum


* `PRIMITIVE_UNSPECIFIED` (value: `"PRIMITIVE_UNSPECIFIED"`)

* `STRING` (value: `"STRING"`)

* `VARIES` (value: `"VARIES"`)

* `UNESCAPED_STRING` (value: `"UNESCAPED_STRING"`)




