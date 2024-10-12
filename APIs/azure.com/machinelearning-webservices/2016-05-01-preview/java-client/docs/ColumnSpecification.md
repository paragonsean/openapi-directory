

# ColumnSpecification

Swagger 2.0 schema for a column within the data table representing a web service input or output. See Swagger specification: http://swagger.io/specification/

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**_enum** | **List&lt;Object&gt;** | If the data type is categorical, this provides the list of accepted categories. |  [optional] |
|**format** | [**FormatEnum**](#FormatEnum) | Additional format information for the data type. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Data type of the column. |  |
|**xMsIsnullable** | **Boolean** | Flag indicating if the type supports null values or not. |  [optional] |
|**xMsIsordered** | **Boolean** | Flag indicating whether the categories are treated as an ordered set or not, if this is a categorical column. |  [optional] |



## Enum: FormatEnum

| Name | Value |
|---- | -----|
| BYTE | &quot;Byte&quot; |
| CHAR | &quot;Char&quot; |
| COMPLEX64 | &quot;Complex64&quot; |
| COMPLEX128 | &quot;Complex128&quot; |
| DATE_TIME | &quot;Date-time&quot; |
| DATE_TIME_OFFSET | &quot;Date-timeOffset&quot; |
| DOUBLE | &quot;Double&quot; |
| DURATION | &quot;Duration&quot; |
| FLOAT | &quot;Float&quot; |
| INT8 | &quot;Int8&quot; |
| INT16 | &quot;Int16&quot; |
| INT32 | &quot;Int32&quot; |
| INT64 | &quot;Int64&quot; |
| UINT8 | &quot;Uint8&quot; |
| UINT16 | &quot;Uint16&quot; |
| UINT32 | &quot;Uint32&quot; |
| UINT64 | &quot;Uint64&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| BOOLEAN | &quot;Boolean&quot; |
| INTEGER | &quot;Integer&quot; |
| NUMBER | &quot;Number&quot; |
| STRING | &quot;String&quot; |



