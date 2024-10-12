# CloudHealthcareApi.Consent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consentArtifact** | **String** | Required. The resource name of the Consent artifact that contains proof of the end user&#39;s consent, of the form &#x60;projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/consentStores/{consent_store_id}/consentArtifacts/{consent_artifact_id}&#x60;. | [optional] 
**expireTime** | **String** | Timestamp in UTC of when this Consent is considered expired. | [optional] 
**metadata** | **{String: String}** | Optional. User-supplied key-value pairs used to organize Consent resources. Metadata keys must: - be between 1 and 63 characters long - have a UTF-8 encoding of maximum 128 bytes - begin with a letter - consist of up to 63 characters including lowercase letters, numeric characters, underscores, and dashes Metadata values must be: - be between 1 and 63 characters long - have a UTF-8 encoding of maximum 128 bytes - consist of up to 63 characters including lowercase letters, numeric characters, underscores, and dashes No more than 64 metadata entries can be associated with a given consent. | [optional] 
**name** | **String** | Identifier. Resource name of the Consent, of the form &#x60;projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/consentStores/{consent_store_id}/consents/{consent_id}&#x60;. Cannot be changed after creation. | [optional] 
**policies** | [**[GoogleCloudHealthcareV1beta1ConsentPolicy]**](GoogleCloudHealthcareV1beta1ConsentPolicy.md) | Optional. Represents a user&#39;s consent in terms of the resources that can be accessed and under what conditions. | [optional] 
**revisionCreateTime** | **String** | Output only. The timestamp that the revision was created. | [optional] [readonly] 
**revisionId** | **String** | Output only. The revision ID of the Consent. The format is an 8-character hexadecimal string. Refer to a specific revision of a Consent by appending &#x60;@{revision_id}&#x60; to the Consent&#39;s resource name. | [optional] [readonly] 
**state** | **String** | Required. Indicates the current state of this Consent. | [optional] 
**ttl** | **String** | Input only. The time to live for this Consent from when it is created. | [optional] 
**userId** | **String** | Required. User&#39;s UUID provided by the client. | [optional] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `ACTIVE` (value: `"ACTIVE"`)

* `ARCHIVED` (value: `"ARCHIVED"`)

* `REVOKED` (value: `"REVOKED"`)

* `DRAFT` (value: `"DRAFT"`)

* `REJECTED` (value: `"REJECTED"`)




