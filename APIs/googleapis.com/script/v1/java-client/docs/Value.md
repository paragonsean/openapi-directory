

# Value

`Value` represents a dynamically typed value which is the outcome of an executed script.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**boolValue** | **Boolean** | Represents a boolean value. |  [optional] |
|**bytesValue** | **byte[]** | Represents raw byte values. |  [optional] |
|**dateValue** | **String** | Represents a date in ms since the epoch. |  [optional] |
|**listValue** | [**ListValue**](ListValue.md) |  |  [optional] |
|**nullValue** | [**NullValueEnum**](#NullValueEnum) | Represents a null value. |  [optional] |
|**numberValue** | **Double** | Represents a double value. |  [optional] |
|**protoValue** | **Map&lt;String, Object&gt;** | Represents a structured proto value. |  [optional] |
|**stringValue** | **String** | Represents a string value. |  [optional] |
|**structValue** | [**Struct**](Struct.md) |  |  [optional] |



## Enum: NullValueEnum

| Name | Value |
|---- | -----|
| NULL_VALUE | &quot;NULL_VALUE&quot; |



