# CloudFirestoreApi.GoogleFirestoreAdminV1ExportDocumentsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collectionIds** | **[String]** | Which collection ids to export. Unspecified means all collections. | [optional] 
**namespaceIds** | **[String]** | An empty list represents all namespaces. This is the preferred usage for databases that don&#39;t use namespaces. An empty string element represents the default namespace. This should be used if the database has data in non-default namespaces, but doesn&#39;t want to include them. Each namespace in this list must be unique. | [optional] 
**outputUriPrefix** | **String** | The output URI. Currently only supports Google Cloud Storage URIs of the form: &#x60;gs://BUCKET_NAME[/NAMESPACE_PATH]&#x60;, where &#x60;BUCKET_NAME&#x60; is the name of the Google Cloud Storage bucket and &#x60;NAMESPACE_PATH&#x60; is an optional Google Cloud Storage namespace path. When choosing a name, be sure to consider Google Cloud Storage naming guidelines: https://cloud.google.com/storage/docs/naming. If the URI is a bucket (without a namespace path), a prefix will be generated based on the start time. | [optional] 
**snapshotTime** | **String** | The timestamp that corresponds to the version of the database to be exported. The timestamp must be in the past, rounded to the minute and not older than earliestVersionTime. If specified, then the exported documents will represent a consistent view of the database at the provided time. Otherwise, there are no guarantees about the consistency of the exported documents. | [optional] 


