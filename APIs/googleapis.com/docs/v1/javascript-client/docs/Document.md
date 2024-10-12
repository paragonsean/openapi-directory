# GoogleDocsApi.Document

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | [**Body**](Body.md) |  | [optional] 
**documentId** | **String** | Output only. The ID of the document. | [optional] 
**documentStyle** | [**DocumentStyle**](DocumentStyle.md) |  | [optional] 
**footers** | [**{String: Footer}**](Footer.md) | Output only. The footers in the document, keyed by footer ID. | [optional] 
**footnotes** | [**{String: Footnote}**](Footnote.md) | Output only. The footnotes in the document, keyed by footnote ID. | [optional] 
**headers** | [**{String: Header}**](Header.md) | Output only. The headers in the document, keyed by header ID. | [optional] 
**inlineObjects** | [**{String: InlineObject}**](InlineObject.md) | Output only. The inline objects in the document, keyed by object ID. | [optional] 
**lists** | **{String: Array}** | Output only. The lists in the document, keyed by list ID. | [optional] 
**namedRanges** | [**{String: NamedRanges}**](NamedRanges.md) | Output only. The named ranges in the document, keyed by name. | [optional] 
**namedStyles** | [**NamedStyles**](NamedStyles.md) |  | [optional] 
**positionedObjects** | [**{String: PositionedObject}**](PositionedObject.md) | Output only. The positioned objects in the document, keyed by object ID. | [optional] 
**revisionId** | **String** | Output only. The revision ID of the document. Can be used in update requests to specify which revision of a document to apply updates to and how the request should behave if the document has been edited since that revision. Only populated if the user has edit access to the document. The revision ID is not a sequential number but an opaque string. The format of the revision ID might change over time. A returned revision ID is only guaranteed to be valid for 24 hours after it has been returned and cannot be shared across users. If the revision ID is unchanged between calls, then the document has not changed. Conversely, a changed ID (for the same document and user) usually means the document has been updated. However, a changed ID can also be due to internal factors such as ID format changes. | [optional] 
**suggestedDocumentStyleChanges** | [**{String: SuggestedDocumentStyle}**](SuggestedDocumentStyle.md) | Output only. The suggested changes to the style of the document, keyed by suggestion ID. | [optional] 
**suggestedNamedStylesChanges** | [**{String: SuggestedNamedStyles}**](SuggestedNamedStyles.md) | Output only. The suggested changes to the named styles of the document, keyed by suggestion ID. | [optional] 
**suggestionsViewMode** | **String** | Output only. The suggestions view mode applied to the document. Note: When editing a document, changes must be based on a document with SUGGESTIONS_INLINE. | [optional] 
**title** | **String** | The title of the document. | [optional] 



## Enum: SuggestionsViewModeEnum


* `DEFAULT_FOR_CURRENT_ACCESS` (value: `"DEFAULT_FOR_CURRENT_ACCESS"`)

* `SUGGESTIONS_INLINE` (value: `"SUGGESTIONS_INLINE"`)

* `PREVIEW_SUGGESTIONS_ACCEPTED` (value: `"PREVIEW_SUGGESTIONS_ACCEPTED"`)

* `PREVIEW_WITHOUT_SUGGESTIONS` (value: `"PREVIEW_WITHOUT_SUGGESTIONS"`)




