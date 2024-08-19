# MyBusinessBusinessInformationApi.AttributeMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deprecated** | **Boolean** | If true, the attribute is deprecated and should no longer be used. If deprecated, updating this attribute will not result in an error, but updates will not be saved. At some point after being deprecated, the attribute will be removed entirely and it will become an error. | [optional] 
**displayName** | **String** | The localized display name for the attribute, if available; otherwise, the English display name. | [optional] 
**groupDisplayName** | **String** | The localized display name of the group that contains this attribute, if available; otherwise, the English group name. Related attributes are collected into a group and should be displayed together under the heading given here. | [optional] 
**parent** | **String** | The unique identifier for the attribute. | [optional] 
**repeatable** | **Boolean** | If true, the attribute supports multiple values. If false, only a single value should be provided. | [optional] 
**valueMetadata** | [**[AttributeValueMetadata]**](AttributeValueMetadata.md) | For some types of attributes (for example, enums), a list of supported values and corresponding display names for those values is provided. | [optional] 
**valueType** | **String** | The value type for the attribute. Values set and retrieved should be expected to be of this type. | [optional] 



## Enum: ValueTypeEnum


* `ATTRIBUTE_VALUE_TYPE_UNSPECIFIED` (value: `"ATTRIBUTE_VALUE_TYPE_UNSPECIFIED"`)

* `BOOL` (value: `"BOOL"`)

* `ENUM` (value: `"ENUM"`)

* `URL` (value: `"URL"`)

* `REPEATED_ENUM` (value: `"REPEATED_ENUM"`)




