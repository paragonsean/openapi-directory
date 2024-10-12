

# HealthQuestionDefinitionResourceAttributes


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**category** | [**CategoryEnum**](#CategoryEnum) | The category for the health profile definition |  [optional] |
|**format** | [**HealthQuestionDefinitionResourceAttributesFormat**](HealthQuestionDefinitionResourceAttributesFormat.md) |  |  [optional] |
|**requirements** | [**List&lt;HealthQuestionDefinitionResourceAttributesRequirementsInner&gt;**](HealthQuestionDefinitionResourceAttributesRequirementsInner.md) | The lsit of age and gender requirements for the question to be included |  [optional] |
|**text** | **String** | The question text which corresponds to the answer choices |  [optional] |



## Enum: CategoryEnum

| Name | Value |
|---- | -----|
| LIFESTYLE_BEHAVIORS | &quot;lifestyle_behaviors&quot; |
| MENTAL_WELLBEING | &quot;mental_wellbeing&quot; |
| PREVENTATIVE_CARE | &quot;preventative_care&quot; |



