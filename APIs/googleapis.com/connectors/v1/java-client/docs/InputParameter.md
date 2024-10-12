

# InputParameter

Metadata of an input parameter.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataType** | [**DataTypeEnum**](#DataTypeEnum) | The data type of the Parameter. |  [optional] |
|**defaultValue** | **Object** | The following field specifies the default value of the Parameter provided by the external system if a value is not provided. |  [optional] |
|**description** | **String** | A brief description of the Parameter. |  [optional] |
|**jsonSchema** | [**JsonSchema**](JsonSchema.md) |  |  [optional] |
|**nullable** | **Boolean** | Specifies whether a null value is allowed. |  [optional] |
|**parameter** | **String** | Name of the Parameter. |  [optional] |



## Enum: DataTypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;DATA_TYPE_UNSPECIFIED&quot; |
| INT | &quot;DATA_TYPE_INT&quot; |
| SMALLINT | &quot;DATA_TYPE_SMALLINT&quot; |
| DOUBLE | &quot;DATA_TYPE_DOUBLE&quot; |
| DATE | &quot;DATA_TYPE_DATE&quot; |
| DATETIME | &quot;DATA_TYPE_DATETIME&quot; |
| TIME | &quot;DATA_TYPE_TIME&quot; |
| STRING | &quot;DATA_TYPE_STRING&quot; |
| LONG | &quot;DATA_TYPE_LONG&quot; |
| BOOLEAN | &quot;DATA_TYPE_BOOLEAN&quot; |
| DECIMAL | &quot;DATA_TYPE_DECIMAL&quot; |
| UUID | &quot;DATA_TYPE_UUID&quot; |
| BLOB | &quot;DATA_TYPE_BLOB&quot; |
| BIT | &quot;DATA_TYPE_BIT&quot; |
| TINYINT | &quot;DATA_TYPE_TINYINT&quot; |
| INTEGER | &quot;DATA_TYPE_INTEGER&quot; |
| BIGINT | &quot;DATA_TYPE_BIGINT&quot; |
| FLOAT | &quot;DATA_TYPE_FLOAT&quot; |
| REAL | &quot;DATA_TYPE_REAL&quot; |
| NUMERIC | &quot;DATA_TYPE_NUMERIC&quot; |
| CHAR | &quot;DATA_TYPE_CHAR&quot; |
| VARCHAR | &quot;DATA_TYPE_VARCHAR&quot; |
| LONGVARCHAR | &quot;DATA_TYPE_LONGVARCHAR&quot; |
| TIMESTAMP | &quot;DATA_TYPE_TIMESTAMP&quot; |
| NCHAR | &quot;DATA_TYPE_NCHAR&quot; |
| NVARCHAR | &quot;DATA_TYPE_NVARCHAR&quot; |
| LONGNVARCHAR | &quot;DATA_TYPE_LONGNVARCHAR&quot; |
| NULL | &quot;DATA_TYPE_NULL&quot; |
| OTHER | &quot;DATA_TYPE_OTHER&quot; |
| JAVA_OBJECT | &quot;DATA_TYPE_JAVA_OBJECT&quot; |
| DISTINCT | &quot;DATA_TYPE_DISTINCT&quot; |
| STRUCT | &quot;DATA_TYPE_STRUCT&quot; |
| ARRAY | &quot;DATA_TYPE_ARRAY&quot; |
| CLOB | &quot;DATA_TYPE_CLOB&quot; |
| REF | &quot;DATA_TYPE_REF&quot; |
| DATALINK | &quot;DATA_TYPE_DATALINK&quot; |
| ROWID | &quot;DATA_TYPE_ROWID&quot; |
| BINARY | &quot;DATA_TYPE_BINARY&quot; |
| VARBINARY | &quot;DATA_TYPE_VARBINARY&quot; |
| LONGVARBINARY | &quot;DATA_TYPE_LONGVARBINARY&quot; |
| NCLOB | &quot;DATA_TYPE_NCLOB&quot; |
| SQLXML | &quot;DATA_TYPE_SQLXML&quot; |
| REF_CURSOR | &quot;DATA_TYPE_REF_CURSOR&quot; |
| TIME_WITH_TIMEZONE | &quot;DATA_TYPE_TIME_WITH_TIMEZONE&quot; |
| TIMESTAMP_WITH_TIMEZONE | &quot;DATA_TYPE_TIMESTAMP_WITH_TIMEZONE&quot; |



