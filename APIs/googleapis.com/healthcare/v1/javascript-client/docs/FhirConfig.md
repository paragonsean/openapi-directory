# CloudHealthcareApi.FhirConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**defaultKeepExtensions** | **Boolean** | The behaviour for handling FHIR extensions that aren&#39;t otherwise specified for de-identification. If true, all extensions are preserved during de-identification by default. If false or unspecified, all extensions are removed during de-identification by default. | [optional] 
**fieldMetadataList** | [**[FieldMetadata]**](FieldMetadata.md) | Specifies FHIR paths to match and how to transform them. Any field that is not matched by a FieldMetadata is passed through to the output dataset unmodified. All extensions will be processed according to &#x60;default_keep_extensions&#x60;. | [optional] 


