# CloudHealthcareApi.ExplainDataAccessConsentInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cascadeOrigins** | **[String]** | The compartment base resources that matched a cascading policy. Each resource has the following format: &#x60;projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/fhirStores/{fhir_store_id}/fhir/{resource_type}/{resource_id}&#x60; | [optional] 
**consentResource** | **String** | The resource name of this consent resource. Format: &#x60;projects/{projectId}/datasets/{datasetId}/fhirStores/{fhirStoreId}/fhir/{resourceType}/{id}&#x60;. | [optional] 
**enforcementTime** | **String** | Last enforcement timestamp of this consent resource. | [optional] 
**matchingAccessorScopes** | [**[ConsentAccessorScope]**](ConsentAccessorScope.md) | A list of all the matching accessor scopes of this consent policy that enforced ExplainDataAccessConsentScope.accessor_scope. | [optional] 
**patientConsentOwner** | **String** | The patient owning the consent (only applicable for patient consents), in the format: &#x60;projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/fhirStores/{fhir_store_id}/fhir/Patient/{patient_id}&#x60; | [optional] 
**type** | **String** | The policy type of consent resource (e.g. PATIENT, ADMIN). | [optional] 
**variants** | **[String]** | The consent&#39;s variant combinations. A single consent may have multiple variants. | [optional] 



## Enum: TypeEnum


* `UNSPECIFIED` (value: `"CONSENT_POLICY_TYPE_UNSPECIFIED"`)

* `PATIENT` (value: `"CONSENT_POLICY_TYPE_PATIENT"`)

* `ADMIN` (value: `"CONSENT_POLICY_TYPE_ADMIN"`)





## Enum: [VariantsEnum]


* `UNSPECIFIED` (value: `"VARIANT_UNSPECIFIED"`)

* `STANDARD` (value: `"VARIANT_STANDARD"`)

* `CASCADE` (value: `"VARIANT_CASCADE"`)




