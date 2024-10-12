

# RejectConsentRequest

Rejects the latest revision of the specified Consent by committing a new revision with `state` updated to `REJECTED`. If the latest revision of the given Consent is in the `REJECTED` state, no new revision is committed.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**consentArtifact** | **String** | Optional. The resource name of the Consent artifact that contains documentation of the user&#39;s rejection of the draft Consent, of the form &#x60;projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/consentStores/{consent_store_id}/consentArtifacts/{consent_artifact_id}&#x60;. If the draft Consent had a Consent artifact, this Consent artifact overwrites it. |  [optional] |



