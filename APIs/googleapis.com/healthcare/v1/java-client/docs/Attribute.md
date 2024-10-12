

# Attribute

An attribute value for a Consent or User data mapping. Each Attribute must have a corresponding AttributeDefinition in the consent store that defines the default and allowed values.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attributeDefinitionId** | **String** | Indicates the name of an attribute defined in the consent store. |  [optional] |
|**values** | **List&lt;String&gt;** | Required. The value of the attribute. Must be an acceptable value as defined in the consent store. For example, if the consent store defines \&quot;data type\&quot; with acceptable values \&quot;questionnaire\&quot; and \&quot;step-count\&quot;, when the attribute name is data type, this field must contain one of those values. |  [optional] |



