

# GoogleFirestoreAdminV1ImportDocumentsRequest

The request for FirestoreAdmin.ImportDocuments.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**collectionIds** | **List&lt;String&gt;** | Which collection ids to import. Unspecified means all collections included in the import. |  [optional] |
|**inputUriPrefix** | **String** | Location of the exported files. This must match the output_uri_prefix of an ExportDocumentsResponse from an export that has completed successfully. See: google.firestore.admin.v1.ExportDocumentsResponse.output_uri_prefix. |  [optional] |
|**namespaceIds** | **List&lt;String&gt;** | An empty list represents all namespaces. This is the preferred usage for databases that don&#39;t use namespaces. An empty string element represents the default namespace. This should be used if the database has data in non-default namespaces, but doesn&#39;t want to include them. Each namespace in this list must be unique. |  [optional] |



