# CloudHealthcareApi.ConsentArtifact

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consentContentScreenshots** | [**[Image]**](Image.md) | Optional. Screenshots, PDFs, or other binary information documenting the user&#39;s consent. | [optional] 
**consentContentVersion** | **String** | Optional. An string indicating the version of the consent information shown to the user. | [optional] 
**guardianSignature** | [**Signature**](Signature.md) |  | [optional] 
**metadata** | **{String: String}** | Optional. Metadata associated with the Consent artifact. For example, the consent locale or user agent version. | [optional] 
**name** | **String** | Identifier. Resource name of the Consent artifact, of the form &#x60;projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/consentStores/{consent_store_id}/consentArtifacts/{consent_artifact_id}&#x60;. Cannot be changed after creation. | [optional] 
**userId** | **String** | Required. User&#39;s UUID provided by the client. | [optional] 
**userSignature** | [**Signature**](Signature.md) |  | [optional] 
**witnessSignature** | [**Signature**](Signature.md) |  | [optional] 


