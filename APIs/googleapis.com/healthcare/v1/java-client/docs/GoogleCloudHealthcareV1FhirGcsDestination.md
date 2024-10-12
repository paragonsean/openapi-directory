

# GoogleCloudHealthcareV1FhirGcsDestination

The configuration for exporting to Cloud Storage.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**uriPrefix** | **String** | URI for a Cloud Storage directory where result files should be written, in the format of &#x60;gs://{bucket-id}/{path/to/destination/dir}&#x60;. If there is no trailing slash, the service appends one when composing the object path. The user is responsible for creating the Cloud Storage bucket referenced in &#x60;uri_prefix&#x60;. |  [optional] |



