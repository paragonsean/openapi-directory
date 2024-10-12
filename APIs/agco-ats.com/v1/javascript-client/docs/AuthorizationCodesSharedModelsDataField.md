# AgcoApi.AuthorizationCodesSharedModelsDataField

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**digitsPrecision** | **Number** | The number of decimal digits to be used by this data field. Required only by the &#39;Float&#39; data type. Must be in range 1 - 15. | [optional] 
**maxExponent** | **Number** | The maximum exponent to be used by this data field. Required only by the &#39;Float&#39; data type. May not be greater than 307. | [optional] 
**maxValue** | **Number** | The maximum value that can be represented by this data field. Required only by the &#39;Decimal&#39; data type. | [optional] 
**minExponent** | **Number** | The minimum exponent to be used by this data field. Required only by the &#39;Float&#39; data type. May not be less than -292. | [optional] 
**minValue** | **Number** | The minimum value that can be represented by this data field. Required only by the &#39;Decimal&#39; data type. | [optional] 
**name** | **String** | The name of the field. | 
**scaleFactor** | **Number** | The resolution of values that can be represented by this data field. The base value is multiplied by this to compute the final value. Required only by the &#39;Decimal&#39; data type. | [optional] 
**signed** | **Boolean** | Indicates whether this value is signed. Required only by the &#39;Float&#39; data type. | [optional] 
**type** | **String** | The type of this data field. | 



## Enum: TypeEnum


* `Boolean` (value: `"Boolean"`)

* `Decimal` (value: `"Decimal"`)

* `Float` (value: `"Float"`)

* `VariableLengthByteArray` (value: `"VariableLengthByteArray"`)




