# CloudDatastoreApi.GoogleDatastoreAdminV1ImportEntitiesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entityFilter** | [**GoogleDatastoreAdminV1EntityFilter**](GoogleDatastoreAdminV1EntityFilter.md) |  | [optional] 
**inputUrl** | **String** | Required. The full resource URL of the external storage location. Currently, only Google Cloud Storage is supported. So input_url should be of the form: &#x60;gs://BUCKET_NAME[/NAMESPACE_PATH]/OVERALL_EXPORT_METADATA_FILE&#x60;, where &#x60;BUCKET_NAME&#x60; is the name of the Cloud Storage bucket, &#x60;NAMESPACE_PATH&#x60; is an optional Cloud Storage namespace path (this is not a Cloud Datastore namespace), and &#x60;OVERALL_EXPORT_METADATA_FILE&#x60; is the metadata file written by the ExportEntities operation. For more information about Cloud Storage namespace paths, see [Object name considerations](https://cloud.google.com/storage/docs/naming#object-considerations). For more information, see google.datastore.admin.v1.ExportEntitiesResponse.output_url. | [optional] 
**labels** | **{String: String}** | Client-assigned labels. | [optional] 


