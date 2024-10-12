# ConnectorsApi.JsonSchema

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | A description of this schema. | [optional] 
**_enum** | **[Object]** | Possible values for an enumeration. This works in conjunction with &#x60;type&#x60; to represent types with a fixed set of legal values | [optional] 
**format** | **String** | Format of the value as per https://json-schema.org/understanding-json-schema/reference/string.html#format | [optional] 
**items** | [**JsonSchema**](JsonSchema.md) |  | [optional] 
**jdbcType** | **String** | JDBC datatype of the field. | [optional] 
**properties** | [**{String: JsonSchema}**](JsonSchema.md) | The child schemas, applicable only if this is of type &#x60;object&#x60;. The key is the name of the property and the value is the json schema that describes that property | [optional] 
**required** | **[String]** | Whether this property is required. | [optional] 
**type** | **[String]** | JSON Schema Validation: A Vocabulary for Structural Validation of JSON | [optional] 



## Enum: JdbcTypeEnum


* `UNSPECIFIED` (value: `"DATA_TYPE_UNSPECIFIED"`)

* `INT` (value: `"DATA_TYPE_INT"`)

* `SMALLINT` (value: `"DATA_TYPE_SMALLINT"`)

* `DOUBLE` (value: `"DATA_TYPE_DOUBLE"`)

* `DATE` (value: `"DATA_TYPE_DATE"`)

* `DATETIME` (value: `"DATA_TYPE_DATETIME"`)

* `TIME` (value: `"DATA_TYPE_TIME"`)

* `STRING` (value: `"DATA_TYPE_STRING"`)

* `LONG` (value: `"DATA_TYPE_LONG"`)

* `BOOLEAN` (value: `"DATA_TYPE_BOOLEAN"`)

* `DECIMAL` (value: `"DATA_TYPE_DECIMAL"`)

* `UUID` (value: `"DATA_TYPE_UUID"`)

* `BLOB` (value: `"DATA_TYPE_BLOB"`)

* `BIT` (value: `"DATA_TYPE_BIT"`)

* `TINYINT` (value: `"DATA_TYPE_TINYINT"`)

* `INTEGER` (value: `"DATA_TYPE_INTEGER"`)

* `BIGINT` (value: `"DATA_TYPE_BIGINT"`)

* `FLOAT` (value: `"DATA_TYPE_FLOAT"`)

* `REAL` (value: `"DATA_TYPE_REAL"`)

* `NUMERIC` (value: `"DATA_TYPE_NUMERIC"`)

* `CHAR` (value: `"DATA_TYPE_CHAR"`)

* `VARCHAR` (value: `"DATA_TYPE_VARCHAR"`)

* `LONGVARCHAR` (value: `"DATA_TYPE_LONGVARCHAR"`)

* `TIMESTAMP` (value: `"DATA_TYPE_TIMESTAMP"`)

* `NCHAR` (value: `"DATA_TYPE_NCHAR"`)

* `NVARCHAR` (value: `"DATA_TYPE_NVARCHAR"`)

* `LONGNVARCHAR` (value: `"DATA_TYPE_LONGNVARCHAR"`)

* `NULL` (value: `"DATA_TYPE_NULL"`)

* `OTHER` (value: `"DATA_TYPE_OTHER"`)

* `JAVA_OBJECT` (value: `"DATA_TYPE_JAVA_OBJECT"`)

* `DISTINCT` (value: `"DATA_TYPE_DISTINCT"`)

* `STRUCT` (value: `"DATA_TYPE_STRUCT"`)

* `ARRAY` (value: `"DATA_TYPE_ARRAY"`)

* `CLOB` (value: `"DATA_TYPE_CLOB"`)

* `REF` (value: `"DATA_TYPE_REF"`)

* `DATALINK` (value: `"DATA_TYPE_DATALINK"`)

* `ROWID` (value: `"DATA_TYPE_ROWID"`)

* `BINARY` (value: `"DATA_TYPE_BINARY"`)

* `VARBINARY` (value: `"DATA_TYPE_VARBINARY"`)

* `LONGVARBINARY` (value: `"DATA_TYPE_LONGVARBINARY"`)

* `NCLOB` (value: `"DATA_TYPE_NCLOB"`)

* `SQLXML` (value: `"DATA_TYPE_SQLXML"`)

* `REF_CURSOR` (value: `"DATA_TYPE_REF_CURSOR"`)

* `TIME_WITH_TIMEZONE` (value: `"DATA_TYPE_TIME_WITH_TIMEZONE"`)

* `TIMESTAMP_WITH_TIMEZONE` (value: `"DATA_TYPE_TIMESTAMP_WITH_TIMEZONE"`)




