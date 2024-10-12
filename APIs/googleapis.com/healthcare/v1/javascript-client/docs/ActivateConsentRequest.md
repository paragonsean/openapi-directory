# CloudHealthcareApi.ActivateConsentRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consentArtifact** | **String** | Required. The resource name of the Consent artifact that contains documentation of the user&#39;s consent, of the form &#x60;projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/consentStores/{consent_store_id}/consentArtifacts/{consent_artifact_id}&#x60;. If the draft Consent had a Consent artifact, this Consent artifact overwrites it. | [optional] 
**expireTime** | **String** | Timestamp in UTC of when this Consent is considered expired. | [optional] 
**ttl** | **String** | The time to live for this Consent from when it is marked as active. | [optional] 


