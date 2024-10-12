

# Section

A section of the price list containing one or more items.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**items** | [**List&lt;Item&gt;**](Item.md) | Items that are contained within this section of the price list. |  [optional] |
|**labels** | [**List&lt;Label&gt;**](Label.md) | Required. Language-tagged labels for the section. We recommend that section names and descriptions be 140 characters or less. At least one set of labels is required. |  [optional] |
|**sectionId** | **String** | Required. ID for the section. Price list, section, and item IDs cannot be duplicated within this Location. |  [optional] |
|**sectionType** | [**SectionTypeEnum**](#SectionTypeEnum) | Optional. Type of the current price list section. Default value is FOOD. |  [optional] |



## Enum: SectionTypeEnum

| Name | Value |
|---- | -----|
| SECTION_TYPE_UNSPECIFIED | &quot;SECTION_TYPE_UNSPECIFIED&quot; |
| FOOD | &quot;FOOD&quot; |
| SERVICES | &quot;SERVICES&quot; |



