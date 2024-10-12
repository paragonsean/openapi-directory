# ConnectorsApi.InputParameter

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additionalDetails** | **{String: Object}** | The following map contains fields that are not explicitly mentioned above,this give connectors the flexibility to add new metadata fields. | [optional] 
**dataType** | **String** | The data type of the Parameter | [optional] 
**defaultValue** | **Object** | The following field specifies the default value of the Parameter provided by the external system if a value is not provided. | [optional] 
**description** | **String** | A brief description of the Parameter. | [optional] 
**jsonSchema** | [**JsonSchema**](JsonSchema.md) |  | [optional] 
**name** | **String** | Name of the Parameter. | [optional] 
**nullable** | **Boolean** | Specifies whether a null value is allowed. | [optional] 



## Enum: DataTypeEnum


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




