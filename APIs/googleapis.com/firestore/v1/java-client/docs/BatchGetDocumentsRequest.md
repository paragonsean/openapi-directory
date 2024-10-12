

# BatchGetDocumentsRequest

The request for Firestore.BatchGetDocuments.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**documents** | **List&lt;String&gt;** | The names of the documents to retrieve. In the format: &#x60;projects/{project_id}/databases/{database_id}/documents/{document_path}&#x60;. The request will fail if any of the document is not a child resource of the given &#x60;database&#x60;. Duplicate names will be elided. |  [optional] |
|**mask** | [**DocumentMask**](DocumentMask.md) |  |  [optional] |
|**newTransaction** | [**TransactionOptions**](TransactionOptions.md) |  |  [optional] |
|**readTime** | **String** | Reads documents as they were at the given time. This must be a microsecond precision timestamp within the past one hour, or if Point-in-Time Recovery is enabled, can additionally be a whole minute timestamp within the past 7 days. |  [optional] |
|**transaction** | **byte[]** | Reads documents in a transaction. |  [optional] |



