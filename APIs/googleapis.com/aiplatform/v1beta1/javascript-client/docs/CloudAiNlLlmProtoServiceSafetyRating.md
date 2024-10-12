# VertexAiApi.CloudAiNlLlmProtoServiceSafetyRating

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blocked** | **Boolean** | Indicates whether the content was filtered out because of this rating. | [optional] 
**category** | **String** | Harm category. | [optional] 
**influentialTerms** | [**[CloudAiNlLlmProtoServiceSafetyRatingInfluentialTerm]**](CloudAiNlLlmProtoServiceSafetyRatingInfluentialTerm.md) | The influential terms that could potentially block the response. | [optional] 
**probability** | **String** | Harm probability levels in the content. | [optional] 
**probabilityScore** | **Number** | Harm probability score. | [optional] 
**severity** | **String** | Harm severity levels in the content. | [optional] 
**severityScore** | **Number** | Harm severity score. | [optional] 



## Enum: CategoryEnum


* `UNSPECIFIED` (value: `"HARM_CATEGORY_UNSPECIFIED"`)

* `HATE_SPEECH` (value: `"HARM_CATEGORY_HATE_SPEECH"`)

* `DANGEROUS_CONTENT` (value: `"HARM_CATEGORY_DANGEROUS_CONTENT"`)

* `HARASSMENT` (value: `"HARM_CATEGORY_HARASSMENT"`)

* `SEXUALLY_EXPLICIT` (value: `"HARM_CATEGORY_SEXUALLY_EXPLICIT"`)





## Enum: ProbabilityEnum


* `HARM_PROBABILITY_UNSPECIFIED` (value: `"HARM_PROBABILITY_UNSPECIFIED"`)

* `NEGLIGIBLE` (value: `"NEGLIGIBLE"`)

* `LOW` (value: `"LOW"`)

* `MEDIUM` (value: `"MEDIUM"`)

* `HIGH` (value: `"HIGH"`)





## Enum: SeverityEnum


* `UNSPECIFIED` (value: `"HARM_SEVERITY_UNSPECIFIED"`)

* `NEGLIGIBLE` (value: `"HARM_SEVERITY_NEGLIGIBLE"`)

* `LOW` (value: `"HARM_SEVERITY_LOW"`)

* `MEDIUM` (value: `"HARM_SEVERITY_MEDIUM"`)

* `HIGH` (value: `"HARM_SEVERITY_HIGH"`)




