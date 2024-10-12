# CloudFirestoreApi.GoogleFirestoreAdminV1beta1ExportDocumentsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collectionIds** | **[String]** | Which collection ids to export. Unspecified means all collections. | [optional] 
**outputUriPrefix** | **String** | The output URI. Currently only supports Google Cloud Storage URIs of the form: &#x60;gs://BUCKET_NAME[/NAMESPACE_PATH]&#x60;, where &#x60;BUCKET_NAME&#x60; is the name of the Google Cloud Storage bucket and &#x60;NAMESPACE_PATH&#x60; is an optional Google Cloud Storage namespace path. When choosing a name, be sure to consider Google Cloud Storage naming guidelines: https://cloud.google.com/storage/docs/naming. If the URI is a bucket (without a namespace path), a prefix will be generated based on the start time. | [optional] 


