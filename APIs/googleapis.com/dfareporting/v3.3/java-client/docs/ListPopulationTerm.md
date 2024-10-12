

# ListPopulationTerm

Remarketing List Population Rule Term.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**contains** | **Boolean** | Will be true if the term should check if the user is in the list and false if the term should check if the user is not in the list. This field is only relevant when type is set to LIST_MEMBERSHIP_TERM. False by default. |  [optional] |
|**negation** | **Boolean** | Whether to negate the comparison result of this term during rule evaluation. This field is only relevant when type is left unset or set to CUSTOM_VARIABLE_TERM or REFERRER_TERM. |  [optional] |
|**operator** | [**OperatorEnum**](#OperatorEnum) | Comparison operator of this term. This field is only relevant when type is left unset or set to CUSTOM_VARIABLE_TERM or REFERRER_TERM. |  [optional] |
|**remarketingListId** | **String** | ID of the list in question. This field is only relevant when type is set to LIST_MEMBERSHIP_TERM. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | List population term type determines the applicable fields in this object. If left unset or set to CUSTOM_VARIABLE_TERM, then variableName, variableFriendlyName, operator, value, and negation are applicable. If set to LIST_MEMBERSHIP_TERM then remarketingListId and contains are applicable. If set to REFERRER_TERM then operator, value, and negation are applicable. |  [optional] |
|**value** | **String** | Literal to compare the variable to. This field is only relevant when type is left unset or set to CUSTOM_VARIABLE_TERM or REFERRER_TERM. |  [optional] |
|**variableFriendlyName** | **String** | Friendly name of this term&#39;s variable. This is a read-only, auto-generated field. This field is only relevant when type is left unset or set to CUSTOM_VARIABLE_TERM. |  [optional] |
|**variableName** | **String** | Name of the variable (U1, U2, etc.) being compared in this term. This field is only relevant when type is set to null, CUSTOM_VARIABLE_TERM or REFERRER_TERM. |  [optional] |



## Enum: OperatorEnum

| Name | Value |
|---- | -----|
| NUM_EQUALS | &quot;NUM_EQUALS&quot; |
| NUM_LESS_THAN | &quot;NUM_LESS_THAN&quot; |
| NUM_LESS_THAN_EQUAL | &quot;NUM_LESS_THAN_EQUAL&quot; |
| NUM_GREATER_THAN | &quot;NUM_GREATER_THAN&quot; |
| NUM_GREATER_THAN_EQUAL | &quot;NUM_GREATER_THAN_EQUAL&quot; |
| STRING_EQUALS | &quot;STRING_EQUALS&quot; |
| STRING_CONTAINS | &quot;STRING_CONTAINS&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| CUSTOM_VARIABLE_TERM | &quot;CUSTOM_VARIABLE_TERM&quot; |
| LIST_MEMBERSHIP_TERM | &quot;LIST_MEMBERSHIP_TERM&quot; |
| REFERRER_TERM | &quot;REFERRER_TERM&quot; |



