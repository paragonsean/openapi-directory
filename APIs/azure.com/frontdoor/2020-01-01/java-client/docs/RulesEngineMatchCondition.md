

# RulesEngineMatchCondition

Define a match condition

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**negateCondition** | **Boolean** | Describes if this is negate condition or not |  [optional] |
|**rulesEngineMatchValue** | **List&lt;String&gt;** | Match values to match against. The operator will apply to each value in here with OR semantics. If any of them match the variable with the given operator this match condition is considered a match. |  |
|**rulesEngineMatchVariable** | [**RulesEngineMatchVariableEnum**](#RulesEngineMatchVariableEnum) | Match Variable |  |
|**rulesEngineOperator** | [**RulesEngineOperatorEnum**](#RulesEngineOperatorEnum) | Describes operator to apply to the match condition. |  |
|**selector** | **String** | Name of selector in RequestHeader or RequestBody to be matched |  [optional] |
|**transforms** | **List&lt;Transform&gt;** | List of transforms |  [optional] |



## Enum: RulesEngineMatchVariableEnum

| Name | Value |
|---- | -----|
| IS_MOBILE | &quot;IsMobile&quot; |
| REMOTE_ADDR | &quot;RemoteAddr&quot; |
| REQUEST_METHOD | &quot;RequestMethod&quot; |
| QUERY_STRING | &quot;QueryString&quot; |
| POST_ARGS | &quot;PostArgs&quot; |
| REQUEST_URI | &quot;RequestUri&quot; |
| REQUEST_PATH | &quot;RequestPath&quot; |
| REQUEST_FILENAME | &quot;RequestFilename&quot; |
| REQUEST_FILENAME_EXTENSION | &quot;RequestFilenameExtension&quot; |
| REQUEST_HEADER | &quot;RequestHeader&quot; |
| REQUEST_BODY | &quot;RequestBody&quot; |
| REQUEST_SCHEME | &quot;RequestScheme&quot; |



## Enum: RulesEngineOperatorEnum

| Name | Value |
|---- | -----|
| ANY | &quot;Any&quot; |
| IP_MATCH | &quot;IPMatch&quot; |
| GEO_MATCH | &quot;GeoMatch&quot; |
| EQUAL | &quot;Equal&quot; |
| CONTAINS | &quot;Contains&quot; |
| LESS_THAN | &quot;LessThan&quot; |
| GREATER_THAN | &quot;GreaterThan&quot; |
| LESS_THAN_OR_EQUAL | &quot;LessThanOrEqual&quot; |
| GREATER_THAN_OR_EQUAL | &quot;GreaterThanOrEqual&quot; |
| BEGINS_WITH | &quot;BeginsWith&quot; |
| ENDS_WITH | &quot;EndsWith&quot; |



