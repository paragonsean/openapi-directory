

# JsonSchema

JsonSchema representation of schema metadata

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | A description of this schema. |  [optional] |
|**_enum** | **List&lt;Object&gt;** | Possible values for an enumeration. This works in conjunction with &#x60;type&#x60; to represent types with a fixed set of legal values |  [optional] |
|**format** | **String** | Format of the value as per https://json-schema.org/understanding-json-schema/reference/string.html#format |  [optional] |
|**items** | [**JsonSchema**](JsonSchema.md) |  |  [optional] |
|**jdbcType** | [**JdbcTypeEnum**](#JdbcTypeEnum) | JDBC datatype of the field. |  [optional] |
|**properties** | [**Map&lt;String, JsonSchema&gt;**](JsonSchema.md) | The child schemas, applicable only if this is of type &#x60;object&#x60;. The key is the name of the property and the value is the json schema that describes that property |  [optional] |
|**required** | **List&lt;String&gt;** | Whether this property is required. |  [optional] |
|**type** | **List&lt;String&gt;** | JSON Schema Validation: A Vocabulary for Structural Validation of JSON |  [optional] |



## Enum: JdbcTypeEnum

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



