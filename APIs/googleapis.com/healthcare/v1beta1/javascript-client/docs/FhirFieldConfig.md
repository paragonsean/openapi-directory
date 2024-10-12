# CloudHealthcareApi.FhirFieldConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fieldMetadataList** | [**[GoogleCloudHealthcareV1beta1DeidentifyFieldMetadata]**](GoogleCloudHealthcareV1beta1DeidentifyFieldMetadata.md) | Specifies FHIR paths to match and how to transform them. Any field that is not matched by a FieldMetadata &#x60;action&#x60; is passed through to the output dataset unmodified. All extensions will be processed according to keep_extensions. If a field can be matched by more than one FieldMetadata &#x60;action&#x60;, the first &#x60;action&#x60; option is applied. Overrides options and the union field &#x60;profile&#x60; in FhirFieldConfig. | [optional] 
**options** | [**GoogleCloudHealthcareV1beta1DeidentifyOptions**](GoogleCloudHealthcareV1beta1DeidentifyOptions.md) |  | [optional] 
**profileType** | **String** | Base profile type for handling FHIR fields. | [optional] 



## Enum: ProfileTypeEnum


* `PROFILE_TYPE_UNSPECIFIED` (value: `"PROFILE_TYPE_UNSPECIFIED"`)

* `KEEP_ALL` (value: `"KEEP_ALL"`)

* `BASIC` (value: `"BASIC"`)

* `CLEAN_ALL` (value: `"CLEAN_ALL"`)




