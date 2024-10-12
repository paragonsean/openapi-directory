# CloudHealthcareApi.DeidentifyConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotation** | [**AnnotationConfig**](AnnotationConfig.md) |  | [optional] 
**dicom** | [**DicomConfig**](DicomConfig.md) |  | [optional] 
**dicomTagConfig** | [**DicomTagConfig**](DicomTagConfig.md) |  | [optional] 
**fhir** | [**FhirConfig**](FhirConfig.md) |  | [optional] 
**fhirFieldConfig** | [**FhirFieldConfig**](FhirFieldConfig.md) |  | [optional] 
**image** | [**ImageConfig**](ImageConfig.md) |  | [optional] 
**operationMetadata** | [**DeidentifyOperationMetadata**](DeidentifyOperationMetadata.md) |  | [optional] 
**text** | [**TextConfig**](TextConfig.md) |  | [optional] 
**useRegionalDataProcessing** | **Boolean** | Ensures in-flight data remains in the region of origin during de-identification. Using this option results in a significant reduction of throughput, and is not compatible with &#x60;LOCATION&#x60; or &#x60;ORGANIZATION_NAME&#x60; infoTypes. If the deprecated DicomConfig or FhirConfig are used, then &#x60;LOCATION&#x60; must be excluded within TextConfig, and must also be excluded within ImageConfig if image redaction is required. | [optional] 


