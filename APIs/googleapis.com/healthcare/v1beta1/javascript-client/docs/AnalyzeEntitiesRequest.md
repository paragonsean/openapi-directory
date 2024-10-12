# CloudHealthcareApi.AnalyzeEntitiesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alternativeOutputFormat** | **String** | Optional. Alternative output format to be generated based on the results of analysis. | [optional] 
**documentContent** | **String** | document_content is a document to be annotated. | [optional] 
**licensedVocabularies** | **[String]** | A list of licensed vocabularies to use in the request, in addition to the default unlicensed vocabularies. | [optional] 



## Enum: AlternativeOutputFormatEnum


* `ALTERNATIVE_OUTPUT_FORMAT_UNSPECIFIED` (value: `"ALTERNATIVE_OUTPUT_FORMAT_UNSPECIFIED"`)

* `FHIR_BUNDLE` (value: `"FHIR_BUNDLE"`)





## Enum: [LicensedVocabulariesEnum]


* `LICENSED_VOCABULARY_UNSPECIFIED` (value: `"LICENSED_VOCABULARY_UNSPECIFIED"`)

* `ICD10CM` (value: `"ICD10CM"`)

* `SNOMEDCT_US` (value: `"SNOMEDCT_US"`)




