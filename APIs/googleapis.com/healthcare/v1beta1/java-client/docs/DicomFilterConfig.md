

# DicomFilterConfig

Specifies the filter configuration for DICOM resources.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**resourcePathsGcsUri** | **String** | The Cloud Storage location of the filter configuration file. The &#x60;gcs_uri&#x60; must be in the format &#x60;gs://bucket/path/to/object&#x60;. The filter configuration file must contain a list of resource paths separated by newline characters (\\n or \\r\\n). Each resource path must be in the format \&quot;/studies/{studyUID}[/series/{seriesUID}[/instances/{instanceUID}]]\&quot; The Cloud Healthcare API service account must have the &#x60;roles/storage.objectViewer&#x60; Cloud IAM role for this Cloud Storage location. |  [optional] |



