

# CloudAiNlLlmProtoServiceRaiSignal

An RAI signal for a single category.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**confidence** | [**ConfidenceEnum**](#ConfidenceEnum) | The confidence level for the RAI category. |  [optional] |
|**flagged** | **Boolean** | Whether the category is flagged as being present. Currently, this is set to true if score &gt;&#x3D; 0.5. |  [optional] |
|**raiCategory** | [**RaiCategoryEnum**](#RaiCategoryEnum) | The RAI category. |  [optional] |
|**score** | **Float** | The score for the category, in the range [0.0, 1.0]. |  [optional] |



## Enum: ConfidenceEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;CONFIDENCE_UNSPECIFIED&quot; |
| NONE | &quot;CONFIDENCE_NONE&quot; |
| LOW | &quot;CONFIDENCE_LOW&quot; |
| MEDIUM | &quot;CONFIDENCE_MEDIUM&quot; |
| HIGH | &quot;CONFIDENCE_HIGH&quot; |



## Enum: RaiCategoryEnum

| Name | Value |
|---- | -----|
| RAI_CATEGORY_UNSPECIFIED | &quot;RAI_CATEGORY_UNSPECIFIED&quot; |
| TOXIC | &quot;TOXIC&quot; |
| SEXUALLY_EXPLICIT | &quot;SEXUALLY_EXPLICIT&quot; |
| HATE_SPEECH | &quot;HATE_SPEECH&quot; |
| VIOLENT | &quot;VIOLENT&quot; |
| PROFANITY | &quot;PROFANITY&quot; |
| HARASSMENT | &quot;HARASSMENT&quot; |
| DEATH_HARM_TRAGEDY | &quot;DEATH_HARM_TRAGEDY&quot; |
| FIREARMS_WEAPONS | &quot;FIREARMS_WEAPONS&quot; |
| PUBLIC_SAFETY | &quot;PUBLIC_SAFETY&quot; |
| HEALTH | &quot;HEALTH&quot; |
| RELIGIOUS_BELIEF | &quot;RELIGIOUS_BELIEF&quot; |
| ILLICIT_DRUGS | &quot;ILLICIT_DRUGS&quot; |
| WAR_CONFLICT | &quot;WAR_CONFLICT&quot; |
| POLITICS | &quot;POLITICS&quot; |
| FINANCE | &quot;FINANCE&quot; |
| LEGAL | &quot;LEGAL&quot; |
| CSAI | &quot;CSAI&quot; |
| FRINGE | &quot;FRINGE&quot; |
| THREAT | &quot;THREAT&quot; |
| SEVERE_TOXICITY | &quot;SEVERE_TOXICITY&quot; |
| TOXICITY | &quot;TOXICITY&quot; |
| SEXUAL | &quot;SEXUAL&quot; |
| INSULT | &quot;INSULT&quot; |
| DEROGATORY | &quot;DEROGATORY&quot; |
| IDENTITY_ATTACK | &quot;IDENTITY_ATTACK&quot; |
| VIOLENCE_ABUSE | &quot;VIOLENCE_ABUSE&quot; |
| OBSCENE | &quot;OBSCENE&quot; |
| DRUGS | &quot;DRUGS&quot; |
| CSAM | &quot;CSAM&quot; |
| SPII | &quot;SPII&quot; |
| DANGEROUS_CONTENT | &quot;DANGEROUS_CONTENT&quot; |
| DANGEROUS_CONTENT_SEVERITY | &quot;DANGEROUS_CONTENT_SEVERITY&quot; |
| INSULT_SEVERITY | &quot;INSULT_SEVERITY&quot; |
| DEROGATORY_SEVERITY | &quot;DEROGATORY_SEVERITY&quot; |
| SEXUAL_SEVERITY | &quot;SEXUAL_SEVERITY&quot; |



