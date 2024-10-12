# CloudSearchApi.QueryInterpretation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interpretationType** | **String** |  | [optional] 
**interpretedQuery** | **String** | The interpretation of the query used in search. For example, queries with natural language intent like \&quot;email from john\&quot; will be interpreted as \&quot;from:john source:mail\&quot;. This field will not be filled when the reason is NOT_ENOUGH_RESULTS_FOUND_FOR_USER_QUERY. | [optional] 
**reason** | **String** | The reason for interpretation of the query. This field will not be UNSPECIFIED if the interpretation type is not NONE. | [optional] 



## Enum: InterpretationTypeEnum


* `NONE` (value: `"NONE"`)

* `BLEND` (value: `"BLEND"`)

* `REPLACE` (value: `"REPLACE"`)





## Enum: ReasonEnum


* `UNSPECIFIED` (value: `"UNSPECIFIED"`)

* `QUERY_HAS_NATURAL_LANGUAGE_INTENT` (value: `"QUERY_HAS_NATURAL_LANGUAGE_INTENT"`)

* `NOT_ENOUGH_RESULTS_FOUND_FOR_USER_QUERY` (value: `"NOT_ENOUGH_RESULTS_FOUND_FOR_USER_QUERY"`)




