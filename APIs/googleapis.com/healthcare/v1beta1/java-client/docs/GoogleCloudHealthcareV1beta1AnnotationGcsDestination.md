

# GoogleCloudHealthcareV1beta1AnnotationGcsDestination

The Cloud Storage location for export.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**uriPrefix** | **String** | The Cloud Storage destination to export to. URI for a Cloud Storage directory where the server writes result files, in the format &#x60;gs://{bucket-id}/{path/to/destination/dir}&#x60;. If there is no trailing slash, the service appends one when composing the object path. The user is responsible for creating the Cloud Storage bucket referenced in &#x60;uri_prefix&#x60;. |  [optional] |



