

# LanguageSpoken

Language spoken by at least one staff member.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**languageCode** | **String** | Required. The BCP-47 language code for the spoken language. Currently accepted codes: ar, de, en, es, fil, fr, hi, id, it, ja, ko, nl, pt, ru, vi, yue, zh. |  [optional] |
|**spoken** | **Boolean** | At least one member of the staff can speak the language. |  [optional] |
|**spokenException** | [**SpokenExceptionEnum**](#SpokenExceptionEnum) | Spoken exception. |  [optional] |



## Enum: SpokenExceptionEnum

| Name | Value |
|---- | -----|
| EXCEPTION_UNSPECIFIED | &quot;EXCEPTION_UNSPECIFIED&quot; |
| UNDER_CONSTRUCTION | &quot;UNDER_CONSTRUCTION&quot; |
| DEPENDENT_ON_SEASON | &quot;DEPENDENT_ON_SEASON&quot; |
| DEPENDENT_ON_DAY_OF_WEEK | &quot;DEPENDENT_ON_DAY_OF_WEEK&quot; |



