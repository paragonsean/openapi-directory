# VertexAiApi.CloudAiNlLlmProtoServiceRaiSignal

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confidence** | **String** | The confidence level for the RAI category. | [optional] 
**flagged** | **Boolean** | Whether the category is flagged as being present. Currently, this is set to true if score &gt;&#x3D; 0.5. | [optional] 
**raiCategory** | **String** | The RAI category. | [optional] 
**score** | **Number** | The score for the category, in the range [0.0, 1.0]. | [optional] 



## Enum: ConfidenceEnum


* `UNSPECIFIED` (value: `"CONFIDENCE_UNSPECIFIED"`)

* `NONE` (value: `"CONFIDENCE_NONE"`)

* `LOW` (value: `"CONFIDENCE_LOW"`)

* `MEDIUM` (value: `"CONFIDENCE_MEDIUM"`)

* `HIGH` (value: `"CONFIDENCE_HIGH"`)





## Enum: RaiCategoryEnum


* `RAI_CATEGORY_UNSPECIFIED` (value: `"RAI_CATEGORY_UNSPECIFIED"`)

* `TOXIC` (value: `"TOXIC"`)

* `SEXUALLY_EXPLICIT` (value: `"SEXUALLY_EXPLICIT"`)

* `HATE_SPEECH` (value: `"HATE_SPEECH"`)

* `VIOLENT` (value: `"VIOLENT"`)

* `PROFANITY` (value: `"PROFANITY"`)

* `HARASSMENT` (value: `"HARASSMENT"`)

* `DEATH_HARM_TRAGEDY` (value: `"DEATH_HARM_TRAGEDY"`)

* `FIREARMS_WEAPONS` (value: `"FIREARMS_WEAPONS"`)

* `PUBLIC_SAFETY` (value: `"PUBLIC_SAFETY"`)

* `HEALTH` (value: `"HEALTH"`)

* `RELIGIOUS_BELIEF` (value: `"RELIGIOUS_BELIEF"`)

* `ILLICIT_DRUGS` (value: `"ILLICIT_DRUGS"`)

* `WAR_CONFLICT` (value: `"WAR_CONFLICT"`)

* `POLITICS` (value: `"POLITICS"`)

* `FINANCE` (value: `"FINANCE"`)

* `LEGAL` (value: `"LEGAL"`)

* `CSAI` (value: `"CSAI"`)

* `FRINGE` (value: `"FRINGE"`)

* `THREAT` (value: `"THREAT"`)

* `SEVERE_TOXICITY` (value: `"SEVERE_TOXICITY"`)

* `TOXICITY` (value: `"TOXICITY"`)

* `SEXUAL` (value: `"SEXUAL"`)

* `INSULT` (value: `"INSULT"`)

* `DEROGATORY` (value: `"DEROGATORY"`)

* `IDENTITY_ATTACK` (value: `"IDENTITY_ATTACK"`)

* `VIOLENCE_ABUSE` (value: `"VIOLENCE_ABUSE"`)

* `OBSCENE` (value: `"OBSCENE"`)

* `DRUGS` (value: `"DRUGS"`)

* `CSAM` (value: `"CSAM"`)

* `SPII` (value: `"SPII"`)

* `DANGEROUS_CONTENT` (value: `"DANGEROUS_CONTENT"`)

* `DANGEROUS_CONTENT_SEVERITY` (value: `"DANGEROUS_CONTENT_SEVERITY"`)

* `INSULT_SEVERITY` (value: `"INSULT_SEVERITY"`)

* `DEROGATORY_SEVERITY` (value: `"DEROGATORY_SEVERITY"`)

* `SEXUAL_SEVERITY` (value: `"SEXUAL_SEVERITY"`)




