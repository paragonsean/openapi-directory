

# AttributeMetadata

Metadata for an attribute. Contains display information for the attribute, including a localized name and a heading for grouping related attributes together.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attributeId** | **String** | The ID of the attribute. |  [optional] |
|**displayName** | **String** | The localized display name for the attribute, if available; otherwise, the English display name. |  [optional] |
|**groupDisplayName** | **String** | The localized display name of the group that contains this attribute, if available; otherwise, the English group name. Related attributes are collected into a group and should be displayed together under the heading given here. |  [optional] |
|**isDeprecated** | **Boolean** | If true, the attribute is deprecated and should no longer be used. If deprecated, updating this attribute will not result in an error, but updates will not be saved. At some point after being deprecated, the attribute will be removed entirely and it will become an error. |  [optional] |
|**isRepeatable** | **Boolean** | If true, the attribute supports multiple values. If false, only a single value should be provided. |  [optional] |
|**valueMetadata** | [**List&lt;AttributeValueMetadata&gt;**](AttributeValueMetadata.md) | For some types of attributes (for example, enums), a list of supported values and corresponding display names for those values is provided. |  [optional] |
|**valueType** | [**ValueTypeEnum**](#ValueTypeEnum) | The value type for the attribute. Values set and retrieved should be expected to be of this type. |  [optional] |



## Enum: ValueTypeEnum

| Name | Value |
|---- | -----|
| ATTRIBUTE_VALUE_TYPE_UNSPECIFIED | &quot;ATTRIBUTE_VALUE_TYPE_UNSPECIFIED&quot; |
| BOOL | &quot;BOOL&quot; |
| ENUM | &quot;ENUM&quot; |
| URL | &quot;URL&quot; |
| REPEATED_ENUM | &quot;REPEATED_ENUM&quot; |



