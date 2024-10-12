# GoogleMyBusinessApi.Attribute

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributeId** | **String** | The ID of the attribute. Attribute IDs are provided by Google. | [optional] 
**repeatedEnumValue** | [**RepeatedEnumAttributeValue**](RepeatedEnumAttributeValue.md) |  | [optional] 
**urlValues** | [**[UrlAttributeValue]**](UrlAttributeValue.md) | When the attribute value type is URL, this field contains the value(s) for this attribute, and the other values fields must be empty. | [optional] 
**valueType** | **String** | Output only. The type of value that this attribute contains. This should be used to determine how to interpret the value. | [optional] 
**values** | **[Object]** | The values for this attribute. The type of the values supplied must match that expected for that attribute; see [AttributeValueType](/my-business/reference/rest/v4/AttributeValueType). This is a repeated field where multiple attribute values may be provided. Attribute types only support one value. | [optional] 



## Enum: ValueTypeEnum


* `ATTRIBUTE_VALUE_TYPE_UNSPECIFIED` (value: `"ATTRIBUTE_VALUE_TYPE_UNSPECIFIED"`)

* `BOOL` (value: `"BOOL"`)

* `ENUM` (value: `"ENUM"`)

* `URL` (value: `"URL"`)

* `REPEATED_ENUM` (value: `"REPEATED_ENUM"`)




