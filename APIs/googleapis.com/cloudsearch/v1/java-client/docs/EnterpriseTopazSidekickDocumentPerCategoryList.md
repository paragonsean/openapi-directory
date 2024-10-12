

# EnterpriseTopazSidekickDocumentPerCategoryList


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**documents** | [**List&lt;EnterpriseTopazSidekickDocumentPerCategoryListDocumentPerCategoryListEntry&gt;**](EnterpriseTopazSidekickDocumentPerCategoryListDocumentPerCategoryListEntry.md) |  |  [optional] |
|**helpMessage** | **String** | Localized message explaining how the documents were derived (e.g. from the last 30 days activity). This field is optional. |  [optional] |
|**listType** | [**ListTypeEnum**](#ListTypeEnum) |  |  [optional] |
|**listTypeDescription** | **String** | Description of the types of documents present in the list. |  [optional] |
|**responseMessage** | **String** | Response message in case no documents are present in the card. |  [optional] |



## Enum: ListTypeEnum

| Name | Value |
|---- | -----|
| UNKNOWN_LIST_TYPE | &quot;UNKNOWN_LIST_TYPE&quot; |
| MENTIONS | &quot;MENTIONS&quot; |
| SHARES | &quot;SHARES&quot; |
| NEEDS_ATTENTION | &quot;NEEDS_ATTENTION&quot; |
| VIEWS | &quot;VIEWS&quot; |
| EDITS | &quot;EDITS&quot; |



