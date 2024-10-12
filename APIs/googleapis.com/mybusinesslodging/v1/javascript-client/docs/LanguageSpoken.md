# MyBusinessLodgingApi.LanguageSpoken

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**languageCode** | **String** | Required. The BCP-47 language code for the spoken language. Currently accepted codes: ar, de, en, es, fil, fr, hi, id, it, ja, ko, nl, pt, ru, vi, yue, zh. | [optional] 
**spoken** | **Boolean** | At least one member of the staff can speak the language. | [optional] 
**spokenException** | **String** | Spoken exception. | [optional] 



## Enum: SpokenExceptionEnum


* `EXCEPTION_UNSPECIFIED` (value: `"EXCEPTION_UNSPECIFIED"`)

* `UNDER_CONSTRUCTION` (value: `"UNDER_CONSTRUCTION"`)

* `DEPENDENT_ON_SEASON` (value: `"DEPENDENT_ON_SEASON"`)

* `DEPENDENT_ON_DAY_OF_WEEK` (value: `"DEPENDENT_ON_DAY_OF_WEEK"`)




