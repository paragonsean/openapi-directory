

# EnterpriseTopazSidekickCommonDocumentJustification

Justification of why we are reporting the document.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**justification** | **String** | A locale aware message that explains why this document was selected. |  [optional] |
|**reason** | [**ReasonEnum**](#ReasonEnum) | Reason on why the document is selected. Populate for trending documents. |  [optional] |



## Enum: ReasonEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;UNKNOWN&quot; |
| TRENDING_IN_COLLABORATORS | &quot;TRENDING_IN_COLLABORATORS&quot; |
| TRENDING_IN_DOMAIN | &quot;TRENDING_IN_DOMAIN&quot; |
| FREQUENTLY_VIEWED | &quot;FREQUENTLY_VIEWED&quot; |
| FREQUENTLY_EDITED | &quot;FREQUENTLY_EDITED&quot; |
| NEW_UPDATES | &quot;NEW_UPDATES&quot; |
| NEW_COMMENTS | &quot;NEW_COMMENTS&quot; |
| EVENT_DESCRIPTION | &quot;EVENT_DESCRIPTION&quot; |
| EVENT_ATTACHMENT | &quot;EVENT_ATTACHMENT&quot; |
| EVENT_METADATA_ATTACHMENT | &quot;EVENT_METADATA_ATTACHMENT&quot; |
| MINED_DOCUMENT | &quot;MINED_DOCUMENT&quot; |
| NEW_MENTIONS | &quot;NEW_MENTIONS&quot; |
| NEW_SHARES | &quot;NEW_SHARES&quot; |



