

# ChoiceQuestion

A radio/checkbox/dropdown question.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**options** | [**List&lt;Option&gt;**](Option.md) | Required. List of options that a respondent must choose from. |  [optional] |
|**shuffle** | **Boolean** | Whether the options should be displayed in random order for different instances of the quiz. This is often used to prevent cheating by respondents who might be looking at another respondent&#39;s screen, or to address bias in a survey that might be introduced by always putting the same options first or last. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Required. The type of choice question. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| CHOICE_TYPE_UNSPECIFIED | &quot;CHOICE_TYPE_UNSPECIFIED&quot; |
| RADIO | &quot;RADIO&quot; |
| CHECKBOX | &quot;CHECKBOX&quot; |
| DROP_DOWN | &quot;DROP_DOWN&quot; |



