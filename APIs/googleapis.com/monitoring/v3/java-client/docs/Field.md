

# Field

A single field of a message type.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cardinality** | [**CardinalityEnum**](#CardinalityEnum) | The field cardinality. |  [optional] |
|**defaultValue** | **String** | The string value of the default value of this field. Proto2 syntax only. |  [optional] |
|**jsonName** | **String** | The field JSON name. |  [optional] |
|**kind** | [**KindEnum**](#KindEnum) | The field type. |  [optional] |
|**name** | **String** | The field name. |  [optional] |
|**number** | **Integer** | The field number. |  [optional] |
|**oneofIndex** | **Integer** | The index of the field type in Type.oneofs, for message or enumeration types. The first type has index 1; zero means the type is not in the list. |  [optional] |
|**options** | [**List&lt;Option&gt;**](Option.md) | The protocol buffer options. |  [optional] |
|**packed** | **Boolean** | Whether to use alternative packed wire representation. |  [optional] |
|**typeUrl** | **String** | The field type URL, without the scheme, for message or enumeration types. Example: \&quot;type.googleapis.com/google.protobuf.Timestamp\&quot;. |  [optional] |



## Enum: CardinalityEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;CARDINALITY_UNKNOWN&quot; |
| OPTIONAL | &quot;CARDINALITY_OPTIONAL&quot; |
| REQUIRED | &quot;CARDINALITY_REQUIRED&quot; |
| REPEATED | &quot;CARDINALITY_REPEATED&quot; |



## Enum: KindEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;TYPE_UNKNOWN&quot; |
| DOUBLE | &quot;TYPE_DOUBLE&quot; |
| FLOAT | &quot;TYPE_FLOAT&quot; |
| INT64 | &quot;TYPE_INT64&quot; |
| UINT64 | &quot;TYPE_UINT64&quot; |
| INT32 | &quot;TYPE_INT32&quot; |
| FIXED64 | &quot;TYPE_FIXED64&quot; |
| FIXED32 | &quot;TYPE_FIXED32&quot; |
| BOOL | &quot;TYPE_BOOL&quot; |
| STRING | &quot;TYPE_STRING&quot; |
| GROUP | &quot;TYPE_GROUP&quot; |
| MESSAGE | &quot;TYPE_MESSAGE&quot; |
| BYTES | &quot;TYPE_BYTES&quot; |
| UINT32 | &quot;TYPE_UINT32&quot; |
| ENUM | &quot;TYPE_ENUM&quot; |
| SFIXED32 | &quot;TYPE_SFIXED32&quot; |
| SFIXED64 | &quot;TYPE_SFIXED64&quot; |
| SINT32 | &quot;TYPE_SINT32&quot; |
| SINT64 | &quot;TYPE_SINT64&quot; |



