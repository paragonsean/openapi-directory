

# GoogleCloudAssetV1GcsDestination

A Cloud Storage location.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**uri** | **String** | Required. The URI of the Cloud Storage object. It&#39;s the same URI that is used by gsutil. Example: \&quot;gs://bucket_name/object_name\&quot;. See [Viewing and Editing Object Metadata](https://cloud.google.com/storage/docs/viewing-editing-metadata) for more information. If the specified Cloud Storage object already exists and there is no [hold](https://cloud.google.com/storage/docs/object-holds), it will be overwritten with the analysis result. |  [optional] |



