

# DocumentsTarget

A target specified by a set of documents names.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**documents** | **List&lt;String&gt;** | The names of the documents to retrieve. In the format: &#x60;projects/{project_id}/databases/{database_id}/documents/{document_path}&#x60;. The request will fail if any of the document is not a child resource of the given &#x60;database&#x60;. Duplicate names will be elided. |  [optional] |



