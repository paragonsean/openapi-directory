# CloudHealthcareApi.DeidentifyDatasetRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | [**DeidentifyConfig**](DeidentifyConfig.md) |  | [optional] 
**destinationDataset** | **String** | Required. The name of the dataset resource to create and write the redacted data to. * The destination dataset must not exist. * The destination dataset must be in the same location as the source dataset. De-identifying data across multiple locations is not supported. | [optional] 
**gcsConfigUri** | **String** | Cloud Storage location to read the JSON cloud.healthcare.deidentify.DeidentifyConfig from, overriding the default config. Must be of the form &#x60;gs://{bucket_id}/path/to/object&#x60;. The Cloud Storage location must grant the Cloud IAM role &#x60;roles/storage.objectViewer&#x60; to the project&#39;s Cloud Healthcare Service Agent service account. Only one of &#x60;config&#x60; and &#x60;gcs_config_uri&#x60; can be specified. | [optional] 


