

# Proto2FieldDescriptorProto

Describes a field within a message.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**defaultValue** | **String** | For numeric types, contains the original text representation of the value. For booleans, \&quot;true\&quot; or \&quot;false\&quot;. For strings, contains the default text contents (not escaped in any way). For bytes, contains the C escaped value. All bytes &gt;&#x3D; 128 are escaped. |  [optional] |
|**jsonName** | **String** | JSON name of this field. The value is set by protocol compiler. If the user has set a \&quot;json_name\&quot; option on this field, that option&#39;s value will be used. Otherwise, it&#39;s deduced from the field&#39;s name by converting it to camelCase. |  [optional] |
|**label** | [**LabelEnum**](#LabelEnum) |  |  [optional] |
|**name** | **String** |  |  [optional] |
|**number** | **Integer** |  |  [optional] |
|**oneofIndex** | **Integer** | If set, gives the index of a oneof in the containing type&#39;s oneof_decl list. This field is a member of that oneof. |  [optional] |
|**proto3Optional** | **Boolean** | If true, this is a proto3 \&quot;optional\&quot;. When a proto3 field is optional, it tracks presence regardless of field type. When proto3_optional is true, this field must belong to a oneof to signal to old proto3 clients that presence is tracked for this field. This oneof is known as a \&quot;synthetic\&quot; oneof, and this field must be its sole member (each proto3 optional field gets its own synthetic oneof). Synthetic oneofs exist in the descriptor only, and do not generate any API. Synthetic oneofs must be ordered after all \&quot;real\&quot; oneofs. For message fields, proto3_optional doesn&#39;t create any semantic change, since non-repeated message fields always track presence. However it still indicates the semantic detail of whether the user wrote \&quot;optional\&quot; or not. This can be useful for round-tripping the .proto file. For consistency we give message fields a synthetic oneof also, even though it is not required to track presence. This is especially important because the parser can&#39;t tell if a field is a message or an enum, so it must always create a synthetic oneof. Proto2 optional fields do not set this flag, because they already indicate optional with &#x60;LABEL_OPTIONAL&#x60;. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | If type_name is set, this need not be set. If both this and type_name are set, this must be one of TYPE_ENUM, TYPE_MESSAGE or TYPE_GROUP. |  [optional] |
|**typeName** | **String** | For message and enum types, this is the name of the type. If the name starts with a &#39;.&#39;, it is fully-qualified. Otherwise, C++-like scoping rules are used to find the type (i.e. first the nested types within this message are searched, then within the parent, on up to the root namespace). |  [optional] |



## Enum: LabelEnum

| Name | Value |
|---- | -----|
| OPTIONAL | &quot;LABEL_OPTIONAL&quot; |
| REPEATED | &quot;LABEL_REPEATED&quot; |
| REQUIRED | &quot;LABEL_REQUIRED&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
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



