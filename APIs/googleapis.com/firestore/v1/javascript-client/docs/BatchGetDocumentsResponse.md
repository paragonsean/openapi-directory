# CloudFirestoreApi.BatchGetDocumentsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**found** | [**Document**](Document.md) |  | [optional] 
**missing** | **String** | A document name that was requested but does not exist. In the format: &#x60;projects/{project_id}/databases/{database_id}/documents/{document_path}&#x60;. | [optional] 
**readTime** | **String** | The time at which the document was read. This may be monotically increasing, in this case the previous documents in the result stream are guaranteed not to have changed between their read_time and this one. | [optional] 
**transaction** | **Blob** | The transaction that was started as part of this request. Will only be set in the first response, and only if BatchGetDocumentsRequest.new_transaction was set in the request. | [optional] 


