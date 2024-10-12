# CampaignManager360Api.ListPopulationTerm

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contains** | **Boolean** | Will be true if the term should check if the user is in the list and false if the term should check if the user is not in the list. This field is only relevant when type is set to LIST_MEMBERSHIP_TERM. False by default. | [optional] 
**negation** | **Boolean** | Whether to negate the comparison result of this term during rule evaluation. This field is only relevant when type is left unset or set to CUSTOM_VARIABLE_TERM or REFERRER_TERM. | [optional] 
**operator** | **String** | Comparison operator of this term. This field is only relevant when type is left unset or set to CUSTOM_VARIABLE_TERM or REFERRER_TERM. | [optional] 
**remarketingListId** | **String** | ID of the list in question. This field is only relevant when type is set to LIST_MEMBERSHIP_TERM. | [optional] 
**type** | **String** | List population term type determines the applicable fields in this object. If left unset or set to CUSTOM_VARIABLE_TERM, then variableName, variableFriendlyName, operator, value, and negation are applicable. If set to LIST_MEMBERSHIP_TERM then remarketingListId and contains are applicable. If set to REFERRER_TERM then operator, value, and negation are applicable. | [optional] 
**value** | **String** | Literal to compare the variable to. This field is only relevant when type is left unset or set to CUSTOM_VARIABLE_TERM or REFERRER_TERM. | [optional] 
**variableFriendlyName** | **String** | Friendly name of this term&#39;s variable. This is a read-only, auto-generated field. This field is only relevant when type is left unset or set to CUSTOM_VARIABLE_TERM. | [optional] 
**variableName** | **String** | Name of the variable (U1, U2, etc.) being compared in this term. This field is only relevant when type is set to null, CUSTOM_VARIABLE_TERM or REFERRER_TERM. | [optional] 



## Enum: OperatorEnum


* `NUM_EQUALS` (value: `"NUM_EQUALS"`)

* `NUM_LESS_THAN` (value: `"NUM_LESS_THAN"`)

* `NUM_LESS_THAN_EQUAL` (value: `"NUM_LESS_THAN_EQUAL"`)

* `NUM_GREATER_THAN` (value: `"NUM_GREATER_THAN"`)

* `NUM_GREATER_THAN_EQUAL` (value: `"NUM_GREATER_THAN_EQUAL"`)

* `STRING_EQUALS` (value: `"STRING_EQUALS"`)

* `STRING_CONTAINS` (value: `"STRING_CONTAINS"`)





## Enum: TypeEnum


* `CUSTOM_VARIABLE_TERM` (value: `"CUSTOM_VARIABLE_TERM"`)

* `LIST_MEMBERSHIP_TERM` (value: `"LIST_MEMBERSHIP_TERM"`)

* `REFERRER_TERM` (value: `"REFERRER_TERM"`)




