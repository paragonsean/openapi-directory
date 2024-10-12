# CloudAssetApi.GcsDestination

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uri** | **String** | The URI of the Cloud Storage object. It&#39;s the same URI that is used by gsutil. Example: \&quot;gs://bucket_name/object_name\&quot;. See [Viewing and Editing Object Metadata](https://cloud.google.com/storage/docs/viewing-editing-metadata) for more information. If the specified Cloud Storage object already exists and there is no [hold](https://cloud.google.com/storage/docs/object-holds), it will be overwritten with the exported result. | [optional] 
**uriPrefix** | **String** | The URI prefix of all generated Cloud Storage objects. Example: \&quot;gs://bucket_name/object_name_prefix\&quot;. Each object URI is in format: \&quot;gs://bucket_name/object_name_prefix// and only contains assets for that type. starts from 0. Example: \&quot;gs://bucket_name/object_name_prefix/compute.googleapis.com/Disk/0\&quot; is the first shard of output objects containing all compute.googleapis.com/Disk assets. An INVALID_ARGUMENT error will be returned if file with the same name \&quot;gs://bucket_name/object_name_prefix\&quot; already exists. | [optional] 


