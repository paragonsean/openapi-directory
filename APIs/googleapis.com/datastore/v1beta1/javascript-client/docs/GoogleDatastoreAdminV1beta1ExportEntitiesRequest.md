# CloudDatastoreApi.GoogleDatastoreAdminV1beta1ExportEntitiesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entityFilter** | [**GoogleDatastoreAdminV1beta1EntityFilter**](GoogleDatastoreAdminV1beta1EntityFilter.md) |  | [optional] 
**labels** | **{String: String}** | Client-assigned labels. | [optional] 
**outputUrlPrefix** | **String** | Location for the export metadata and data files. The full resource URL of the external storage location. Currently, only Google Cloud Storage is supported. So output_url_prefix should be of the form: &#x60;gs://BUCKET_NAME[/NAMESPACE_PATH]&#x60;, where &#x60;BUCKET_NAME&#x60; is the name of the Cloud Storage bucket and &#x60;NAMESPACE_PATH&#x60; is an optional Cloud Storage namespace path (this is not a Cloud Datastore namespace). For more information about Cloud Storage namespace paths, see [Object name considerations](https://cloud.google.com/storage/docs/naming#object-considerations). The resulting files will be nested deeper than the specified URL prefix. The final output URL will be provided in the google.datastore.admin.v1beta1.ExportEntitiesResponse.output_url field. That value should be used for subsequent ImportEntities operations. By nesting the data files deeper, the same Cloud Storage bucket can be used in multiple ExportEntities operations without conflict. | [optional] 


