# CloudHealthcareApi.ConsentConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessDeterminationLogConfig** | [**AccessDeterminationLogConfig**](AccessDeterminationLogConfig.md) |  | [optional] 
**accessEnforced** | **Boolean** | Optional. If set to true, when accessing FHIR resources, the consent headers will be verified against consents given by patients. See the ConsentEnforcementVersion for the supported consent headers. | [optional] 
**consentHeaderHandling** | [**ConsentHeaderHandling**](ConsentHeaderHandling.md) |  | [optional] 
**enforcedAdminConsents** | **[String]** | The versioned names of the enforced admin Consent resource(s), in the format &#x60;projects/{project_id}/locations/{location}/datasets/{dataset_id}/fhirStores/{fhir_store_id}/fhir/Consent/{resource_id}/_history/{version_id}&#x60;. For FHIR stores with &#x60;disable_resource_versioning&#x3D;true&#x60;, the format is &#x60;projects/{project_id}/locations/{location}/datasets/{dataset_id}/fhirStores/{fhir_store_id}/fhir/Consent/{resource_id}&#x60;. This field can only be updated using ApplyAdminConsents. | [optional] 
**version** | **String** | Required. Specifies which consent enforcement version is being used for this FHIR store. This field can only be set once by either CreateFhirStore or UpdateFhirStore. After that, you must call ApplyConsents to change the version. | [optional] 



## Enum: VersionEnum


* `CONSENT_ENFORCEMENT_VERSION_UNSPECIFIED` (value: `"CONSENT_ENFORCEMENT_VERSION_UNSPECIFIED"`)

* `V1` (value: `"V1"`)




