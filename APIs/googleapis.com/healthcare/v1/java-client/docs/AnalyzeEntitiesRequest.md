

# AnalyzeEntitiesRequest

The request to analyze healthcare entities in a document.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**alternativeOutputFormat** | [**AlternativeOutputFormatEnum**](#AlternativeOutputFormatEnum) | Optional. Alternative output format to be generated based on the results of analysis. |  [optional] |
|**documentContent** | **String** | document_content is a document to be annotated. |  [optional] |
|**licensedVocabularies** | [**List&lt;LicensedVocabulariesEnum&gt;**](#List&lt;LicensedVocabulariesEnum&gt;) | A list of licensed vocabularies to use in the request, in addition to the default unlicensed vocabularies. |  [optional] |



## Enum: AlternativeOutputFormatEnum

| Name | Value |
|---- | -----|
| ALTERNATIVE_OUTPUT_FORMAT_UNSPECIFIED | &quot;ALTERNATIVE_OUTPUT_FORMAT_UNSPECIFIED&quot; |
| FHIR_BUNDLE | &quot;FHIR_BUNDLE&quot; |



## Enum: List&lt;LicensedVocabulariesEnum&gt;

| Name | Value |
|---- | -----|
| LICENSED_VOCABULARY_UNSPECIFIED | &quot;LICENSED_VOCABULARY_UNSPECIFIED&quot; |
| ICD10_CM | &quot;ICD10CM&quot; |
| SNOMEDCT_US | &quot;SNOMEDCT_US&quot; |



