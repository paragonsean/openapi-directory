

# Attribute

A location attribute. Attributes provide additional information about a location. The attributes that can be set on a location may vary based on the properties of that location (for example, category). Available attributes are determined by Google and may be added and removed without API changes.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attributeId** | **String** | The ID of the attribute. Attribute IDs are provided by Google. |  [optional] |
|**repeatedEnumValue** | [**RepeatedEnumAttributeValue**](RepeatedEnumAttributeValue.md) |  |  [optional] |
|**urlValues** | [**List&lt;UrlAttributeValue&gt;**](UrlAttributeValue.md) | When the attribute value type is URL, this field contains the value(s) for this attribute, and the other values fields must be empty. |  [optional] |
|**valueType** | [**ValueTypeEnum**](#ValueTypeEnum) | Output only. The type of value that this attribute contains. This should be used to determine how to interpret the value. |  [optional] |
|**values** | **List&lt;Object&gt;** | The values for this attribute. The type of the values supplied must match that expected for that attribute; see [AttributeValueType](/my-business/reference/rest/v4/AttributeValueType). This is a repeated field where multiple attribute values may be provided. Attribute types only support one value. |  [optional] |



## Enum: ValueTypeEnum

| Name | Value |
|---- | -----|
| ATTRIBUTE_VALUE_TYPE_UNSPECIFIED | &quot;ATTRIBUTE_VALUE_TYPE_UNSPECIFIED&quot; |
| BOOL | &quot;BOOL&quot; |
| ENUM | &quot;ENUM&quot; |
| URL | &quot;URL&quot; |
| REPEATED_ENUM | &quot;REPEATED_ENUM&quot; |



