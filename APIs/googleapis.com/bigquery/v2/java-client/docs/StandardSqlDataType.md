

# StandardSqlDataType

The data type of a variable such as a function argument. Examples include: * INT64: `{\"typeKind\": \"INT64\"}` * ARRAY: { \"typeKind\": \"ARRAY\", \"arrayElementType\": {\"typeKind\": \"STRING\"} } * STRUCT>: { \"typeKind\": \"STRUCT\", \"structType\": { \"fields\": [ { \"name\": \"x\", \"type\": {\"typeKind\": \"STRING\"} }, { \"name\": \"y\", \"type\": { \"typeKind\": \"ARRAY\", \"arrayElementType\": {\"typeKind\": \"DATE\"} } } ] } }

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**arrayElementType** | [**StandardSqlDataType**](StandardSqlDataType.md) |  |  [optional] |
|**rangeElementType** | [**StandardSqlDataType**](StandardSqlDataType.md) |  |  [optional] |
|**structType** | [**StandardSqlStructType**](StandardSqlStructType.md) |  |  [optional] |
|**typeKind** | [**TypeKindEnum**](#TypeKindEnum) | Required. The top level type of this field. Can be any GoogleSQL data type (e.g., \&quot;INT64\&quot;, \&quot;DATE\&quot;, \&quot;ARRAY\&quot;). |  [optional] |



## Enum: TypeKindEnum

| Name | Value |
|---- | -----|
| TYPE_KIND_UNSPECIFIED | &quot;TYPE_KIND_UNSPECIFIED&quot; |
| INT64 | &quot;INT64&quot; |
| BOOL | &quot;BOOL&quot; |
| FLOAT64 | &quot;FLOAT64&quot; |
| STRING | &quot;STRING&quot; |
| BYTES | &quot;BYTES&quot; |
| TIMESTAMP | &quot;TIMESTAMP&quot; |
| DATE | &quot;DATE&quot; |
| TIME | &quot;TIME&quot; |
| DATETIME | &quot;DATETIME&quot; |
| INTERVAL | &quot;INTERVAL&quot; |
| GEOGRAPHY | &quot;GEOGRAPHY&quot; |
| NUMERIC | &quot;NUMERIC&quot; |
| BIGNUMERIC | &quot;BIGNUMERIC&quot; |
| JSON | &quot;JSON&quot; |
| ARRAY | &quot;ARRAY&quot; |
| STRUCT | &quot;STRUCT&quot; |
| RANGE | &quot;RANGE&quot; |



