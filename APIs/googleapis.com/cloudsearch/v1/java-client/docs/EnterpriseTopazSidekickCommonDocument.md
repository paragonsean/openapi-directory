

# EnterpriseTopazSidekickCommonDocument

Representation of a document. NEXT_TAG: 15

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accessType** | [**AccessTypeEnum**](#AccessTypeEnum) | Access type, i.e., whether the user has access to the document or not. |  [optional] |
|**debugInfo** | [**EnterpriseTopazSidekickCommonDebugInfo**](EnterpriseTopazSidekickCommonDebugInfo.md) |  |  [optional] |
|**documentId** | **String** | Document id. |  [optional] |
|**driveDocumentMetadata** | [**EnterpriseTopazSidekickCommonDocumentDriveDocumentMetadata**](EnterpriseTopazSidekickCommonDocumentDriveDocumentMetadata.md) |  |  [optional] |
|**genericUrl** | **String** | Generic Drive-based url in the format of drive.google.com/open to be used for deeplink |  [optional] |
|**justification** | [**EnterpriseTopazSidekickCommonDocumentJustification**](EnterpriseTopazSidekickCommonDocumentJustification.md) |  |  [optional] |
|**mimeType** | **String** | MIME type |  [optional] |
|**provenance** | [**ProvenanceEnum**](#ProvenanceEnum) | Document provenance. |  [optional] |
|**reason** | [**ReasonEnum**](#ReasonEnum) | Justification of why this document is being returned. |  [optional] |
|**snippet** | **String** | A sampling of the text from the document. |  [optional] |
|**thumbnailUrl** | **String** | Thumbnail URL. |  [optional] |
|**title** | **String** | Title of the document. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Type of the document. |  [optional] |
|**url** | **String** | Absolute URL of the document. |  [optional] |



## Enum: AccessTypeEnum

| Name | Value |
|---- | -----|
| UNKNOWN_ACCESS | &quot;UNKNOWN_ACCESS&quot; |
| ALLOWED | &quot;ALLOWED&quot; |
| NOT_ALLOWED | &quot;NOT_ALLOWED&quot; |



## Enum: ProvenanceEnum

| Name | Value |
|---- | -----|
| UNKNOWN_PROVENANCE | &quot;UNKNOWN_PROVENANCE&quot; |
| CALENDAR_DESCRIPTION | &quot;CALENDAR_DESCRIPTION&quot; |
| CALENDAR_ATTACHMENT | &quot;CALENDAR_ATTACHMENT&quot; |
| MINED | &quot;MINED&quot; |
| CALENDAR_ASSIST_ATTACHMENT | &quot;CALENDAR_ASSIST_ATTACHMENT&quot; |



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



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;UNKNOWN&quot; |
| DOCUMENT | &quot;DOCUMENT&quot; |
| PRESENTATION | &quot;PRESENTATION&quot; |
| SPREADSHEET | &quot;SPREADSHEET&quot; |
| PDF | &quot;PDF&quot; |
| IMAGE | &quot;IMAGE&quot; |
| BINARY_BLOB | &quot;BINARY_BLOB&quot; |
| FUSION_TABLE | &quot;FUSION_TABLE&quot; |
| FOLDER | &quot;FOLDER&quot; |
| DRAWING | &quot;DRAWING&quot; |
| VIDEO | &quot;VIDEO&quot; |
| FORM | &quot;FORM&quot; |
| LINK_URL | &quot;LINK_URL&quot; |
| LINK_GO | &quot;LINK_GO&quot; |
| LINK_GOO_GL | &quot;LINK_GOO_GL&quot; |
| LINK_BIT_LY | &quot;LINK_BIT_LY&quot; |
| LINK_GMAIL | &quot;LINK_GMAIL&quot; |
| LINK_MAILTO | &quot;LINK_MAILTO&quot; |
| VIDEO_YOUTUBE | &quot;VIDEO_YOUTUBE&quot; |
| VIDEO_LIVE | &quot;VIDEO_LIVE&quot; |
| GROUPS | &quot;GROUPS&quot; |
| NEWS | &quot;NEWS&quot; |
| SITES | &quot;SITES&quot; |
| HANGOUT | &quot;HANGOUT&quot; |
| AUDIO | &quot;AUDIO&quot; |
| MS_WORD | &quot;MS_WORD&quot; |
| MS_POWERPOINT | &quot;MS_POWERPOINT&quot; |
| MS_EXCEL | &quot;MS_EXCEL&quot; |
| MS_OUTLOOK | &quot;MS_OUTLOOK&quot; |



