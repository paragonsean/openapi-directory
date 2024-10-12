# Asana.CustomFieldCompact

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **String** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resourceType** | **String** | The base type of this resource. | [optional] [readonly] 
**dateValue** | [**CustomFieldCompactAllOfDateValue**](CustomFieldCompactAllOfDateValue.md) |  | [optional] 
**displayValue** | **String** | A string representation for the value of the custom field. Integrations that don&#39;t require the underlying type should use this field to read values. Using this field will future-proof an app against new custom field types. | [optional] [readonly] 
**enabled** | **Boolean** | *Conditional*. Determines if the custom field is enabled or not. | [optional] 
**enumOptions** | [**[EnumOption]**](EnumOption.md) | *Conditional*. Only relevant for custom fields of type &#x60;enum&#x60;. This array specifies the possible values which an &#x60;enum&#x60; custom field can adopt. To modify the enum options, refer to [working with enum options](/docs/create-an-enum-option). | [optional] 
**enumValue** | [**CustomFieldCompactAllOfEnumValue**](CustomFieldCompactAllOfEnumValue.md) |  | [optional] 
**multiEnumValues** | [**[EnumOption]**](EnumOption.md) | *Conditional*. Only relevant for custom fields of type &#x60;multi_enum&#x60;. This object is the chosen values of a &#x60;multi_enum&#x60; custom field. | [optional] 
**name** | **String** | The name of the custom field. | [optional] 
**numberValue** | **Number** | *Conditional*. This number is the value of a &#x60;number&#x60; custom field. | [optional] 
**resourceSubtype** | **String** | The type of the custom field. Must be one of the given values.  | [optional] 
**textValue** | **String** | *Conditional*. This string is the value of a &#x60;text&#x60; custom field. | [optional] 
**type** | **String** | *Deprecated: new integrations should prefer the resource_subtype field.* The type of the custom field. Must be one of the given values.  | [optional] [readonly] 



## Enum: ResourceSubtypeEnum


* `text` (value: `"text"`)

* `enum` (value: `"enum"`)

* `multi_enum` (value: `"multi_enum"`)

* `number` (value: `"number"`)

* `date` (value: `"date"`)

* `people` (value: `"people"`)





## Enum: TypeEnum


* `text` (value: `"text"`)

* `enum` (value: `"enum"`)

* `multi_enum` (value: `"multi_enum"`)

* `number` (value: `"number"`)




