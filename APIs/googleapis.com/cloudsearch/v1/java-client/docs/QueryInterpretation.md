

# QueryInterpretation


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**interpretationType** | [**InterpretationTypeEnum**](#InterpretationTypeEnum) |  |  [optional] |
|**interpretedQuery** | **String** | The interpretation of the query used in search. For example, queries with natural language intent like \&quot;email from john\&quot; will be interpreted as \&quot;from:john source:mail\&quot;. This field will not be filled when the reason is NOT_ENOUGH_RESULTS_FOUND_FOR_USER_QUERY. |  [optional] |
|**reason** | [**ReasonEnum**](#ReasonEnum) | The reason for interpretation of the query. This field will not be UNSPECIFIED if the interpretation type is not NONE. |  [optional] |



## Enum: InterpretationTypeEnum

| Name | Value |
|---- | -----|
| NONE | &quot;NONE&quot; |
| BLEND | &quot;BLEND&quot; |
| REPLACE | &quot;REPLACE&quot; |



## Enum: ReasonEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;UNSPECIFIED&quot; |
| QUERY_HAS_NATURAL_LANGUAGE_INTENT | &quot;QUERY_HAS_NATURAL_LANGUAGE_INTENT&quot; |
| NOT_ENOUGH_RESULTS_FOUND_FOR_USER_QUERY | &quot;NOT_ENOUGH_RESULTS_FOUND_FOR_USER_QUERY&quot; |



