# CloudSearchApi.EnterpriseTopazSidekickCommonDocument

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessType** | **String** | Access type, i.e., whether the user has access to the document or not. | [optional] 
**debugInfo** | [**EnterpriseTopazSidekickCommonDebugInfo**](EnterpriseTopazSidekickCommonDebugInfo.md) |  | [optional] 
**documentId** | **String** | Document id. | [optional] 
**driveDocumentMetadata** | [**EnterpriseTopazSidekickCommonDocumentDriveDocumentMetadata**](EnterpriseTopazSidekickCommonDocumentDriveDocumentMetadata.md) |  | [optional] 
**genericUrl** | **String** | Generic Drive-based url in the format of drive.google.com/open to be used for deeplink | [optional] 
**justification** | [**EnterpriseTopazSidekickCommonDocumentJustification**](EnterpriseTopazSidekickCommonDocumentJustification.md) |  | [optional] 
**mimeType** | **String** | MIME type | [optional] 
**provenance** | **String** | Document provenance. | [optional] 
**reason** | **String** | Justification of why this document is being returned. | [optional] 
**snippet** | **String** | A sampling of the text from the document. | [optional] 
**thumbnailUrl** | **String** | Thumbnail URL. | [optional] 
**title** | **String** | Title of the document. | [optional] 
**type** | **String** | Type of the document. | [optional] 
**url** | **String** | Absolute URL of the document. | [optional] 



## Enum: AccessTypeEnum


* `UNKNOWN_ACCESS` (value: `"UNKNOWN_ACCESS"`)

* `ALLOWED` (value: `"ALLOWED"`)

* `NOT_ALLOWED` (value: `"NOT_ALLOWED"`)





## Enum: ProvenanceEnum


* `UNKNOWN_PROVENANCE` (value: `"UNKNOWN_PROVENANCE"`)

* `CALENDAR_DESCRIPTION` (value: `"CALENDAR_DESCRIPTION"`)

* `CALENDAR_ATTACHMENT` (value: `"CALENDAR_ATTACHMENT"`)

* `MINED` (value: `"MINED"`)

* `CALENDAR_ASSIST_ATTACHMENT` (value: `"CALENDAR_ASSIST_ATTACHMENT"`)





## Enum: ReasonEnum


* `UNKNOWN` (value: `"UNKNOWN"`)

* `TRENDING_IN_COLLABORATORS` (value: `"TRENDING_IN_COLLABORATORS"`)

* `TRENDING_IN_DOMAIN` (value: `"TRENDING_IN_DOMAIN"`)

* `FREQUENTLY_VIEWED` (value: `"FREQUENTLY_VIEWED"`)

* `FREQUENTLY_EDITED` (value: `"FREQUENTLY_EDITED"`)

* `NEW_UPDATES` (value: `"NEW_UPDATES"`)

* `NEW_COMMENTS` (value: `"NEW_COMMENTS"`)

* `EVENT_DESCRIPTION` (value: `"EVENT_DESCRIPTION"`)

* `EVENT_ATTACHMENT` (value: `"EVENT_ATTACHMENT"`)

* `EVENT_METADATA_ATTACHMENT` (value: `"EVENT_METADATA_ATTACHMENT"`)

* `MINED_DOCUMENT` (value: `"MINED_DOCUMENT"`)

* `NEW_MENTIONS` (value: `"NEW_MENTIONS"`)

* `NEW_SHARES` (value: `"NEW_SHARES"`)





## Enum: TypeEnum


* `UNKNOWN` (value: `"UNKNOWN"`)

* `DOCUMENT` (value: `"DOCUMENT"`)

* `PRESENTATION` (value: `"PRESENTATION"`)

* `SPREADSHEET` (value: `"SPREADSHEET"`)

* `PDF` (value: `"PDF"`)

* `IMAGE` (value: `"IMAGE"`)

* `BINARY_BLOB` (value: `"BINARY_BLOB"`)

* `FUSION_TABLE` (value: `"FUSION_TABLE"`)

* `FOLDER` (value: `"FOLDER"`)

* `DRAWING` (value: `"DRAWING"`)

* `VIDEO` (value: `"VIDEO"`)

* `FORM` (value: `"FORM"`)

* `LINK_URL` (value: `"LINK_URL"`)

* `LINK_GO` (value: `"LINK_GO"`)

* `LINK_GOO_GL` (value: `"LINK_GOO_GL"`)

* `LINK_BIT_LY` (value: `"LINK_BIT_LY"`)

* `LINK_GMAIL` (value: `"LINK_GMAIL"`)

* `LINK_MAILTO` (value: `"LINK_MAILTO"`)

* `VIDEO_YOUTUBE` (value: `"VIDEO_YOUTUBE"`)

* `VIDEO_LIVE` (value: `"VIDEO_LIVE"`)

* `GROUPS` (value: `"GROUPS"`)

* `NEWS` (value: `"NEWS"`)

* `SITES` (value: `"SITES"`)

* `HANGOUT` (value: `"HANGOUT"`)

* `AUDIO` (value: `"AUDIO"`)

* `MS_WORD` (value: `"MS_WORD"`)

* `MS_POWERPOINT` (value: `"MS_POWERPOINT"`)

* `MS_EXCEL` (value: `"MS_EXCEL"`)

* `MS_OUTLOOK` (value: `"MS_OUTLOOK"`)




