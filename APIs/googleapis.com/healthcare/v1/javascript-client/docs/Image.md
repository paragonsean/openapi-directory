# CloudHealthcareApi.Image

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gcsUri** | **String** | Input only. Points to a Cloud Storage URI containing the consent artifact content. The URI must be in the following format: &#x60;gs://{bucket_id}/{object_id}&#x60;. The Cloud Healthcare API service account must have the &#x60;roles/storage.objectViewer&#x60; Cloud IAM role for this Cloud Storage location. The consent artifact content at this URI is copied to a Cloud Storage location managed by the Cloud Healthcare API. Responses to fetching requests return the consent artifact content in raw_bytes. | [optional] 
**rawBytes** | **Blob** | Consent artifact content represented as a stream of bytes. This field is populated when returned in GetConsentArtifact response, but not included in CreateConsentArtifact and ListConsentArtifact response. | [optional] 


