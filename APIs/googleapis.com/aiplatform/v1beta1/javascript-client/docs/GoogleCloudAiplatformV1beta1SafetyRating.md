# VertexAiApi.GoogleCloudAiplatformV1beta1SafetyRating

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blocked** | **Boolean** | Output only. Indicates whether the content was filtered out because of this rating. | [optional] [readonly] 
**category** | **String** | Output only. Harm category. | [optional] [readonly] 
**probability** | **String** | Output only. Harm probability levels in the content. | [optional] [readonly] 
**probabilityScore** | **Number** | Output only. Harm probability score. | [optional] [readonly] 
**severity** | **String** | Output only. Harm severity levels in the content. | [optional] [readonly] 
**severityScore** | **Number** | Output only. Harm severity score. | [optional] [readonly] 



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




