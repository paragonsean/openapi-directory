# SearchIndexClient.IndexingResult

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errorMessage** | **String** | The error message explaining why the indexing operation failed for the document identified by the key; null if indexing succeeded. | [optional] [readonly] 
**key** | **String** | The key of a document that was in the indexing request. | [optional] [readonly] 
**status** | **Boolean** | A value indicating whether the indexing operation succeeded for the document identified by the key. | [optional] [readonly] 
**statusCode** | **Number** | The status code of the indexing operation. Possible values include: 200 for a successful update or delete, 201 for successful document creation, 400 for a malformed input document, 404 for document not found, 409 for a version conflict, 422 when the index is temporarily unavailable, or 503 for when the service is too busy. | [optional] [readonly] 


