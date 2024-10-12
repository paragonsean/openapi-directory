

# Page

A page in a presentation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**layoutProperties** | [**LayoutProperties**](LayoutProperties.md) |  |  [optional] |
|**masterProperties** | [**MasterProperties**](MasterProperties.md) |  |  [optional] |
|**notesProperties** | [**NotesProperties**](NotesProperties.md) |  |  [optional] |
|**objectId** | **String** | The object ID for this page. Object IDs used by Page and PageElement share the same namespace. |  [optional] |
|**pageElements** | [**List&lt;PageElement&gt;**](PageElement.md) | The page elements rendered on the page. |  [optional] |
|**pageProperties** | [**PageProperties**](PageProperties.md) |  |  [optional] |
|**pageType** | [**PageTypeEnum**](#PageTypeEnum) | The type of the page. |  [optional] |
|**revisionId** | **String** | Output only. The revision ID of the presentation. Can be used in update requests to assert the presentation revision hasn&#39;t changed since the last read operation. Only populated if the user has edit access to the presentation. The revision ID is not a sequential number but an opaque string. The format of the revision ID might change over time. A returned revision ID is only guaranteed to be valid for 24 hours after it has been returned and cannot be shared across users. If the revision ID is unchanged between calls, then the presentation has not changed. Conversely, a changed ID (for the same presentation and user) usually means the presentation has been updated. However, a changed ID can also be due to internal factors such as ID format changes. |  [optional] |
|**slideProperties** | [**SlideProperties**](SlideProperties.md) |  |  [optional] |



## Enum: PageTypeEnum

| Name | Value |
|---- | -----|
| SLIDE | &quot;SLIDE&quot; |
| MASTER | &quot;MASTER&quot; |
| LAYOUT | &quot;LAYOUT&quot; |
| NOTES | &quot;NOTES&quot; |
| NOTES_MASTER | &quot;NOTES_MASTER&quot; |



