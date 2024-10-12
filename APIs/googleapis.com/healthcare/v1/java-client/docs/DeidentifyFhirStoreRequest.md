

# DeidentifyFhirStoreRequest

Creates a new FHIR store with sensitive information de-identified.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**config** | [**DeidentifyConfig**](DeidentifyConfig.md) |  |  [optional] |
|**destinationStore** | **String** | Required. The name of the FHIR store to create and write the redacted data to. For example, &#x60;projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/fhirStores/{fhir_store_id}&#x60;. * The destination dataset must exist. * The source dataset and destination dataset must both reside in the same location. De-identifying data across multiple locations is not supported. * The destination FHIR store must exist. * The caller must have the healthcare.fhirResources.update permission to write to the destination FHIR store. |  [optional] |
|**gcsConfigUri** | **String** | Cloud Storage location to read the JSON cloud.healthcare.deidentify.DeidentifyConfig from, overriding the default config. Must be of the form &#x60;gs://{bucket_id}/path/to/object&#x60;. The Cloud Storage location must grant the Cloud IAM role &#x60;roles/storage.objectViewer&#x60; to the project&#39;s Cloud Healthcare Service Agent service account. Only one of &#x60;config&#x60; and &#x60;gcs_config_uri&#x60; can be specified. |  [optional] |
|**resourceFilter** | [**FhirFilter**](FhirFilter.md) |  |  [optional] |
|**skipModifiedResources** | **Boolean** | If true, skips resources that are created or modified after the de-identify operation is created. |  [optional] |



