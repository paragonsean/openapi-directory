# BigQueryApi.StandardSqlDataType

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arrayElementType** | [**StandardSqlDataType**](StandardSqlDataType.md) |  | [optional] 
**rangeElementType** | [**StandardSqlDataType**](StandardSqlDataType.md) |  | [optional] 
**structType** | [**StandardSqlStructType**](StandardSqlStructType.md) |  | [optional] 
**typeKind** | **String** | Required. The top level type of this field. Can be any GoogleSQL data type (e.g., \&quot;INT64\&quot;, \&quot;DATE\&quot;, \&quot;ARRAY\&quot;). | [optional] 



## Enum: TypeKindEnum


* `TYPE_KIND_UNSPECIFIED` (value: `"TYPE_KIND_UNSPECIFIED"`)

* `INT64` (value: `"INT64"`)

* `BOOL` (value: `"BOOL"`)

* `FLOAT64` (value: `"FLOAT64"`)

* `STRING` (value: `"STRING"`)

* `BYTES` (value: `"BYTES"`)

* `TIMESTAMP` (value: `"TIMESTAMP"`)

* `DATE` (value: `"DATE"`)

* `TIME` (value: `"TIME"`)

* `DATETIME` (value: `"DATETIME"`)

* `INTERVAL` (value: `"INTERVAL"`)

* `GEOGRAPHY` (value: `"GEOGRAPHY"`)

* `NUMERIC` (value: `"NUMERIC"`)

* `BIGNUMERIC` (value: `"BIGNUMERIC"`)

* `JSON` (value: `"JSON"`)

* `ARRAY` (value: `"ARRAY"`)

* `STRUCT` (value: `"STRUCT"`)

* `RANGE` (value: `"RANGE"`)




