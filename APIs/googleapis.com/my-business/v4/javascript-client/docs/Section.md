# GoogleMyBusinessApi.Section

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**[Item]**](Item.md) | Items that are contained within this section of the price list. | [optional] 
**labels** | [**[Label]**](Label.md) | Required. Language-tagged labels for the section. We recommend that section names and descriptions be 140 characters or less. At least one set of labels is required. | [optional] 
**sectionId** | **String** | Required. ID for the section. Price list, section, and item IDs cannot be duplicated within this Location. | [optional] 
**sectionType** | **String** | Optional. Type of the current price list section. Default value is FOOD. | [optional] 



## Enum: SectionTypeEnum


* `SECTION_TYPE_UNSPECIFIED` (value: `"SECTION_TYPE_UNSPECIFIED"`)

* `FOOD` (value: `"FOOD"`)

* `SERVICES` (value: `"SERVICES"`)




