

# AuthorizationCodesSharedModelsDataField


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**digitsPrecision** | **Integer** | The number of decimal digits to be used by this data field. Required only by the &#39;Float&#39; data type. Must be in range 1 - 15. |  [optional] |
|**maxExponent** | **Integer** | The maximum exponent to be used by this data field. Required only by the &#39;Float&#39; data type. May not be greater than 307. |  [optional] |
|**maxValue** | **Double** | The maximum value that can be represented by this data field. Required only by the &#39;Decimal&#39; data type. |  [optional] |
|**minExponent** | **Integer** | The minimum exponent to be used by this data field. Required only by the &#39;Float&#39; data type. May not be less than -292. |  [optional] |
|**minValue** | **Double** | The minimum value that can be represented by this data field. Required only by the &#39;Decimal&#39; data type. |  [optional] |
|**name** | **String** | The name of the field. |  |
|**scaleFactor** | **Double** | The resolution of values that can be represented by this data field. The base value is multiplied by this to compute the final value. Required only by the &#39;Decimal&#39; data type. |  [optional] |
|**signed** | **Boolean** | Indicates whether this value is signed. Required only by the &#39;Float&#39; data type. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of this data field. |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| BOOLEAN | &quot;Boolean&quot; |
| DECIMAL | &quot;Decimal&quot; |
| FLOAT | &quot;Float&quot; |
| VARIABLE_LENGTH_BYTE_ARRAY | &quot;VariableLengthByteArray&quot; |



