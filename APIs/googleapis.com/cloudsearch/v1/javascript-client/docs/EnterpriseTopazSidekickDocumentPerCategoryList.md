# CloudSearchApi.EnterpriseTopazSidekickDocumentPerCategoryList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**documents** | [**[EnterpriseTopazSidekickDocumentPerCategoryListDocumentPerCategoryListEntry]**](EnterpriseTopazSidekickDocumentPerCategoryListDocumentPerCategoryListEntry.md) |  | [optional] 
**helpMessage** | **String** | Localized message explaining how the documents were derived (e.g. from the last 30 days activity). This field is optional. | [optional] 
**listType** | **String** |  | [optional] 
**listTypeDescription** | **String** | Description of the types of documents present in the list. | [optional] 
**responseMessage** | **String** | Response message in case no documents are present in the card. | [optional] 



## Enum: ListTypeEnum


* `UNKNOWN_LIST_TYPE` (value: `"UNKNOWN_LIST_TYPE"`)

* `MENTIONS` (value: `"MENTIONS"`)

* `SHARES` (value: `"SHARES"`)

* `NEEDS_ATTENTION` (value: `"NEEDS_ATTENTION"`)

* `VIEWS` (value: `"VIEWS"`)

* `EDITS` (value: `"EDITS"`)




