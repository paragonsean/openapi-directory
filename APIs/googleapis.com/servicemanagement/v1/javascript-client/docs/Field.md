# ServiceManagementApi.Field

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cardinality** | **String** | The field cardinality. | [optional] 
**defaultValue** | **String** | The string value of the default value of this field. Proto2 syntax only. | [optional] 
**jsonName** | **String** | The field JSON name. | [optional] 
**kind** | **String** | The field type. | [optional] 
**name** | **String** | The field name. | [optional] 
**number** | **Number** | The field number. | [optional] 
**oneofIndex** | **Number** | The index of the field type in &#x60;Type.oneofs&#x60;, for message or enumeration types. The first type has index 1; zero means the type is not in the list. | [optional] 
**options** | [**[Option]**](Option.md) | The protocol buffer options. | [optional] 
**packed** | **Boolean** | Whether to use alternative packed wire representation. | [optional] 
**typeUrl** | **String** | The field type URL, without the scheme, for message or enumeration types. Example: &#x60;\&quot;type.googleapis.com/google.protobuf.Timestamp\&quot;&#x60;. | [optional] 



## Enum: CardinalityEnum


* `UNKNOWN` (value: `"CARDINALITY_UNKNOWN"`)

* `OPTIONAL` (value: `"CARDINALITY_OPTIONAL"`)

* `REQUIRED` (value: `"CARDINALITY_REQUIRED"`)

* `REPEATED` (value: `"CARDINALITY_REPEATED"`)





## Enum: KindEnum


* `UNKNOWN` (value: `"TYPE_UNKNOWN"`)

* `DOUBLE` (value: `"TYPE_DOUBLE"`)

* `FLOAT` (value: `"TYPE_FLOAT"`)

* `INT64` (value: `"TYPE_INT64"`)

* `UINT64` (value: `"TYPE_UINT64"`)

* `INT32` (value: `"TYPE_INT32"`)

* `FIXED64` (value: `"TYPE_FIXED64"`)

* `FIXED32` (value: `"TYPE_FIXED32"`)

* `BOOL` (value: `"TYPE_BOOL"`)

* `STRING` (value: `"TYPE_STRING"`)

* `GROUP` (value: `"TYPE_GROUP"`)

* `MESSAGE` (value: `"TYPE_MESSAGE"`)

* `BYTES` (value: `"TYPE_BYTES"`)

* `UINT32` (value: `"TYPE_UINT32"`)

* `ENUM` (value: `"TYPE_ENUM"`)

* `SFIXED32` (value: `"TYPE_SFIXED32"`)

* `SFIXED64` (value: `"TYPE_SFIXED64"`)

* `SINT32` (value: `"TYPE_SINT32"`)

* `SINT64` (value: `"TYPE_SINT64"`)




