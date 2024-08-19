# GoogleFormsApi.ChoiceQuestion

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**options** | [**[Option]**](Option.md) | Required. List of options that a respondent must choose from. | [optional] 
**shuffle** | **Boolean** | Whether the options should be displayed in random order for different instances of the quiz. This is often used to prevent cheating by respondents who might be looking at another respondent&#39;s screen, or to address bias in a survey that might be introduced by always putting the same options first or last. | [optional] 
**type** | **String** | Required. The type of choice question. | [optional] 



## Enum: TypeEnum


* `CHOICE_TYPE_UNSPECIFIED` (value: `"CHOICE_TYPE_UNSPECIFIED"`)

* `RADIO` (value: `"RADIO"`)

* `CHECKBOX` (value: `"CHECKBOX"`)

* `DROP_DOWN` (value: `"DROP_DOWN"`)




