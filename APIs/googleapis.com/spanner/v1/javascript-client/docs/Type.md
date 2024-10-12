# CloudSpannerApi.Type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arrayElementType** | [**Type**](Type.md) |  | [optional] 
**code** | **String** | Required. The TypeCode for this type. | [optional] 
**protoTypeFqn** | **String** | If code &#x3D;&#x3D; PROTO or code &#x3D;&#x3D; ENUM, then &#x60;proto_type_fqn&#x60; is the fully qualified name of the proto type representing the proto/enum definition. | [optional] 
**structType** | [**StructType**](StructType.md) |  | [optional] 
**typeAnnotation** | **String** | The TypeAnnotationCode that disambiguates SQL type that Spanner will use to represent values of this type during query processing. This is necessary for some type codes because a single TypeCode can be mapped to different SQL types depending on the SQL dialect. type_annotation typically is not needed to process the content of a value (it doesn&#39;t affect serialization) and clients can ignore it on the read path. | [optional] 



## Enum: CodeEnum


* `TYPE_CODE_UNSPECIFIED` (value: `"TYPE_CODE_UNSPECIFIED"`)

* `BOOL` (value: `"BOOL"`)

* `INT64` (value: `"INT64"`)

* `FLOAT64` (value: `"FLOAT64"`)

* `FLOAT32` (value: `"FLOAT32"`)

* `TIMESTAMP` (value: `"TIMESTAMP"`)

* `DATE` (value: `"DATE"`)

* `STRING` (value: `"STRING"`)

* `BYTES` (value: `"BYTES"`)

* `ARRAY` (value: `"ARRAY"`)

* `STRUCT` (value: `"STRUCT"`)

* `NUMERIC` (value: `"NUMERIC"`)

* `JSON` (value: `"JSON"`)

* `PROTO` (value: `"PROTO"`)

* `ENUM` (value: `"ENUM"`)





## Enum: TypeAnnotationEnum


* `TYPE_ANNOTATION_CODE_UNSPECIFIED` (value: `"TYPE_ANNOTATION_CODE_UNSPECIFIED"`)

* `PG_NUMERIC` (value: `"PG_NUMERIC"`)

* `PG_JSONB` (value: `"PG_JSONB"`)




