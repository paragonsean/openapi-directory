

# GoogleFirestoreAdminV1beta2ImportDocumentsRequest

The request for FirestoreAdmin.ImportDocuments.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**collectionIds** | **List&lt;String&gt;** | Which collection ids to import. Unspecified means all collections included in the import. |  [optional] |
|**inputUriPrefix** | **String** | Location of the exported files. This must match the output_uri_prefix of an ExportDocumentsResponse from an export that has completed successfully. See: google.firestore.admin.v1beta2.ExportDocumentsResponse.output_uri_prefix. |  [optional] |



