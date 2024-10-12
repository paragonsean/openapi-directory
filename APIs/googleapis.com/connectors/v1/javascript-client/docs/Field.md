# ConnectorsApi.Field

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additionalDetails** | **{String: Object}** | The following map contains fields that are not explicitly mentioned above,this give connectors the flexibility to add new metadata fields. | [optional] 
**dataType** | **String** | The data type of the Field. | [optional] 
**defaultValue** | **Object** | The following field specifies the default value of the Field provided by the external system if a value is not provided. | [optional] 
**description** | **String** | A brief description of the Field. | [optional] 
**field** | **String** | Name of the Field. | [optional] 
**jsonSchema** | [**JsonSchema**](JsonSchema.md) |  | [optional] 
**key** | **Boolean** | The following boolean field specifies if the current Field acts as a primary key or id if the parent is of type entity. | [optional] 
**nullable** | **Boolean** | Specifies whether a null value is allowed. | [optional] 
**readonly** | **Boolean** | Specifies if the Field is readonly. | [optional] 



## Enum: DataTypeEnum


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




