

# Type

`Type` indicates the type of a Cloud Spanner value, as might be stored in a table cell or returned from an SQL query.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**arrayElementType** | [**Type**](Type.md) |  |  [optional] |
|**code** | [**CodeEnum**](#CodeEnum) | Required. The TypeCode for this type. |  [optional] |
|**protoTypeFqn** | **String** | If code &#x3D;&#x3D; PROTO or code &#x3D;&#x3D; ENUM, then &#x60;proto_type_fqn&#x60; is the fully qualified name of the proto type representing the proto/enum definition. |  [optional] |
|**structType** | [**StructType**](StructType.md) |  |  [optional] |
|**typeAnnotation** | [**TypeAnnotationEnum**](#TypeAnnotationEnum) | The TypeAnnotationCode that disambiguates SQL type that Spanner will use to represent values of this type during query processing. This is necessary for some type codes because a single TypeCode can be mapped to different SQL types depending on the SQL dialect. type_annotation typically is not needed to process the content of a value (it doesn&#39;t affect serialization) and clients can ignore it on the read path. |  [optional] |



## Enum: CodeEnum

| Name | Value |
|---- | -----|
| TYPE_CODE_UNSPECIFIED | &quot;TYPE_CODE_UNSPECIFIED&quot; |
| BOOL | &quot;BOOL&quot; |
| INT64 | &quot;INT64&quot; |
| FLOAT64 | &quot;FLOAT64&quot; |
| FLOAT32 | &quot;FLOAT32&quot; |
| TIMESTAMP | &quot;TIMESTAMP&quot; |
| DATE | &quot;DATE&quot; |
| STRING | &quot;STRING&quot; |
| BYTES | &quot;BYTES&quot; |
| ARRAY | &quot;ARRAY&quot; |
| STRUCT | &quot;STRUCT&quot; |
| NUMERIC | &quot;NUMERIC&quot; |
| JSON | &quot;JSON&quot; |
| PROTO | &quot;PROTO&quot; |
| ENUM | &quot;ENUM&quot; |



## Enum: TypeAnnotationEnum

| Name | Value |
|---- | -----|
| TYPE_ANNOTATION_CODE_UNSPECIFIED | &quot;TYPE_ANNOTATION_CODE_UNSPECIFIED&quot; |
| PG_NUMERIC | &quot;PG_NUMERIC&quot; |
| PG_JSONB | &quot;PG_JSONB&quot; |



