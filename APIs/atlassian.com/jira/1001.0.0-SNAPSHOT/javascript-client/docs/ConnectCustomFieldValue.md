# TheJiraCloudPlatformRestApi.ConnectCustomFieldValue

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **String** | The type of custom field. | 
**fieldID** | **Number** | The custom field ID. | 
**issueID** | **Number** | The issue ID. | 
**number** | **Number** | The value of number type custom field when &#x60;_type&#x60; is &#x60;NumberIssueField&#x60;. | [optional] 
**optionID** | **String** | The value of single select and multiselect custom field type when &#x60;_type&#x60; is &#x60;SingleSelectIssueField&#x60; or &#x60;MultiSelectIssueField&#x60;. | [optional] 
**richText** | **String** | The value of richText type custom field when &#x60;_type&#x60; is &#x60;RichTextIssueField&#x60;. | [optional] 
**string** | **String** | The value of string type custom field when &#x60;_type&#x60; is &#x60;StringIssueField&#x60;. | [optional] 
**text** | **String** | The value of of text custom field type when &#x60;_type&#x60; is &#x60;TextIssueField&#x60;. | [optional] 



## Enum: TypeEnum


* `StringIssueField` (value: `"StringIssueField"`)

* `NumberIssueField` (value: `"NumberIssueField"`)

* `RichTextIssueField` (value: `"RichTextIssueField"`)

* `SingleSelectIssueField` (value: `"SingleSelectIssueField"`)

* `MultiSelectIssueField` (value: `"MultiSelectIssueField"`)

* `TextIssueField` (value: `"TextIssueField"`)




