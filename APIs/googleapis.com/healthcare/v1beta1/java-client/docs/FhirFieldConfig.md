

# FhirFieldConfig

Specifies how to handle the de-identification of a FHIR store.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fieldMetadataList** | [**List&lt;GoogleCloudHealthcareV1beta1DeidentifyFieldMetadata&gt;**](GoogleCloudHealthcareV1beta1DeidentifyFieldMetadata.md) | Specifies FHIR paths to match and how to transform them. Any field that is not matched by a FieldMetadata &#x60;action&#x60; is passed through to the output dataset unmodified. All extensions will be processed according to keep_extensions. If a field can be matched by more than one FieldMetadata &#x60;action&#x60;, the first &#x60;action&#x60; option is applied. Overrides options and the union field &#x60;profile&#x60; in FhirFieldConfig. |  [optional] |
|**options** | [**GoogleCloudHealthcareV1beta1DeidentifyOptions**](GoogleCloudHealthcareV1beta1DeidentifyOptions.md) |  |  [optional] |
|**profileType** | [**ProfileTypeEnum**](#ProfileTypeEnum) | Base profile type for handling FHIR fields. |  [optional] |



## Enum: ProfileTypeEnum

| Name | Value |
|---- | -----|
| PROFILE_TYPE_UNSPECIFIED | &quot;PROFILE_TYPE_UNSPECIFIED&quot; |
| KEEP_ALL | &quot;KEEP_ALL&quot; |
| BASIC | &quot;BASIC&quot; |
| CLEAN_ALL | &quot;CLEAN_ALL&quot; |



