

# Attributes27

The attributes of the Registration Schema Block.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**blockType** | [**BlockTypeEnum**](#BlockTypeEnum) | A string that represents the type of input that the schema will take and the UI element that appears to the user on the frontend. |  [optional] [readonly] |
|**displayText** | **String** | The text that will accompany the UI element displayed on this Registration Schema Block. |  [optional] [readonly] |
|**exampleText** | **String** | The text that will accompany the UI element displayed on this Registration Schema Block. |  [optional] [readonly] |
|**index** | **Integer** | Integer beginning at zero that represents the order of Registration Schema Block in the Registration Schema. |  [optional] [readonly] |
|**registrationResponseKey** | **String** | This string is the the block key for the Registration Schema Block&#39;s corresponding block on the Schema Response. |  [optional] [readonly] |
|**required** | **Boolean** | Bool that represents if this field is required for creation of a Schema Response. |  [optional] [readonly] |
|**schemaBlockGroupKey** | **String** | This string indicates if a block is part of a block group, block groups may contain the different options dropdown menu or a group of inputs and display elements that are validated together. |  [optional] [readonly] |



## Enum: BlockTypeEnum

| Name | Value |
|---- | -----|
| PAGE_HEADING | &quot;page-heading&quot; |
| SECTION_HEADING | &quot;section-heading&quot; |
| SUBSECTION_HEADING | &quot;subsection-heading&quot; |
| PARAGRAPH | &quot;paragraph&quot; |
| QUESTION_LABEL | &quot;question-label&quot; |
| SHORT_TEXT_INPUT | &quot;short-text-input&quot; |
| LONG_TEXT_INPUT | &quot;long-text-input&quot; |
| FILE_INPUT | &quot;file-input&quot; |
| CONTRIBUTORS_INPUT | &quot;contributors-input&quot; |
| SINGLE_SELECT_INPUT | &quot;single-select-input&quot; |
| MULTI_SELECT_INPUT | &quot;multi-select-input&quot; |
| SELECT_INPUT_OPTION | &quot;select-input-option&quot; |
| SELECT_OTHER_OPTION | &quot;select-other-option&quot; |



