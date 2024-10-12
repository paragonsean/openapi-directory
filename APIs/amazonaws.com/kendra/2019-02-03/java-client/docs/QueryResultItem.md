

# QueryResultItem

<p>A single query result.</p> <p>A query result contains information about a document returned by the query. This includes the original location of the document, a list of attributes assigned to the document, and relevant text from the document that satisfies the query.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | [**String**](String.md) |  |  [optional] |
|**type** | [**QueryResultType**](QueryResultType.md) |  |  [optional] |
|**format** | [**QueryResultFormat**](QueryResultFormat.md) |  |  [optional] |
|**additionalAttributes** | [**List**](List.md) |  |  [optional] |
|**documentId** | [**String**](String.md) |  |  [optional] |
|**documentTitle** | [**QueryResultItemDocumentTitle**](QueryResultItemDocumentTitle.md) |  |  [optional] |
|**documentExcerpt** | [**QueryResultItemDocumentExcerpt**](QueryResultItemDocumentExcerpt.md) |  |  [optional] |
|**documentURI** | [**String**](String.md) |  |  [optional] |
|**documentAttributes** | [**List**](List.md) |  |  [optional] |
|**scoreAttributes** | [**QueryResultItemScoreAttributes**](QueryResultItemScoreAttributes.md) |  |  [optional] |
|**feedbackToken** | [**String**](String.md) |  |  [optional] |
|**tableExcerpt** | [**QueryResultItemTableExcerpt**](QueryResultItemTableExcerpt.md) |  |  [optional] |



