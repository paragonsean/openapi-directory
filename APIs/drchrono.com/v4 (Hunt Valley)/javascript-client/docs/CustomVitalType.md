# OpenapiJsClient.CustomVitalType

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowedValues** | **[String]** | If &#x60;data_type&#x60; is &#x60;single_sel&#x60;, this is the array of values in the select&#39;s dropdown. | [optional] 
**archived** | **Boolean** | Indicates that the object has been soft-deleted and should not be used | [optional] 
**dataType** | **String** | One of &#x60;text&#x60;, &#x60;number&#x60;, or &#x60;single_sel&#x60; | [optional] 
**description** | **String** |  | [optional] 
**doctor** | **String** | ID of the doctor who created the custom vital | [optional] [readonly] 
**fractionDelimiter** | **String** | If &#x60;is_fraction_field&#x60; is true, this is the character separating the numerator and denominator | [optional] 
**id** | **Number** |  | [optional] [readonly] 
**isFractionField** | **Boolean** |  | [optional] 
**name** | **String** |  | [optional] 
**unit** | **String** |  | [optional] 



## Enum: DataTypeEnum


* `text` (value: `"text"`)

* `number` (value: `"number"`)

* `single_sel` (value: `"single_sel"`)




