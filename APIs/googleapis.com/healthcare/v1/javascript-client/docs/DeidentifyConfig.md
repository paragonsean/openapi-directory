# CloudHealthcareApi.DeidentifyConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dicom** | [**DicomConfig**](DicomConfig.md) |  | [optional] 
**fhir** | [**FhirConfig**](FhirConfig.md) |  | [optional] 
**image** | [**ImageConfig**](ImageConfig.md) |  | [optional] 
**text** | [**TextConfig**](TextConfig.md) |  | [optional] 
**useRegionalDataProcessing** | **Boolean** | Ensures in-flight data remains in the region of origin during de-identification. Using this option results in a significant reduction of throughput, and is not compatible with &#x60;LOCATION&#x60; or &#x60;ORGANIZATION_NAME&#x60; infoTypes. &#x60;LOCATION&#x60; must be excluded within TextConfig, and must also be excluded within ImageConfig if image redaction is required. | [optional] 


