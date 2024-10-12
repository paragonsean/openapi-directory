

# CloudAiLargeModelsVisionFilteredText

Details for filtered input text.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**category** | [**CategoryEnum**](#CategoryEnum) | Confidence level |  [optional] |
|**confidence** | [**ConfidenceEnum**](#ConfidenceEnum) | Filtered category |  [optional] |
|**prompt** | **String** | Input prompt |  [optional] |
|**score** | **Double** | Score for category |  [optional] |



## Enum: CategoryEnum

| Name | Value |
|---- | -----|
| RAI_CATEGORY_UNSPECIFIED | &quot;RAI_CATEGORY_UNSPECIFIED&quot; |
| OBSCENE | &quot;OBSCENE&quot; |
| SEXUALLY_EXPLICIT | &quot;SEXUALLY_EXPLICIT&quot; |
| IDENTITY_ATTACK | &quot;IDENTITY_ATTACK&quot; |
| VIOLENCE_ABUSE | &quot;VIOLENCE_ABUSE&quot; |
| CSAI | &quot;CSAI&quot; |
| SPII | &quot;SPII&quot; |
| CELEBRITY | &quot;CELEBRITY&quot; |
| FACE_IMG | &quot;FACE_IMG&quot; |
| WATERMARK_IMG | &quot;WATERMARK_IMG&quot; |
| MEMORIZATION_IMG | &quot;MEMORIZATION_IMG&quot; |
| CSAI_IMG | &quot;CSAI_IMG&quot; |
| PORN_IMG | &quot;PORN_IMG&quot; |
| VIOLENCE_IMG | &quot;VIOLENCE_IMG&quot; |
| CHILD_IMG | &quot;CHILD_IMG&quot; |
| TOXIC | &quot;TOXIC&quot; |
| SENSITIVE_WORD | &quot;SENSITIVE_WORD&quot; |
| PERSON_IMG | &quot;PERSON_IMG&quot; |
| ICA_IMG | &quot;ICA_IMG&quot; |
| SEXUAL_IMG | &quot;SEXUAL_IMG&quot; |
| IU_IMG | &quot;IU_IMG&quot; |
| RACY_IMG | &quot;RACY_IMG&quot; |
| PEDO_IMG | &quot;PEDO_IMG&quot; |
| DEATH_HARM_TRAGEDY | &quot;DEATH_HARM_TRAGEDY&quot; |
| HEALTH | &quot;HEALTH&quot; |
| FIREARMS_WEAPONS | &quot;FIREARMS_WEAPONS&quot; |
| RELIGIOUS_BELIEF | &quot;RELIGIOUS_BELIEF&quot; |
| ILLICIT_DRUGS | &quot;ILLICIT_DRUGS&quot; |
| WAR_CONFLICT | &quot;WAR_CONFLICT&quot; |
| POLITICS | &quot;POLITICS&quot; |
| HATE_SYMBOL_IMG | &quot;HATE_SYMBOL_IMG&quot; |
| CHILD_TEXT | &quot;CHILD_TEXT&quot; |
| DANGEROUS_CONTENT | &quot;DANGEROUS_CONTENT&quot; |
| RECITATION_TEXT | &quot;RECITATION_TEXT&quot; |
| CELEBRITY_IMG | &quot;CELEBRITY_IMG&quot; |



## Enum: ConfidenceEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;CONFIDENCE_UNSPECIFIED&quot; |
| LOW | &quot;CONFIDENCE_LOW&quot; |
| MEDIUM | &quot;CONFIDENCE_MEDIUM&quot; |
| HIGH | &quot;CONFIDENCE_HIGH&quot; |



