# ConnectorsApi.JsonSchema

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additionalDetails** | **{String: Object}** | Additional details apart from standard json schema fields, this gives flexibility to store metadata about the schema | [optional] 
**description** | **String** | A description of this schema. | [optional] 
**_enum** | **[Object]** | Possible values for an enumeration. This works in conjunction with &#x60;type&#x60; to represent types with a fixed set of legal values | [optional] 
**format** | **String** | Format of the value as per https://json-schema.org/understanding-json-schema/reference/string.html#format | [optional] 
**items** | [**JsonSchema**](JsonSchema.md) |  | [optional] 
**jdbcType** | **String** | JDBC datatype of the field. | [optional] 
**properties** | [**{String: JsonSchema}**](JsonSchema.md) | The child schemas, applicable only if this is of type &#x60;object&#x60;. The key is the name of the property and the value is the json schema that describes that property | [optional] 
**required** | **[String]** | Whether this property is required. | [optional] 
**type** | **[String]** | JSON Schema Validation: A Vocabulary for Structural Validation of JSON | [optional] 



## Enum: JdbcTypeEnum


* `DATA_TYPE_UNSPECIFIED` (value: `"DATA_TYPE_UNSPECIFIED"`)

* `INT` (value: `"INT"`)

* `SMALLINT` (value: `"SMALLINT"`)

* `DOUBLE` (value: `"DOUBLE"`)

* `DATE` (value: `"DATE"`)

* `DATETIME` (value: `"DATETIME"`)

* `TIME` (value: `"TIME"`)

* `STRING` (value: `"STRING"`)

* `LONG` (value: `"LONG"`)

* `BOOLEAN` (value: `"BOOLEAN"`)

* `DECIMAL` (value: `"DECIMAL"`)

* `UUID` (value: `"UUID"`)

* `BLOB` (value: `"BLOB"`)

* `BIT` (value: `"BIT"`)

* `TINYINT` (value: `"TINYINT"`)

* `INTEGER` (value: `"INTEGER"`)

* `BIGINT` (value: `"BIGINT"`)

* `FLOAT` (value: `"FLOAT"`)

* `REAL` (value: `"REAL"`)

* `NUMERIC` (value: `"NUMERIC"`)

* `CHAR` (value: `"CHAR"`)

* `VARCHAR` (value: `"VARCHAR"`)

* `LONGVARCHAR` (value: `"LONGVARCHAR"`)

* `TIMESTAMP` (value: `"TIMESTAMP"`)

* `NCHAR` (value: `"NCHAR"`)

* `NVARCHAR` (value: `"NVARCHAR"`)

* `LONGNVARCHAR` (value: `"LONGNVARCHAR"`)

* `NULL` (value: `"NULL"`)

* `OTHER` (value: `"OTHER"`)

* `JAVA_OBJECT` (value: `"JAVA_OBJECT"`)

* `DISTINCT` (value: `"DISTINCT"`)

* `STRUCT` (value: `"STRUCT"`)

* `ARRAY` (value: `"ARRAY"`)

* `CLOB` (value: `"CLOB"`)

* `REF` (value: `"REF"`)

* `DATALINK` (value: `"DATALINK"`)

* `ROWID` (value: `"ROWID"`)

* `BINARY` (value: `"BINARY"`)

* `VARBINARY` (value: `"VARBINARY"`)

* `LONGVARBINARY` (value: `"LONGVARBINARY"`)

* `NCLOB` (value: `"NCLOB"`)

* `SQLXML` (value: `"SQLXML"`)

* `REF_CURSOR` (value: `"REF_CURSOR"`)

* `TIME_WITH_TIMEZONE` (value: `"TIME_WITH_TIMEZONE"`)

* `TIMESTAMP_WITH_TIMEZONE` (value: `"TIMESTAMP_WITH_TIMEZONE"`)




